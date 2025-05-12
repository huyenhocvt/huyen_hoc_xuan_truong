
from flask import Flask, render_template, request
from google_sheets import append_row_cong_viec
from time_helper import get_vietnam_time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lap-cong-viec/", methods=["GET", "POST"])
def lap_cong_viec():
    if request.method == "POST":
        noi_dung = request.form["noi_dung"]
        han_hoan_thanh = request.form["han_hoan_thanh"]
        nguoi_thuc_hien = request.form["nguoi_thuc_hien"]
        loai_viec = request.form["loai_viec"]
        ghi_chu = request.form["ghi_chu"]
        ngay_setup = get_vietnam_time()

        success = append_row_cong_viec([
            ngay_setup,
            noi_dung,
            han_hoan_thanh,
            nguoi_thuc_hien,
            loai_viec,
            ghi_chu,
        ])

        if not success:
            print("❌ GHI SHEET THẤT BẠI")
        else:
            print("✅ GHI SHEET THÀNH CÔNG")

    return render_template("lap_cong_viec.html")

if __name__ == "__main__":
    print("⚙ TEST GHI SHEET...")
    test = append_row_cong_viec([
        get_vietnam_time(), "TEST", "2025-05-13", "Người test", "Test", "Nội dung test"
    ])
    if not test:
        print("❌ TEST GHI SHEET THẤT BẠI")
    else:
        print("✅ TEST GHI SHEET OK")

    app.run(debug=False, host="0.0.0.0", port=10000)
