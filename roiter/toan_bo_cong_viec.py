from utils.google_sheets import read_sheet
from datetime import datetime

SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

def toan_bo_cong_viec():
    data = read_sheet(SHEET_ID, "Sheet1!A2:F")
    ket_qua = []

    for row in data:
        if len(row) < 3:
            continue
        noi_dung = row[1]
        han = row[2]
        try:
            han_date = datetime.strptime(han, "%H:%M - %d/%m/%Y")
            ket_qua.append((han_date, f"Tên công việc: {noi_dung} ({han})"))
        except:
            continue

    ket_qua.sort()
    if ket_qua:
        print("TOÀN BỘ CÔNG VIỆC")
        for i, (_, dong) in enumerate(ket_qua, 1):
            print(f"{i}. {dong}")
    else:
        print("Không có công việc nào trong danh sách.")
