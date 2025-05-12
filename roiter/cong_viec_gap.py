from flask import Blueprint, render_template
from utils.google_sheets import read_sheet
from utils.time_helper import get_today_date
from datetime import datetime

cong_viec_gap_bp = Blueprint("cong_viec_gap", __name__, url_prefix="/cong-viec-gap")
SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

@cong_viec_gap_bp.route("/")
def cong_viec_gap():
    ket_qua = []
    try:
        data = read_sheet(SHEET_ID, "Sheet1!A2:F")
        today = get_today_date()
        for row in data:
            if len(row) >= 3:
                try:
                    han_date = datetime.strptime(row[2], "%H:%M - %d/%m/%Y").date()
                    if han_date == today:
                        ket_qua.append(f"Tên công việc: {row[1]} ({row[2]})")
                except: continue
    except: pass
    return render_template("cong_viec_gap.html", list_cong_viec=ket_qua)
