
from utils.google_sheets import append_row_cong_viec

if __name__ == "__main__":
    row = [
        "15:00 – 13/05/2025",  # ngay_setup
        "Test ghi lên Sheet",  # noi_dung
        "18:00–13/05/2025",    # han_hoan_thanh
        "GPT Support",         # nguoi_thuc_hien
        "Kiểm tra",            # loai_viec
        "Dòng test"            # ghi_chu
    ]
    success = append_row_cong_viec(row)
    print("✅ Ghi thành công!" if success else "❌ Ghi thất bại!")
