from flask import Flask, render_template_string, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head><title>Giờ hiện tại</title></head>
    <body>
        <h2>Kiểm tra giờ hiện tại ở TP.HCM</h2>
        <button onclick="layGio()">Giờ hiện tại</button>
        <p id="gio"></p>
        <script>
            function layGio() {
                fetch("/get-time").then(res => res.json()).then(data => {
                    document.getElementById("gio").innerText = data.time;
                });
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/get-time')
def get_time():
    now = datetime.now()
    return jsonify({"time": f"Bây giờ là {now.strftime('%Hh%M')} ngày {now.strftime('%d/%m/%Y')}"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)