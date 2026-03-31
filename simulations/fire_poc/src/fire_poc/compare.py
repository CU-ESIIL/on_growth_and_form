"""Top-level workflow orchestration for the proof of concept."""

from __future__ import annotations

from dataclasses import dataclass
import json
import logging
import platform
from pathlib import Path
from typing import Any

import numpy as np

from .config import DomainConfig, RunConfig
from .earth2_provider import Earth2StudioFetchError, Earth2StudioGEFSProvider, Earth2StudioUnavailable
from .elmfire_runner import BenchmarkStatus, ElmfireRunner, build_proxy_benchmark
from .mock_provider import MockEarth2Provider
from .plotting import create_comparison_figure, create_elmfire_time_sequence_map, create_extreme_conditions_panel
from .regime_model import FireModelResult, RegimeAwareModel

LOGGER = logging.getLogger(__name__)


@dataclass
class PipelineOutputs:
    """High-level output summary for a completed workflow."""

    forcing_source: str
    benchmark_status: BenchmarkStatus
    regime_result: FireModelResult
    benchmark_result: FireModelResult | None
    figure_path: Path
    map_figure_path: Path | None
    workdir: Path
    status_path: Path


@dataclass
class ExtremeScenarioRun:
    """One completed scenario run used in the extremes panel."""

    slug: str
    title: str
    description: str
    forcing: Any
    benchmark_status: BenchmarkStatus


@dataclass
class ExtremePanelOutputs:
    """Summary for the extremes-panel workflow."""

    forcing_source: str
    scenario_runs: list[ExtremeScenarioRun]
    figure_path: Path
    workdir: Path
    status_path: Path


def configure_logging(verbose: bool = True) -> None:
    """Configure basic logging once per CLI or notebook run."""

    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(level=level, format="%(levelname)s %(name)s: %(message)s")


def run_pipeline(
    provider_name: str,
    workdir: Path,
    elmfire_cmd: str | None = None,
    duration_hours: float = 12.0,
    step_hours: float = 1.0,
) -> PipelineOutputs:
    """Run the full workflow and write organized outputs."""

    configure_logging()
    maybe_warn_about_platform()
    run_config = RunConfig(provider=provider_name, workdir=Path(workdir), elmfire_cmd=elmfire_cmd, duration_hours=duration_hours, step_hours=step_hours)
    domain = DomainConfig()
    run_config.workdir.mkdir(parents=True, exist_ok=True)
    case_dir = run_config.workdir / "case"
    figure_dir = run_config.workdir / "figures"
    logs_dir = run_config.workdir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    provider = make_provider(run_config)
    forcing = provider.fetch_forcing(domain=domain, duration_hours=run_config.duration_hours, step_hours=run_config.step_hours)
    (run_config.workdir / "forcing.json").write_text(json.dumps(forcing.to_serializable(), indent=2))

    runner = ElmfireRunner(executable_command=run_config.elmfire_cmd)
    benchmark_status = runner.run(case_dir=case_dir, domain=domain, forcing=forcing)
    if benchmark_status.run_completed:
        benchmark_result = None
    else:
        benchmark_result = build_proxy_benchmark(forcing=forcing, domain=domain)

    regime_result = RegimeAwareModel().run(forcing=forcing, domain=domain)
    figure_path = create_comparison_figure(
        forcing=forcing,
        benchmark_status=benchmark_status,
        regime_result=regime_result,
        benchmark_result=benchmark_result,
        output_path=figure_dir / "elmfire_vs_regime_model.png",
        title="ELMFIRE benchmark scaffold vs regime-aware fire model",
    )
    map_figure_path = None
    if benchmark_status.run_completed:
        map_figure_path = create_elmfire_time_sequence_map(
            case_dir=case_dir,
            forcing=forcing,
            domain=domain,
            benchmark_status=benchmark_status,
            output_path=figure_dir / "elmfire_time_sequence_map.png",
            title="ELMFIRE time-sequence map and labeled run parameters",
        )
    status_path = run_config.workdir / "pipeline_status.json"
    status_payload = {
        "forcing_source": forcing.source_name,
        "benchmark_type": benchmark_status.benchmark_type,
        "benchmark_status": benchmark_status.status,
        "benchmark_message": benchmark_status.message,
        "figure_path": str(figure_path),
        "map_figure_path": str(map_figure_path) if map_figure_path is not None else None,
        "case_dir": str(benchmark_status.case_artifacts.case_dir),
        "proxy_used_for_plotting": bool(benchmark_result is not None and benchmark_result.is_proxy),
    }
    status_path.write_text(json.dumps(status_payload, indent=2))
    LOGGER.info("Saved comparison figure to %s", figure_path)
    return PipelineOutputs(
        forcing_source=forcing.source_name,
        benchmark_status=benchmark_status,
        regime_result=regime_result,
        benchmark_result=benchmark_result,
        figure_path=figure_path,
        map_figure_path=map_figure_path,
        workdir=run_config.workdir,
        status_path=status_path,
    )


