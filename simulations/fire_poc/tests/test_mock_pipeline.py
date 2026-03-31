from __future__ import annotations

from pathlib import Path

from fire_poc.compare import run_pipeline


def test_mock_pipeline_writes_figure_and_status(tmp_path: Path) -> None:
    outputs = run_pipeline(provider_name="mock", workdir=tmp_path / "demo")
    assert outputs.figure_path.exists()
    assert outputs.status_path.exists()
    assert outputs.benchmark_status.benchmark_type == "case-written-only"

