import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def insert_item(self, product_id, product_data):
        # Firebase에 데이터 저장
        try:
            self.db.child("items").child(product_id).set(product_data)
            print("Item successfully inserted into Firebase.")
            return True
        except Exception as e:
            print(f"Error inserting item into Firebase: {e}")
            return False