def run_extreme_conditions_panel(
    provider_name: str,
    workdir: Path,
    elmfire_cmd: str,
    duration_hours: float = 12.0,
    step_hours: float = 3.0,
) -> ExtremePanelOutputs:
    """Run a column-wise panel of ELMFIRE cases across extreme-condition scenarios."""

    if not elmfire_cmd:
        raise ValueError("A real ELMFIRE executable is required for the extremes panel.")

    configure_logging()
    maybe_warn_about_platform()
    run_config = RunConfig(provider=provider_name, workdir=Path(workdir), elmfire_cmd=elmfire_cmd, duration_hours=duration_hours, step_hours=step_hours)
    run_config.workdir.mkdir(parents=True, exist_ok=True)
    domain = DomainConfig(
        nx=700,
        ny=700,
        width_km=21.0,
        height_km=21.0,
        ignition_x_m=5_250.0,
        ignition_y_m=15_750.0,
    )
    provider = make_provider(run_config)
    baseline = provider.fetch_forcing(domain=domain, duration_hours=run_config.duration_hours, step_hours=run_config.step_hours)
    scenarios = build_extreme_forcing_scenarios(baseline)

    runner = ElmfireRunner(executable_command=run_config.elmfire_cmd)
    scenario_runs: list[ExtremeScenarioRun] = []
    scenarios_root = run_config.workdir / "scenarios"
    scenarios_root.mkdir(parents=True, exist_ok=True)
    for scenario in scenarios:
        scenario_root = scenarios_root / scenario["slug"]
        scenario_root.mkdir(parents=True, exist_ok=True)
        forcing = scenario["forcing"]
        (scenario_root / "forcing.json").write_text(json.dumps(forcing.to_serializable(), indent=2))
        benchmark_status = runner.run(case_dir=scenario_root / "case", domain=domain, forcing=forcing)
        scenario_runs.append(
            ExtremeScenarioRun(
                slug=scenario["slug"],
                title=scenario["title"],
                description=scenario["description"],
                forcing=forcing,
                benchmark_status=benchmark_status,
            )
        )

    figure_path = create_extreme_conditions_panel(
        scenario_runs=scenario_runs,
        snapshot_hours=baseline.time_hours,
        domain=domain,
        output_path=run_config.workdir / "figures" / "extreme_conditions_panel.png",
        title="ELMFIRE simulations with extreme weather that produce 1/2 scaling",
    )
    status_path = run_config.workdir / "extreme_conditions_panel_status.json"
    status_payload = {
        "forcing_source": baseline.source_name,
        "figure_path": str(figure_path),
        "scenario_statuses": [
            {
                "slug": run.slug,
                "title": run.title,
                "description": run.description,
                "benchmark_status": run.benchmark_status.status,
                "case_dir": str(run.benchmark_status.case_artifacts.case_dir),
                "forcing_summary": run.forcing.weather_summary(),
            }
            for run in scenario_runs
        ],
    }
    status_path.write_text(json.dumps(status_payload, indent=2))
    return ExtremePanelOutputs(
        forcing_source=baseline.source_name,
        scenario_runs=scenario_runs,
        figure_path=figure_path,
        workdir=run_config.workdir,
        status_path=status_path,
    )


