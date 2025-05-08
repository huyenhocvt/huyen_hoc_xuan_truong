from flask import Flask, render_template, request, send_file, jsonify
from datetime import datetime
import os
from xuat_so_do_nha import xu_ly_dau_vao_va_xuat_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-time')
def get_time():
    now = datetime.now()
    return jsonify({'time': now.strftime("Bây giờ là %Hh%M ngày %d/%m/%Y")})

@app.route('/do-nha', methods=['GET', 'POST'])
def do_nha():
    if request.method == 'POST':
        dulieu = request.form['dulieu']
        file_path = xu_ly_dau_vao_va_xuat_file(dulieu)
        return send_file(file_path, as_attachment=True)
    return render_template('do_nha_input.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)