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

def append_row_cong_viec(row_data):
    try:
        sheet_id = "1kcbVll1grO42t4-NV9YPQFjlGG9RxDelXUgOMntCz_Y"
        range_name = "'ngay_setup'!A2"
        service = get_service()
        sheet = service.spreadsheets()
        body = {"values": [row_data]}
        sheet.values().append(
            spreadsheetId=sheet_id,
            range=range_name,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()
        return True
    except Exception as e:
        print("❌ Lỗi ghi sheet:", e)
        return False
