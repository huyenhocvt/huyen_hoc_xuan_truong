
from flask import redirect, Flask, render_template, render_template_string
import pandas as pd
import os

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
    df = pd.read_excel("data/72_nha.xlsx")
    links = []
    for i, row in df.iterrows():
        so_nha = i + 1
        mo_ta = row['huong']
        link = f'<a href="/static/nha_html/nha_{so_nha:02}.html">Nhà số {so_nha}: {mo_ta}</a>'
        links.append(link)

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>72 Nhà – Danh sách tự động</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #FAF3DD; }}
            h1 {{ color: #004488; }}
            .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
            .cell {{ border: 1px solid #ccc; padding: 10px; background: #fff; }}
            .cell a {{ display: block; margin: 5px 0; color: #004488; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>72 Nhà – Danh sách từ Excel (HTML động)</h1>
        <div class="grid">
            <div class="cell">
                {''.join(links)}
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route("/98_ma_phuong")
def index_98_ma_phuong():
    return render_template("ma_phuong/index_98_ma_phuong.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
