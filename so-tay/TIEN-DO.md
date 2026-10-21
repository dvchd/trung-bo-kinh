# Ghi chú tiến độ — Trung Bộ Kinh

> Cập nhật: 2026-10-21, cuối phiên dài 19:00–09:45 JST.

## Đã xong: 122/152 bài

3, 5, 6, 8, 12, 17, 18, 23, 24, 25, 29, 30, 31, 32, 33, 34, 35, 37, 40, 41, 42, 45, 46, 47,
49, 50, 53, 55, 56, 57, 58, 60, 63, 65, 66, 68, 71, 72, 74, 75, 77, 78, 79, 80, 81, 82, 83,
84, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
106, 107, 108, 109, 110, 111, 117, 119, 121, 122, 125, 129, 130, 135, 136, 137, 139, 140,
141, 142, 143, 144, 146, 147, 148, 152 (cộng 26 bài của đợt đầu: 1, 2, 4, 7, 9, 10, 13, 19,
20, 21, 22, 26, 27, 28, 36, 38, 39, 43, 44, 48, 54, 61, 62, 64, 70, 86, 118, 131).

Mỗi bài đều có: `Kinh-<Tên>.md` (bản ghép), `ban-dich/` (bản dịch theo đoạn), `00-gioi-thieu.md`,
`README.md`, `HUONG-DAN-DICH.md`; và đã qua `kiem-tra-marker.py` + `ra-soat.py`.

## Còn lại: 30 bài

11, 14, 15, 16, 51, 52, 59, 67, 69, 73, 76, 112, 113, 114, 115, 116, 120, 123, 124, 126,
127, 128, 132, 133, 134, 138, 145, 149, 150, 151.

## Bài kế tiếp (chia đợt cho phiên sau)

Đợt 1: 112, 113, 116, 120, 123, 124
Đợt 2: 126, 127, 128, 132, 133, 134
Đợt 3: 138, 145, 149, 150, 151, 11
Đợt 4: 14, 15, 16, 51, 52, 59
Đợt 5: 67, 69, 73, 76

Sau đó chạy `cong-cu/tao-muc-luc-goc.py` và `cong-cu/ra-soat-toan-bo.py`, rồi viết bài tổng kết.

## Quy trình một bài

```bash
# trong thư mục bài, sau khi viết ban-dich/*.md
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-<Tên>.md
python3 ra-soat.py
python3 tien-do.py
```

Yêu cầu: `kiem-tra-marker.py` in `ĐẠT`, `ra-soat.py` in `KẾT LUẬN: ĐẠT`,
`tien-do.py` báo không thiếu đoạn. Sau đó, ở thư mục gốc:

```bash
python3 cong-cu/tao-muc-luc-goc.py   # cập nhật 152 dòng trạng thái
python3 cong-cu/ra-soat-toan-bo.py   # quét toàn bộ
```

## Quy ước cần nhớ khi dịch

- `evaṁ me sutaṁ` → "Tôi nghe như vầy."; `ekaṁ samayaṁ` → "Một thuở nọ".
- Người kể gọi **Đức Thế Tôn** (không "Đức Phật"); Ngài gọi các tỳ-kheo là **"các ông"**.
- Không dùng "ngươi/mày"; không dùng `...` hay `…` ngoài `[Chú thích: …]`; không ngoặc kép cong.
- Mỗi đoạn nguồn = một khối, mở đầu bằng `<!-- seg: mnN:X.Y -->`, không gộp không tách.
- Đoạn Pali viết tắt `…pe…` phải viết đủ nội dung theo khuôn.
- Chú thích tối đa 3 câu, không HTML, không link.
- Danh hiệu chín phần dùng đúng một dạng trong `HUONG-DAN-CHUNG.md`.
- Tránh 10 từ cấm: như thị, nhất thời, bất khả tư nghì, vô lượng vô biên, chấp trước,
  Phật giáo đồ, như trên, lược đi, nói rằng là, tiền thân là.
- Câu hỏi ngắn dịch tự nhiên: "Katame cattāro?" → "Bốn là những gì?".

## Lịch chạy

- Phiên ngắn: 13:00–14:45 JST (thứ Hai–thứ Sáu).
- Phiên dài: 19:00 JST – 09:45 JST hôm sau (mọi ngày).
- Tránh 10:00–13:00 và 15:00–19:00 JST thứ Hai–thứ Sáu (giờ cao điểm, giá gấp đôi).
- Mục tiêu mỗi phiên: 6 bài mỗi đợt sóng, tối đa khoảng 5 đợt (30 bài) mỗi phiên dài.
