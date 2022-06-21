import http.server
import socketserver

import config

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", config.SERVER_PORT), Handler) as httpd:
    print("serving at port", config.SERVER_PORT)
    httpd.serve_forever()