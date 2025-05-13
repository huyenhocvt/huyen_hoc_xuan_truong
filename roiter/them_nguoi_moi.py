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
            "nam_sinh": request.form.get("nam_sinh"),
            "tham_gia_ngay": "",
        }

        raw_date = request.form.get("tham_gia_ngay")
        if raw_date:
            try:
                row["tham_gia_ngay"] = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%d/%m/%Y")
            except:
                row["tham_gia_ngay"] = raw_date

        session["danh_sach_nguoi"].append(row)
        session.modified = True
        return redirect("/them-nguoi-moi")

    return render_template("bo_sung_nguoi_day_du.html", data=session.get("danh_sach_nguoi", []))