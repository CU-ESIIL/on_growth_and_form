# Fire POC Workflow Buildout, March 30 2026

This document is a deliberately detailed reconstruction of the `fire_poc` workflow as it was built and extended across today's work session. It draws from the code now present in `simulations/fire_poc/`, the tracked prompt/action history in `PROMPT_ACTION_LOG.md`, and the actual run artifacts preserved under `simulations/fire_poc/outputs/`. The intent is to make the workflow legible to a future collaborator who was not present for the incremental decisions, the failed attempts, the environment workarounds, or the truthfulness boundaries that shaped the final design. The result is not a polished methods section; it is a full engineering narrative for how a local-first benchmark scaffold was assembled on a Mac M3 so that proposal figures could be produced honestly, repeatably, and with enough provenance to survive later scrutiny.

The core idea of the build is simple even though the implementation became fairly layered. We wanted one self-contained part of the repository where a forcing source could be selected, a fire-weather time series could be assembled, an ELMFIRE case could be written as real raster inputs plus a real `elmfire.data` namelist, an external benchmark could be attempted without pretending success when it failed, a simple regime-aware Python model could be run in parallel, and the outputs could be turned into proposal-facing figures. The important nuance is that every one of those steps had to be robust against missing dependencies. That requirement is what forced the architecture to separate forcing, case writing, execution, plotting, and status reporting rather than wrapping everything into one opaque script. The package therefore became less a single simulation and more a small workflow system whose main outputs are figures, manifests, and truthful status files.

## System architecture

At the highest level, the package is organized around one narrow data contract, the `Forcing` dataclass in `src/fire_poc/config.py`, and two orchestration entry points in `src/fire_poc/compare.py`. Everything else either produces that forcing, consumes it, or writes artifacts derived from it. The workflow can be pictured as follows:

```text
user / notebook / CLI
        |
        v
  fire_poc.cli
        |
        v
  compare.py
        |
        +------------------------------+
        |                              |
        v                              v
 make_provider()                RegimeAwareModel.run()
        |                              |
        |                              v
        |                      perimeters + area series
        v
 mock_provider.py  or  earth2_provider.py
        |
        v
   Forcing dataclass
        |
        +------------------------------+
        |                              |
        v                              v
 forcing.json                   ElmfireRunner.run()
                                       |
                                       v
                               ElmfireCaseWriter.write_case()
                                       |
                                       +--> GeoTIFF weather stacks
                                       +--> GeoTIFF fuels/topography rasters
                                       +--> elmfire.data
                                       +--> ignition_points.json
                                       +--> manifest.json
                                       +--> run_elmfire.sh
                                       |
                                       v
                               external elmfire executable
                                       |
                                       +--> stdout/stderr logs
                                       +--> ENVI/BIL outputs
                                       +--> fire_size_stats.csv
                                       |
                                       v
                                   BenchmarkStatus
        |
        v
 plotting.py
        |
        +--> elmfire_vs_regime_model.png
        +--> elmfire_time_sequence_map.png
        +--> extreme_conditions_panel.png
        +--> pipeline_status.json / extreme_conditions_panel_status.json
```

The architectural choice that matters most is that `ElmfireRunner` never assumes the benchmark succeeded just because the case could be written. The runner first asks `ElmfireCaseWriter` to prepare a case directory, then decides whether a real run is even possible, then records the exact command, logs, return code, and failure reason. If no executable is supplied, the workflow remains useful because the case directory is still complete and a proxy benchmark can still be plotted. If an executable is supplied but fails, the workflow still remains useful because the logs and written case survive. If the executable succeeds, the workflow marks that as a real ELMFIRE run even when no full parser exists yet. That separation is the central truthfulness design principle of the package, and nearly every later refinement depends on it.

## Repository layout and why it was kept isolated

