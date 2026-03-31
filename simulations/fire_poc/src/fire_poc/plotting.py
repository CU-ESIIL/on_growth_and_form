"""Plotting utilities for the comparison figure."""

from __future__ import annotations

from dataclasses import dataclass
import csv
import os
from pathlib import Path
from typing import Any

os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from .config import DomainConfig, Forcing
from .elmfire_runner import BenchmarkStatus
from .regime_model import FireModelResult


def create_comparison_figure(
    forcing: Forcing,
    benchmark_status: BenchmarkStatus,
    regime_result: FireModelResult,
    benchmark_result: FireModelResult | None,
    output_path: Path,
    title: str,
) -> Path:
    """Create and save the main proof-of-concept figure."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 3, height_ratios=[1.0, 1.2, 1.2])
    ax_forcing = fig.add_subplot(gs[0, :])
    ax_overlay = fig.add_subplot(gs[1, 0])
    ax_area = fig.add_subplot(gs[1, 1:])
    snapshot_axes = [fig.add_subplot(gs[2, i]) for i in range(3)]

    _plot_forcing(ax_forcing, forcing)
    _plot_overlay(ax_overlay, regime_result, benchmark_result, benchmark_status)
    _plot_area(ax_area, regime_result, benchmark_result, benchmark_status)
    _plot_snapshots(snapshot_axes, regime_result, benchmark_result, benchmark_status)

    fig.suptitle(title, fontsize=15)
    fig.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_elmfire_time_sequence_map(
    case_dir: Path,
    forcing: Forcing,
    domain: DomainConfig,
    benchmark_status: BenchmarkStatus,
    output_path: Path,
    title: str,
) -> Path | None:
    """Create a labeled ELMFIRE time-sequence map from real output rasters."""

    case_dir = Path(case_dir)
    toa_path = _find_single_output(case_dir / "outputs", "time_of_arrival_*.bil")
    stats_path = _find_single_output(case_dir / "outputs", "fire_size_stats.csv")
    if toa_path is None or stats_path is None:
        return None

    toa_seconds, hdr = _read_envi_bil_float(toa_path)
    toa_hours = _orient_raster_for_plotting(np.where(toa_seconds > 0.0, toa_seconds / 3600.0, np.nan))
    x_coords, y_coords, extent = _grid_coordinates(hdr)
    stats = _read_fire_size_stats(stats_path)
    snapshot_times = forcing.time_hours.copy()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 3, width_ratios=[1.0, 1.0, 0.9], hspace=0.25, wspace=0.2)
    map_axes = [fig.add_subplot(gs[i // 2, i % 2]) for i in range(4)]
    ax_final = fig.add_subplot(gs[:, 2])

    cmap = plt.get_cmap("YlOrRd")
    finite_toa = toa_hours[np.isfinite(toa_hours)]
    vmax = float(np.nanmax(finite_toa)) if finite_toa.size else float(snapshot_times[-1])

    indices = np.linspace(0, len(snapshot_times) - 1, len(map_axes), dtype=int)
    for ax, idx in zip(map_axes, indices):
        snapshot_hr = float(snapshot_times[idx])
        burned = np.isfinite(toa_hours) & (toa_hours <= snapshot_hr + 1e-9)
        masked_toa = np.ma.masked_where(~burned, toa_hours)
        ax.imshow(masked_toa, extent=extent, origin="lower", cmap=cmap, vmin=0.0, vmax=vmax)
        if np.any(burned):
            ax.contour(x_coords, y_coords, burned.astype(float), levels=[0.5], colors="black", linewidths=1.1)
        ax.scatter(
            domain.origin_x + domain.ignition_x_m,
            domain.origin_y + domain.ignition_y_m,
            marker="*",
            s=90,
            color="cyan",
            edgecolor="black",
            linewidth=0.8,
            zorder=3,
        )
        ax.set_title(f"Arrival by {snapshot_hr:.0f} h")
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("Easting (m)")
        if idx in indices[:2]:
            ax.set_ylabel("Northing (m)")
        ax.grid(True, alpha=0.15)

    ax_final.axis("off")
    parameter_text = _format_parameter_panel(
        forcing=forcing,
        domain=domain,
        benchmark_status=benchmark_status,
        stats=stats,
        hdr=hdr,
    )
    ax_final.text(
        0.0,
        1.0,
        parameter_text,
        va="top",
        ha="left",
        fontsize=10,
        family="monospace",
        linespacing=1.35,
    )

    fig.suptitle(title, fontsize=16)
    cbar_ax = fig.add_axes([0.12, 0.08, 0.42, 0.02])
    mappable = matplotlib.cm.ScalarMappable(cmap=cmap)
    mappable.set_clim(0.0, vmax)
    cbar = fig.colorbar(mappable, cax=cbar_ax, orientation="horizontal")
    cbar.set_label("Time of arrival (hours)")
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_extreme_conditions_panel(
    scenario_runs: list[Any],
    snapshot_hours: np.ndarray,
    domain: DomainConfig,
    output_path: Path,
    title: str,
) -> Path:
    """Create a multi-column map panel across extreme-condition scenarios."""

    scenarios = []
    vmax = 0.0
    for run in scenario_runs:
        toa_path = _find_single_output(Path(run.benchmark_status.case_artifacts.case_dir) / "outputs", "time_of_arrival_*.bil")
        stats_path = _find_single_output(Path(run.benchmark_status.case_artifacts.case_dir) / "outputs", "fire_size_stats.csv")
        toa_hours = None
        hdr = None
        stats = {}
        if toa_path is not None and stats_path is not None:
            toa_seconds, hdr = _read_envi_bil_float(toa_path)
            toa_hours = _orient_raster_for_plotting(np.where(toa_seconds > 0.0, toa_seconds / 3600.0, np.nan))
            finite = toa_hours[np.isfinite(toa_hours)]
            if finite.size:
                vmax = max(vmax, float(np.nanmax(finite)))
            stats = _read_fire_size_stats(stats_path)
        scenarios.append(
            {
                "run": run,
                "toa_hours": toa_hours,
                "hdr": hdr,
                "stats": stats,
            }
        )

    vmax = max(vmax, float(snapshot_hours[-1]))
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ncols = len(scenarios)
    map_rows = len(snapshot_hours)
    nrows = map_rows + 1
    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=(4.1 * ncols, 3.0 * nrows),
        squeeze=False,
        gridspec_kw={"height_ratios": [1.0] * map_rows + [0.95]},
    )
    cmap = plt.get_cmap("YlOrRd")

    for col, scenario in enumerate(scenarios):
        run = scenario["run"]
        forcing = run.forcing
        toa_hours = scenario["toa_hours"]
        hdr = scenario["hdr"]
        stats = scenario["stats"]
        if toa_hours is not None and hdr is not None:
            x_coords, y_coords, extent = _grid_coordinates(hdr)
            x_limits, y_limits = _burned_extent_limits(
                toa_hours=toa_hours,
                x_coords=x_coords,
                y_coords=y_coords,
                ignition_x=domain.origin_x + domain.ignition_x_m,
                ignition_y=domain.origin_y + domain.ignition_y_m,
            )
            scaling = _scaling_metrics_from_toa(
                toa_hours=toa_hours,
                snapshot_hours=snapshot_hours,
                cell_size_m=domain.cell_size_m,
            )
        else:
            x_coords = y_coords = extent = x_limits = y_limits = scaling = None
        summary = (
            f"{run.title}\n"
            f"{run.description}\n"
            f"W {np.min(forcing.wind_speed_mps):.1f}-{np.max(forcing.wind_speed_mps):.1f} m/s | "
            f"T {np.min(forcing.temperature_c):.1f}-{np.max(forcing.temperature_c):.1f} C | "
            f"RH {np.min(forcing.relative_humidity_pct):.0f}-{np.max(forcing.relative_humidity_pct):.0f}%\n"
            f"Final area {stats.get('Total fire area (ac)', 'n/a')} ac"
        )
        axes[0, col].set_title(summary, fontsize=9)
        for row, snapshot_hr in enumerate(snapshot_hours):
            ax = axes[row, col]
            if toa_hours is None or hdr is None:
                ax.axis("off")
                ax.text(0.5, 0.5, f"{run.benchmark_status.status}", ha="center", va="center", transform=ax.transAxes)
                continue
            burned = np.isfinite(toa_hours) & (toa_hours <= float(snapshot_hr) + 1e-9)
            masked = np.ma.masked_where(~burned, toa_hours)
            ax.imshow(masked, extent=extent, origin="lower", cmap=cmap, vmin=0.0, vmax=vmax)
            if np.any(burned):
                ax.contour(x_coords, y_coords, burned.astype(float), levels=[0.5], colors="black", linewidths=0.85)
            ax.scatter(
                domain.origin_x + domain.ignition_x_m,
                domain.origin_y + domain.ignition_y_m,
                marker="*",
                s=60,
                color="cyan",
                edgecolor="black",
                linewidth=0.7,
                zorder=3,
            )
            if col == 0:
                ax.set_ylabel(f"{snapshot_hr:.0f} h\nNorthing (m)")
            if row == nrows - 1:
                ax.set_xlabel("Easting (m)")
            ax.set_aspect("equal", adjustable="box")
            if x_limits is not None and y_limits is not None:
                ax.set_xlim(*x_limits)
                ax.set_ylim(*y_limits)
            ax.grid(True, alpha=0.12)
            ax.tick_params(labelsize=8)
            ax.text(
                0.03,
                0.97,
                f"{snapshot_hr:.0f} h",
                transform=ax.transAxes,
                va="top",
                ha="left",
                fontsize=8,
                bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none", "pad": 1.5},
            )

        scaling_ax = axes[map_rows, col]
        if scaling is None or scaling["valid"].sum() < 2:
            scaling_ax.axis("off")
            scaling_ax.text(0.5, 0.5, "Not enough burned snapshots", ha="center", va="center", transform=scaling_ax.transAxes)
            continue
        area = scaling["area_m2"][scaling["valid"]]
        perimeter = scaling["perimeter_m"][scaling["valid"]]
        area_ref = np.geomspace(float(np.min(area)), float(np.max(area)), 100)
        area_anchor = float(area[0])
        perimeter_anchor = float(perimeter[0])
        ref_half = perimeter_anchor * (area_ref / area_anchor) ** (0.5)
        ref_two_thirds = perimeter_anchor * (area_ref / area_anchor) ** (2.0 / 3.0)
        beta = float(np.polyfit(np.log10(area), np.log10(perimeter), 1)[0])
        scaling_ax.loglog(area, perimeter, marker="o", color="tab:orange", linewidth=1.8, markersize=4)
        scaling_ax.loglog(area_ref, ref_half, linestyle="--", color="0.45", linewidth=1.0, label=r"$P \sim A^{1/2}$")
        scaling_ax.loglog(area_ref, ref_two_thirds, linestyle=":", color="0.25", linewidth=1.2, label=r"$P \sim A^{2/3}$")
        scaling_ax.grid(True, alpha=0.18, which="both")
        scaling_ax.tick_params(labelsize=8)
        scaling_ax.set_xlabel(r"log Area ($m^2$)", fontsize=8)
        if col == 0:
            scaling_ax.set_ylabel("log Perimeter (m)", fontsize=8)
        scaling_ax.text(
            0.04,
            0.08,
            rf"$\beta \approx {beta:.2f}$",
            transform=scaling_ax.transAxes,
            fontsize=8,
            bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none", "pad": 1.5},
        )
        if col == 0:
            scaling_ax.legend(loc="upper right", fontsize=7, frameon=True)

    fig.suptitle(title, fontsize=16)
    footer = (
        f"Common setup: {domain.nx}x{domain.ny} cells at {domain.cell_size_m:.0f} m, {domain.crs}, "
        f"ignition=({domain.origin_x + domain.ignition_x_m:.0f}, {domain.origin_y + domain.ignition_y_m:.0f}) m, "
        "Earth2/GEFS baseline perturbed into explicit extreme-condition scenarios; each column auto-frames the final burned extent, "
        "and the final row shows log(P) vs log(A) with reference slopes for P~A^(1/2) and P~A^(2/3)."
    )
    fig.text(0.02, 0.02, footer, fontsize=9)
    cbar_ax = fig.add_axes([0.2, 0.05, 0.6, 0.02])
    mappable = matplotlib.cm.ScalarMappable(cmap=cmap)
    mappable.set_clim(0.0, vmax)
    cbar = fig.colorbar(mappable, cax=cbar_ax, orientation="horizontal")
    cbar.set_label("Time of arrival (hours)")
    fig.tight_layout(rect=[0, 0.08, 1, 0.94])
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return output_path


def _plot_forcing(ax, forcing: Forcing) -> None:
    time_hours = forcing.time_hours
    ax.plot(time_hours, forcing.wind_speed_mps, label="Wind speed (m/s)", color="tab:blue", linewidth=2)
    ax.plot(time_hours, forcing.relative_humidity_pct, label="RH (%)", color="tab:green", linewidth=2)
    ax.plot(time_hours, forcing.temperature_c, label="Temperature (C)", color="tab:red", linewidth=2)
    ax.set_title(f"Forcing: {forcing.source_name}")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", ncol=3)


def _plot_overlay(ax, regime_result: FireModelResult, benchmark_result: FireModelResult | None, benchmark_status: BenchmarkStatus) -> None:
    ax.plot(regime_result.perimeters_xy[-1][:, 0], regime_result.perimeters_xy[-1][:, 1], label="Regime-aware model", color="tab:orange", linewidth=2)
    if benchmark_result is not None:
        label = "Proxy benchmark" if benchmark_result.is_proxy else "Benchmark perimeter"
        ax.plot(benchmark_result.perimeters_xy[-1][:, 0], benchmark_result.perimeters_xy[-1][:, 1], label=label, color="tab:blue", linewidth=2)
    ax.set_title(f"Final perimeter overlay\nBenchmark status: {benchmark_status.benchmark_type}")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.2)
    ax.legend(loc="upper right")


def _plot_area(ax, regime_result: FireModelResult, benchmark_result: FireModelResult | None, benchmark_status: BenchmarkStatus) -> None:
    ax.plot(regime_result.times_hours, regime_result.areas_m2 / 10_000.0, label="Regime-aware model", color="tab:orange", linewidth=2)
    if benchmark_result is not None:
        label = "Proxy benchmark" if benchmark_result.is_proxy else benchmark_status.benchmark_type
        ax.plot(benchmark_result.times_hours, benchmark_result.areas_m2 / 10_000.0, label=label, color="tab:blue", linewidth=2, linestyle="--")
    else:
        ax.text(0.03, 0.9, "No benchmark perimeter products available.", transform=ax.transAxes)
    ax.set_title("Area through time")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Area (ha)")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left")


def _plot_snapshots(snapshot_axes, regime_result: FireModelResult, benchmark_result: FireModelResult | None, benchmark_status: BenchmarkStatus) -> None:
    indices = np.linspace(0, len(regime_result.times_hours) - 1, len(snapshot_axes), dtype=int)
    for ax, idx in zip(snapshot_axes, indices):
        ax.plot(regime_result.perimeters_xy[idx][:, 0], regime_result.perimeters_xy[idx][:, 1], color="tab:orange", label="Regime-aware")
        if benchmark_result is not None:
            label = "Proxy" if benchmark_result.is_proxy else "Benchmark"
            ax.plot(benchmark_result.perimeters_xy[idx][:, 0], benchmark_result.perimeters_xy[idx][:, 1], color="tab:blue", linestyle="--", label=label)
        ax.set_title(f"t = {regime_result.times_hours[idx]:.1f} h")
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True, alpha=0.2)
        if idx == indices[0]:
            ax.legend(loc="upper right")
    snapshot_axes[0].set_ylabel(f"Status: {benchmark_status.status}")


def _find_single_output(outputs_dir: Path, pattern: str) -> Path | None:
    matches = list(outputs_dir.glob(pattern))
    if not matches:
        return None
    return max(matches, key=lambda path: (path.stat().st_mtime_ns, path.name))


def _read_fire_size_stats(path: Path) -> dict[str, str]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            return {key.strip(): value.strip() for key, value in row.items() if key is not None}
    return {}


def _read_envi_bil_float(path: Path) -> tuple[np.ndarray, dict[str, float | int | str]]:
    hdr_path = path.with_suffix(".hdr")
    header: dict[str, float | int | str] = {}
    for line in hdr_path.read_text().splitlines():
        if not line.strip():
            continue
        key, value = line.split(maxsplit=1)
        key = key.strip().lower()
        value = value.strip()
        if key in {"nrows", "ncols", "nbands", "nbits", "bandrowbytes", "totalrowbytes"}:
            header[key] = int(value)
        elif key in {"ulxmap", "ulymap", "xdim", "ydim", "nodata"}:
            header[key] = float(value)
        else:
            header[key] = value
    nrows = int(header["nrows"])
    ncols = int(header["ncols"])
    nbands = int(header["nbands"])
    dtype = np.float32 if int(header["nbits"]) == 32 else np.float64
    data = np.fromfile(path, dtype=dtype)
    if nbands == 1:
        array = data.reshape((nrows, ncols))
    else:
        array = data.reshape((nrows, nbands, ncols))[:, 0, :]
    return array, header


def _orient_raster_for_plotting(array: np.ndarray) -> np.ndarray:
    """Flip top-origin ENVI rasters so row 0 maps to the lower edge of the plot."""

    return np.flipud(np.asarray(array))


def _grid_coordinates(hdr: dict[str, float | int | str]) -> tuple[np.ndarray, np.ndarray, list[float]]:
    nrows = int(hdr["nrows"])
    ncols = int(hdr["ncols"])
    xdim = float(hdr["xdim"])
    ydim = float(hdr["ydim"])
    ulx = float(hdr["ulxmap"])
    uly = float(hdr["ulymap"])
    x_centers = ulx + np.arange(ncols) * xdim
    y_centers = uly - np.arange(nrows) * ydim
    x_min = ulx - 0.5 * xdim
    x_max = x_centers[-1] + 0.5 * xdim
    y_max = uly + 0.5 * ydim
    y_min = y_centers[-1] - 0.5 * ydim
    return x_centers, y_centers[::-1], [x_min, x_max, y_min, y_max]


def _format_parameter_panel(
    forcing: Forcing,
    domain: DomainConfig,
    benchmark_status: BenchmarkStatus,
    stats: dict[str, str],
    hdr: dict[str, float | int | str],
) -> str:
    wind_min = np.min(forcing.wind_speed_mps)
    wind_max = np.max(forcing.wind_speed_mps)
    temp_min = np.min(forcing.temperature_c)
    temp_max = np.max(forcing.temperature_c)
    rh_min = np.min(forcing.relative_humidity_pct)
    rh_max = np.max(forcing.relative_humidity_pct)
    direction_start = forcing.wind_direction_deg_from[0]
    direction_end = forcing.wind_direction_deg_from[-1]
    metadata = forcing.metadata
    lines = [
        "Run Parameters",
        f"Benchmark: {benchmark_status.benchmark_type}",
        f"Status: {benchmark_status.status}",
        f"Forcing: {forcing.source_name}",
    ]
    if metadata:
        if metadata.get("member"):
            lines.append(f"GEFS member: {metadata['member']}")
        if metadata.get("init_time_utc"):
            lines.append(f"Init UTC: {metadata['init_time_utc']}")
    lines += [
        "",
        "Domain",
        f"Grid: {domain.nx} x {domain.ny} cells",
        f"Cell size: {domain.cell_size_m:.1f} m",
        f"CRS: {domain.crs}",
        f"Origin: ({domain.origin_x:.0f}, {domain.origin_y:.0f}) m",
        f"Ignition abs: ({domain.origin_x + domain.ignition_x_m:.0f}, {domain.origin_y + domain.ignition_y_m:.0f}) m",
        f"Raster UL: ({float(hdr['ulxmap']):.0f}, {float(hdr['ulymap']):.0f}) m",
        "",
        "Meteorology",
        f"Duration: {forcing.time_hours[-1]:.1f} h",
        f"DT_METEOROLOGY: {forcing.dt_hours:.1f} h",
        f"Wind: {wind_min:.2f} to {wind_max:.2f} m/s",
        f"Wind dir: {direction_start:.1f} to {direction_end:.1f} deg from",
        f"Temp: {temp_min:.1f} to {temp_max:.1f} C",
        f"RH: {rh_min:.1f} to {rh_max:.1f} %",
    ]
    if stats:
        lines += [
            "",
            "ELMFIRE Outputs",
            f"Final tstop: {stats.get('tstop (h)', 'n/a')} h",
            f"Total fire area: {stats.get('Total fire area (ac)', 'n/a')} ac",
            f"Crown fire area: {stats.get('Crown fire area (ac)', 'n/a')} ac",
            f"Fire volume: {stats.get('Fire volume (ac-ft)', 'n/a')} ac-ft",
            f"Wall time: {stats.get('Wall clock time (s)', 'n/a')} s",
            f"Cases: {stats.get('icase', 'n/a')}",
            f"Meteorology band: {stats.get('Meteorology band', 'n/a')}",
        ]
    return "\n".join(lines)


def _burned_extent_limits(
    toa_hours: np.ndarray,
    x_coords: np.ndarray,
    y_coords: np.ndarray,
    ignition_x: float,
    ignition_y: float,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Return padded plot limits centered on the final burned extent for one scenario."""

    burned = np.isfinite(toa_hours)
    x_min_domain = float(x_coords[0])
    x_max_domain = float(x_coords[-1])
    y_min_domain = float(y_coords[0])
    y_max_domain = float(y_coords[-1])
    if not np.any(burned):
        return (x_min_domain, x_max_domain), (y_min_domain, y_max_domain)

    row_mask = burned.any(axis=1)
    col_mask = burned.any(axis=0)
    y_burned = y_coords[row_mask]
    x_burned = x_coords[col_mask]
    x_min = min(float(x_burned[0]), ignition_x)
    x_max = max(float(x_burned[-1]), ignition_x)
    y_min = min(float(y_burned[0]), ignition_y)
    y_max = max(float(y_burned[-1]), ignition_y)
    span = max(x_max - x_min, y_max - y_min, 2400.0)
    pad = max(0.18 * span, 450.0)
    half = 0.5 * span + pad
    x_center = 0.5 * (x_min + x_max)
    y_center = 0.5 * (y_min + y_max)
    x_limits = (max(x_min_domain, x_center - half), min(x_max_domain, x_center + half))
    y_limits = (max(y_min_domain, y_center - half), min(y_max_domain, y_center + half))
    return x_limits, y_limits


