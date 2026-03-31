"""Earth2Studio-backed GEFS weather provider."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import math

import numpy as np

from .config import DomainConfig, Forcing
from .forcing import WeatherProvider, build_time_hours, wind_uv_to_speed_dir


class Earth2StudioUnavailable(RuntimeError):
    """Raised when Earth2Studio is not importable."""


class Earth2StudioFetchError(RuntimeError):
    """Raised when Earth2Studio import works but data fetch fails."""


class Earth2StudioGEFSProvider(WeatherProvider):
    """Fetch domain-mean GEFS weather from Earth2Studio when available."""

    name = "earth2"
    variables = ("u10m", "v10m", "t2m", "r2m", "sp")

    def __init__(self, member: str = "gec00", cycle_lag_hours: int = 6) -> None:
        self.member = member
        self.cycle_lag_hours = cycle_lag_hours

    def fetch_forcing(
        self,
        domain: DomainConfig,
        duration_hours: float,
        step_hours: float,
    ) -> Forcing:
        if step_hours <= 0:
            raise ValueError("step_hours must be positive.")
        if step_hours % 3 != 0:
            raise Earth2StudioFetchError(
                "Earth2Studio GEFS requires 3-hour lead-time intervals for this forecast range. "
                "Use --step-hours 3 (or another multiple of 3) with --provider earth2."
            )
        try:
            import xarray as xr  # noqa: F401
            from earth2studio import data
        except ImportError as exc:
            raise Earth2StudioUnavailable(
                "Earth2Studio is not installed. Install the optional dependency and retry, "
                "or switch to --provider mock."
            ) from exc

        init_time = self._latest_available_cycle_time()
        time_hours = build_time_hours(duration_hours, step_hours)
        lead_times = [timedelta(hours=float(hour)) for hour in time_hours]

        try:
            source = data.GEFS_FX(member=self.member, cache=True, verbose=False)
            data_array = source(time=[init_time], lead_time=lead_times, variable=list(self.variables))
        except Exception as exc:  # pragma: no cover - exercised only with real dependency
            raise Earth2StudioFetchError(
                "Earth2Studio imported successfully, but the GEFS fetch failed. "
                "Use --provider mock for local proof-of-concept runs or inspect your Earth2Studio setup."
            ) from exc

        reduced = self._reduce_to_domain_mean(data_array, domain)
        speed, direction = wind_uv_to_speed_dir(reduced["u10m"], reduced["v10m"])
        temperature_c = self._kelvin_to_celsius(reduced["t2m"])
        relative_humidity = self._normalize_rh(reduced["r2m"])
        pressure_pa = np.asarray(reduced["sp"], dtype=float)
        precipitation = np.zeros_like(speed)
        return Forcing(
            time_hours=time_hours,
            wind_speed_mps=speed,
            wind_direction_deg_from=direction,
            temperature_c=temperature_c,
            relative_humidity_pct=relative_humidity,
            pressure_pa=pressure_pa,
            precipitation_mmhr=precipitation,
            source_name="earth2studio_gefs",
            metadata={
                "provider": self.name,
                "member": self.member,
                "init_time_utc": init_time.isoformat(),
                "variables": list(self.variables),
                "cycle_lag_hours": self.cycle_lag_hours,
            },
        )

    def _latest_available_cycle_time(self) -> datetime:
        """Choose a conservative GEFS cycle time to reduce missing-object fetches."""

        now_utc = datetime.now(timezone.utc) - timedelta(hours=self.cycle_lag_hours)
        cycle_hour = (now_utc.hour // 6) * 6
        return now_utc.replace(hour=cycle_hour, minute=0, second=0, microsecond=0, tzinfo=None)

    def _reduce_to_domain_mean(self, data_array, domain: DomainConfig) -> dict[str, np.ndarray]:
        """Reduce a forecast cube to a domain-mean time series."""

        subset = data_array
        coord_names = set(getattr(subset, "coords", {}))
        lat_name = "lat" if "lat" in coord_names else "latitude" if "latitude" in coord_names else None
        lon_name = "lon" if "lon" in coord_names else "longitude" if "longitude" in coord_names else None
        if lat_name and lon_name:
            lat_radius = domain.height_km / 111.0 / 2.0
            lon_radius = domain.width_km / (111.0 * max(math.cos(math.radians(domain.center_lat)), 0.2)) / 2.0
            lat_values = np.asarray(subset.coords[lat_name])
            lon_values = np.asarray(subset.coords[lon_name])
            lat_slice = slice(domain.center_lat - lat_radius, domain.center_lat + lat_radius)
            if lat_values[0] > lat_values[-1]:
                lat_slice = slice(domain.center_lat + lat_radius, domain.center_lat - lat_radius)
            center_lon = domain.center_lon
            if np.nanmin(lon_values) >= 0.0 and center_lon < 0.0:
                center_lon = center_lon % 360.0
            lon_min = center_lon - lon_radius
            lon_max = center_lon + lon_radius
            if np.nanmin(lon_values) >= 0.0 and lon_min < 0.0:
                lon_min += 360.0
                lon_max += 360.0
            lon_slice = slice(lon_min, lon_max)
            subset = subset.sel({lat_name: lat_slice, lon_name: lon_slice})
        reduced: dict[str, np.ndarray] = {}
        for variable in self.variables:
            item = subset.sel(variable=variable)
            mean_dims = [dim for dim in item.dims if dim not in {"time", "lead_time", "variable"}]
            if mean_dims:
                item = item.mean(dim=mean_dims)
            if "time" in item.dims:
                item = item.isel(time=0)
            values = np.asarray(item, dtype=float)
            reduced[variable] = np.atleast_1d(values)
        return reduced

    @staticmethod
    def _kelvin_to_celsius(values: np.ndarray) -> np.ndarray:
        values = np.asarray(values, dtype=float)
        if np.nanmean(values) > 100.0:
            return values - 273.15
        return values

    @staticmethod
    def _normalize_rh(values: np.ndarray) -> np.ndarray:
        values = np.asarray(values, dtype=float)
        if np.nanmax(values) <= 1.0:
            values = values * 100.0
        return np.clip(values, 0.0, 100.0)
