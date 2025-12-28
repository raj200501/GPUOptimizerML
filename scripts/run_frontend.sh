#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEB_DIR="${ROOT_DIR}/web_interface"

if [ ! -d "${WEB_DIR}/node_modules" ]; then
  echo "node_modules not found; run 'npm install' in ${WEB_DIR} first."
fi

cd "${WEB_DIR}"
npm start
