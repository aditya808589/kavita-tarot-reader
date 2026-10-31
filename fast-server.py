#!/usr/bin/env python3
"""
High-Performance Multi-threaded Local HTTP Server with Gzip & Caching
Designed for ultra-fast <1 second page loads over Cloudflare Tunnels & local networks.
"""

import os
import sys
import gzip
import io
import mimetypes
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

COMPRESSIBLE_TYPES = {
    'text/html',
    'text/css',
    'application/javascript',
    'text/javascript',
    'application/json',
    'image/svg+xml',
    'text/plain'
}

class FastRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # High performance browser caching
        path = self.path.split('?')[0]
        if path.endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif', '.ico', '.woff2', '.woff')):
            self.send_header('Cache-Control', 'public, max-age=604800, immutable')
        elif path.endswith(('.css', '.js')):
            self.send_header('Cache-Control', 'public, max-age=86400')
        else:
            self.send_header('Cache-Control', 'no-cache')

        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    def do_GET(self):
        # Check if client supports gzip
        accept_encoding = self.headers.get('Accept-Encoding', '')
        supports_gzip = 'gzip' in accept_encoding

        # Map request to local file path
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for index in "index.html", "index.htm":
                index_path = os.path.join(path, index)
                if os.path.exists(index_path):
                    path = index_path
                    break

        if not os.path.isfile(path):
            return super().do_GET()

        ctype = self.guess_type(path)
        is_compressible = any(ctype.startswith(t) for t in COMPRESSIBLE_TYPES)

        if supports_gzip and is_compressible:
            try:
                with open(path, 'rb') as f:
                    content = f.read()

                # Compress content in-memory
                out = io.BytesIO()
                with gzip.GzipFile(fileobj=out, mode='wb', compresslevel=6) as gz:
                    gz.write(content)
                compressed = out.getvalue()

                self.send_response(200)
                self.send_header('Content-Type', ctype)
                self.send_header('Content-Encoding', 'gzip')
                self.send_header('Content-Length', str(len(compressed)))
                self.end_headers()
                self.wfile.write(compressed)
                return
            except Exception:
                pass

        return super().do_GET()

    def log_message(self, format, *args):
        # Keep logs clean
        pass

if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', PORT), FastRequestHandler)
    print(f"Fast ThreadingHTTPServer running on port {PORT} with Gzip & Caching enabled.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
