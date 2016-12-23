from http.server import BaseHTTPRequestHandler, HTTPServer
from pprint import pprint


def authenticate():

    class RequestHandler(BaseHTTPRequestHandler):
        def _respond(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

        def do_GET(self):
            self._respond()

            with open('bot/html/auth.html', 'r') as f:
                self.wfile.write(bytes(f.read(), 'utf8'))

            return

        def do_POST(self):
            self._respond()

            data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            d_obj = {}

            for string in data.split('&'):
                key_val = string.split('=')
                d_obj[key_val[0]] = key_val[1]

            with open('login', 'w') as f:
                f.write(d_obj['server'] + '\n' + d_obj['username'] + '\noauth:' + d_obj['access_token'])

            self.wfile.write(bytes("Authentication complete. You can now close the window.", 'utf-8'))

            return


    httpd = HTTPServer(('127.0.0.1', 8082), RequestHandler)

    print("Hey, it doesn't seem like you've authenticated yet. Navigate to the below link and hit accept for me, if you don't mind.")
    print("https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=0kvzk36qysxe0sltumcip8wfil4vfs&redirect_uri=http%3A%2F%2Flocalhost%3A8082&scope=chat_login&force_verify=true")

    httpd.handle_request()
    httpd.handle_request()
