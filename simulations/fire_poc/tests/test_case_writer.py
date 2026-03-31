from __future__ import annotations

from pathlib import Path

import rasterio

from fire_poc.config import DomainConfig
from fire_poc.elmfire_case import ElmfireCaseWriter
from fire_poc.mock_provider import MockEarth2Provider


def test_case_writer_creates_expected_files(tmp_path: Path) -> None:
    domain = DomainConfig()
    forcing = MockEarth2Provider().fetch_forcing(domain=domain, duration_hours=4.0, step_hours=1.0)
    forcing.metadata.update(
        {
            "heterogeneity_strength": 0.35,
            "gust_corridor_strength": 1.2,
            "wind_streak_strength": 0.8,
            "dryness_patch_strength": 0.7,
        }
    )
    artifacts = ElmfireCaseWriter().write_case(tmp_path / "case", domain=domain, forcing=forcing)
    expected_paths = [
        artifacts.manifest_path,
        artifacts.elmfire_data_path,
        artifacts.ignition_path,
        artifacts.run_script_path,
        artifacts.weather_dir / "ws.tif",
        artifacts.weather_dir / "wd.tif",
        artifacts.topo_dir / "dem.tif",
        artifacts.topo_dir / "fbfm40.tif",
    ]
    for path in expected_paths:
        assert path.exists(), f"Missing expected artifact: {path}"
    with rasterio.open(artifacts.weather_dir / "ws.tif") as src:
        assert src.count == forcing.num_steps
        ws = src.read(1)
        assert float(ws.max()) > float(ws.min())
    text = artifacts.elmfire_data_path.read_text()
    assert "ASP_FILENAME = 'asp'" in text
    assert "OUTPUTS_DIRECTORY" in text
    assert "NUM_IGNITIONS = 1" in text
