"""Pure Python regime-aware fire spread model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from .config import DomainConfig, Forcing
from .geometry import area_series, ellipse_perimeter


@dataclass
class FireModelResult:
    """Common fire-model output used by plotting and comparison."""

    model_name: str
    benchmark_label: str
    times_hours: np.ndarray
    perimeters_xy: list[np.ndarray]
    areas_m2: np.ndarray
    is_proxy: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


class RegimeAwareModel:
    """Simple model with a clear regime transition."""

    def __init__(self, wind_threshold_mps: float = 7.5, transition_time_hr: float = 5.0) -> None:
        self.wind_threshold_mps = wind_threshold_mps
        self.transition_time_hr = transition_time_hr

    def run(self, forcing: Forcing, domain: DomainConfig) -> FireModelResult:
        center = (domain.ignition_x_m, domain.ignition_y_m)
        perimeters: list[np.ndarray] = []
        cumulative_drive = np.cumsum(forcing.wind_speed_mps) * max(forcing.dt_hours, 1.0)
        regime_index = None
        for idx, time_hr in enumerate(forcing.time_hours):
            wind = forcing.wind_speed_mps[idx]
            transitioned = bool(wind >= self.wind_threshold_mps or time_hr >= self.transition_time_hr)
            if transitioned and regime_index is None:
                regime_index = idx
            major = 55.0 + cumulative_drive[idx] * (23.0 if transitioned else 14.0)
            minor = 35.0 + cumulative_drive[idx] * (9.5 if transitioned else 12.0)
            orientation = (forcing.wind_direction_deg_from[idx] + 180.0) % 360.0
            perimeters.append(ellipse_perimeter(center, major, minor, orientation))
        return FireModelResult(
            model_name="regime-aware model",
            benchmark_label="regime-aware model",
            times_hours=forcing.time_hours.copy(),
            perimeters_xy=perimeters,
            areas_m2=area_series(perimeters),
            metadata={
                "wind_threshold_mps": self.wind_threshold_mps,
                "transition_time_hr": self.transition_time_hr,
                "transition_index": regime_index,
            },
        )

