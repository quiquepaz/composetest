import http.server
import socketserver
from http import HTTPStatus
from urllib.request import urlopen


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        if self.path == "/httpbin":
            res = urlopen("https://httpbin.org/bytes/32")
            self.wfile.write("httpbin says: ".encode() + res.read())
        else:
            self.wfile.write(b"server.py says: Hello, world!\n")


httpd = socketserver.TCPServer(("", 8080), Handler)
httpd.serve_forever()
