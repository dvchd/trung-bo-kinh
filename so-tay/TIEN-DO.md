# Ghi chú tiến độ — Trung Bộ Kinh

> Cập nhật: 2026-10-20, cuối phiên ngắn 13:00–14:45 JST.

## Đã xong: 28/152 bài

1, 2, 4, 7, 9, 10, 13, 19, 20, 21, 22, 26, 27, 28, 36, 38, 39, 43, 44, 48, 54, 61, 62,
64, 70, 86, 118, 131.

Mỗi bài đều có: `Kinh-<Tên>.md` (bản ghép), `ban-dich/` (bản dịch theo đoạn), `00-gioi-thieu.md`,
`README.md`, `HUONG-DAN-DICH.md`; và đã qua `kiem-tra-marker.py` + `ra-soat.py`.

## Bài kế tiếp (thứ tự ưu tiên cho phiên 19:00)

Đợt 1: 12, 29, 30, 35, 37, 40
Đợt 2: 41, 45, 46, 49, 50, 63
Đợt 3: 72, 75, 101, 107, 117, 119
Đợt 4: 121, 122, 125, 129, 130, 135
Đợt 5: 136, 137, 139, 140, 141, 142
Đợt 6: 143, 144, 146, 147, 148, 152

Sau đó dịch nốt các bài còn lại theo thứ tự số.

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
