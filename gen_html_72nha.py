
import pandas as pd
import os

# Đường dẫn đến file Excel và thư mục xuất
excel_path = "data/72_nha.xlsx"
output_dir = "static/nha_html"
index_output = "templates/72_nha/index_72_nha_day_du.html"

# Đọc dữ liệu từ Excel
df = pd.read_excel(excel_path)

# Tạo thư mục nếu chưa có
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.dirname(index_output), exist_ok=True)

# Mẫu HTML cho từng nhà
html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Nhà số {so_nha} – {mo_ta}</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #FAF3DD; }}
        h1 {{ color: #004488; }}
        .content {{ border: 1px solid #ccc; padding: 15px; background: #fff; }}
    </style>
</head>
<body>
    <h1>Nhà số {so_nha} – {mo_ta}</h1>
    <div class="content">
        {noi_dung}
    </div>
</body>
</html>"""

# Danh sách liên kết để tạo index
link_blocks = []

# Tạo file HTML cho từng nhà
for i, row in df.iterrows():
    so_nha = i + 1
    mo_ta = row['huong']
    noi_dung = f"""
    <p><strong>Hướng:</strong> {row['huong']}</p>
    <p><strong>Vận:</strong> {row.get('van', '')}</p>
    <p><strong>Ô 1:</strong> {row.get('o_1', '')}</p>
    <p><strong>Cách cục vận:</strong> {row.get('cach_cuc_van', '')}</p>
    """

    html_content = html_template.format(
        so_nha=so_nha,
        mo_ta=mo_ta,
        noi_dung=noi_dung
    )

    file_name = f"nha_{so_nha:02}.html"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    link_blocks.append(f'<a href="/static/nha_html/{file_name}">Nhà số {so_nha}: {mo_ta}</a>')

# Tạo file index HTML
index_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>72 Nhà – Danh sách tự động</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #FAF3DD; }}
        h1 {{ color: #004488; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
        .cell {{ border: 1px solid #ccc; padding: 10px; background: #fff; }}
        .cell a {{ display: block; margin: 5px 0; color: #004488; text-decoration: none; }}
    </style>
</head>
<body>
    <h1>72 Nhà – Danh sách tự động từ Excel</h1>
    <div class="grid">
        <div class="cell">
            {''.join(link_blocks)}
        </div>
    </div>
</body>
</html>"""

with open(index_output, "w", encoding="utf-8") as f:
    f.write(index_html)

print("✅ Đã tạo xong tất cả file HTML.")
