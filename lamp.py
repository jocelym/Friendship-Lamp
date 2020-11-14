import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials 

# define scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive',     'https://www.googleapis.com/auth/spreadsheets',
]


# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('FriendshipLamp-4703d7cd20c9.json', scope)

client = gspread.authorize(creds)

# get instance of the Spreadsheet
sheet = client.open('LampColor')

# get the first sheet of the spreadsheet
sheet_instance = sheet.get_worksheet(0)

sheet_instance.update_cell(1, 1, 1)

