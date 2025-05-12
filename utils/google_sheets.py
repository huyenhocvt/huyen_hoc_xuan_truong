import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Ủy quyền sử dụng Google Sheets
def get_gspread_client():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    service_account_info = json.loads(os.environ.get("GOOGLE_SERVICE_ACCOUNT", "{}"))
    credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)
    return gspread.authorize(credentials)

def append_row_cong_viec(row_data):
    try:
        gc = get_gspread_client()
        sheet = gc.open("cong_viec_gsheet")
        worksheet = sheet.worksheet("ngay_setup")  # Tên tab thực tế
        worksheet.append_row(row_data)
        return True
    except Exception as e:
        print("❌ Lỗi append_row_cong_viec:", e)
        return False
