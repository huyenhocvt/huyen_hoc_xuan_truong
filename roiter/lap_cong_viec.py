
from flask import Blueprint, render_template, request, session
from datetime import datetime
from utils.google_sheets import append_row_cong_viec
from utils.time_helper import get_vietnam_time

lap_cong_viec_bp = Blueprint("lap_cong_viec", __name__, url_prefix="/lap-cong-viec")

@lap_cong_viec_bp.route("/", methods=["GET", "POST"])
def lap_cong_viec():
    if "cong_viec_list" not in session:
        session["cong_viec_list"] = []

    if request.method == "POST":
        now = get_vietnam_time().strftime("%H:%M – %d/%m/%Y")
        row = {
            "ngay_setup": now,
            "noi_dung": request.form.get("noi_dung"),
            "han_hoan_thanh": request.form.get("han_hoan_thanh"),
            "nguoi_thuc_hien": request.form.get("nguoi_thuc_hien"),
            "loai_viec": request.form.get("loai_viec"),
            "ghi_chu": request.form.get("ghi_chu")
        }
        session["cong_viec_list"].append(row)
        append_row_cong_viec([
            now,
            row["noi_dung"],
            row["han_hoan_thanh"],
            row["nguoi_thuc_hien"],
            row["loai_viec"],
            row["ghi_chu"]
        ])
        session.modified = True

    return render_template("lap_cong_viec_day_du.html", data=session.get("cong_viec_list", []))