The entire build lives under `simulations/fire_poc/` so that proposal-supporting experimentation does not leak into the core narrative directories. The package root contains a `pyproject.toml`, a `README.md`, a notebook under `notebooks/`, source code under `src/fire_poc/`, and a small test suite under `tests/`. Generated results are written below `simulations/fire_poc/outputs/`, which now contains demonstration runs, Earth2-backed real runs, the real benchmark directory used for the labeled time-sequence map, and the extreme-scenarios panel workspace. Keeping the workflow in this dedicated subtree matters because most of the artifacts here are not proposal prose; they are scaffolds, simulations, logs, figures, and manifests used to support proposal claims. The package was deliberately designed so that the only thing the proposal really needs to borrow from it is the resulting figure or, later, the logic for describing what that figure means.

## The weather-forcing layer

The forcing layer was designed around a single narrow requirement: both the benchmark path and the regime-aware model should read the same abstract weather object. The `Forcing` dataclass therefore stores `time_hours`, `wind_speed_mps`, `wind_direction_deg_from`, `temperature_c`, `relative_humidity_pct`, `pressure_pa`, and `precipitation_mmhr`, along with a free-form `metadata` dictionary. This is simple enough to inspect in JSON yet rich enough to support the transient weather stacks that ELMFIRE expects when `DT_METEOROLOGY` and `NUM_METEOROLOGY_TIMES` are being used.

The always-available path is `MockEarth2Provider` in `src/fire_poc/mock_provider.py`. It produces a deterministic synthetic forcing time series based on a few explicit sinusoidal patterns and a linear wind increase. The point of that provider is not realism. Its real purpose is to guarantee that the notebook, tests, and CLI remain runnable on a machine that has none of the Earth2 dependencies and no external weather connectivity at all. The mock forcing therefore functions as both a development tool and a truthfulness boundary: when Earth2Studio is unavailable, the code does not fake a successful Earth2 integration, it switches to a provider that is openly labeled mock.

The Earth2 path is `Earth2StudioGEFSProvider` in `src/fire_poc/earth2_provider.py`. That provider imports `earth2studio`, selects the documented `GEFS_FX` data source, and requests the variables `u10m`, `v10m`, `t2m`, `r2m`, and `sp`, which are then reduced to a domain-mean time series over the requested box. The provider explicitly enforces a `3`-hour cadence because the GEFS forecast range being used here is being queried at `0`, `3`, `6`, `9`, and `12` hour leads, and the code now raises a clear exception if the user requests a step that is not a multiple of `3`. The default member is `gec00`, the cycle lag is `6` hours so the provider biases toward a completed forecast cycle, the coordinates are adjusted to work with GEFS longitudes in `0..360` if necessary, and the returned `metadata` records the member, init time, variables, and cycle lag so the run can be audited later from `forcing.json` alone.

The practical meaning of the Earth2 integration is narrower than the phrase "digital twin" might suggest. In this build, Earth2Studio is being used as a real weather-source interface and GEFS reduction layer, not as a general counterfactual world engine. The workflow uses actual forecast fields, averages them over an idealized domain, and then passes that one-dimensional forcing into two model branches. That is why later scenario panels were constructed as explicit perturbations around an Earth2-backed baseline rather than as fully Earth2-native counterfactual worlds. The code is transparent about that distinction, and the documentation should preserve it because otherwise a figure built from this package could easily be oversold.

## The case-writing layer

The most important artifact-writing logic lives in `src/fire_poc/elmfire_case.py`. This module writes an actual ELMFIRE-style case directory with inputs that can be inspected outside the Python workflow. The directory contains transient float weather rasters `ws`, `wd`, `m1`, `m10`, `m100`, `adj`, and `phi`, along with static integer rasters `slp`, `asp`, `dem`, `fbfm40`, `cc`, `ch`, `cbh`, and `cbd`. These are written as GeoTIFFs using `rasterio`, with the raster transform derived from the configured domain origin, cell size, and grid dimensions. In addition to the rasters, the writer produces a real `elmfire.data` namelist, a human-readable `ignition_points.json`, a `manifest.json` summarizing the event and file paths, and a tiny `run_elmfire.sh` helper so the case remains inspectable even outside Python.

