import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("./firestore/ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

studentsCollection = store.collection("students")

students = studentsCollection.where('class', '==', 1).get()

studentsArray = []

studentsDict = {el.id: el.to_dict() for el in students}
studentsArray = [student for student in studentsDict.items()]

print(studentsArray)

