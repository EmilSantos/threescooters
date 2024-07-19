import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = int(os.environ.get("PORT", 8000))
handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", port), handler)

print(f"Serving on port {port}")
httpd.serve_forever()