Several details in the case writer only make sense in light of the debugging path we went through today. Wind speed rasters are converted from meters per second to miles per hour because that matches current ELMFIRE expectations for the tutorial-like setup we targeted, and the namelist sets `WS_AT_10M = .TRUE.` so that interpretation is explicit. The filenames in `elmfire.data` omit `.tif` suffixes because ELMFIRE expects basenames. `DT_METEOROLOGY` is derived from the forcing step size in seconds, `NUM_METEOROLOGY_TIMES` is taken from the forcing length, and the writer sets `SIMULATION_DT = 5.0`, `TARGET_CFL = 0.2`, and `DUMP_TIME_OF_ARRIVAL = .TRUE.` because the current proof of concept is optimized around getting truthful, inspectable spread outputs rather than around elaborate postprocessing.

The case writer also contains one of the most consequential fixes from the session: ignition coordinates in the namelist are now written in absolute CRS coordinates rather than local offsets from the lower-left corner. Earlier attempts wrote local coordinates, which caused ELMFIRE to index fuel arrays incorrectly during initialization and crash in native code. The JSON ignition sidecar keeps both the local and absolute values so the case remains interpretable, but the namelist now uses the absolute coordinates ELMFIRE expects. That one detail is what allowed the Mac M3 benchmark path to move from repeated native failures to a verified successful run.

Another important refinement that arrived late in the day is the deterministic roughness machinery. The first proof-of-concept perimeters looked overly smooth because the underlying inputs were almost perfectly homogeneous. To address that, `_build_pattern_fields()` now generates repeatable spatial structure aligned to the mean downwind direction, including corridor, lee-shadow, ridge, streak, and dry-patch fields. Those deterministic patterns are then used to spatially vary `ws`, `wd`, `m1`, `m10`, `m100`, `adj`, `phi`, `dem`, `slp`, `asp`, canopy structure, and related exposure terms. This does not pretend to be a turbulence-resolving atmospheric model. What it does do is provide a transparent, scenario-controlled way to make the fire edge look more like a fire edge and less like a perfect ellipse generated over a featureless plane.

There is one more case-writing change worth highlighting because it affects rerun integrity rather than fire behavior. Repeated ELMFIRE runs were leaving multiple output rasters in the same scenario directories, which meant later plotting code could accidentally grab an older `time_of_arrival` file. The case writer now clears prior generated case artifacts before writing a fresh case, and the plotting helper that resolves output files now chooses the most recently modified matching file rather than the lexicographically first one. That fix matters because it closes a quiet provenance bug: without it, a later rerun could have appeared to succeed while still feeding an older raster into the figure.

## The runner and truthfulness boundary

`src/fire_poc/elmfire_runner.py` is intentionally narrow. Its job is to prepare a case, attempt an external ELMFIRE command if one is configured, preserve stdout and stderr, and return a `BenchmarkStatus` object that says what actually happened. It does not guess. It does not infer success from partial files. It does not declare the benchmark real when only a proxy ran. If no executable is supplied, the status is `case_written_run_skipped` and the benchmark type is `case-written-only`. If the command cannot be found, the status is `run_failed_missing_executable`. If the executable runs and returns successfully without obvious failure markers, the benchmark type becomes `real ELMFIRE` and the status becomes `run_completed_parser_not_implemented`, which is an intentionally honest phrase: the benchmark really ran, but the workflow has not yet been generalized into a full product parser for every possible output.

The runner also retains a Python proxy benchmark for one specific purpose: plotting continuity when the real benchmark path is unavailable. That proxy is an explicitly labeled smooth-front ellipse model, built from cumulative wind drive, and its `FireModelResult` metadata states that it exists only because no real ELMFIRE run completed. This distinction is crucial for proposal integrity. The package can always produce a figure, but it will only label that figure as benchmarked by real ELMFIRE when the executable actually completed.

