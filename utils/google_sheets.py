import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_service():
    creds_info = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
    creds = service_account.Credentials.from_service_account_info(
        creds_info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)

def read_sheet(spreadsheet_id, range_name):
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get("values", [])

def write_sheet(spreadsheet_id, range_name, values):
    service = get_service()
    sheet = service.spreadsheets()
    body = {"values": values}
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()

def append_to_sheet(spreadsheet_id, range_name, values):
    service = get_service()
    sheet = service.spreadsheets()
    body = {"values": values}
    sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
