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
                self.send_header('Content-type', "image/png")
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

                """
                f = open(path,"rb")
                l = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                #self.wfile.write(bytes("< img src = 'Capture.png' alt = 'Capture.png' width = '320' >", "utf-8"))
                #self.wfile.write(bytes("<a href= \"/Capture.png\"  download> \n <img src= \"/Capture.png\" alt=\"aa\"> \n </a>", "utf-8"))
                self.wfile.write(bytes("<a href= \"/Capture.png\"  \n  download>Download link</a>", "utf-8"))
                #self.wfile.write(bytes("<img src=\"Capture.png\" width=60% height=20%>","utf-8"))
                #self.wfile.write(l)
                #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
                f.close()


            except IOError:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>serial response</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("image not found", "utf-8"))
                #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
        if (dict(urlparse.parse_qsl(parsed_path.query))['func'] == 'facedetection'):
            path="volume/"+dict(urlparse.parse_qsl(parsed_path.query))['picname']
            try:
                f = open(path,"rb")
                # Create the haar cascade
                faceCascade = cv2.CascadeClassifier("haarcascade_frontface_default.xml")
                # Read the image
                image = cv2.imread(path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Detect faces in the image
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                    # flags = cv2..CV_HAAR_SCALE_IMAGE
                )
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>facedetection</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("Found {0} faces!".format(len(faces)), "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
                print("Found {0} faces!".format(len(faces)))
                f.close()
            except IOError:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>facedetection</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request:  %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("image not found", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))





def main():
    PORT = 8080
    server = HTTPServer(('',PORT),MyServer)
    print(server.server_address)
    print('server running on port %s' % PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()
