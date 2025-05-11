from utils.google_sheets import read_sheet, append_to_sheet
from utils.time_helper import get_current_time_str
from datetime import datetime

# ID Google Sheets
CONG_VIEC_SHEET_ID = "1KfVDpk6mXT3kisWTZDUMjtlH9xIj5elG"      # Công việc
DANH_SACH_SHEET_ID = "17NAAz052lT0wHPT2A8fU_qWOzMZxNV_C"       # Danh sách người

def lap_cong_viec():
    print("=== LẬP CÔNG VIỆC MỚI ===")

    # a. ngay_setup (tự động)
    ngay_setup = get_current_time_str()

    # b. noi_dung
    noi_dung = input("Nhập nội dung công việc: ")

    # c. han_hoan_thanh
    han_str = input("Nhập hạn hoàn thành (định dạng: HH:MM - dd/mm/yyyy): ")

    # d. nguoi_thuc_hien
    ds = read_sheet(DANH_SACH_SHEET_ID, "Sheet1!A2:A")
    ten_list = [row[0] for row in ds if row]
    print("Chọn người thực hiện từ danh sách:")
    for i, ten in enumerate(ten_list, 1):
        print(f"{i}. {ten}")
    print(f"{len(ten_list)+1}. Thêm người mới")

    chon = int(input("Nhập lựa chọn: "))
    if 1 <= chon <= len(ten_list):
        nguoi_thuc_hien = ten_list[chon - 1]
    else:
        nguoi_thuc_hien = input("Nhập tên người mới: ")
        append_to_sheet(DANH_SACH_SHEET_ID, "Sheet1!A2", [[nguoi_thuc_hien]])
        print("✅ Đã thêm người mới vào danh sách.")

    # e. loai_viec
    loai_viec = input("Nhập loại việc (ví dụ: phong thủy, cúng lễ...): ")

    # f. ghi_chu
    ghi_chu = input("Ghi chú (hoặc để trống): ")

    # Ghi vào Google Sheet
    row = [[ngay_setup, noi_dung, han_str, nguoi_thuc_hien, loai_viec, ghi_chu]]
    append_to_sheet(CONG_VIEC_SHEET_ID, "Sheet1!A2", row)

    print("✅ Đã ghi công việc mới thành công.")
