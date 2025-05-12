import os
import json
from flask import Flask, render_template

from roiter.lap_cong_viec import lap_cong_viec_bp
from roiter.cong_viec_gap import cong_viec_gap_bp
from roiter.cong_viec_ngay_mai import cong_viec_ngay_mai_bp
from roiter.toan_bo_cong_viec import toan_bo_cong_viec_bp
from roiter.them_nguoi_moi import them_nguoi_moi_bp

# Ghi test vào Google Sheet khi server khởi động
def try_append_to_sheet():
    from datetime import datetime
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    try:
        creds_info = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
        creds = service_account.Credentials.from_service_account_info(
            creds_info,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        now = datetime.now().strftime("%H:%M - %d/%m/%Y")
        values = [[now, "AUTO-TEST", "Test khi khởi động", "GPT", "render", "ghi sheet"]]
        body = {"values": values}
        sheet.values().append(
            spreadsheetId="1kcbVll1grO42t4-NV9YPQFjlGG9RxDelXUgOMntCz_Y",
            range="Sheet1!A2",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()
        print("✅ TEST GHI SHEET THÀNH CÔNG")
    except Exception as e:
        print("❌ TEST GHI SHEET THẤT BẠI:", e)

app = Flask(__name__)

# Đăng ký blueprint
app.register_blueprint(lap_cong_viec_bp)
app.register_blueprint(cong_viec_gap_bp)
app.register_blueprint(cong_viec_ngay_mai_bp)
app.register_blueprint(toan_bo_cong_viec_bp)
app.register_blueprint(them_nguoi_moi_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    try_append_to_sheet()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
