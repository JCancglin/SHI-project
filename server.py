from http.server import HTTPServer, BaseHTTPRequestHandler
import openbrewerydb
breweries = openbrewerydb.load(state='texas')

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/home.html'
        
        file = open(self.path[1:]).read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

httpd = HTTPServer(('localhost',8888),Serv)
httpd.serve_forever()