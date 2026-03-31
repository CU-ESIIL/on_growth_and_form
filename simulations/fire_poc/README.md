# fire_poc

This self-contained project builds a local-first proof of concept for comparing a regime-aware fire model against an `ELMFIRE` benchmark scaffold. The proposal-facing artifact is the final figure; everything else stays isolated in this directory so the exploratory machinery does not leak into the rest of the repository.

## What works on a Mac M3 now

- The mock weather pipeline runs locally with deterministic synthetic forcing.
- The regime-aware comparison model runs locally in pure Python.
- The `ELMFIRE` case writer generates inspectable GeoTIFF inputs, `elmfire.data`, ignition metadata, and a run manifest.
- The plotting pipeline writes a proposal-ready comparison figure from the mock workflow.
- `earth2studio` GEFS forcing works from the separate Python 3.12 environment at `simulations/fire_poc/.venv312`.
- A native `ELMFIRE` benchmark run now completes for the current proof-of-concept case on macOS after installing Homebrew `gcc`, `open-mpi`, and `gdal`.
- The extremes-panel workflow now uses a larger common domain, scenario-specific auto-framing, and deterministic spatial heterogeneity in fuels, exposure, and moisture so proposal figures can show rougher, less idealized perimeters.

## What requires Earth2Studio

- The `earth2` provider path depends on `earth2studio` being installed and on its `GEFS_FX` forecast source being reachable.
- This proof of concept uses documented `GEFS_FX` variables `u10m`, `v10m`, `t2m`, `r2m`, and `sp`, then reduces the gridded data to a domain-mean time series.
- If `earth2studio` import or fetch fails, the code raises a clear exception and the CLI suggests switching to the mock provider.

## What likely requires a Linux VM or container

- NVIDIA-oriented Earth-2 workflows beyond basic remote data access, especially local CorrDiff-style inference, are not expected to be practical on a Mac M3.
- `ELMFIRE` is generally tested upstream on Ubuntu-like environments, so macOS execution should be treated as best-effort even if a local executable is available later.
- This local success is still a proof-of-concept benchmark path, not a broad guarantee that arbitrary upstream ELMFIRE cases will be stable on macOS.

## Quickstart

```bash
cd simulations/fire_poc
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m fire_poc.cli --provider mock --workdir outputs/demo
```

To try the optional Earth2Studio path after installing its dependency:

```bash
python -m pip install -e .[earth2]
python -m fire_poc.cli --provider earth2 --workdir outputs/demo_earth2
```

To open the notebook:

```bash
cd simulations/fire_poc
jupyter notebook notebooks/elmfire_earth2_poc.ipynb
```

For the Earth2Studio path on this Mac, use the separate Python 3.12 environment:

```bash
cd simulations/fire_poc
source .venv312/bin/activate
python -m fire_poc.cli --provider earth2 --step-hours 3 --workdir outputs/demo_earth2
```

## Command line examples

```bash
python -m fire_poc.cli --provider mock --workdir outputs/demo
python -m fire_poc.cli --provider earth2 --workdir outputs/demo
python -m fire_poc.cli --provider earth2 --elmfire-cmd /path/to/elmfire --workdir outputs/demo
python -m fire_poc.cli --mode extremes-panel --provider earth2 --step-hours 3 --elmfire-cmd /path/to/elmfire --workdir outputs/extreme_panel
```

## Truthfulness policy

This code never labels a case as a real `ELMFIRE` run unless the external executable actually completed. It distinguishes among:

- mock weather versus Earth2Studio weather,
- proxy benchmark versus real `ELMFIRE` benchmark,
- successful case generation versus successful external execution.

If `ELMFIRE` is missing or cannot run, the workflow still writes the full case directory and reports the boundary honestly.
