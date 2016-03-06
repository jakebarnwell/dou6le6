from firebase import firebase

class FirebaseWrapper:
    def __init__(self, url, db_store):
        self.firebase = firebase.FirebaseApplication(url, None)
        self.db_store = db_store
        
    def write_data(self, key, data):
        result = self.firebase.put(self.db_store, key, data)
        return result

    def get_data(self, key):
        result = self.firebase.get(self.db_store, key)
        return result
