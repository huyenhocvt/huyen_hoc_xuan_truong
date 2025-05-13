from flask import Blueprint, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import base64
import io

nhan_seri_bp = Blueprint('nhan_seri', __name__)

@nhan_seri_bp.route('/nhan-seri-tien', methods=['GET'])
def nhan_seri_tien():
    return render_template('nhan_seri_tien.html')

@nhan_seri_bp.route('/process-seri-tien', methods=['POST'])
def process_seri_tien():
    seri_result = ''
    image_data = request.form.get('image_data', '')

    # Ưu tiên ảnh dán vào textarea (base64)
    if 'file_upload' in request.files and request.files['file_upload'].filename != '':
        file = request.files['file_upload']
        img = Image.open(file.stream)
        seri_result = pytesseract.image_to_string(img)
        img.save('static/images/seri_sample.jpg')  # ghi đè ảnh mẫu
    elif image_data.startswith('data:image'):
        # Trích base64
        header, encoded = image_data.split(',', 1)
        img_bytes = base64.b64decode(encoded)
        img = Image.open(io.BytesIO(img_bytes))
        seri_result = pytesseract.image_to_string(img)
        img.save('static/images/seri_sample.jpg')

    return render_template('nhan_seri_tien.html', seri_result=seri_result.strip())