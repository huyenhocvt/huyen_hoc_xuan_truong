from flask import Blueprint, render_template, request, redirect
from utils.google_sheets import append_to_sheet, read_sheet
from utils.time_helper import get_current_time_str

lap_cong_viec_bp = Blueprint("lap_cong_viec", __name__, url_prefix="/lap-cong-viec")

CONG_VIEC_SHEET_ID = "1kcbVll1grO42t4-NV9YPQFjlGG9RxDelXUgOMntCz_Y"
DANH_SACH_SHEET_ID = "1rKdIcZ2e0Qp7eRCVt6y9-sibEs9t5KmkvH1LzU3WYT8"

@lap_cong_viec_bp.route("/", methods=["GET", "POST"])
def lap_cong_viec():
    try:
        ds_nguoi = [row[0] for row in read_sheet(DANH_SACH_SHEET_ID, "Sheet1!A2:A") if row]
        if not ds_nguoi:
            ds_nguoi = ["Không có người nào"]
    except:
        ds_nguoi = ["Không có dữ liệu"]

    ds_loai = ["phong thủy", "cúng lễ", "dự án", "liên hệ khách"]

    if request.method == "POST":
        noi_dung = request.form.get("noi_dung", "")
        han = request.form.get("han_hoan_thanh", "")
        nguoi_thuc_hien = request.form.get("nguoi_thuc_hien", "")
        loai_viec = request.form.get("loai_viec", "")
        ghi_chu = request.form.get("ghi_chu", "")

        row = [[
            get_current_time_str(),
            noi_dung,
            han,
            nguoi_thuc_hien,
            loai_viec,
            ghi_chu
        ]]

        try:
            append_to_sheet(CONG_VIEC_SHEET_ID, "Sheet1!A2", row)
        except:
            pass

        return redirect(f"/lap-cong-viec/?success=1&ten={noi_dung}")

    ten_vua_ghi = request.args.get("ten")
    return render_template("lap_cong_viec.html", ds_nguoi=ds_nguoi, ds_loai=ds_loai, ten_vua_ghi=ten_vua_ghi)
