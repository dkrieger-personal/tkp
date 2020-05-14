import http.server as http

class MyHandler(http.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>TEST</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web serverxxx</p>", "utf-8"))
        self.wfile.write(bytes("<iframe>src='file:///C:/Users/David/web/erase.txt' width='1000' height='1000'</iframe>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

def run(server_class=http.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    print('serving...')
    run()