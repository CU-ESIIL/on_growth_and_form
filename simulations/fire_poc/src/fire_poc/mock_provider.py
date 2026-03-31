"""Deterministic synthetic forcing provider."""

from __future__ import annotations

import numpy as np

from .config import DomainConfig, Forcing
from .forcing import WeatherProvider, build_time_hours


class MockEarth2Provider(WeatherProvider):
    """Always-available deterministic synthetic weather."""

    name = "mock"

    def fetch_forcing(
        self,
        domain: DomainConfig,
        duration_hours: float,
        step_hours: float,
    ) -> Forcing:
        time_hours = build_time_hours(duration_hours, step_hours)
        phase = time_hours / max(duration_hours, 1.0)
        wind_speed = 4.5 + 2.0 * np.sin(2.0 * np.pi * phase) + 0.45 * time_hours
        wind_direction = (225.0 + 20.0 * np.sin(np.pi * phase)) % 360.0
        temperature_c = 20.0 + 7.0 * np.sin(np.pi * phase)
        relative_humidity = 48.0 - 12.0 * np.sin(np.pi * phase) + 4.0 * np.cos(2.0 * np.pi * phase)
        pressure_pa = np.full_like(time_hours, 82_500.0)
        precipitation = np.where((time_hours >= duration_hours * 0.6) & (time_hours <= duration_hours * 0.75), 0.3, 0.0)
        return Forcing(
            time_hours=time_hours,
            wind_speed_mps=wind_speed,
            wind_direction_deg_from=wind_direction,
            temperature_c=temperature_c,
            relative_humidity_pct=np.clip(relative_humidity, 12.0, 95.0),
            pressure_pa=pressure_pa,
            precipitation_mmhr=precipitation,
            source_name="mock",
            metadata={
                "provider": self.name,
                "description": "Deterministic synthetic forcing for local proof-of-concept runs.",
                "domain_center": [domain.center_lat, domain.center_lon],
            },
        )

