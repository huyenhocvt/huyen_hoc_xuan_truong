
from flask import Blueprint, render_template_string
from utils.time_helper import get_vietnam_time

time_checkbox_bp = Blueprint("time_checkbox", __name__, url_prefix="/chon-gio")

@time_checkbox_bp.route("/")
def chon_gio():
    gio = [f"{h:02d}:00" for h in range(6, 23)]
    current_date = get_vietnam_time().strftime("%d/%m/%Y")
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Chọn giờ thực hiện</title>
    </head>
    <body>
        <h2>Chọn giờ cho ngày {{ ngay }}</h2>
        <form method="POST">
            {% for g in gio %}
                <input type="checkbox" name="chon_gio" value="{{ g }}"> {{ g }}<br>
            {% endfor %}
            <br><button type="submit">Xác nhận</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(html, gio=gio, ngay=current_date)
