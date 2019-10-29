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

        query = urllib.parse.parse_qs(self.path)
        betreff = str(query.get('/?Betreff')
                      ).replace("[", "").replace("]", "").replace("'", "")
        aktionstyp = str(query.get('Aktionstyp')).replace(
            "[", "").replace("]", "").replace("'", "")
        print("Betreff="+betreff + " Aktionstyp="+aktionstyp)

        query=urllib.parse.parse_qs(self.path)
        betreff=str(query.get('/?Betreff')).replace("[","").replace("]","").replace("'","")
        aktionstyp=str(query.get('Aktionstyp')).replace("[","").replace("]","").replace("'","")
        print ("Betreff="+betreff+ " Aktionstyp="+aktionstyp)

        if aktionstyp=="updated":
            print(students.test.getClass(betreff))
            pupils =students.test.getClass(betreff)
            for pupil in pupils:
                msg = f"Hey {pupil['first_name']} deine Stunde fällt aus, wie wäre es mit dem Thema {pupil['topics']['topic1']}"

                youtubeLink = "https://www.youtube.com/results?search_query=" + \
                    pupil['topics']['topic1'].replace(" ", "+")

                data = {
                    "msg": msg, "link": youtubeLink}

                print(data)
                requests.post(pupil['flow_id'], json=data)

        response = {"Betreff": str(query.get('/?Betreff')),
                    "Startzeit": str(query.get('Startzeit')),
                    "Endzeit": str(query.get('Endzeit')),
                    "Aktionstyp": str(query.get('Aktionstyp')),
                    }
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return


if __name__ == '__main__':
    debugserver.serve(handler)
