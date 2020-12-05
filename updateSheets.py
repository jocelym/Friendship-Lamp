 
import gspread
#import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials 

# define scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive',     'https://www.googleapis.com/auth/spreadsheets',
]


# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('friendshiplamp-294814-6adcb4a4b415.json', scope)

client = gspread.authorize(creds)

# get instance of the Spreadsheet
sheet = client.open('LampColor')

sheet_instance = sheet.get_worksheet(0)


def updateSheetColour(colour):# get the first sheet of the spreadsheet
    sheet_instance.update_cell(1, 1, colour)
    
def getSheetColour():
    return sheet_instance.cell(1,1).value