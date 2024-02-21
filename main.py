from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class App(BaseHTTPRequestHandler):
    def do_POST(self):
        length = self.headers.get("content-length", 0)
        body = json.loads(self.rfile.read(int(length)))

        self.send_response(200)
        self.end_headers()

        if set(body.keys()) == {'name', 'password'}:
            if body['name'] != 'Lucas' and body['password'] != 'pass':
                self.wfile.write(bytes("Invalid username and password", "utf-8"))
                return

            if body['name'] != 'Lucas':
                self.wfile.write(bytes("Invalid username", "utf-8"))
                return

            if body['password'] != 'pass':
                self.wfile.write(bytes("Invalid password", "utf-8"))
                return

            self.wfile.write(bytes(F"Welcome {body['name']}!", "utf-8"))
            return
        pass
    pass

if __name__ == "__main__":
    app = HTTPServer(("localhost", 8080), App)
    app.serve_forever()

