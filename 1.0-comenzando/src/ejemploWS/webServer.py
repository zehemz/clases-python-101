
from socketserver import ThreadingTCPServer
from http.server import SimpleHTTPRequestHandler

if __name__ == "__main__":
    PORT = 8000
    httpd = ThreadingTCPServer(("", PORT), SimpleHTTPRequestHandler)
    print ("serving at port", PORT)
    httpd.serve_forever()
