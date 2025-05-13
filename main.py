
from flask import Flask, send_from_directory
from roiter.lap_cong_viec import lap_cong_viec_bp

app = Flask(__name__)
app.register_blueprint(lap_cong_viec_bp)

@app.route("/tai-cong-viec")
def tai_cong_viec():
    return send_from_directory("data", "cong_viec.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run()