def make_provider(run_config: RunConfig):
    """Construct the requested forcing provider."""

    if run_config.provider == "mock":
        return MockEarth2Provider()
    if run_config.provider == "earth2":
        return Earth2StudioGEFSProvider(member=run_config.benchmark_member)
    raise ValueError(f"Unknown provider: {run_config.provider}")


def maybe_warn_about_platform() -> None:
    """Warn on platforms where local NVIDIA-centric workflows are not expected."""

    if platform.system() == "Darwin":
        LOGGER.warning(
            "Running on macOS. Local Earth-2 CorrDiff-style inference is not expected here; "
            "a Linux/NVIDIA environment may be needed for later acceleration workflows."
        )


def explain_provider_error(exc: Exception) -> str:
    """Return a user-facing provider fallback hint."""

    if isinstance(exc, (Earth2StudioUnavailable, Earth2StudioFetchError)):
        return f"{exc} Suggestion: rerun with --provider mock for the local proof of concept."
    return str(exc)


def build_extreme_forcing_scenarios(base_forcing):
    """Create a small gradient of extreme-condition manifestations from a baseline forcing."""

    gust_profile = np.array([1.0, 1.35, 1.8, 1.45, 1.15], dtype=float)
    downburst_profile = np.array([1.2, 1.9, 2.4, 1.7, 1.2], dtype=float)
    return [
        {
            "slug": "baseline",
            "title": "Baseline",
            "description": "Unmodified Earth2/GEFS forcing",
            "forcing": clone_forcing(
                base_forcing,
                metadata_updates={
                    "scenario": "baseline",
                    "heterogeneity_strength": 0.20,
                    "wind_streak_strength": 0.15,
                    "dryness_patch_strength": 0.10,
                    "canopy_patchiness_pct": 10,
                    "slope_variability_deg": 5.0,
                },
            ),
        },
        {
            "slug": "downburst",
            "title": "Downburst Forcing",
            "description": "Strong downward wind forcing with high surface coupling",
            "forcing": clone_forcing(
                base_forcing,
                wind_speed_profile=downburst_profile,
                wind_direction_mode_deg=262.0,
                relative_humidity_scale=0.72,
                temperature_offset_c=4.0,
                metadata_updates={
                    "scenario": "downburst",
                    "adj_scale": 2.8,
                    "phi_scale": 2.0,
                    "heterogeneity_strength": 0.35,
                    "gust_corridor_strength": 1.55,
                    "wind_streak_strength": 0.70,
                    "dryness_patch_strength": 0.45,
                    "canopy_patchiness_pct": 8,
                    "slope_variability_deg": 8.0,
                    "canopy_cover_pct": 5,
                    "canopy_height_x10_m": 1,
                    "canopy_base_height_x10_m": 0,
                    "canopy_bulk_density_x100": 2,
                },
            ),
        },
        {
            "slug": "directional_gusts",
            "title": "Directional Gust Front",
            "description": "Strong directional wind with repeated gust pulses",
            "forcing": clone_forcing(
                base_forcing,
                wind_speed_profile=gust_profile * 2.1,
                wind_direction_mode_deg=255.0,
                relative_humidity_scale=0.68,
                temperature_offset_c=3.5,
                metadata_updates={
                    "scenario": "directional_gusts",
                    "adj_scale": 1.9,
                    "phi_scale": 1.7,
                    "heterogeneity_strength": 0.30,
                    "gust_corridor_strength": 1.05,
                    "wind_streak_strength": 1.30,
                    "dryness_patch_strength": 0.35,
                    "canopy_patchiness_pct": 10,
                    "slope_variability_deg": 7.0,
                    "canopy_cover_pct": 8,
                    "canopy_height_x10_m": 1,
                    "canopy_base_height_x10_m": 0,
                    "canopy_bulk_density_x100": 2,
                },
            ),
        },
        {
            "slug": "light_dry_fuels",
            "title": "Light Dry Fuels",
            "description": "Open fine fuels with critically low dead-fuel moisture",
            "forcing": clone_forcing(
                base_forcing,
                wind_speed_scale=1.35,
                temperature_offset_c=9.0,
                relative_humidity_scale=0.32,
                pressure_offset_pa=-900.0,
                metadata_updates={
                    "scenario": "light_dry_fuels",
                    "adj_scale": 1.5,
                    "phi_scale": 1.45,
                    "heterogeneity_strength": 0.35,
                    "gust_corridor_strength": 0.45,
                    "wind_streak_strength": 0.55,
                    "dryness_patch_strength": 1.25,
                    "canopy_patchiness_pct": 6,
                    "slope_variability_deg": 6.0,
                    "m1_offset_pct": -5.0,
                    "m10_offset_pct": -4.0,
                    "m100_offset_pct": -3.0,
                    "fuel_model_code": 101,
                    "canopy_cover_pct": 0,
                    "canopy_height_x10_m": 0,
                    "canopy_base_height_x10_m": 0,
                    "canopy_bulk_density_x100": 0,
                },
            ),
        },
        {
            "slug": "compound_blowup",
            "title": "Compound Blowup",
            "description": "Downburst-like coupling, gusts, and light dry fine fuels together",
            "forcing": clone_forcing(
                base_forcing,
                wind_speed_profile=downburst_profile * 2.25,
                wind_direction_mode_deg=258.0,
                temperature_offset_c=12.0,
                relative_humidity_scale=0.24,
                pressure_offset_pa=-1200.0,
                metadata_updates={
                    "scenario": "compound_blowup",
                    "adj_scale": 3.4,
                    "phi_scale": 2.4,
                    "heterogeneity_strength": 0.45,
                    "gust_corridor_strength": 1.75,
                    "wind_streak_strength": 1.45,
                    "dryness_patch_strength": 1.35,
                    "canopy_patchiness_pct": 4,
                    "slope_variability_deg": 9.0,
                    "m1_offset_pct": -7.0,
                    "m10_offset_pct": -5.0,
                    "m100_offset_pct": -4.0,
                    "fuel_model_code": 101,
                    "canopy_cover_pct": 0,
                    "canopy_height_x10_m": 0,
                    "canopy_base_height_x10_m": 0,
                    "canopy_bulk_density_x100": 0,
                },
            ),
        },
    ]


