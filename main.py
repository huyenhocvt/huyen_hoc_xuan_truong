from flask import Flask, render_template, request, redirect
from utils.google_sheets import read_sheet, append_to_sheet
from utils.time_helper import get_current_time_str, get_today_date, get_tomorrow_date
from datetime import datetime

app = Flask(__name__)

SHEET_CONG_VIEC = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"
SHEET_DANH_SACH = "17NAAz052lT0wHPT2A8fU_qWOzMZxNV_C"

@app.route("/")
def home():
    return redirect("/lap-cong-viec")

@app.route("/lap-cong-viec", methods=["GET", "POST"])
def lap_cong_viec():
    if request.method == "POST":
        noi_dung = request.form["noi_dung"]
        han = request.form["han_hoan_thanh"]
        nguoi = request.form["nguoi_thuc_hien"]
        loai = request.form["loai_viec"]
        ghi_chu = request.form.get("ghi_chu", "")
        ngay_setup = get_current_time_str()
        row = [[ngay_setup, noi_dung, han, nguoi, loai, ghi_chu]]
        append_to_sheet(SHEET_CONG_VIEC, "Sheet1!A2", row)
        return redirect("/lap-cong-viec")

    ds_nguoi = [row[0] for row in read_sheet(SHEET_DANH_SACH, "Sheet1!A2:A") if row]
    ds_loai = sorted(set([row[4] for row in read_sheet(SHEET_CONG_VIEC, "Sheet1!E2:E") if len(row) >= 5]))
    return render_template("lap_cong_viec.html", ds_nguoi=ds_nguoi, ds_loai=ds_loai)

@app.route("/them-nguoi-moi", methods=["GET", "POST"])
def them_nguoi_moi():
    if request.method == "POST":
        ten = request.form["ten"]
        append_to_sheet(SHEET_DANH_SACH, "Sheet1!A2", [[ten]])
        return redirect("/lap-cong-viec")
    return render_template("them_nguoi_moi.html")

@app.route("/cong-viec-gap")
def cong_viec_gap():
    today = get_today_date()
    data = read_sheet(SHEET_CONG_VIEC, "Sheet1!A2:F")
    kq = []
    for row in data:
        if len(row) >= 3:
            try:
                d = datetime.strptime(row[2], "%Y-%m-%dT%H:%M")
                if d.date() == today:
                    kq.append(f"Tên công việc: {row[1]} ({row[2]})")
            except:
                continue
    return render_template("cong_viec_gap.html", list_cong_viec=kq)

@app.route("/cong-viec-ngay-mai")
def cong_viec_ngay_mai():
    tomorrow = get_tomorrow_date()
    data = read_sheet(SHEET_CONG_VIEC, "Sheet1!A2:F")
    kq = []
    for row in data:
        if len(row) >= 3:
            try:
                d = datetime.strptime(row[2], "%Y-%m-%dT%H:%M")
                if d.date() == tomorrow:
                    kq.append(f"Tên công việc: {row[1]} ({row[2]})")
            except:
                continue
    return render_template("cong_viec_ngay_mai.html", list_cong_viec=kq)

@app.route("/toan-bo-cong-viec")
def toan_bo_cong_viec():
    data = read_sheet(SHEET_CONG_VIEC, "Sheet1!A2:F")
    kq = []
    for row in data:
        if len(row) >= 3:
            try:
                d = datetime.strptime(row[2], "%Y-%m-%dT%H:%M")
                kq.append((d, f"Tên công việc: {row[1]} ({row[2]})"))
            except:
                continue
    kq.sort()
    return render_template("toan_bo_cong_viec.html", list_cong_viec=[i[1] for i in kq])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
