
from flask import Blueprint, render_template, request, session
from datetime import datetime

lap_cong_viec_bp = Blueprint("lap_cong_viec", __name__, url_prefix="/lap-cong-viec")

@lap_cong_viec_bp.route("/", methods=["GET", "POST"])
def lap_cong_viec():
    if "cong_viec_list" not in session:
        session["cong_viec_list"] = []

    if request.method == "POST":
        row = {
            "Thời gian tạo": datetime.now().strftime("%H:%M – %d/%m/%Y"),
            "Nội dung": request.form.get("noi_dung"),
            "Hạn hoàn thành": request.form.get("han_hoan_thanh"),
            "Người thực hiện": request.form.get("nguoi_thuc_hien"),
            "Loại công việc": request.form.get("loai_viec"),
            "Ghi chú": request.form.get("ghi_chu")
        }
        session["cong_viec_list"].append(row)
        session.modified = True

    return render_template("lap_cong_viec.html", data=session.get("cong_viec_list", []))
