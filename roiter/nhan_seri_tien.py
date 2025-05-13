from flask import Blueprint, render_template, request
import pytesseract
from PIL import Image
import base64
import io
import os

nhan_seri_bp = Blueprint('nhan_seri', __name__)

@nhan_seri_bp.route('/nhan-seri-tien', methods=['GET'])
def nhan_seri_tien():
    return render_template('nhan_seri_tien.html', seri_result='')

@nhan_seri_bp.route('/process-seri-tien', methods=['POST'])
def process_seri_tien():
    seri_result = ''
    try:
        image_data = request.form.get('image_data', '')
        file = request.files.get('file_upload')

        if file and file.filename != '':
            img = Image.open(file.stream)
            seri_result = pytesseract.image_to_string(img)
            img.save('static/images/seri_sample.jpg')

        elif image_data.startswith('data:image'):
            header, encoded = image_data.split(',', 1)
            img_bytes = base64.b64decode(encoded)
            img = Image.open(io.BytesIO(img_bytes))
            seri_result = pytesseract.image_to_string(img)
            img.save('static/images/seri_sample.jpg')

        else:
            seri_result = 'Không tìm thấy ảnh hợp lệ.'

    except Exception as e:
        seri_result = f'Lỗi xử lý ảnh: {str(e)}'

    return render_template('nhan_seri_tien.html', seri_result=seri_result.strip())