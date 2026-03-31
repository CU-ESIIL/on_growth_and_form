"""Configuration models for the fire proof of concept."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np


@dataclass
class DomainConfig:
    """Idealized spatial domain for the proof of concept."""

    nx: int = 80
    ny: int = 80
    cell_size_m: float = 30.0
    origin_x: float = 500_000.0
    origin_y: float = 4_400_000.0
    crs: str = "EPSG:32613"
    center_lat: float = 39.5
    center_lon: float = -105.5
    width_km: float = 12.0
    height_km: float = 12.0
    ignition_x_m: float = 1_200.0
    ignition_y_m: float = 1_200.0


@dataclass
class RunConfig:
    """Runtime settings for the pipeline."""

    provider: str = "mock"
    duration_hours: float = 12.0
    step_hours: float = 1.0
    title: str = "ELMFIRE vs regime-aware fire model"
    workdir: Path = Path("outputs/demo")
    elmfire_cmd: str | None = None
    benchmark_member: str = "gec00"


@dataclass
class Forcing:
    """Common forcing container shared by all models."""

    time_hours: np.ndarray
    wind_speed_mps: np.ndarray
    wind_direction_deg_from: np.ndarray
    temperature_c: np.ndarray
    relative_humidity_pct: np.ndarray
    pressure_pa: np.ndarray
    precipitation_mmhr: np.ndarray
    source_name: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        arrays = [
            np.asarray(self.time_hours, dtype=float),
            np.asarray(self.wind_speed_mps, dtype=float),
            np.asarray(self.wind_direction_deg_from, dtype=float),
            np.asarray(self.temperature_c, dtype=float),
            np.asarray(self.relative_humidity_pct, dtype=float),
            np.asarray(self.pressure_pa, dtype=float),
            np.asarray(self.precipitation_mmhr, dtype=float),
        ]
        length = len(arrays[0])
        if length == 0:
            raise ValueError("Forcing arrays must not be empty.")
        if any(len(arr) != length for arr in arrays):
            raise ValueError("All forcing arrays must have the same length.")
        (
            self.time_hours,
            self.wind_speed_mps,
            self.wind_direction_deg_from,
            self.temperature_c,
            self.relative_humidity_pct,
            self.pressure_pa,
            self.precipitation_mmhr,
        ) = arrays

    @property
    def num_steps(self) -> int:
        return len(self.time_hours)

    @property
    def dt_hours(self) -> float:
        if self.num_steps < 2:
            return 0.0
        return float(self.time_hours[1] - self.time_hours[0])

    def weather_summary(self) -> dict[str, float]:
        """Return compact summary statistics for manifests and logs."""

        return {
            "n_steps": int(self.num_steps),
            "duration_hours": float(self.time_hours[-1]),
            "wind_speed_min_mps": float(np.min(self.wind_speed_mps)),
            "wind_speed_max_mps": float(np.max(self.wind_speed_mps)),
            "temperature_min_c": float(np.min(self.temperature_c)),
            "temperature_max_c": float(np.max(self.temperature_c)),
            "relative_humidity_min_pct": float(np.min(self.relative_humidity_pct)),
            "relative_humidity_max_pct": float(np.max(self.relative_humidity_pct)),
        }

    def to_serializable(self) -> dict[str, Any]:
        """Convert forcing arrays to plain Python objects."""

        return {
            "time_hours": self.time_hours.tolist(),
            "wind_speed_mps": self.wind_speed_mps.tolist(),
            "wind_direction_deg_from": self.wind_direction_deg_from.tolist(),
            "temperature_c": self.temperature_c.tolist(),
            "relative_humidity_pct": self.relative_humidity_pct.tolist(),
            "pressure_pa": self.pressure_pa.tolist(),
            "precipitation_mmhr": self.precipitation_mmhr.tolist(),
            "source_name": self.source_name,
            "metadata": self.metadata,
        }

