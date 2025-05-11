import os
import io
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
from openpyxl import load_workbook

# Lấy thông tin credentials từ biến môi trường
json_str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not json_str:
    raise ValueError("Missing GOOGLE_APPLICATION_CREDENTIALS_JSON")

creds_info = json.loads(json_str)
creds = service_account.Credentials.from_service_account_info(creds_info)

# Kết nối Google Drive API
drive_service = build("drive", "v3", credentials=creds)

# ID thư mục chứa các file xlsx
folder_id = "1A_VwKn0UqsQIRcbySCzVeSo4guhN0Jdq"

# Lọc các file .xlsx trong thư mục
query = f"'{folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and trashed = false"
results = drive_service.files().list(q=query, fields="files(id, name)").execute()
files = results.get("files", [])

if not files:
    raise Exception("Không tìm thấy file .xlsx nào trong thư mục.")

print("Danh sách file .xlsx:")
for i, file in enumerate(files):
    print(f"{i+1}. {file['name']} ({file['id']})")

# Chọn file để ghi dữ liệu (ở đây chọn file đầu tiên)
file_id = files[0]['id']
print(f"Chọn file: {files[0]['name']}")

# Tải file về RAM
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while not done:
    status, done = downloader.next_chunk()

fh.seek(0)

# Sử dụng openpyxl để chỉnh sửa file
wb = load_workbook(fh)
ws = wb.active
ws.append(["Tên mới", 99])  # Dòng dữ liệu mới

# Ghi đè lại lên Drive
output = io.BytesIO()
wb.save(output)
output.seek(0)

media = MediaIoBaseUpload(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
updated_file = drive_service.files().update(fileId=file_id, media_body=media).execute()

print("Đã ghi dữ liệu vào file:", updated_file['name'])
