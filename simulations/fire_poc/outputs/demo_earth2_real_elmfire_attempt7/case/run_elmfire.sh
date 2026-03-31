#!/usr/bin/env bash
set -euo pipefail
ELMFIRE_CMD="${1:-elmfire}"
echo "Running ${ELMFIRE_CMD} in $(pwd)"
exec ${ELMFIRE_CMD}
