
from flask import Blueprint, render_template, request, redirect
import pandas as pd
import os
from utils.time_helper import get_current_time_str

lap_cong_viec_bp = Blueprint("lap_cong_viec", __name__, url_prefix="/lap-cong-viec")

CV_FILE = "data/cong_viec.xlsx"
DS_FILE = "data/danh_sach.xlsx"

@lap_cong_viec_bp.route("/", methods=["GET", "POST"])
def lap_cong_viec():
    try:
        df_ds = pd.read_excel(DS_FILE)
        ds_nguoi = df_ds["Tên"].tolist()
    except:
        ds_nguoi = ["Không có dữ liệu"]

    ds_loai = ["phong thủy", "cúng lễ", "dự án", "liên hệ khách"]

    if request.method == "POST":
        noi_dung = request.form.get("noi_dung", "")
        han = request.form.get("han_hoan_thanh", "")
        nguoi_thuc_hien = request.form.get("nguoi_thuc_hien", "")
        loai_viec = request.form.get("loai_viec", "")
        ghi_chu = request.form.get("ghi_chu", "")

        new_row = {
            "Thời gian tạo": get_current_time_str(),
            "Nội dung": noi_dung,
            "Hạn hoàn thành": han,
            "Người thực hiện": nguoi_thuc_hien,
            "Loại công việc": loai_viec,
            "Ghi chú": ghi_chu
        }

        try:
            df_cv = pd.read_excel(CV_FILE)
            df_cv = pd.concat([df_cv, pd.DataFrame([new_row])], ignore_index=True)
        except:
            df_cv = pd.DataFrame([new_row])

        os.makedirs("data", exist_ok=True)
        df_cv.to_excel(CV_FILE, index=False)

        return redirect(f"/lap-cong-viec/?success=1&ten={noi_dung}")

    ten_vua_ghi = request.args.get("ten")
    return render_template("lap_cong_viec.html", ds_nguoi=ds_nguoi, ds_loai=ds_loai, ten_vua_ghi=ten_vua_ghi)
