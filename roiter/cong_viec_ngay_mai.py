from flask import Blueprint, render_template
from utils.google_sheets import read_sheet
from utils.time_helper import get_tomorrow_date
from datetime import datetime

cong_viec_ngay_mai_bp = Blueprint("cong_viec_ngay_mai", __name__, url_prefix="/cong-viec-ngay-mai")
SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

@cong_viec_ngay_mai_bp.route("/")
def cong_viec_ngay_mai():
    data = read_sheet(SHEET_ID, "Sheet1!A2:F")
    tomorrow = get_tomorrow_date()
    ket_qua = []

    for row in data:
        if len(row) < 3:
            continue
        noi_dung = row[1]
        han = row[2]
        try:
            han_date = datetime.strptime(han, "%H:%M - %d/%m/%Y").date()
            if han_date == tomorrow:
                ket_qua.append(f"Tên công việc: {noi_dung} ({han})")
        except:
            continue

    return render_template("cong_viec_ngay_mai.html", list_cong_viec=ket_qua)
