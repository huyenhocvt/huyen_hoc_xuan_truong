from flask import Blueprint, render_template
from utils.google_sheets import read_sheet
from datetime import datetime

toan_bo_cong_viec_bp = Blueprint("toan_bo_cong_viec", __name__, url_prefix="/toan-bo-cong-viec")
SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

@toan_bo_cong_viec_bp.route("/")
def toan_bo_cong_viec():
    ket_qua = []
    try:
        data = read_sheet(SHEET_ID, "Sheet1!A2:F")
        for row in data:
            if len(row) >= 3:
                try:
                    han_date = datetime.strptime(row[2], "%H:%M - %d/%m/%Y")
                    ket_qua.append((han_date, f"Tên công việc: {row[1]} ({row[2]})"))
                except: continue
        ket_qua.sort()
    except: pass
    return render_template("toan_bo_cong_viec.html", list_cong_viec=[k[1] for k in ket_qua])
