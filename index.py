from http.server import BaseHTTPRequestHandler
import debugserver
import json
import urllib.parse 
import students
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()


        query=urllib.parse.parse_qs(self.path)
        betreff=str(query.get('/?Betreff')).replace("[","").replace("]","").replace("'","")
        aktionstyp=str(query.get('Aktionstyp')).replace("[","").replace("]","").replace("'","")
        print ("Betreff="+betreff+ " Aktionstyp="+aktionstyp)

        if aktionstyp=="deleted":
            print(students.test.getClass(betreff))
            pupils =students.test.getClass(betreff)
            for pupil in pupils:
                msg={"msg":"es geht"}
                print("FlowID="+pupil['flow_id'])
                requests.post(pupil['flow_id'],json=msg)

        response = {"Betreff": str(query.get('/?Betreff')),
        "Startzeit":str(query.get('Startzeit')),
        "Endzeit":str(query.get('Endzeit')),
        "Aktionstyp":str(query.get('Aktionstyp')),
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return

if __name__ == '__main__':
    debugserver.serve(handler)
