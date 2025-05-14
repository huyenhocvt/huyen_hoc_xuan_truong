from flask import Flask
from roiter.nhan_seri_tien_easy import nhan_seri_easy_bp

app = Flask(__name__)
app.secret_key = "seri_tien_secret"

# Đăng ký blueprint mới (easyocr)
app.register_blueprint(nhan_seri_easy_bp)

@app.route("/")
def index():
    return '''
    <h1>Hệ thống Huyền Học Xuân Trường</h1>
    <p><a href="/ocr-seri">🔍 Nhận dạng seri tiền (EasyOCR)</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True)