## The regime-aware model

The comparison model in `src/fire_poc/regime_model.py` is intentionally simple because it is not the point of the workflow. It is a pure Python model that advances an ellipse through time, changes its spread coefficients once either a wind threshold or a time threshold is crossed, and returns perimeters plus area through time. The default transition is triggered when wind speed reaches `7.5 m/s` or time reaches `5.0 h`, and the model increases its major-axis growth rate relative to the pre-transition regime. The value of this model is pedagogical and comparative. It gives the workflow a transparent alternative branch that is easy to inspect, easy to rerun in a notebook, and easy to compare against the benchmark scaffold without needing to claim that it is an operational fire model.

## Plotting and figure generation

The plotting layer in `src/fire_poc/plotting.py` now produces three distinct figure types. The first is the basic comparison figure, `elmfire_vs_regime_model.png`, which combines a forcing panel, a final perimeter overlay, area-through-time curves, and a set of snapshots. The second is `elmfire_time_sequence_map.png`, which is generated only after a real ELMFIRE run completes and which reads actual ENVI/BIL `time_of_arrival` output plus `fire_size_stats.csv` to create a labeled sequence map and a textual parameter panel. The third is `extreme_conditions_panel.png`, which assembles multiple real ELMFIRE runs into a grid where time proceeds down the rows and extreme-condition manifestations proceed across the columns.

One subtle but important plotting fix arrived late in the day. The ELMFIRE `time_of_arrival` rasters are written in top-origin image order, while the maps in Matplotlib were initially being drawn as if row zero belonged at the lower edge of the domain. That mismatch mirrored the fire vertically and made the ignition star look as though it had been placed far away from the burn. The benchmark inputs themselves were correct; the display transform was not. The plotting code now flips ENVI/BIL rasters into map orientation before drawing them, which brings the ignition marker, the arrival raster, and the burned contours into the same coordinate frame. This matters because it changes the panel from something that merely looked suspicious into something that can now be read directly as a map.

The extreme-conditions panel required the most iterative design work. The first version simply perturbed the Earth2-backed baseline forcing and produced scenarios that were too similar to be proposal-useful. The next version increased wind coupling and fuel dryness but still looked too smooth. The current version goes further: the baseline is still grounded in Earth2/GEFS forcing, but the scenarios now use explicit metadata to strengthen downburst corridors, directional gust streaks, dead-fuel drying, and canopy openness, while the case writer turns those metadata controls into real raster heterogeneity. The plotting code then auto-frames each column to the final burned extent so a large common domain can be used for simulation without wasting panel real estate in the figure.

Even with auto-framing, the user correctly noticed that the issue was no longer just plot framing. A few scenarios looked constrained by the size and placement of the computational domain itself. The current extremes workflow therefore uses a larger domain than earlier builds and also places the ignition upwind of the domain center so the fire has more downwind room to grow. After the latest change, the extreme-panel domain is `700 x 700` cells at `30 m` resolution, which corresponds to `21.0 km x 21.0 km`, and the ignition is offset to `x = 5,250 m`, `y = 15,750 m` relative to the lower-left corner. In absolute coordinates with the current origin, that means the ignition is placed at `(505250, 4415750)` in `EPSG:32613`. This asymmetric placement is intentional: the strongest scenarios predominantly run toward the east-southeast, so centering the ignition was less useful than giving those directions more genuine space. After the domain enlargement, an explicit raster-edge check confirmed that none of the five scenarios touched the computational boundary in the current run, so the figure is no longer hiding a clipped benchmark behind smarter framing.

The final row of the extreme-conditions panel has also evolved into something more analytically useful than the initial map-only layout. Each column now ends with a log-log scaling subplot of perimeter versus area, estimated directly from the burned masks at the same snapshot times shown in the rows above. The row includes a fitted exponent `beta` from `log(P)` versus `log(A)` and two reference trends corresponding to `P ~ A^(1/2)` and `P ~ A^(2/3)`. This is a much cleaner diagnostic than the earlier perimeter-to-area-ratio view because it puts the observed scaling law and the two reference exponents onto the same geometric footing. It also means the current panel is doing two jobs at once: the upper rows show spatial form through time, and the lower row gives a compact quantitative read on whether those forms behave more like a diffusion-style boundary, a rougher superlinear perimeter, or something in between.

