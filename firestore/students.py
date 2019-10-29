import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json


class Students():
    def __init__(self):
        self.data = self.connectFirestore

    def connectFirestore(self):
        cred = credentials.Certificate("./firestore/ServiceAccountKey.json")
        app = firebase_admin.initialize_app(cred)

        store = firestore.client()

        studentsCollection = store.collection("students")
        return studentsCollection

    def getClass(self, classID):
        students = self.data.select(u'class', u'==', self.classID)
        return students


test = Students()

test.getClass(1)

