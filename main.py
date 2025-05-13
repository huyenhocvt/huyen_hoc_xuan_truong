
from flask import Flask
from roiter.lap_cong_viec import lap_cong_viec_bp

app = Flask(__name__)
app.secret_key = "congviec_secret_2025"  # để dùng session

app.register_blueprint(lap_cong_viec_bp)

@app.route("/")
def index():
    return '<h2><a href="/lap-cong-viec/">Lập công việc</a></h2>'

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