## The CLI and notebook interfaces

The package was built to be usable both from a notebook and from the command line, and that dual-path requirement changed several engineering choices. The CLI in `src/fire_poc/cli.py` supports two modes, `compare` and `extremes-panel`, and lets the user choose `--provider mock` or `--provider earth2`, supply an optional `--elmfire-cmd`, set `--duration-hours`, and set `--step-hours`. The compare mode is the general single-run scaffold. The extremes-panel mode assumes that a real ELMFIRE executable is available because the whole point of that panel is to compare real benchmark runs across scenario variants. The notebook under `notebooks/elmfire_earth2_poc.ipynb` mirrors the single-run workflow in eight sections: setup, choose provider, fetch forcing, write ELMFIRE case, run benchmark if available, run regime-aware model, make figure, and inspect generated files. The notebook is intentionally conservative and defaults to the mock provider so it can always run locally.

## Environment split and why it was necessary

The local environment story turned out to be one of the main engineering problems of the day. The original project virtual environment at `simulations/fire_poc/.venv` is tied to `Python 3.9.6`. That was sufficient for the package scaffold itself but not for Earth2Studio. Rather than breaking the original environment or pretending the dependency mismatch was not real, a separate environment was created at `simulations/fire_poc/.venv312` using `uv`, and that environment is the one now used for the Earth2-backed path and the real ELMFIRE tests. This split is not accidental clutter. It is a record of the fact that the package still claims compatibility from `Python >=3.9` in its local build metadata, while the Earth2-backed path on this machine currently depends on a newer interpreter.

**`uv 0.5.26`** was used as the lightweight environment and package manager for the Earth2-capable branch. Its role was not scientific; it was operational. It allowed a clean `Python 3.12` environment to be created inside `simulations/fire_poc/` without destabilizing the older `.venv`. The important setting here is simply the interpreter target: the Earth2-capable environment points at `Python 3.12.8`, and the package plus the optional `earth2` extra were installed into that interpreter.

**`Python 3.12.8`** in `.venv312` is the environment that now matters for live Earth2Studio runs and the latest real ELMFIRE-backed panel regeneration. Within that environment the package currently sees `earth2studio 0.13.0`, `numpy 2.4.4`, `matplotlib 3.10.8`, and `rasterio 1.5.0`. The older `.venv` remains available as a historical artifact of the initial scaffold, but it is not the environment to use for Earth2-backed work.

**`earth2studio 0.13.0`** is used exclusively through the `Earth2StudioGEFSProvider`. In this build it is configured to fetch `GEFS_FX` member `gec00` using variables `u10m`, `v10m`, `t2m`, `r2m`, and `sp`, then reduce them to a domain-mean time series over the idealized box. The key settings are the `3`-hour time step requirement and the `6`-hour cycle lag. We do not currently use Earth2Studio for CorrDiff inference, spatially resolved dynamic downscaling, or arbitrary counterfactual scenario generation on the Mac.

**Homebrew `gcc 15.2.0_1`**, and specifically **`gfortran 15.2.0`**, was installed because upstream ELMFIRE is a Fortran codebase and the Mac did not initially have the toolchain needed to compile it. The role of `gfortran` here is straightforward: it is the compiler used to build the local `elmfire` executable in `simulations/elmfire_src/build/linux/elmfire/elmfire`. A notable nuance is that the build path had to work around a Linux-specific `-unroll` link issue, so the current successful build on macOS should be understood as a best-effort native port rather than a claim of broad upstream support.

