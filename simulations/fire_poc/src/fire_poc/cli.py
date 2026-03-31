"""Command-line interface for the fire proof of concept."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .compare import explain_provider_error, run_extreme_conditions_panel, run_pipeline


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""

    parser = argparse.ArgumentParser(description="Run the ELMFIRE vs regime-aware fire model proof of concept.")
    parser.add_argument("--mode", choices=("compare", "extremes-panel"), default="compare", help="Workflow to run.")
    parser.add_argument("--provider", choices=("mock", "earth2"), required=True, help="Weather forcing provider.")
    parser.add_argument("--workdir", type=Path, required=True, help="Output run directory.")
    parser.add_argument("--elmfire-cmd", default=None, help="Optional path or command used to attempt an ELMFIRE run.")
    parser.add_argument("--duration-hours", type=float, default=12.0, help="Simulation duration in hours.")
    parser.add_argument("--step-hours", type=float, default=1.0, help="Weather time step in hours.")
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""

    args = build_parser().parse_args(argv)
    try:
        if args.mode == "extremes-panel":
            outputs = run_extreme_conditions_panel(
                provider_name=args.provider,
                workdir=args.workdir,
                elmfire_cmd=args.elmfire_cmd,
                duration_hours=args.duration_hours,
                step_hours=args.step_hours,
            )
        else:
            outputs = run_pipeline(
                provider_name=args.provider,
                workdir=args.workdir,
                elmfire_cmd=args.elmfire_cmd,
                duration_hours=args.duration_hours,
                step_hours=args.step_hours,
            )
    except Exception as exc:
        print(f"[fire_poc] ERROR: {explain_provider_error(exc)}", file=sys.stderr)
        return 1

    print(f"[fire_poc] Forcing source: {outputs.forcing_source}")
    if args.mode == "extremes-panel":
        print(f"[fire_poc] Scenario panel: {outputs.figure_path}")
        print(f"[fire_poc] Status manifest: {outputs.status_path}")
    else:
        print(f"[fire_poc] Benchmark type: {outputs.benchmark_status.benchmark_type}")
        print(f"[fire_poc] Benchmark status: {outputs.benchmark_status.status}")
        print(f"[fire_poc] Case directory: {outputs.benchmark_status.case_artifacts.case_dir}")
        print(f"[fire_poc] Figure saved: {outputs.figure_path}")
        if outputs.map_figure_path is not None:
            print(f"[fire_poc] Time-sequence map: {outputs.map_figure_path}")
        print(f"[fire_poc] Status manifest: {outputs.status_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
