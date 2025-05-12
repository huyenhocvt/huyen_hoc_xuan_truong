import os
from flask import Flask
from roiter.lap_cong_viec import *
from roiter.cong_viec_gap import *
from roiter.cong_viec_ngay_mai import *
from roiter.toan_bo_cong_viec import *

app = Flask(__name__)

# Nếu cần route mặc định để kiểm tra server
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
