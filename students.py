import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json


class Students():
    def __init__(self):
        self.data = self.connectFirestore()

    def connectFirestore(self):
        cred = credentials.Certificate(
            "./ServiceAccountKey.json")
        app = firebase_admin.initialize_app(cred)

        store = firestore.client()

        studentsCollection = store.collection("students")
        return studentsCollection

    def getClass(self, classID):
        documents = self.data.where('class', '==', classID).stream()
        studentsDict = {el.id: el.to_dict() for el in documents}
        studentsArray = []
        for studentKey, studentValue in studentsDict.items():
            studentsArray.append(studentValue)

        return studentsArray

test = Students()


#print("Klasse 1")
#print(test.getClass("IT8o"))
#print("Klasse 2")
#print(test.getClass())
