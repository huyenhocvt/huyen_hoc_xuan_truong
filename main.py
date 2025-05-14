from flask import Flask, render_template
from roiter.nhan_seri_tien import nhan_seri_bp

app = Flask(__name__)
app.secret_key = "seri_tien_secret"

# Đăng ký lại route nhận dạng seri (nếu cần)
app.register_blueprint(nhan_seri_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)