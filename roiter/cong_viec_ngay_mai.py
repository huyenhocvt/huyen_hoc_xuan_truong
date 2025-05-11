from utils.google_sheets import read_sheet
from utils.time_helper import get_tomorrow_date
from datetime import datetime

SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"

def cong_viec_ngay_mai():
    data = read_sheet(SHEET_ID, "Sheet1!A2:F")
    tomorrow = get_tomorrow_date()
    ket_qua = []

    for row in data:
        if len(row) < 3:
            continue
        noi_dung = row[1]
        han = row[2]
        try:
            han_date = datetime.strptime(han, "%H:%M - %d/%m/%Y").date()
            if han_date == tomorrow:
                ket_qua.append(f"Tên công việc: {noi_dung} ({han})")
        except:
            continue

    if ket_qua:
        print("CÔNG VIỆC NGÀY MAI")
        for i, dong in enumerate(ket_qua, 1):
            print(f"{i}. {dong}")
    else:
        print("✅ Ngày mai chưa có công việc.")
