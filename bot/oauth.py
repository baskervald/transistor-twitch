from http.server import BaseHTTPRequestHandler, HTTPServer
from pprint import pprint

def authenticate(auth_obj):
    class RequestHandler(BaseHTTPRequestHandler):
        def _respond(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

        def do_GET(self):
            self._respond()

            if self.path == '/auth':
                with open('bot/html/auth.html', 'r') as f:
                    self.wfile.write(bytes(f.read(), 'utf8'))
            else:
                with open('bot/html/main.html', 'r') as f:
                    self.wfile.write(bytes(f.read(), 'utf8'))

            return

        def do_POST(self):
            self._respond()

            data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')

            for string in data.split('&'):
                key_val = string.split('=')
                auth_obj[key_val[0]] = key_val[1]

            return

    httpd = HTTPServer(('127.0.0.1', 8082), RequestHandler)
    while not auth_obj:
        httpd.handle_request()
