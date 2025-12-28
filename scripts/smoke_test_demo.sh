#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export DEMO_STATIC_DIR="${ROOT_DIR}/web_interface/demo"
export DEMO_DB_PATH="${ROOT_DIR}/backend_api/demo.db"
export MODEL_STORAGE_DIR="${ROOT_DIR}/backend_api/model_storage"
export DEMO_PORT=8090

python "${ROOT_DIR}/backend_api/demo_server.py" &
APP_PID=$!

cleanup() {
  kill "${APP_PID}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

sleep 1

curl -sSf "http://localhost:${DEMO_PORT}/api/gpu/stats"

TEST_MODEL="${MODEL_STORAGE_DIR}/demo_test_model.pth"
mkdir -p "$(dirname "${TEST_MODEL}")"
echo "demo" > "${TEST_MODEL}"

curl -sSf -X POST -F "file=@${TEST_MODEL}" "http://localhost:${DEMO_PORT}/api/model/upload"
curl -sSf "http://localhost:${DEMO_PORT}/api/model/monitor"
