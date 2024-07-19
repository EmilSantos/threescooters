import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

port = int(os.environ.get("PORT", 8000))
handler = CustomHTTPRequestHandler
httpd = HTTPServer(("", port), handler)

print(f"Serving on port {port}")
httpd.serve_forever()
