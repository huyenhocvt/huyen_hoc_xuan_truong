import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_sheets_service():
    json_str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not json_str:
        raise ValueError("Thiếu biến môi trường GOOGLE_APPLICATION_CREDENTIALS_JSON")
    creds_info = json.loads(json_str)
    creds = service_account.Credentials.from_service_account_info(creds_info)
    return build("sheets", "v4", credentials=creds)

def read_sheet(spreadsheet_id, range_name):
    service = get_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get("values", [])

def append_to_sheet(spreadsheet_id, range_name, values):
    service = get_sheets_service()
    body = {"values": values}
    sheet = service.spreadsheets()
    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
    return result
