
from flask import Blueprint, request, render_template, redirect
from utils.google_sheets import append_to_sheet
from utils.time_helper import get_vietnam_time

them_nguoi_moi_bp = Blueprint("them_nguoi_moi", __name__, url_prefix="/them-nguoi-moi")
DANH_SACH_SHEET_ID = "17NAAz052lT0wHPT2A8fU_qWOzMZxNV_C"

@them_nguoi_moi_bp.route("/", methods=["GET", "POST"])
def them_nguoi_moi():
    if request.method == "POST":
        ten = request.form.get("ten")
        dia_phuong = request.form.get("dia_phuong")
        ns_duong = request.form.get("nam_sinh_duong")
        ns_am = request.form.get("nam_sinh_am")
        ngay_tham_gia = request.form.get("tham_gia_ngay") or get_vietnam_time().strftime("%Y-%m-%d")
        if ten:
            try:
                append_to_sheet(DANH_SACH_SHEET_ID, "Sheet1!A2", [[ten, dia_phuong, ns_duong, ns_am, ngay_tham_gia]])
            except: pass
        return redirect("/them-nguoi-moi")
    return render_template("bo_sung_nguoi_day_du.html")
