from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
from openai import OpenAI
from PIL import Image
import pytesseract

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        try:
            toa_do, ten_nguoi_dung = [x.strip() for x in dulieu.split(',', 1)]
            return f"Sẽ xử lý tọa độ: {toa_do}, người dùng: {ten_nguoi_dung}"
        except Exception as e:
            return f"Lỗi xử lý: {e}"
    return render_template('do_nha_input.html')

@app.route('/tra-loi-khach', methods=['GET', 'POST'])
def tra_loi_khach():
    response_text = ""
    if request.method == "POST":
        text_input = request.form.get("text_input", "")
        image = request.files.get("image")

        if image:
            img = Image.open(image.stream)
            text_input = pytesseract.image_to_string(img)

        if text_input.strip():
            prompt = f"Khách hàng gửi nội dung sau:\n{text_input.strip()}\n\nHãy đưa ra 3 phương án trả lời phù hợp, lịch sự và hỗ trợ tốt."
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=600
                )
                response_text = response.choices[0].message.content.strip()
            except Exception as e:
                response_text = f"Lỗi GPT: {e}"

    output_list = [s.strip() for s in response_text.split("\n") if s.strip()]
    return render_template("tra_loi_khach.html", output=output_list)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)