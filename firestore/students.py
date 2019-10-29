import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json


class Students():
    def __init__(self):
        self.data = self.connectFirestore()

    def connectFirestore(self):
        cred = credentials.Certificate(
            "./firestore/ServiceAccountKey.json")
        app = firebase_admin.initialize_app(cred)

        store = firestore.client()

        studentsCollection = store.collection("students")
        return studentsCollection

    def getClass(self, classID):
        documents = self.data.where('class', '==', 1).stream()
        studentsDict = {el.id: el.to_dict() for el in documents}
        studentsArray = [student for student in studentsDict.items()]

        return studentsArray


test = Students()

#print("Klasse 1")
#print(test.getClass(1))
#print("Klasse 2")
#print(test.getClass())
