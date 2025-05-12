import os
from flask import Flask, render_template

from roiter.lap_cong_viec import lap_cong_viec_bp
from roiter.cong_viec_gap import cong_viec_gap_bp
from roiter.cong_viec_ngay_mai import cong_viec_ngay_mai_bp
from roiter.toan_bo_cong_viec import toan_bo_cong_viec_bp
from roiter.them_nguoi_moi import them_nguoi_moi_bp

app = Flask(__name__)

# Đăng ký các blueprint
app.register_blueprint(lap_cong_viec_bp)
app.register_blueprint(cong_viec_gap_bp)
app.register_blueprint(cong_viec_ngay_mai_bp)
app.register_blueprint(toan_bo_cong_viec_bp)
app.register_blueprint(them_nguoi_moi_bp)

@app.route("/")
def home():
     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
