"""Weather-provider interfaces and shared forcing helpers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

import numpy as np

from .config import DomainConfig, Forcing


class WeatherProvider(ABC):
    """Abstract provider for weather forcing time series."""

    name: str = "abstract"

    @abstractmethod
    def fetch_forcing(
        self,
        domain: DomainConfig,
        duration_hours: float,
        step_hours: float,
    ) -> Forcing:
        """Fetch forcing for the requested domain and time span."""


def build_time_hours(duration_hours: float, step_hours: float) -> np.ndarray:
    """Create inclusive time stamps on a regular grid."""

    n_steps = int(round(duration_hours / step_hours)) + 1
    return np.linspace(0.0, duration_hours, n_steps)


def wind_uv_to_speed_dir(u10m: Iterable[float], v10m: Iterable[float]) -> tuple[np.ndarray, np.ndarray]:
    """Convert eastward/northward wind components to speed and meteorological direction."""

    u = np.asarray(list(u10m), dtype=float)
    v = np.asarray(list(v10m), dtype=float)
    speed = np.sqrt(u**2 + v**2)
    direction_from = (270.0 - np.degrees(np.arctan2(v, u))) % 360.0
    return speed, direction_from


def estimate_dead_fuel_moisture(relative_humidity_pct: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Map relative humidity to simple dead-fuel moisture proxies."""

    rh = np.clip(np.asarray(relative_humidity_pct, dtype=float), 5.0, 100.0)
    m1 = np.clip(2.0 + 0.12 * rh, 2.0, 18.0)
    m10 = np.clip(m1 + 2.0, 4.0, 22.0)
    m100 = np.clip(m10 + 3.0, 7.0, 28.0)
    return m1, m10, m100

