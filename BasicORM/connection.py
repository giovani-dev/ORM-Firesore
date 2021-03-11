import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials


class DataBaseConnection(object):
    def __init__(self):
        cred = credentials.ApplicationDefault()
        cred = credentials.Certificate("C:\\Users\\Pichau\\Documents\\projects\\ORM-Firesore\\BasicORM\\auth\\token.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
