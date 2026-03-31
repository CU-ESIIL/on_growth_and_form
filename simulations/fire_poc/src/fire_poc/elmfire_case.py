"""ELMFIRE case-directory writer."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from typing import Any

import numpy as np
import rasterio
from rasterio.transform import from_origin

from .config import DomainConfig, Forcing
from .forcing import estimate_dead_fuel_moisture


@dataclass
class CaseArtifacts:
    """Paths describing a written ELMFIRE case."""

    case_dir: Path
    inputs_dir: Path
    weather_dir: Path
    topo_dir: Path
    outputs_dir: Path
    manifest_path: Path
    elmfire_data_path: Path
    ignition_path: Path
    run_script_path: Path


class ElmfireCaseWriter:
    """Write a minimal but inspectable ELMFIRE-style case directory."""

    float_names = ("ws", "wd", "m1", "m10", "m100", "adj", "phi")
    int_names = ("slp", "asp", "dem", "fbfm40", "cc", "ch", "cbh", "cbd")

    def _detect_gdal_bin(self) -> str:
        """Find a GDAL binary directory suitable for ELMFIRE's command calls."""

        gdal_translate = shutil.which("gdal_translate")
        if gdal_translate:
            return str(Path(gdal_translate).resolve().parent)
        homebrew_bin = Path("/opt/homebrew/bin")
        if homebrew_bin.exists():
            return str(homebrew_bin)
        return "/usr/bin"

    def write_case(self, case_dir: Path, domain: DomainConfig, forcing: Forcing) -> CaseArtifacts:
        case_dir = Path(case_dir).resolve()
        inputs_dir = case_dir / "inputs"
        weather_dir = inputs_dir / "weather"
        topo_dir = inputs_dir / "fuels_and_topography"
        outputs_dir = case_dir / "outputs"
        scratch_dir = case_dir / "scratch"
        self._clear_generated_case_artifacts(case_dir)
        weather_dir.mkdir(parents=True, exist_ok=True)
        topo_dir.mkdir(parents=True, exist_ok=True)
        outputs_dir.mkdir(parents=True, exist_ok=True)
        scratch_dir.mkdir(parents=True, exist_ok=True)
        transform = from_origin(domain.origin_x, domain.origin_y + domain.ny * domain.cell_size_m, domain.cell_size_m, domain.cell_size_m)

        dynamic_float = self._build_dynamic_float_layers(domain, forcing)
        static_int = self._build_static_int_layers(domain, forcing)
        for name, array in dynamic_float.items():
            self._write_geotiff(weather_dir / f"{name}.tif", array, transform, domain.crs)
        for name, array in static_int.items():
            self._write_geotiff(topo_dir / f"{name}.tif", array, transform, domain.crs)
        # ELMFIRE reads ADJ/PHI through the fuels/topography path even when transient
        # weather stacks are present, so we provide static first-band copies there too.
        for name in ("adj", "phi"):
            self._write_geotiff(topo_dir / f"{name}.tif", dynamic_float[name][0], transform, domain.crs)

        ignition_path = case_dir / "ignition_points.json"
        ignition_payload = {
            "type": "point_ignition",
            "description": "Inspectable ignition input for the proof of concept.",
            "points": [
                {
                    "x_local_m": domain.ignition_x_m,
                    "y_local_m": domain.ignition_y_m,
                    "x_m": domain.ignition_x_m,
                    "y_m": domain.ignition_y_m,
                    "x_abs_m": domain.origin_x + domain.ignition_x_m,
                    "y_abs_m": domain.origin_y + domain.ignition_y_m,
                    "time_hr": 0.0,
                }
            ],
        }
        ignition_path.write_text(json.dumps(ignition_payload, indent=2))

        run_script_path = case_dir / "run_elmfire.sh"
        run_script_path.write_text(self._render_run_script())
        run_script_path.chmod(0o755)

        elmfire_data_path = case_dir / "elmfire.data"
        elmfire_data_path.write_text(
            self._render_elmfire_data(domain, forcing, topo_dir, weather_dir, outputs_dir, scratch_dir)
        )

        manifest_path = case_dir / "manifest.json"
        manifest_payload = {
            "event_settings": {
                "nx": domain.nx,
                "ny": domain.ny,
                "cell_size_m": domain.cell_size_m,
                "crs": domain.crs,
                "ignition_xy_m": [domain.ignition_x_m, domain.ignition_y_m],
            },
            "weather_summary": forcing.weather_summary(),
            "forcing_source": forcing.source_name,
            "file_paths": {
                "inputs_dir": str(inputs_dir),
                "weather_dir": str(weather_dir),
                "fuels_and_topography_dir": str(topo_dir),
                "outputs_dir": str(outputs_dir),
                "elmfire_data": str(elmfire_data_path),
                "ignition": str(ignition_path),
                "run_script": str(run_script_path),
            },
        }
        manifest_path.write_text(json.dumps(manifest_payload, indent=2))
        return CaseArtifacts(
            case_dir=case_dir,
            inputs_dir=inputs_dir,
            weather_dir=weather_dir,
            topo_dir=topo_dir,
            outputs_dir=outputs_dir,
            manifest_path=manifest_path,
            elmfire_data_path=elmfire_data_path,
            ignition_path=ignition_path,
            run_script_path=run_script_path,
        )

    def _clear_generated_case_artifacts(self, case_dir: Path) -> None:
        """Remove prior generated artifacts so reruns do not mix old and new outputs."""

        if not case_dir.exists():
            return
        for directory in (case_dir / "inputs", case_dir / "outputs", case_dir / "scratch"):
            if directory.exists():
                shutil.rmtree(directory)
        for path in case_dir.iterdir():
            if path.is_file() and (
                path.name in {"elmfire.data", "elmfire_stdout.log", "elmfire_stderr.log", "manifest.json", "ignition_points.json", "run_elmfire.sh"}
                or path.suffix.lower() in {".bsq", ".bil", ".hdr", ".aux", ".xml"}
            ):
                path.unlink()

    def _build_dynamic_float_layers(self, domain: DomainConfig, forcing: Forcing) -> dict[str, np.ndarray]:
        shape = (forcing.num_steps, domain.ny, domain.nx)
        adj_scale = float(forcing.metadata.get("adj_scale", 1.0))
        phi_scale = float(forcing.metadata.get("phi_scale", 1.0))
        patterns = self._build_pattern_fields(domain, forcing)
        ws_mph = forcing.wind_speed_mps * 2.23693629
        wind_factor = np.clip(
            1.0
            + 0.32 * patterns["streak"] * patterns["wind_streak_strength"]
            + 0.24 * patterns["corridor"] * patterns["gust_corridor_strength"]
            - 0.10 * patterns["lee_shadow"],
            0.55,
            2.6,
        )
        ws = np.broadcast_to(ws_mph[:, None, None], shape) * wind_factor[None, :, :]
        direction_delta = (
            12.0 * patterns["crosswind"] * patterns["wind_streak_strength"]
            + 8.0 * patterns["ridge"] * patterns["heterogeneity_strength"]
        )
        wd = (
            np.broadcast_to(forcing.wind_direction_deg_from[:, None, None], shape)
            + direction_delta[None, :, :]
        ) % 360.0
        m1, m10, m100 = estimate_dead_fuel_moisture(forcing.relative_humidity_pct)
        m1 = np.clip(m1 + float(forcing.metadata.get("m1_offset_pct", 0.0)), 1.0, 18.0)
        m10 = np.clip(m10 + float(forcing.metadata.get("m10_offset_pct", 0.0)), 2.0, 22.0)
        m100 = np.clip(m100 + float(forcing.metadata.get("m100_offset_pct", 0.0)), 4.0, 28.0)
        dryness_factor = np.clip(
            1.0
            - 0.28 * patterns["dry_patch"] * patterns["dryness_patch_strength"]
            - 0.16 * patterns["corridor"] * patterns["gust_corridor_strength"]
            + 0.10 * patterns["lee_shadow"],
            0.45,
            1.25,
        )
        m1_r = np.broadcast_to(m1[:, None, None], shape) * dryness_factor[None, :, :]
        m10_r = np.broadcast_to(m10[:, None, None], shape) * np.clip(dryness_factor[None, :, :] + 0.05, 0.55, 1.35)
        m100_r = np.broadcast_to(m100[:, None, None], shape) * np.clip(dryness_factor[None, :, :] + 0.10, 0.65, 1.40)
        adj_factor = np.clip(
            1.0
            + 0.45 * patterns["ridge"] * patterns["heterogeneity_strength"]
            + 0.42 * patterns["corridor"] * patterns["gust_corridor_strength"]
            + 0.20 * patterns["streak"] * patterns["wind_streak_strength"],
            0.45,
            3.5,
        )
        phi_factor = np.clip(
            1.0
            + 0.25 * patterns["ridge"] * patterns["heterogeneity_strength"]
            + 0.36 * patterns["corridor"] * patterns["gust_corridor_strength"]
            + 0.16 * patterns["streak"] * patterns["wind_streak_strength"],
            0.55,
            3.0,
        )
        adj = np.broadcast_to((adj_scale * np.ones_like(forcing.wind_speed_mps))[:, None, None], shape) * adj_factor[None, :, :]
        phi = np.broadcast_to(((0.15 + 0.03 * forcing.wind_speed_mps) * phi_scale)[:, None, None], shape) * phi_factor[None, :, :]
        return {
            "ws": ws.astype(np.float32),
            "wd": wd.astype(np.float32),
            "m1": np.clip(m1_r, 1.0, 25.0).astype(np.float32),
            "m10": np.clip(m10_r, 2.0, 28.0).astype(np.float32),
            "m100": np.clip(m100_r, 4.0, 35.0).astype(np.float32),
            "adj": adj.astype(np.float32),
            "phi": phi.astype(np.float32),
        }

    def _build_static_int_layers(self, domain: DomainConfig, forcing: Forcing) -> dict[str, np.ndarray]:
        yy, xx = np.mgrid[0:domain.ny, 0:domain.nx]
        patterns = self._build_pattern_fields(domain, forcing)
        slope_base = float(forcing.metadata.get("slope_deg", 12))
        slope_variability = float(forcing.metadata.get("slope_variability_deg", 7.0))
        aspect_base = float(forcing.metadata.get("aspect_deg", 180))
        dem = (
            1750
            + 2 * yy
            + xx
            + 26.0 * patterns["ridge"]
            + 18.0 * patterns["corridor"]
            - 11.0 * patterns["lee_shadow"]
        ).astype(np.int16)
        slp = np.clip(
            np.rint(
                slope_base
                + slope_variability * (0.75 * patterns["ridge"] + 0.45 * patterns["streak"] + 0.35 * patterns["corridor"])
            ),
            0,
            60,
        ).astype(np.int16)
        asp = np.mod(
            np.rint(aspect_base + 32.0 * patterns["crosswind"] + 18.0 * patterns["ridge"]),
            360.0,
        ).astype(np.int16)
        fbfm40 = np.full((domain.ny, domain.nx), int(forcing.metadata.get("fuel_model_code", 101)), dtype=np.int16)
        canopy_base = float(forcing.metadata.get("canopy_cover_pct", 25))
        canopy_roughness = float(forcing.metadata.get("canopy_patchiness_pct", 16.0))
        cc = np.clip(
            np.rint(canopy_base + canopy_roughness * (0.65 * patterns["dry_patch"] - 0.45 * patterns["corridor"] + 0.30 * patterns["ridge"])),
            0,
            100,
        ).astype(np.int16)
        ch_base = float(forcing.metadata.get("canopy_height_x10_m", 4))
        ch = np.clip(np.rint(ch_base + 1.8 * patterns["ridge"] - 1.2 * patterns["corridor"]), 0, 40).astype(np.int16)
        cbh_base = float(forcing.metadata.get("canopy_base_height_x10_m", 2))
        cbh = np.clip(np.rint(cbh_base + 0.8 * patterns["dry_patch"] - 0.5 * patterns["ridge"]), 0, 30).astype(np.int16)
        cbd_base = float(forcing.metadata.get("canopy_bulk_density_x100", 12))
        cbd = np.clip(np.rint(cbd_base + 2.4 * patterns["ridge"] - 1.7 * patterns["corridor"]), 0, 40).astype(np.int16)
        return {
            "slp": slp,
            "asp": asp,
            "dem": dem,
            "fbfm40": fbfm40,
            "cc": cc,
            "ch": ch,
            "cbh": cbh,
            "cbd": cbd,
        }

    def _build_pattern_fields(self, domain: DomainConfig, forcing: Forcing) -> dict[str, np.ndarray | float]:
        """Construct deterministic spatial fields that roughen otherwise idealized cases."""

        y_idx, x_idx = np.mgrid[0:domain.ny, 0:domain.nx]
        x = (x_idx + 0.5) / domain.nx
        y = (y_idx + 0.5) / domain.ny
        x_centered = x - 0.5
        y_centered = y - 0.5
        mean_toward_rad = np.deg2rad((float(np.mean(forcing.wind_direction_deg_from)) + 180.0) % 360.0)
        along = x_centered * np.cos(mean_toward_rad) + y_centered * np.sin(mean_toward_rad)
        cross = -x_centered * np.sin(mean_toward_rad) + y_centered * np.cos(mean_toward_rad)
        corridor = np.exp(-((cross / 0.12) ** 2 + ((along - 0.04) / 0.42) ** 2))
        lee_shadow = np.exp(-((cross / 0.18) ** 2 + ((along + 0.18) / 0.26) ** 2))
        ridge = (
            0.7 * np.sin(2.0 * np.pi * (1.4 * x + 0.7 * y))
            + 0.45 * np.cos(2.0 * np.pi * (2.7 * x - 1.1 * y))
            + 0.25 * np.sin(2.0 * np.pi * (4.1 * x + 3.4 * y))
        )
        streak = (
            0.8 * np.sin(2.0 * np.pi * (5.5 * along + 1.6 * cross))
            + 0.35 * np.cos(2.0 * np.pi * (8.2 * along - 1.8 * cross))
        )
        dry_patch = np.clip(0.55 * ridge + 0.55 * corridor + 0.35 * streak, -1.0, 1.0)
        return {
            "corridor": corridor,
            "lee_shadow": lee_shadow,
            "ridge": ridge,
            "streak": streak,
            "dry_patch": dry_patch,
            "crosswind": cross / max(np.max(np.abs(cross)), 1e-6),
            "heterogeneity_strength": float(forcing.metadata.get("heterogeneity_strength", 0.25)),
            "gust_corridor_strength": float(forcing.metadata.get("gust_corridor_strength", 0.0)),
            "wind_streak_strength": float(forcing.metadata.get("wind_streak_strength", 0.0)),
            "dryness_patch_strength": float(forcing.metadata.get("dryness_patch_strength", 0.0)),
        }

    def _write_geotiff(self, path: Path, array: np.ndarray, transform, crs: str) -> None:
        array = np.asarray(array)
        if array.ndim == 2:
            count = 1
            height, width = array.shape
        elif array.ndim == 3:
            count, height, width = array.shape
        else:
            raise ValueError(f"Unsupported raster shape for {path}: {array.shape}")
        with rasterio.open(
            path,
            "w",
            driver="GTiff",
            height=height,
            width=width,
            count=count,
            dtype=array.dtype,
            transform=transform,
            crs=crs,
        ) as dst:
            if array.ndim == 2:
                dst.write(array, 1)
            else:
                dst.write(array)

    def _render_elmfire_data(
        self,
        domain: DomainConfig,
        forcing: Forcing,
        topo_dir: Path,
        weather_dir: Path,
        outputs_dir: Path,
        scratch_dir: Path,
    ) -> str:
        dt_seconds = int(round(forcing.dt_hours * 3600.0)) if forcing.num_steps > 1 else 3600
        gdal_bin = self._detect_gdal_bin()
        ignition_x_abs = domain.origin_x + domain.ignition_x_m
        ignition_y_abs = domain.origin_y + domain.ignition_y_m
        lines = [
            "&INPUTS",
            "  FUELS_AND_TOPOGRAPHY_DIRECTORY = './inputs/fuels_and_topography'",
            "  WEATHER_DIRECTORY = './inputs/weather'",
            "  ASP_FILENAME = 'asp'",
            "  CBD_FILENAME = 'cbd'",
            "  CBH_FILENAME = 'cbh'",
            "  CC_FILENAME = 'cc'",
            "  CH_FILENAME = 'ch'",
            "  DEM_FILENAME = 'dem'",
            "  FBFM_FILENAME = 'fbfm40'",
            "  SLP_FILENAME = 'slp'",
            "  ADJ_FILENAME = 'adj'",
            "  PHI_FILENAME = 'phi'",
            f"  DT_METEOROLOGY = {float(dt_seconds):.1f}",
            "  WS_AT_10M = .TRUE.",
            "  WS_FILENAME = 'ws'",
            "  WD_FILENAME = 'wd'",
            "  M1_FILENAME = 'm1'",
            "  M10_FILENAME = 'm10'",
            "  M100_FILENAME = 'm100'",
            "  LH_MOISTURE_CONTENT = 90.0",
            "  LW_MOISTURE_CONTENT = 90.0",
            "/",
            "&OUTPUTS",
            "  OUTPUTS_DIRECTORY = './outputs'",
            f"  DTDUMP = {float(dt_seconds):.1f}",
            "  DUMP_FLIN = .TRUE.",
            "  DUMP_SPREAD_RATE = .TRUE.",
            "  DUMP_TIME_OF_ARRIVAL = .TRUE.",
            "  CONVERT_TO_GEOTIFF = .FALSE.",
            "/",
            "&COMPUTATIONAL_DOMAIN",
            f"  A_SRS = '{domain.crs}'",
            f"  COMPUTATIONAL_DOMAIN_CELLSIZE = {domain.cell_size_m}",
            f"  COMPUTATIONAL_DOMAIN_XLLCORNER = {domain.origin_x}",
            f"  COMPUTATIONAL_DOMAIN_YLLCORNER = {domain.origin_y}",
            "/",
            "&TIME_CONTROL",
            "  SIMULATION_DT = 5.0",
            "  TARGET_CFL = 0.2",
            f"  SIMULATION_TSTOP = {float(int(round(forcing.time_hours[-1] * 3600.0))):.1f}",
            "/",
            "&MONTE_CARLO",
            f"  NUM_METEOROLOGY_TIMES = {forcing.num_steps}",
            "/",
            "&SIMULATOR",
            "  NUM_IGNITIONS = 1",
            f"  X_IGN(1) = {ignition_x_abs}",
            f"  Y_IGN(1) = {ignition_y_abs}",
            "  T_IGN(1) = 0.0",
            "  WX_BILINEAR_INTERPOLATION = .FALSE.",
            "  WSMFEFF_LOW_MULT = 0.011364",
            "/",
            "&MISCELLANEOUS",
            f"  PATH_TO_GDAL = '{gdal_bin}'",
            "  SCRATCH = './scratch'",
            "/",
        ]
        return "\n".join(lines) + "\n"

    def _render_run_script(self) -> str:
        """Provide an inspectable helper script for manual local runs."""

        return "\n".join(
            [
                "#!/usr/bin/env bash",
                "set -euo pipefail",
                'ELMFIRE_CMD=\"${1:-elmfire}\"',
                'echo \"Running ${ELMFIRE_CMD} in $(pwd)\"',
                'exec ${ELMFIRE_CMD}',
                "",
            ]
        )
