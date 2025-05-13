from roiter.nhan_seri_tien import nhan_seri_bp

from flask import Flask, render_template
from roiter.lap_cong_viec import lap_cong_viec_bp
from roiter.them_nguoi_moi import them_nguoi_moi_bp
from roiter.time_checkbox import time_checkbox_bp

app = Flask(__name__)
app.secret_key = "lapcongviec_2025"

# Đăng ký các blueprint
app.register_blueprint(nhan_seri_bp)
app.register_blueprint(lap_cong_viec_bp)
app.register_blueprint(them_nguoi_moi_bp)
app.register_blueprint(time_checkbox_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)