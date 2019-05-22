#!/usr/local/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(b"hello !")


print('starting server...')
serv = HTTPServer(("93.175.2.143", 80), HttpProcessor)
print('running server...')
serv.serve_forever()