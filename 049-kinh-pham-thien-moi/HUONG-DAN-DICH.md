# Hướng dẫn dịch — Kinh Phạm Thiên Mời (*Brahmanimantanika Sutta*, Trung Bộ Kinh MN 49)

> Chuẩn chung bắt buộc: [`../../HUONG-DAN-CHUNG.md`](../../HUONG-DAN-CHUNG.md) — quy ước câu chữ,
> xưng hô, chú thích, số hiệu đoạn, từ cấm. Tệp này **chỉ ghi những quyết định riêng của bài**:
> tên nhân vật, thuật ngữ đặc thù, những chỗ dễ dịch sai.

---

## 1. Nội dung bài này

<!-- Một đoạn 3–5 câu: bài nói về ai, việc gì, kết thúc ra sao. Người dịch tự viết sau khi đọc bản Pali. -->

## 2. Nhân vật

| Pali | Dịch trong bài | Ghi chú (lần đầu xuất hiện) |
|---|---|---|
| | | |

## 3. Thuật ngữ riêng của bài

| Pali | Dịch chuẩn | Ghi chú |
|---|---|---|
| | | |

## 4. Chỗ dễ dịch sai

<!-- Liệt kê những câu/cụm mà người dịch dễ hiểu lệch: từ đa nghĩa, câu Pali rút gọn,
     chỗ Sujato dịch thoát, chỗ bản Pali lặp lại nguyên văn. -->

## 5. Kiểm tra trước khi commit

```bash
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-Kinh-Pham-Thien-Moi.md
python3 ra-soat.py
python3 tien-do.py
```

`kiem-tra-marker.py` và `ra-soat.py` phải in `DAT`, `tien-do.py` phải báo không thiếu đoạn nào.
