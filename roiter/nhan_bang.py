from flask import Blueprint, render_template, request, redirect, url_for, session
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import pandas as pd
import io
import base64
import os

nhan_bang_bp = Blueprint('nhan_bang', __name__)
nhan_bang_bp.secret_key = 'bang_session_key'

@nhan_bang_bp.route('/nhan-bang', methods=['GET', 'POST'])
def nhan_bang():
    if request.method == 'POST':
        image_data = request.form.get('image_data', '')
        file = request.files.get('file_upload')
        result_text = ''

        try:
            if file and file.filename.endswith('.pdf'):
                images = convert_from_bytes(file.read(), first_page=1, last_page=1)
                img = images[0].convert('L')
                img.save('static/images/bang_sample.jpg')
            elif file and file.filename != '':
                img = Image.open(file.stream).convert('L')
                img.save('static/images/bang_sample.jpg')
            elif image_data.startswith('data:image'):
                header, encoded = image_data.split(',', 1)
                img_bytes = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(img_bytes)).convert('L')
                img.save('static/images/bang_sample.jpg')
            else:
                session['bang_result'] = 'Không tìm thấy ảnh hoặc PDF hợp lệ.'
                return redirect(url_for('nhan_bang.ket_qua_bang'))

            img = img.resize((img.width * 2, img.height * 2))
            raw_text = pytesseract.image_to_string(img)

            df = pd.DataFrame([[line] for line in raw_text.splitlines() if line.strip()])
            output_path = 'static/outputs/nhan_bang.xlsx'
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            df.to_excel(output_path, index=False, header=False)

            session['bang_result'] = 'Đã xuất bảng thành công.'
        except Exception as e:
            session['bang_result'] = f'Lỗi xử lý: {str(e)}'

        return redirect(url_for('nhan_bang.ket_qua_bang'))

    return render_template('nhan_bang.html')

@nhan_bang_bp.route('/ket-qua-bang')
def ket_qua_bang():
    result = session.get('bang_result', 'Không có dữ liệu.')
    return render_template('ket_qua_bang.html', bang_result=result)