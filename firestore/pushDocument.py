import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json

# Credentials
cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

jsonPath = "./students.json"
collection = "students"

data = json.load(open(jsonPath, "r").read())

for student in data:
    documentName = student["id"]

store.collection(collection).document(documentName).set(data)