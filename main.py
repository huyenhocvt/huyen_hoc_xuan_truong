import os
import json
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Đọc JSON từ biến môi trường
json_str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not json_str:
    raise ValueError("Environment variable GOOGLE_APPLICATION_CREDENTIALS_JSON is missing")

creds_info = json.loads(json_str)
creds = service_account.Credentials.from_service_account_info(creds_info)

# Kết nối tới Google Drive API
service = build("drive", "v3", credentials=creds)

# Test: liệt kê 10 file đầu tiên
results = service.files().list(pageSize=10, fields="files(id, name)").execute()
items = results.get("files", [])

print("Files:")
for item in items:
    print(f"{item['name']} ({item['id']})")