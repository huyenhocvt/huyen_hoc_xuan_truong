from flask import Blueprint, request, render_template, redirect
from utils.google_sheets import append_to_sheet

them_nguoi_moi_bp = Blueprint("them_nguoi_moi", __name__, url_prefix="/them-nguoi-moi")
DANH_SACH_SHEET_ID = "17NAAz052lT0wHPT2A8fU_qWOzMZxNV_C"

@them_nguoi_moi_bp.route("/", methods=["GET", "POST"])
def them_nguoi_moi():
    if request.method == "POST":
        ten = request.form.get("nguoi_moi")
        if ten:
            try:
                append_to_sheet(DANH_SACH_SHEET_ID, "Sheet1!A2", [[ten]])
            except: pass
        return redirect("/lap-cong-viec")
    return render_template("danh_sach_nguoi.html")