**Homebrew `open-mpi 5.0.9`**, exposed through **`mpirun 5.0.9`**, was installed because ELMFIRE’s build and execution ecosystem expects MPI-aware tooling even when the present proof-of-concept runs are launched as a single local executable rather than through a large parallel job. In other words, Open MPI is part of making the code compile and remain compatible with its expected runtime environment, even though the current local CLI path does not rely on a complicated multi-rank launch.

**Homebrew `gdal 3.12.3`** was installed because ELMFIRE internally calls `gdal_translate` when converting GeoTIFF inputs into the ENVI products it uses during runtime. The case writer therefore now detects a Homebrew GDAL binary directory and writes `PATH_TO_GDAL` into `elmfire.data`. Without this installation, the real benchmark path could write a case but could not get through the raster conversion stage on macOS. In practical terms, the installation of GDAL is what moved the workflow from "case written" to "benchmark gets far enough to use its own raster ingestion path."

Although it was not something we installed today, it is also worth noting that **LLDB**, the macOS debugger, was used during the bring-up because one of the hardest failures was a native `SIGBUS` inside ELMFIRE initialization. That debugging step is part of the workflow history because it explains why the ignition-coordinate fix was found and why we can say with confidence that the later success was earned rather than guessed.

## The ELMFIRE bring-up sequence on the Mac M3

The ELMFIRE story matters because the current workflow is only credible if the steps that made it work are documented. The progression today went roughly as follows. First, the case writer existed but the environment did not have an executable. Then the toolchain was installed and the upstream source was built locally under `simulations/elmfire_src/`. Then the benchmark moved through a series of failures: missing executable, namelist mismatches, fuel-model-table handling, GDAL conversion issues, path-length issues, and finally a native initialization crash. The crash was eventually traced to the ignition coordinates being wrong for the arrays ELMFIRE had allocated. Once the ignition coordinates were written in absolute CRS space and the case used local relative paths for its inputs, outputs, and scratch directory, the real ELMFIRE run completed successfully on the Mac for the proof-of-concept case.

That history is important because the current workflow has more credibility than a "greenfield success" story would. We know, for example, that the real benchmark path is not merely syntactically accepted. It has gone through actual compilation, actual raster conversion, actual ELMFIRE execution, actual writing of ENVI outputs, and actual figure generation from those outputs. We also know what still remains incomplete. The code does not yet provide a generalized parser that reconstructs benchmark perimeters from every ELMFIRE output product. Instead, it currently reads the time-of-arrival raster and fire-size statistics where needed and marks the broader parser boundary honestly.

## The current extreme-scenarios design

The current extremes panel begins with a baseline Earth2/GEFS forcing, then clones that forcing into a set of intentionally explicit scenario variants in `compare.py`. The baseline is left largely alone but still receives mild spatial heterogeneity so it does not behave like a mathematically pristine fire spreading over a blank surface. The `Downburst Forcing` scenario applies the `downburst_profile` wind-speed multiplier through time, fixes the direction to `262` degrees from, dries the air modestly, raises temperature by `4 C`, and strengthens surface coupling via `adj_scale`, `phi_scale`, corridor strength, and reduced canopy. The `Directional Gust Front` scenario uses a pulsed gust profile multiplied more aggressively, fixes the wind direction to `255` degrees from, warms the case slightly, lowers RH, and increases wind-streak structure so the final perimeter reflects repeated directional forcing rather than just one stronger mean wind.

The `Light Dry Fuels` scenario works differently. Instead of relying mostly on stronger winds, it raises temperature by `9 C`, scales RH down to `32%` of baseline, decreases pressure slightly, and applies negative offsets to the dead-fuel moisture proxies. It also removes canopy structure so the fire can run through open fine fuels. The `Compound Blowup` scenario stacks all of those mechanisms: a strong downburst-like wind multiplier, a fixed strong direction, a `12 C` temperature increase, RH scaled to `24%` of baseline, lower pressure, stronger `adj` and `phi` amplification, and the driest fuel offsets in the set. The important point is that the scenarios are not hidden behind arbitrary names. Each one is implemented by explicit, inspectable scalars in code, and each one is still grounded in the same Earth2-backed baseline series rather than being invented as a disconnected synthetic weather world.

