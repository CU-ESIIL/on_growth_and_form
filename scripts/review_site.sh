#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 scripts/generate_fire_model_gantt.py
python3 -m mkdocs build --strict --clean --site-dir dist
pytest tests/test_site.py "$@"
