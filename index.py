from http.server import BaseHTTPRequestHandler
import debugserver
import json
import urllib.parse 

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
       
        query=urllib.parse.parse_qs(self.path)
        print ("msg="+str(query.get('msg')));
        response = {"hello": "world"}
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return

if __name__ == '__main__':
    debugserver.serve(handler)