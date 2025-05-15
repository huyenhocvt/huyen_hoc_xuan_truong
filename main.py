from flask import redirect, Flask, render_template
from roiter.do_nha import do_nha_bp
from roiter.lap_cong_viec import lap_cong_viec_bp
from roiter.them_nguoi_moi import them_nguoi_moi_bp
from roiter.time_checkbox import time_checkbox_bp

app = Flask(__name__)
app.secret_key = "huyen_hoc_secret"

# Đăng ký các blueprint
app.register_blueprint(do_nha_bp)
app.register_blueprint(lap_cong_viec_bp)
app.register_blueprint(them_nguoi_moi_bp)
app.register_blueprint(time_checkbox_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/72_nha/index_72_nha")
def index_72_nha_legacy():
    return redirect("/72_nha/day_du")

@app.route("/72_nha/day_du")
def index_72_day_du():
    return render_template("72_nha/index_72_nha_day_du.html")
@app.route("/98_ma_phuong")
def index_98_ma_phuong():
    return render_template("ma_phuong/index_98_ma_phuong.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
