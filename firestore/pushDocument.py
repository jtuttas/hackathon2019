import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json

# Credentials
cred = credentials.Certificate("./firestore/ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

jsonPath = open("./firestore/students.json", "r", encoding="UTF-8")
collection = "students"

data = json.load(jsonPath)

for student in data:
    documentName = student["first_name"] + student["last_name"]

    store.collection(collection).document(documentName).set(student)
