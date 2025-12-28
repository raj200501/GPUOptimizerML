#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export PYTHONPATH="${ROOT_DIR}/backend_api:${PYTHONPATH:-}"
export SQLALCHEMY_DATABASE_URI="${SQLALCHEMY_DATABASE_URI:-sqlite:///${ROOT_DIR}/backend_api/gpu_optimizer.db}"
export MODEL_STORAGE_DIR="${MODEL_STORAGE_DIR:-${ROOT_DIR}/backend_api/model_storage}"
export PORT="${PORT:-5000}"

python "${ROOT_DIR}/backend_api/app.py"
