from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())

        elif self.path == "/show-more":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome to the Python Backend")

        elif self.path == "/style.css":
            self.send_response(200)
            self.send_header("Content-Type", "text/css")
            self.end_headers()
            with open("style.css", "rb") as f:
                self.wfile.write(f.read())

    def do_POST(self):
        if self.path == "/upload":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome to the Python Backend")


PORT = 8000
server = HTTPServer(("127.0.0.1", PORT), MyHandler)
print(f"Running → http://127.0.0.1:{PORT}")
server.serve_forever()
