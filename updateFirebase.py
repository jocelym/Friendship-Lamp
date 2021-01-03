from firebase import Firebase
from Crypto.Cipher import AES
print("hello")
config = {
  "apiKey": "AIzaSyCNJKRu3PRBUgbWmCp_CwYZ4pHZHICjs_U",
  "authDomain": "friendshiplamp-294814.firebaseapp.com",
  "databaseURL": "https://friendshiplamp-294814-default-rtdb.firebaseio.com",
  "storageBucket": "friendshiplamp-294814.appspot.com",
}

firebase = Firebase(config)
db = firebase.database()
ref = db.reference('LampData')
db.reference('LampData').set({lampColor: "Red"})
