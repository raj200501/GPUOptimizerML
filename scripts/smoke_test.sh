#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="${ROOT_DIR}/backend_api"

python -m pip install -r "${BACKEND_DIR}/requirements.txt"

export PYTHONPATH="${BACKEND_DIR}:${PYTHONPATH:-}"
export SQLALCHEMY_DATABASE_URI="sqlite:///${BACKEND_DIR}/gpu_optimizer.db"
export MODEL_STORAGE_DIR="${BACKEND_DIR}/model_storage"
export PORT=5050

python "${BACKEND_DIR}/app.py" &
APP_PID=$!

cleanup() {
  kill "${APP_PID}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

sleep 2

curl -sSf "http://localhost:${PORT}/api/gpu/stats"

TEST_MODEL="${BACKEND_DIR}/model_storage/test_model.pth"
mkdir -p "$(dirname "${TEST_MODEL}")"
echo "dummy" > "${TEST_MODEL}"

curl -sSf -X POST -F "file=@${TEST_MODEL}" "http://localhost:${PORT}/api/model/upload"
curl -sSf "http://localhost:${PORT}/api/model/monitor"
