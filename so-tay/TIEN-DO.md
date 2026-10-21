# Ghi chú tiến độ — Trung Bộ Kinh

> Cập nhật: 2026-10-21, cuối phiên ngắn 13:00–14:45 JST.

## Đã xong: 147/152 bài

Tất cả các bài từ 1 đến 152, trừ 69 và 73. Mỗi bài có `Kinh-<Tên>.md`, `ban-dich/`,
`00-gioi-thieu.md`, `README.md`, `HUONG-DAN-DICH.md`, đã qua `kiem-tra-marker.py` và `ra-soat.py`.

## Còn lại: 2 bài

69 (Gulissāni), 73 (Đại kinh Vacchagotta).

## Việc cuối cùng sau khi dịch xong 2 bài

1. `python3 cong-cu/tao-muc-luc-goc.py` — cập nhật bảng 152 dòng và dòng trạng thái README.
2. `python3 cong-cu/ra-soat-toan-bo.py` — phải in `TONG VAN DE: 0`.
3. Đọc lại README gốc, thêm mục tổng kết (số bài, số từ, cách dùng repo).
4. Commit cuối và push.

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