## Current commands and settings that matter in practice

The single-run Earth2-backed workflow that produced the real ELMFIRE benchmark and the labeled time-sequence map is executed from `simulations/fire_poc/` in the `.venv312` environment and uses a command of the form `python -m fire_poc.cli --provider earth2 --step-hours 3 --elmfire-cmd /absolute/path/to/elmfire --workdir outputs/earth2_real_repo`. The `3`-hour step is essential for the current Earth2 provider. The `--elmfire-cmd` path currently points to `simulations/elmfire_src/build/linux/elmfire/elmfire`. The extreme-panel workflow uses the same environment and executable, but adds `--mode extremes-panel` and writes to `outputs/extreme_panel`.

The most important namelist settings embedded by the case writer are worth stating plainly because they shape what the benchmark is actually doing. Weather and topography paths are relative to the case directory so reruns are self-contained. `DT_METEOROLOGY` is derived from the forcing cadence, `NUM_METEOROLOGY_TIMES` is the number of forcing steps, `SIMULATION_TSTOP` is the final forcing hour in seconds, and the outputs requested include flame length, spread rate, and time of arrival. The workflow is intentionally built around time-of-arrival because that output can be inspected, contoured, and compared without inventing an elaborate postprocessor.

## Testing, verification, and provenance

The current automated tests remain intentionally small but useful. `test_geometry.py` checks the area and perimeter utilities, `test_case_writer.py` checks that the case writer creates the expected artifacts and now also verifies that heterogeneity metadata produces spatially varying weather rasters, and `test_mock_pipeline.py` checks that the mock workflow writes a figure and a truthful status file. Throughout the build today, these tests were rerun repeatedly in `.venv312` after major changes. That does not prove physical realism, but it does prove that the local workflow remains internally coherent as the architecture evolves.

Provenance in this workflow comes from more than tests. Each run writes `forcing.json`, `manifest.json`, benchmark logs, figures, and a status manifest. The repository also preserves the higher-level decision history in `PROMPT_ACTION_LOG.md`, which is especially important here because many of the design decisions were responses to discovered boundaries rather than features planned in advance. Anyone trying to understand why the package has two environments, why it chooses domain means rather than gridded forcing, or why the runner is so careful about benchmark labeling should read that log alongside the code.

## Current limitations and the honest next steps

The workflow is now far more complete than it was at the start of the day, but it still has sharp boundaries. The Earth2 path is a domain-mean GEFS reduction, not a spatially distributed Earth2 atmospheric simulation. The regime-aware model is intentionally simple. The benchmark parser is still specialized around time-of-arrival and summary CSV outputs rather than a full reconstruction of every ELMFIRE product. The extreme-scenarios panel is physically more convincing than it was, but it is still an idealized benchmark landscape rather than a real observed fire footprint with mapped fuels and topography. Those are not reasons to distrust the workflow; they are reasons to describe it precisely.

What the package does provide now is a credible and inspectable scaffold. On this Mac M3, we can write real ELMFIRE cases, fetch real Earth2Studio GEFS forcing when the compatible environment is active, run the real ELMFIRE executable that was built locally, preserve logs and status honestly, generate labeled benchmark figures, and build an extreme-scenarios panel from multiple real benchmark runs. That panel currently summarizes a run in which the final burned areas were approximately `14.0 ac` for the baseline, `1290.1 ac` for the downburst case, `1011.7 ac` for the directional gust-front case, `517.7 ac` for the light-dry-fuels case, and `6449.2 ac` for the compound blowup case. That is a substantial leap from a generic local mock-up. It is also exactly the kind of scaffold that proposal work benefits from: detailed enough to support a figure and a methods description, modular enough to survive future refinement, and honest enough not to overclaim what has not yet been implemented.
