from utils.google_sheets import append_row_cong_viec

if __name__ == "__main__":
    test_data = [
        "05:55 – 13/05/2025",
        "Test ghi dữ liệu",
        "20/05/2025",
        "Xuân Trường",
        "Test",
        "Dòng kiểm tra"
    ]
    success = append_row_cong_viec(test_data)
    print("✅ Ghi thành công!" if success else "❌ Ghi thất bại!")
