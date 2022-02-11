from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from os import curdir, sep
import cv2

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path=urlparse.urlparse(self.path)
        print(dict(urlparse.parse_qsl(parsed_path.query))['func'])
        if (dict(urlparse.parse_qsl(parsed_path.query))['func'] == 'Serial'):
            path="volume/"+dict(urlparse.parse_qsl(parsed_path.query))['picname']
            try:
                """
                f = open( curdir+sep+"/index.html")
                self.send_response(200)
                self.send_header('Content-type', "text/html")
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

                """
                f = open(path,"rb")
                l = f.read()
                self.send_response(200)
                self.send_header("Content-type", "image/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("< img src = 'help.jpg' alt = 'help.jpg' width = '320' >","utf-8"))
                #self.wfile.write(l)
                #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
                f.close()


            except IOError:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("image not found", "utf-8"))
                #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
        if (dict(urlparse.parse_qsl(parsed_path.query))['func'] == 'facedetection'):
            path="volume/"+dict(urlparse.parse_qsl(parsed_path.query))['picname']
            try:
                f = open(path,"rb")
                f.close()
            except IOError:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("image not found", "utf-8"))
                self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))





def main():
    PORT = 8080
    server = HTTPServer(('',PORT),MyServer)
    print(server.server_address)
    print('server running on port %s' % PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()
