import os
cwd = os.getcwd()

token_dir = os.path.join(cwd, "token")

import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
# Path to your service account key file
# CREDENTIALS = os.environ['CREDENTIALS']
CREDENTIALS = os.path.join('credentials.json')
creds = Credentials.from_service_account_file(CREDENTIALS, scopes=scopes)
client = gspread.authorize(creds)

# sheet_id = os.environ['SHEET_ID']
sheet = client.open_by_key('1_SyiH5d-02uHIx9ID4ab2EuZTx2uTsVO8KF8EenI7yo').sheet1

# values_list = sheet.sheet1.get_all_values()
