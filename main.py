
from utils.google_sheets import append_row_cong_viec

# Ghi 1 dòng test cố định
append_row_cong_viec([
    "Test 1 dòng",           # ngay_setup
    "Nội dung test",         # noi_dung
    "2025-05-14",            # han_hoan_thanh
    "Người thử",             # nguoi_thuc_hien
    "Loại thử",              # loai_viec
    "Dòng test ghi sheet"    # ghi_chu
])
