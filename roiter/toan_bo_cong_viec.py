from flask import Blueprint, render_template
from utils.google_sheets import read_sheet
from datetime import datetime

toan_bo_cong_viec_bp = Blueprint("toan_bo_cong_viec", __name__, url_prefix="/toan-bo-cong-viec")
SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

@toan_bo_cong_viec_bp.route("/")
def toan_bo_cong_viec():
    data = read_sheet(SHEET_ID, "Sheet1!A2:F")
    ket_qua = []

    for row in data:
        if len(row) < 3:
            continue
        noi_dung = row[1]
        han = row[2]
        try:
            han_date = datetime.strptime(han, "%H:%M - %d/%m/%Y")
            ket_qua.append((han_date, f"Tên công việc: {noi_dung} ({han})"))
        except:
            continue

    ket_qua.sort()
    list_cong_viec = [row[1] for row in ket_qua]
    return render_template("toan_bo_cong_viec.html", list_cong_viec=list_cong_viec)
