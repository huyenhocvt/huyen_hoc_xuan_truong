from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd
import os

def xuat_so_do(toa_do, ten_nguoi_dung, file_out="so_do_nha.pdf"):
    # Định nghĩa đường dẫn tương đối
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, "fonts", "ARIAL.TTF")
    data_path = os.path.join(current_dir, "data", "72_nha.xlsx")

    # Đăng ký font Arial
    pdfmetrics.registerFont(TTFont("Arial", font_path))

    # Đọc file Excel
    df = pd.read_excel(data_path)

    # Kiểm tra cột 'toa_do' có tồn tại không
    if 'toa_do' not in df.columns:
        raise ValueError("Không tìm thấy cột 'toa_do' trong dữ liệu")

    # Lọc dữ liệu theo tọa độ
    data_loc = df[df['toa_do'] == toa_do]

    if data_loc.empty:
        raise ValueError(f"Không tìm thấy dữ liệu với tọa độ: {toa_do}")

    # Tạo canvas PDF
    c = canvas.Canvas(file_out, pagesize=A4)
    width, height = A4
    c.setFont("Arial", 14)
    c.drawString(50, height - 50, f"Sơ đồ nhà cho tọa độ: {toa_do}")
    c.setFont("Arial", 12)
    c.drawString(50, height - 70, f"Người dùng: {ten_nguoi_dung}")
    
    # Ghi dữ liệu từng dòng
    y = height - 100
    for index, row in data_loc.iterrows():
        for col, val in row.items():
            text = f"{col}: {val}"
            c.drawString(50, y, text)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Arial", 12)
    
    c.save()
    return f"Đã tạo file {file_out} thành công."
