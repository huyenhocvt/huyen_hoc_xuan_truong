from flask import Blueprint, request, render_template, redirect, session
from datetime import datetime, timedelta

them_nguoi_moi_bp = Blueprint("them_nguoi_moi", __name__, url_prefix="/them-nguoi-moi")

def get_vietnam_time():
    return datetime.utcnow() + timedelta(hours=7)

def nam_sinh_can_chi(nam):
    can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    return f"{nam} – {can[(nam + 6) % 10]} {chi[(nam + 8) % 12]}"

@them_nguoi_moi_bp.route("/", methods=["GET", "POST"])
def them_nguoi_moi():
    if request.method == "GET":
        session["danh_sach_nguoi"] = []

    if "danh_sach_nguoi" not in session:
        session["danh_sach_nguoi"] = []

    if request.method == "POST":
        ten = request.form.get("ten")
        dia_phuong = request.form.get("dia_phuong")
        ns_raw = request.form.get("nam_sinh")  # có thể là "1974" hoặc "1974 – Giáp Dần"

        try:
            nam = int(ns_raw.strip().split("–")[0])
            nam_sinh = nam_sinh_can_chi(nam)
        except:
            nam_sinh = ns_raw

        try:
            raw_date = request.form.get("tham_gia_ngay")
            if raw_date:
                ngay_tham_gia = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%d/%m/%Y")
            else:
                ngay_tham_gia = get_vietnam_time().strftime("%d/%m/%Y")
        except:
            ngay_tham_gia = get_vietnam_time().strftime("%d/%m/%Y")

        row = {
            "ten": ten,
            "dia_phuong": dia_phuong,
            "nam_sinh": nam_sinh,
            "tham_gia_ngay": ngay_tham_gia
        }

        session["danh_sach_nguoi"].append(row)
        session.modified = True
        return redirect("/them-nguoi-moi")

    return render_template("bo_sung_nguoi_day_du.html", data=session.get("danh_sach_nguoi", []))