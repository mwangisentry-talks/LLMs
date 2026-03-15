#!/usr/bin/env python3
"""
ollama_proxy.py — CORS proxy for LLM Forensic Scanner
Listens on :11435, forwards all requests to Ollama on :11434
with CORS headers added so the browser doesn't block them.

Usage:
    python3 ollama_proxy.py

Optional env vars:
    OLLAMA_HOST   — target Ollama host (default: http://localhost:11434)
    PROXY_PORT    — port this proxy listens on (default: 11435)
"""

import http.server
import urllib.request
import urllib.error
import os
import sys

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
PROXY_PORT  = int(os.environ.get("PROXY_PORT", 11435))

CORS_HEADERS = {
    "Access-Control-Allow-Origin":  "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
}

class ProxyHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        print(f"  [{self.address_string()}] {fmt % args}")

    def send_cors(self):
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)

    # ── Preflight ────────────────────────────────────────────────────────────
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors()
        self.end_headers()

    # ── GET (used for /api/tags) ──────────────────────────────────────────────
    def do_GET(self):
        target = OLLAMA_HOST + self.path
        print(f"  → GET  {target}")
        try:
            req = urllib.request.Request(target)
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read()
                self.send_response(resp.status)
                self.send_cors()
                self.send_header("Content-Type",
                                 resp.headers.get("Content-Type", "application/json"))
                self.end_headers()
                self.wfile.write(body)
        except urllib.error.URLError as e:
            self._error(502, str(e))

    # ── POST (used for /api/chat) ─────────────────────────────────────────────
    def do_POST(self):
        target = OLLAMA_HOST + self.path
        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length)
        print(f"  → POST {target}  ({length} bytes)")
        try:
            req = urllib.request.Request(
                target,
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_cors()
                self.send_header("Content-Type",
                                 resp.headers.get("Content-Type", "application/json"))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.URLError as e:
            self._error(502, str(e))

    def _error(self, code, msg):
        self.send_response(code)
        self.send_cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(f'{{"error":"{msg}"}}'.encode())
        print(f"  ✗ Error {code}: {msg}")


def main():
    print("┌─────────────────────────────────────────────────┐")
    print("│  Ollama CORS Proxy — LLM Forensic Scanner       │")
    print("├─────────────────────────────────────────────────┤")
    print(f"│  Listening  →  http://localhost:{PROXY_PORT}          │")
    print(f"│  Forwarding →  {OLLAMA_HOST:<33}│")
    print("│  Toggle PROXY switch ON in the scanner UI       │")
    print("│  Press Ctrl+C to stop                           │")
    print("└─────────────────────────────────────────────────┘")

    server = http.server.HTTPServer(("localhost", PROXY_PORT), ProxyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Proxy stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
