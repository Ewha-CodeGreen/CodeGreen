import pyrebase
import json

class DBhandler:
    def __init__(self):
        # Firebase 초기화
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def insert_item(self, product_id, product_data):
        try:
            self.db.child("items").child(product_id).set(product_data)
            print(f"Item {product_id} successfully inserted into Firebase.")
            return True
        except Exception as e:
            print(f"Error inserting item {product_id} into Firebase: {e}")
            return False

    def get_items(self):
        try:
            items = self.db.child("items").get()
            if items.val():
                print("Items successfully retrieved from Firebase.")
                return items.val()
            return {}
        except Exception as e:
            print(f"Error retrieving items from Firebase: {e}")
            return {}

    def get_item_by_id(self, product_id):
        try:
            item = self.db.child("items").child(product_id).get()
            if item.val():
                print(f"Item {product_id} successfully retrieved from Firebase.")
                return item.val()
            return None
        except Exception as e:
            print(f"Error retrieving item {product_id} from Firebase: {e}")
            return None