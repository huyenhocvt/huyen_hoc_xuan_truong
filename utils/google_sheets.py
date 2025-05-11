import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

def get_service():
    creds = service_account.Credentials.from_service_account_file(
        "huyen-hoc-xuan-truong-65735531de1c.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)

def load_sheet_id(alias):
    with open("data/sheet_ids.json", "r") as f:
        sheet_ids = json.load(f)
    return sheet_ids.get(alias)

def read_sheet(alias, range_name):
    sheet_id = load_sheet_id(alias)
    return get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute().get("values", [])

def append_to_sheet(alias, range_name, values):
    sheet_id = load_sheet_id(alias)
    return get_service().spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={"values": values}
    ).execute()
