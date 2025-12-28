#!/usr/bin/env python3
import json
import os
import sqlite3
import threading
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import cgi

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = Path(os.getenv("DEMO_DB_PATH", ROOT_DIR / "backend_api" / "demo.db"))
MODEL_STORAGE_DIR = Path(
    os.getenv("MODEL_STORAGE_DIR", ROOT_DIR / "backend_api" / "model_storage")
)
STATIC_DIR = Path(
    os.getenv("DEMO_STATIC_DIR", ROOT_DIR / "web_interface" / "demo")
)


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS models (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def insert_model(name, status):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "INSERT INTO models (name, status, created_at) VALUES (?, ?, ?)",
            (name, status, datetime.utcnow().isoformat()),
        )
        conn.commit()
        return cursor.lastrowid


def update_model_status(model_id, status):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE models SET status = ? WHERE id = ?", (status, model_id))
        conn.commit()


def fetch_models():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT id, name, status FROM models ORDER BY id DESC")
        return [
            {"id": row[0], "name": row[1], "status": row[2]}
            for row in cursor.fetchall()
        ]


def optimize_model(filepath):
    optimized_path = Path(str(filepath) + "_optimized_trt.pth")
    with open(filepath, "rb") as source_file, open(optimized_path, "wb") as target_file:
        target_file.write(source_file.read())
    return optimized_path


class DemoHandler(BaseHTTPRequestHandler):
    server_version = "GPUOptimizerDemo/1.0"

    def _send_json(self, data, status=HTTPStatus.OK):
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_file(self, path):
        if not path.exists() or not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return
        content_type = "text/html"
        if path.suffix == ".js":
            content_type = "application/javascript"
        elif path.suffix == ".css":
            content_type = "text/css"
        with open(path, "rb") as file_handle:
            content = file_handle.read()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/gpu/stats":
            self._send_json(
                [
                    {
                        "utilization": "0",
                        "memory_total": "0",
                        "memory_free": "0",
                        "memory_used": "0",
                        "note": "demo mode",
                    }
                ]
            )
            return
        if parsed.path == "/api/model/monitor":
            self._send_json(fetch_models())
            return
        if parsed.path.startswith("/assets/"):
            asset_path = STATIC_DIR / parsed.path.replace("/assets/", "")
            self._send_file(asset_path)
            return
        if parsed.path in ("/", "/index.html"):
            self._send_file(STATIC_DIR / "index.html")
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_POST(self):
        if self.path != "/api/model/upload":
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return
        content_type = self.headers.get("Content-Type", "")
        if "multipart/form-data" not in content_type:
            self.send_error(HTTPStatus.BAD_REQUEST, "Expected multipart form data")
            return
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD": "POST", "CONTENT_TYPE": content_type},
        )
        if "file" not in form:
            self.send_error(HTTPStatus.BAD_REQUEST, "Missing file field")
            return
        file_item = form["file"]
        filename = os.path.basename(file_item.filename)
        MODEL_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
        filepath = MODEL_STORAGE_DIR / filename
        with open(filepath, "wb") as output_file:
            output_file.write(file_item.file.read())
        model_id = insert_model(filename, "uploaded")

        def optimize():
            optimize_model(filepath)
            update_model_status(model_id, "optimized")

        threading.Thread(target=optimize, daemon=True).start()
        self._send_json({"message": "Model uploaded and optimized successfully"})


def run():
    init_db()
    host = os.getenv("DEMO_HOST", "0.0.0.0")
    port = int(os.getenv("DEMO_PORT", "8080"))
    server = ThreadingHTTPServer((host, port), DemoHandler)
    print(f"Demo server running on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
