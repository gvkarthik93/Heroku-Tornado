import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import threading
import os


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write("searchDetail:Detail".encode("utf-8"))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

try:
    PORT = int(os.environ.get("PORT", 5000))
    server = ThreadedTCPServer(('', PORT), myHandler)
    print ('Started httpserver on port ' , PORT)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    allow_reuse_address = True
    server.serve_forever()

except KeyboardInterrupt:
    print ('CTRL + C RECEIVED - Shutting down the REST server')
    server.socket.close()
