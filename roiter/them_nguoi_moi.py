from flask import Blueprint, request, render_template, redirect, session
from datetime import datetime

them_nguoi_moi_bp = Blueprint("them_nguoi_moi", __name__, url_prefix="/them-nguoi-moi")

@them_nguoi_moi_bp.route("/", methods=["GET", "POST"])
def them_nguoi_moi():
    if "danh_sach_nguoi" not in session:
        session["danh_sach_nguoi"] = []

    if request.method == "POST":
        row = {
            "ten": request.form.get("ten"),
            "dia_phuong": request.form.get("dia_phuong"),
            "nam_sinh_duong": request.form.get("nam_sinh_duong"),
            "nam_sinh_am": request.form.get("nam_sinh_am"),
            "tham_gia_ngay": request.form.get("tham_gia_ngay") or datetime.now().strftime("%Y-%m-%d")
        }
        session["danh_sach_nguoi"].append(row)
        session.modified = True
        return redirect("/them-nguoi-moi")

    return render_template("bo_sung_nguoi_day_du.html", data=session.get("danh_sach_nguoi", []))