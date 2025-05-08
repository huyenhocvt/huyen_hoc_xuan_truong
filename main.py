from flask import Flask, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-time')
def get_time():
    now = datetime.now()
    return jsonify({'time': now.strftime("Bây giờ là %Hh%M ngày %d/%m/%Y")})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Cổng mặc định cho Render
    app.run(host="0.0.0.0", port=port)