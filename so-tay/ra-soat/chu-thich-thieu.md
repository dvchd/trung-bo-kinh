# Rà soát 13 chỗ nghi thiếu chú thích Sujato

Ngày rà soát: 2026-10-22

Danh sách do dò tự động: đoạn có **NOTE** trong `nguon/sections/*.md` mà bản dịch không có
`[Chú thích: …]` đúng đoạn ấy. Với từng chỗ, đã đọc NOTE của đoạn, rồi đối chiếu **nội dung**
( không chỉ số đoạn) với toàn bộ `[Chú thích: …]` trong `ban-dich/` của bài, kể cả đoạn liền trước
và liền sau. Kết quả: 6 chỗ chú thích đã được dịch nhưng đặt sang đoạn khác (không sửa), 7 chỗ thật
sự thiếu nên đã dịch và chèn ngay sau đoạn.

## Bảng kết quả

| Đoạn | Bài | Trạng thái | Ghi chú |
|---|---|---|---|
| mn5:17.2 | MN 5 — Kinh Không Uế Nhiễm | đã có, đặt lệch đoạn | Nằm ở đoạn 18-20.2 (mục "giảng Pháp cho tỳ-kheo-ni"), nội dung khớp: giảng Pháp cho tỳ-kheo-ni vì động cơ thế tục thì phạm tội |
| mn13:3.4 | MN 13 — Đại Kinh Khổ Uẩn | đã có, đặt lệch đoạn | Nằm ở đoạn 3.5, cùng ý "du sĩ sáng suốt hơn nhiều người ngày nay" |
| mn24:1.2 | MN 24 — Kinh Cỗ Xe | đã chèn mới | Trúc Lâm là tu viện lớn gần Rājagaha, được vua Bimbisāra dâng cúng đầu tiên (Luật tạng Kd 1:22.16.1) |
| mn24:17.5 | MN 24 — Kinh Cỗ Xe | đã chèn mới | *satthukappa*, "sánh được với bậc Đạo sư", là cách gọi chỉ có trong kinh Pali sơ kỳ |
| mn25:10.21 | MN 25 — Kinh Mồi Nhử | đã chèn mới | Mười điểm không được tuyên bố, bảng kiểm phân loại triết gia, dẫn Bhagavatisūtra và nghĩa chữ *loka* |
| mn28:8.2 | MN 28 — Đại Kinh Dấu Chân Voi | đã có, đặt lệch đoạn | Nằm ở đoạn 8.5, cùng ý quán duyên khởi như phương pháp làm lắng cảm xúc phản ứng |
| mn28:28.5 | MN 28 — Đại Kinh Dấu Chân Voi | đã có, đặt lệch đoạn | Nằm ở đoạn 28.6, cùng ý Sāriputta gom các hệ thống trí tuệ lớn vào một bài giảng |
| mn30:2.6 | MN 30 — Tiểu Kinh Lõi Cây | đã có, đặt lệch đoạn | Nằm ở đoạn 2.7, cùng ý Đức Thế Tôn đáp y như vậy với du sĩ Subhadda (DN 16) |
| mn93:11.14 | MN 93 — Kinh Assalāyana | đã chèn mới | Lập luận tương tự cũng được nêu về thức ở đoạn 11.5 của bài kinh này |
| mn95:8.2 | MN 95 — Kinh Caṅkī | đã chèn mới | So với Trường Bộ Kinh 4, đoạn 5.2 và Trường Bộ Kinh 5, đoạn 6.2 |
| mn95:11.5 | MN 95 — Kinh Caṅkī | đã có, đặt lệch đoạn | Nằm ở đoạn 11.6, cùng ý Đức Thế Tôn hiếm khi gọi người tại gia là "tôn giả" |
| mn95:13.5 | MN 95 — Kinh Caṅkī | đã chèn mới | So với Trường Bộ Kinh 13, đoạn 12.1 |
| mn99:2.3 | MN 99 — Kinh Subha | đã chèn mới | Đoạn này cho thấy đây là lần đầu Subha gặp Đức Thế Tôn |

Tổng: 7 chèn mới, 6 đã có nhưng đặt lệch đoạn.

## Bài đã sửa (chỉ trong `ban-dich/`)

- `024-kinh-co-xe` — chèn 2 chú thích (mn24:1.2; mn24:17.5)
- `025-kinh-moi-nhu` — chèn 1 chú thích (mn25:10.21)
- `093-kinh-assalayana` — chèn 1 chú thích (mn93:11.14)
- `095-kinh-canki` — chèn 2 chú thích (mn95:8.2; mn95:13.5)
- `099-kinh-subha` — chèn 1 chú thích (mn99:2.3)

Các bài không sửa: 005 (mn5), 013 (mn13), 028 (mn28), 030 (mn30).

## Kiểm tra sau khi sửa

Mỗi bài có thay đổi đều chạy lại dây chuyền, cả 5 bài đều đạt:

| Bài | ghep.py | ra-soat.py | kiem-tra-marker.py |
|---|---|---|---|
| 024-kinh-co-xe | 5 phần, 139 marker | KET LUAN: DAT | ==> ĐẠT |
| 025-kinh-moi-nhu | 6 phần, 199 marker | KET LUAN: DAT | ==> ĐẠT |
| 093-kinh-assalayana | 7 phần, 244 marker | KET LUAN: DAT | ==> ĐẠT |
| 095-kinh-canki | 9 phần, 305 marker | KET LUAN: DAT | ==> ĐẠT |
| 099-kinh-subha | 8 phần, 270 marker | KET LUAN: DAT | ==> ĐẠT |

Mọi chú thích chèn mới đều là văn xuôi, không HTML, không link, không ngoặc kép cong, không dấu
ba chấm, tối đa 3 câu. Không commit.
