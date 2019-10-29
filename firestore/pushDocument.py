import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json

# Credentials
cred = credentials.Certificate("./firestore/ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

jsonPath = open("./firestore/students.json", "r")
collection = "students"

data = json.load(jsonPath)

for student in data:
    documentName = student["id"]

store.collection(collection).document(documentName).set(data)
