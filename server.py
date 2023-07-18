from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

hostName = "localhost"
serverPort = 8080

class MusicServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = Path(self.path)
        
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            f = open('index.html', 'rb')
            self.wfile.write(f.read())
            f.close()
        else:
            self.send_error(404, 'File Not Found')

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MusicServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")