def clone_forcing(
    base_forcing,
    wind_speed_scale: float = 1.0,
    wind_speed_profile: np.ndarray | None = None,
    temperature_offset_c: float = 0.0,
    relative_humidity_scale: float = 1.0,
    pressure_offset_pa: float = 0.0,
    wind_direction_offset_deg: float = 0.0,
    wind_direction_mode_deg: float | None = None,
    metadata_updates: dict[str, Any] | None = None,
):
    """Copy a forcing object with simple transparent perturbations."""

    metadata = dict(base_forcing.metadata)
    if metadata_updates:
        metadata.update(metadata_updates)
    if wind_speed_profile is None:
        wind_speed = np.clip(base_forcing.wind_speed_mps * wind_speed_scale, 0.0, None)
    else:
        profile = np.asarray(wind_speed_profile, dtype=float)
        if profile.shape != base_forcing.wind_speed_mps.shape:
            raise ValueError("wind_speed_profile must match the forcing time dimension.")
        wind_speed = np.clip(base_forcing.wind_speed_mps * profile, 0.0, None)
    if wind_direction_mode_deg is None:
        wind_direction = (base_forcing.wind_direction_deg_from + wind_direction_offset_deg) % 360.0
    else:
        wind_direction = np.full_like(base_forcing.wind_direction_deg_from, float(wind_direction_mode_deg))
    return type(base_forcing)(
        time_hours=base_forcing.time_hours.copy(),
        wind_speed_mps=wind_speed,
        wind_direction_deg_from=wind_direction,
        temperature_c=base_forcing.temperature_c + temperature_offset_c,
        relative_humidity_pct=np.clip(base_forcing.relative_humidity_pct * relative_humidity_scale, 5.0, 100.0),
        pressure_pa=base_forcing.pressure_pa + pressure_offset_pa,
        precipitation_mmhr=base_forcing.precipitation_mmhr.copy(),
        source_name=base_forcing.source_name,
        metadata=metadata,
    )
