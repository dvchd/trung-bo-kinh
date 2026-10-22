# Ghi chú tiến độ — Trung Bộ Kinh

> Cập nhật: 2026-10-22. Dịch xong 152/152 bài; đợt đọc lại văn phong đã chạy được 22 bài.

## Đã xong: 152/152 bài — TRỌN BỘ TRUNG BỘ KINH

Mọi bài 1–152 đều có `Kinh-<Tên>.md`, `ban-dich/`, `00-gioi-thieu.md`, `README.md`,
`HUONG-DAN-DICH.md`, và đã qua `kiem-tra-marker.py` + `ra-soat.py` (ĐẠT).

Tổng: 888.406 từ (không kể chú thích), 26.891 đoạn văn dịch, 27.195 neo đoạn, 905 tệp `ban-dich/`.

Ngoài bản dịch, kho có thêm:

- `so-tay/GIOI-THIEU-BO-KINH.md` — giới thiệu bộ kinh, cấu trúc, đường đọc.
- `so-tay/BANG-THUAT-NGU.md` — bảng thuật ngữ Pali – Việt.
- Bốn script kiểm tra dùng chung trong `cong-cu/`.

## Đợt đọc lại văn phong: 22/152 bài

Đọc trọn từng bài, đối chiếu PLI và bản Anh ở những đoạn dài và đoạn có chú thích, sửa lỗi rồi
chạy lại toàn bộ kiểm tra. Đã làm:

| Bài | Chỗ sửa | Ghi chú |
|---|---|---|
| MN 44 | 6 | thiếu xưng hô so với PLI, tên kinh viết thường trong chú thích |
| MN 57 | 5 | câu chữ và quy ước |
| MN 69 | 8 | 18.4 thiếu nghĩa "vượt khỏi sắc, thuộc cõi vô sắc" |
| MN 112 | 10 | công thức "Lành thay" bị dịch thành lời tỳ-kheo |
| MN 115 | 10 | lặp động từ, thiếu trợ từ, câu giới thiệu viết theo trí nhớ |
| MN 116 | 10 | tên núi và tính từ trong kệ, giới tính đại từ |
| MN 120 | 9 | câu mở bị nén, tám câu thiếu tân ngữ |
| MN 123 | 11 | trật tự từ trong câu phủ định, một vế rơi khi khai triển `…pe…` |
| MN 124 | 5 | sai chủ ngữ ở 1.2, rơi tiểu từ `pana` |
| MN 128 | 6 | ngoặc kép thừa, nghĩa của `dhovitvā`, chú thích nói sai vị trí |
| MN 131 | 1 | dòng ghi kết thúc bài kinh |
| MN 132 | 2 | lặp danh hiệu ở chỗ quy ước dùng "Ngài" |
| MN 96 | 9 | ngoặc kép lệch, hai chú thích dẫn chữ không khớp, một công thức lặp dịch lệch |
| MN 134 | 2 | dấu câu, nhất quán địa danh |
| MN 137 | 18 | bớt hô cách trong câu trích, câu văn hỏng vì dịch sát |
| MN 138 | 16 | bớt hô cách, bốn câu giới thiệu hỏng |
| MN 144 | 3 | chữ "là" thừa trong `mittakulāni`, câu giới thiệu tối nghĩa |
| MN 145 | 2 | nhịp lặp ba lần ở 7.4, chữ thừa ở 6.2 |
| MN 149 | 4 | diễn đạt |
| MN 150 | 5 | dấu chấm phẩy cắt sai mệnh đề |
| MN 151 | 10 | trật tự từ ở công thức quán sáu xứ |
| MN 152 | 4 | hô cách ở 9.10, chữ "rơi" thêm vào ở 6.9 |

Tổng 156 chỗ. Báo cáo chi tiết từng bài nằm trong `so-tay/ra-soat/`, gồm cả những chỗ đã cân
nhắc mà **không** sửa (khoảng 110 điểm), để lần sau khỏi phải xét lại từ đầu.

## Việc còn lại (tùy chọn)

1. Đọc lại 130 bài chưa rà từng dòng. Nếu làm tiếp, mỗi đợt 6 bài, mỗi bài một người đọc; quy
   trình như trên.
2. Quyết khoảng 100 điểm "chưa chắc" đã ghi trong `so-tay/ra-soat/`. Phần lớn là chỗ phải chọn
   giữa hai cách hiểu Pali, không phải lỗi rõ ràng.
3. Bổ sung sổ tay chú giải cho các bài lớn nếu muốn (như bên Trường Bộ Kinh).
4. Chạy `python3 cong-cu/ra-soat-toan-bo.py` và `ra-soat-van-phong.py` sau mỗi lần sửa.

## Bốn lớp kiểm tra tự động

| Script | Quét | Bắt được |
|---|---|---|
| `ra-soat-toan-bo.py` | 753 tệp | đủ neo đoạn và đúng thứ tự, ngoặc kép cân, từ cấm, công thức lặp |
| `ra-soat-van-phong.py` | 1057 tệp | tiếng Anh sót, ký tự lạ, lỗi khoảng trắng, danh hiệu chín phần lệch dạng |
| `ra-soat-cong-thuc.py` | toàn kho | báo cáo đoạn Pali nào đang được dịch khác nhau giữa các bài |
| `dong-nhat-cong-thuc.py` | toàn kho | ép các đoạn ấy về một cách dịch chuẩn |

Ba script đầu chỉ đọc và báo; script cuối ghi. Chạy script cuối xong phải ghép lại các bài bị
đụng (`ghep.py` + `tao-muc-luc.py`) rồi quét lại.

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
