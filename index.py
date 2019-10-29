from http.server import BaseHTTPRequestHandler
import debugserver
import json
import urllib.parse 
import firestore.students

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

       
        print(firestore.students.test.getClass(1))
        query=urllib.parse.parse_qs(self.path)
        print ("Betreff="+str(query.get('/?Betreff')));
        response = {"Betreff": str(query.get('/?Betreff')),
        "Startzeit":str(query.get('Startzeit')),
        "Endzeit":str(query.get('Endzeit'))}
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return

if __name__ == '__main__':
    debugserver.serve(handler)