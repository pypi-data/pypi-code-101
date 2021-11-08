import http
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = '8756'
PATH = '/tests/resources/'


def start_serve():
    """This method allow us to launch a small http server for our tests."""
    server_address = ("", int(PORT))

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = [""]
    print("Server active on the port :", int(PORT))

    httpd = server(server_address, handler)
    httpd.serve_forever()
