from flask import Blueprint, render_template, request, redirect, url_for, session
import easyocr
from PIL import Image
import base64
import io
import re

nhan_seri_easy_bp = Blueprint('nhan_seri_easy', __name__)
reader = easyocr.Reader(['en'])

@nhan_seri_easy_bp.route('/ocr-seri', methods=['GET', 'POST'])
def ocr_seri():
    if request.method == 'POST':
        image_data = request.form.get('image_data', '')
        file = request.files.get('file_upload')
        seri_result = ''

        try:
            if file and file.filename != '':
                img = Image.open(file.stream).convert('L')
                img.save('static/images/seri_sample.jpg')
            elif image_data.startswith('data:image'):
                _, encoded = image_data.split(',', 1)
                img_bytes = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(img_bytes)).convert('L')
                img.save('static/images/seri_sample.jpg')
            else:
                session['seri_result'] = 'Không tìm thấy ảnh hợp lệ.'
                return redirect(url_for('nhan_seri_easy.ket_qua_ocr'))

            img = img.resize((img.width * 2, img.height * 2))
            results = reader.readtext('static/images/seri_sample.jpg', detail=0)

            seri_parts = []
            for r in results:
                cleaned = re.sub(r'[^A-Z0-9]', '', r.upper())
                if len(cleaned) >= 5:
                    seri_parts.append(cleaned)

            seri_result = ' '.join(seri_parts) if seri_parts else 'Không nhận dạng được số seri.'

        except Exception as e:
            seri_result = f'Lỗi xử lý ảnh: {str(e)}'

        session['seri_result'] = seri_result
        return redirect(url_for('nhan_seri_easy.ket_qua_ocr'))

    return render_template('ocr_seri.html')


@nhan_seri_easy_bp.route('/ket-qua-ocr')
def ket_qua_ocr():
    result = session.get('seri_result', 'Không có dữ liệu.')
    return render_template('ket_qua_ocr.html', seri_result=result)