def _scaling_metrics_from_toa(
    toa_hours: np.ndarray,
    snapshot_hours: np.ndarray,
    cell_size_m: float,
) -> dict[str, np.ndarray]:
    """Compute raster-based area, perimeter, and perimeter/area ratio through snapshot time."""

    areas = []
    perimeters = []
    ratios = []
    for snapshot_hr in snapshot_hours:
        burned = np.isfinite(toa_hours) & (toa_hours <= float(snapshot_hr) + 1e-9)
        area_m2, perimeter_m = _burned_area_and_perimeter(burned, cell_size_m)
        areas.append(area_m2)
        perimeters.append(perimeter_m)
        ratios.append(perimeter_m / area_m2 if area_m2 > 0.0 else np.nan)
    area_arr = np.asarray(areas, dtype=float)
    perimeter_arr = np.asarray(perimeters, dtype=float)
    ratio_arr = np.asarray(ratios, dtype=float)
    valid = np.isfinite(ratio_arr) & (area_arr > 0.0) & (perimeter_arr > 0.0)
    return {
        "area_m2": area_arr,
        "perimeter_m": perimeter_arr,
        "perimeter_area_ratio": ratio_arr,
        "valid": valid,
    }


def _burned_area_and_perimeter(burned: np.ndarray, cell_size_m: float) -> tuple[float, float]:
    """Estimate burned area and perimeter from a boolean raster mask using exposed cell edges."""

    burned = np.asarray(burned, dtype=bool)
    if not np.any(burned):
        return 0.0, 0.0
    area_m2 = float(np.count_nonzero(burned) * (cell_size_m**2))
    edge_count = 0
    edge_count += int(np.count_nonzero(burned[0, :]))
    edge_count += int(np.count_nonzero(burned[-1, :]))
    edge_count += int(np.count_nonzero(burned[:, 0]))
    edge_count += int(np.count_nonzero(burned[:, -1]))
    edge_count += int(np.count_nonzero(burned[:, 1:] != burned[:, :-1]))
    edge_count += int(np.count_nonzero(burned[1:, :] != burned[:-1, :]))
    perimeter_m = float(edge_count * cell_size_m)
    return area_m2, perimeter_m
