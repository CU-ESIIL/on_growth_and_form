"""Boundary layer around external ELMFIRE execution."""

from __future__ import annotations

from dataclasses import dataclass, field
import logging
from pathlib import Path
import shlex
import subprocess
from typing import Any

import numpy as np

from .config import DomainConfig, Forcing
from .elmfire_case import CaseArtifacts, ElmfireCaseWriter
from .geometry import area_series, ellipse_perimeter
from .regime_model import FireModelResult

LOGGER = logging.getLogger(__name__)


@dataclass
class BenchmarkStatus:
    """Status returned by the ELMFIRE runner."""

    benchmark_type: str
    status: str
    message: str
    case_artifacts: CaseArtifacts
    command: list[str] = field(default_factory=list)
    return_code: int | None = None
    stdout_path: Path | None = None
    stderr_path: Path | None = None
    run_completed: bool = False
    parser_implemented: bool = False
    failure_reason: str | None = None


class ElmfireRunner:
    """Write an ELMFIRE case and optionally attempt an external run."""

    def __init__(self, executable_command: str | None = None) -> None:
        self.executable_command = executable_command
        self.case_writer = ElmfireCaseWriter()

    def prepare_case(self, case_dir: Path, domain: DomainConfig, forcing: Forcing) -> CaseArtifacts:
        LOGGER.info("Writing ELMFIRE case to %s", case_dir)
        return self.case_writer.write_case(case_dir=case_dir, domain=domain, forcing=forcing)

    def run(self, case_dir: Path, domain: DomainConfig, forcing: Forcing) -> BenchmarkStatus:
        artifacts = self.prepare_case(case_dir=case_dir, domain=domain, forcing=forcing)
        if not self.executable_command:
            return BenchmarkStatus(
                benchmark_type="case-written-only",
                status="case_written_run_skipped",
                message="ELMFIRE case written, run skipped because no executable command was provided.",
                case_artifacts=artifacts,
            )

        command = self._build_command(artifacts)
        stdout_path = artifacts.case_dir / "elmfire_stdout.log"
        stderr_path = artifacts.case_dir / "elmfire_stderr.log"
        LOGGER.info("Attempting external ELMFIRE run: %s", command)
        try:
            completed = subprocess.run(
                command,
                cwd=artifacts.case_dir,
                text=True,
                capture_output=True,
                check=False,
            )
        except FileNotFoundError as exc:
            stdout_path.write_text("")
            stderr_path.write_text(str(exc))
            return BenchmarkStatus(
                benchmark_type="case-written-only",
                status="run_failed_missing_executable",
                message="ELMFIRE case written, but the requested executable command was not found.",
                case_artifacts=artifacts,
                command=command,
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                failure_reason=str(exc),
            )
        stdout_path.write_text(completed.stdout)
        stderr_path.write_text(completed.stderr)
        failure_markers = (
            "ERROR 4:",
            "Problem opening input file",
            "Problem opening new fuel model table file",
            "Problem opening fuel model table file",
            "Problem opening bsq xml header",
            "Error: Problem with namelist group",
            "Error, no input file specified.",
            "Fortran runtime error",
        )
        combined_output = "\n".join([completed.stdout, completed.stderr])
        output_indicates_failure = any(marker in combined_output for marker in failure_markers)
        if completed.returncode == 0 and not output_indicates_failure:
            return BenchmarkStatus(
                benchmark_type="real ELMFIRE",
                status="run_completed_parser_not_implemented",
                message="ELMFIRE executable completed, but no parser is implemented for output products yet.",
                case_artifacts=artifacts,
                command=command,
                return_code=completed.returncode,
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                run_completed=True,
                parser_implemented=False,
            )
        return BenchmarkStatus(
            benchmark_type="real ELMFIRE",
            status="run_failed",
            message="ELMFIRE executable did not complete successfully. Case artifacts and logs were preserved.",
            case_artifacts=artifacts,
            command=command,
            return_code=completed.returncode,
            stdout_path=stdout_path,
            stderr_path=stderr_path,
            run_completed=False,
            parser_implemented=False,
            failure_reason=completed.stderr.strip() or completed.stdout.strip() or f"Return code {completed.returncode}",
        )

    def _build_command(self, artifacts: CaseArtifacts) -> list[str]:
        """Resolve the external command, supporting simple placeholders."""

        original_template = self.executable_command or ""
        command_template = original_template
        replacements = {
            "{case_dir}": str(artifacts.case_dir.resolve()),
            "{input_file}": str(artifacts.elmfire_data_path.resolve()),
            "{run_script}": str(artifacts.run_script_path.resolve()),
        }
        for key, value in replacements.items():
            command_template = command_template.replace(key, value)
        command = shlex.split(command_template)
        if "{input_file}" not in original_template and len(command) == 1:
            command.append(str(artifacts.elmfire_data_path.resolve()))
        return command


def build_proxy_benchmark(forcing: Forcing, domain: DomainConfig) -> FireModelResult:
    """Smooth-front proxy used only when a real ELMFIRE benchmark does not run."""

    center = (domain.ignition_x_m, domain.ignition_y_m)
    cumulative_drive = np.cumsum(forcing.wind_speed_mps) * max(forcing.dt_hours, 1.0)
    perimeters = []
    for idx, _ in enumerate(forcing.time_hours):
        major = 60.0 + cumulative_drive[idx] * 16.0
        minor = 45.0 + cumulative_drive[idx] * 10.5
        angle = (forcing.wind_direction_deg_from[idx] + 180.0) % 360.0
        perimeters.append(ellipse_perimeter(center, major, minor, angle))
    return FireModelResult(
        model_name="proxy benchmark",
        benchmark_label="proxy benchmark",
        times_hours=forcing.time_hours.copy(),
        perimeters_xy=perimeters,
        areas_m2=area_series(perimeters),
        is_proxy=True,
        metadata={"note": "Used only because a real ELMFIRE benchmark did not run."},
    )
