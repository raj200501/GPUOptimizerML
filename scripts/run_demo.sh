#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export DEMO_STATIC_DIR="${DEMO_STATIC_DIR:-${ROOT_DIR}/web_interface/demo}"
export DEMO_DB_PATH="${DEMO_DB_PATH:-${ROOT_DIR}/backend_api/demo.db}"
export MODEL_STORAGE_DIR="${MODEL_STORAGE_DIR:-${ROOT_DIR}/backend_api/model_storage}"
export DEMO_PORT="${DEMO_PORT:-8080}"

python "${ROOT_DIR}/backend_api/demo_server.py"
