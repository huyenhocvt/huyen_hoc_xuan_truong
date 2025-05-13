from flask import Blueprint, render_template, request, redirect, url_for, session
import easyocr
from PIL import Image
import base64
import io
import os

nhan_seri_bp = Blueprint('nhan_seri', __name__)
nhan_seri_bp.secret_key = 'seri_session_key'

reader = easyocr.Reader(['en'])

@nhan_seri_bp.route('/nhan-seri-tien', methods=['GET', 'POST'])
def nhan_seri_tien():
    if request.method == 'POST':
        image_data = request.form.get('image_data', '')
        file = request.files.get('file_upload')
        seri_result = ''

        try:
            if file and file.filename != '':
                img = Image.open(file.stream).convert('L')
                img.save('static/images/seri_sample.jpg')
            elif image_data.startswith('data:image'):
                header, encoded = image_data.split(',', 1)
                img_bytes = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(img_bytes)).convert('L')
                img.save('static/images/seri_sample.jpg')
            else:
                session['seri_result'] = 'Không tìm thấy ảnh hợp lệ.'
                return redirect(url_for('nhan_seri.ket_qua_seri'))

            img = img.resize((img.width * 2, img.height * 2))
            results = reader.readtext('static/images/seri_sample.jpg', detail=0)
            seri_result = ' | '.join(results) or 'Không nhận dạng được số seri.'

        except Exception as e:
            seri_result = f'Lỗi xử lý ảnh: {str(e)}'

        session['seri_result'] = seri_result
        return redirect(url_for('nhan_seri.ket_qua_seri'))

    return render_template('nhan_seri_tien.html')


@nhan_seri_bp.route('/ket-qua-seri')
def ket_qua_seri():
    result = session.get('seri_result', 'Không có dữ liệu.')
    return render_template('ket_qua_seri.html', seri_result=result)