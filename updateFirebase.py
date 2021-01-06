from firebase import firebase
from firebaseData import *

def updateFirebaseColour(colour):  # get the first sheet of the spreadsheet
  firebase.put("lampData", "lampColor", colour)

def getFirebaseColour():
   return (firebase.get("lampData", "lampColor"))



