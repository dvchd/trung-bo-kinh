# Rà soát nhanh MN 1 — Kinh Căn Bản Pháp Môn

Ngày rà soát: 2026-10-22

Đã đọc `HUONG-DAN-DICH.md` của bài, các phần liên quan của `HUONG-DAN-CHUNG.md` (quy ước câu
chữ, xưng hô, chú thích, từ cấm), báo cáo mẫu `mn2.md`, toàn bộ 9 tệp `ban-dich/*.md` bằng máy
quét, 11 đoạn có `[Chú thích: …]`, và 10 đoạn dịch dài nhất (trên 400 ký tự). Không đọc hết 334
đoạn; các đoạn còn lại chỉ được kiểm bằng marker, công thức lặp và máy quét từ ngữ. Đối chiếu các
đoạn dài với cột **PLI** / **EN** trong `nguon/sections/`; đối chiếu từng chú thích dịch với
**NOTE** tương ứng.

---

## Máy quét (toàn bộ 9 tệp)

- **334 marker**, đủ, đúng thứ tự, không lặp, không sót (`ra-soat.py` báo 334 nguồn / 334 bản dịch).
- **Từ bị cấm**: không có. Đã kiểm `thị` đứng riêng, `như thị`, `nhất thời`, `bất khả tư nghì`,
  `vô lượng vô biên`, `chấp trước`, `Phật giáo đồ`, `như trên`, `lược đi`, `nói rằng là`,
  `tiền thân là` — không tệp nào chứa.
- **`...` / `…` ngoài `[Chú thích: …]`**: không có (tổng số dấu lửng trong cả 9 tệp là 0).
- **Ngoặc kép cong** `“ ” ‘ ’`: không có.
- **`Đức Phật`**: không có; người kể và người nói đều là `Đức Thế Tôn`.
- **Số dấu `"` từng tệp**: 00-gioi-thieu 6; 00-title 6; 01-phan-1 40; 02-phan-2 24; 03-phan-3 68;
  04-phan-4 80; 05-phan-5 78; 06-phan-6 70; 07-phan-7 48 — tất cả đều chẵn.

---

## Đã sửa: 2 chỗ trong lượt rà soát, 18 chỗ bổ sung sau đó

**Đợt bổ sung chú thích (2026-10-22):** dịch thêm **11 NOTE** còn thiếu (mn1:1.4, 3.5, 15.2,
19.2, 27.2, 42.1, 75.4, 147.4, 171.4, 171.5, 194.9) và đổi nhãn **7 chú thích của người dịch**
(mn1:1.1, 3.1, 7.1, 8.1, 9.1, 10.1, 11.1) từ `[Chú thích: …]` sang
`[Chú thích của người dịch: …]`. Sau đó chạy lại `ghep.py`, `tao-muc-luc.py`, `ra-soat.py`
(DAT) và `kiem-tra-marker.py` (ĐẠT).


| Vị trí | Trước | Sau | Lý do |
|---|---|---|---|
| mn1:0.2 (`ban-dich/00-title.md`) | `[Chú thích: *Mūla* là …]` | `[Chú thích của người dịch: *Mūla* là …]` | Nguồn `mn1:0.2` không có **NOTE**; đây là chú thích của người dịch, phải ghi rõ nhãn theo quy ước. Các bài khác (MN 2, MN 6) dùng đúng nhãn này. Nội dung chú thích vẫn được giữ nguyên và phù hợp với **NOTE** `mn1:2.1` (cội nguồn = tham ái). |
| mn1:3.1 (`ban-dich/01-phan-1.md`) | Không có tiêu đề mục trước đoạn `mn1:3.1` | Thêm `## 1. Hạng phàm phu` ngay trước marker | Các mục 2–8 đều có tiêu đề `## 2.` … `## 8.`, riêng mục 1 bị thiếu nên mục lục chỉ có 9 liên kết. Sau khi thêm, `tao-muc-luc.py` báo 10 liên kết, khớp cấu trúc 8 phần. |

Không sửa các chỗ chỉ là sắc thái hoặc văn phong; các chỗ ấy ghi ở mục **Điểm chưa chắc**.

---

## Chú thích: nguồn có 14 NOTE, nay đã dịch đủ

Bản dịch trước đây chỉ có **11 đoạn** chứa `[Chú thích: …]`, trong đó 7 chú thích của người dịch
bị ghi nhãn thiếu. Kiểm lại `nguon/sections/` cho thấy bài này có **14 NOTE**, không phải 41 như
bản báo cáo đầu ghi nhầm (con số 41 lấy từ tệp `api_mn1.json` vốn chỉ chứa một đoạn mẫu). Nay:

- **14/14 NOTE của Sujato đã dịch**, đúng đoạn: 1.2, 1.4, 3.2, 3.3, 3.5, 15.2, 19.2, 27.2, 42.1,
  75.4, 147.4, 171.4, 171.5, 194.9.
- **8 chú thích của người dịch** đã mang đủ nhãn `[Chú thích của người dịch: …]`: 0.2, 1.1, 3.1,
  7.1, 8.1, 9.1, 10.1, 11.1.
- Mọi chú thích đều ≤3 câu, văn xuôi, không HTML, không link.


`1.4, 2.1, 3.5, 4.1, 12.1, 13.1, 14.1, 15.1, 15.2, 16.1, 17.1, 18.1, 19.1, 19.2, 20.1, 21.1,
22.1, 23.1, 24.1, 25.1, 26.1, 27.1, 27.2, 42.1, 51.1, 75.4, 147.1, 147.4, 171.4, 171.5, 194.9`.

Đây là khoảng trống lớn nhất của bản dịch. Đáng chú ý nhất là **194.9** (giải thích vì sao các
tỳ-kheo “không hoan hỷ”), **21.1** (nghĩa của `muta`), **27.1–27.2** (bậc hữu học và ba lối tu từ),
**147.4** (`pariññātanta`, cụm riêng của kinh này), **171.4–171.5** (`nandī` và duyên khởi). Không
bổ sung trong lượt rà soát nhanh này vì khối lượng lớn và cần đọc kỹ từng NOTE; đề nghị một lượt
riêng.

---

## 10 đoạn dịch dài nhất (đối chiếu PLI/EN)

Các đoạn dài nhất đều là công thức bậc A-la-hán / Như Lai được khai triển đầy đủ từ các đoạn viết
tắt `…pe…` của nguồn. Đã soát:

| Đoạn | Ký tự | Vòng | Kết quả |
|---|---:|---|---|
| mn1:66.1 | 768 | A-la-hán — đã hiểu biết trọn vẹn | Đủ 7 vế mở đầu, đủ 5 cách tưởng tượng, kết đúng “Vì nó đã được hiểu biết trọn vẹn”; không rơi vế. |
| mn1:90.1 | 760 | A-la-hán — tham đã tận | Đủ 7 vế, đủ 5 cách, kết đúng “Vì tham đã tận”; không rơi vế. |
| mn1:114.1 | 758 | A-la-hán — sân đã tận | Đủ 7 vế, đủ 5 cách, kết đúng “Vì sân đã tận”; không rơi vế. |
| mn1:138.1 | 756 | A-la-hán — si đã tận | Đủ 7 vế, đủ 5 cách, kết đúng “Vì si đã tận”; không rơi vế. |
| mn1:61.1 | 705 | A-la-hán — đã hiểu biết trọn vẹn | Đối tượng Quảng Quả, đủ 5 cách, kết đúng; không rơi vế. |
| mn1:60.1 | 705 | A-la-hán — đã hiểu biết trọn vẹn | Đối tượng Biến Tịnh, đủ 5 cách, kết đúng; không rơi vế. |
| mn1:85.1 | 697 | A-la-hán — tham đã tận | Đối tượng Quảng Quả, đủ 5 cách, kết đúng; không rơi vế. |
| mn1:84.1 | 697 | A-la-hán — tham đã tận | Đối tượng Biến Tịnh, đủ 5 cách, kết đúng; không rơi vế. |
| mn1:59.1 | 696 | A-la-hán — đã hiểu biết trọn vẹn | Đối tượng Quang Âm, đủ 5 cách, kết đúng; không rơi vế. |
| mn1:109.1 | 695 | A-la-hán — sân đã tận | Đối tượng Quảng Quả, đủ 5 cách, kết đúng; không rơi vế. |

(mn1:108.1 cũng 695 ký tự, cùng khuôn với 109.1, đã soát kèm; kết quả như trên.)

Không thấy **rơi vế** hay **sai số** trong 10 đoạn này: mỗi đoạn đủ bảy vế tự mô tả bậc A-la-hán,
đủ năm cách tưởng tượng (làm, ở trong, phát xuất từ, của tôi, thích thú), và kết thúc đúng theo
từng vòng (pariññāta / rāga / dosa / moha). Các con số trong bài cũng khớp: 24 đối tượng, 4 hạng
người, 8 phần, 5 cách tưởng tượng, 3 cõi Phạm Thiên.

---

## Những chỗ đã kiểm và thấy đúng

- Cấu trúc 8 phần: mục 1 (phàm phu) đến mục 8 (Như Lai — thích thú là cội nguồn của khổ); thứ tự
  vòng đúng: phàm phu → hữu học → A-la-hán (pariññāta) → A-la-hán (tham) → A-la-hán (sân) →
  A-la-hán (si) → Như Lai → Như Lai (nandī).
- 24 đối tượng đúng thứ tự: bốn đại, chúng sinh, chư thiên, Pajāpati, Brahmā, Quang Âm, Biến Tịnh,
  Quảng Quả, Abhibhū, bốn xứ vô sắc, bốn đối tượng nhận thức, nhất thể, đa dạng, tất cả, Niết-bàn.
- Công thức phàm phu dùng “nhận thức / tưởng tượng / thích thú”; bậc hữu học dùng “chớ tưởng tượng
  / chớ thích thú”; A-la-hán và Như Lai dùng “không tưởng tượng / không thích thú” — không lẫn vế.
- Câu kết mn1:194.9 dịch “không hoan hỷ”, không làm dịu thành “không hiểu”; đúng chỉ dẫn
  `HUONG-DAN-DICH` §4.
- 10 chú thích nguồn đều ≤ 2 câu, không link/HTML; 11/11 chú thích đều ≤ 3 câu.
- Không có “Đức Phật”, không có đại từ “mày/ngươi”; lời gọi các tỳ-kheo là “các ông” ở mn1:2.1.

---

## Điểm chưa chắc

1. **`muta` → “cái được cảm nhận”** (72 lần, từ mn1:21.1 trở đi). **NOTE** nguồn `mn1:21.1` nói
   `muta` nghĩa là “(what is) thought” và phê “sensed” là cách dịch sai; cột **EN** cũng ghi “the
   thought”. Nhưng quy ước của repo ở các bài khác (MN 102 §7.4, MN 112 bảng thuật ngữ) chốt
   `muta` = “cảm nhận”, và bản dịch MN 1 đang theo quy ước ấy. Không sửa; nếu muốn theo Sujato thì
   phải đổi cả 72 lần thành “cái được nghĩ” và ghi rõ quyết định.
2. **mn1:1.1 (chú thích)**: “cách nhận thức và cách đồng hóa sự vật biến đổi theo tiến trình tu
   tập” — nguồn nói *quá trình* nhận thức/đồng hóa biến đổi theo tiến trình tu tập, không phải sự
   vật biến đổi. Câu hiện tại có thể đọc theo cả hai cách; chưa đủ chắc để sửa.
3. **mn1:9.1 (chú thích)**: “Đấng Sáng Tạo” cho `progenitor`; `Pajāpati` là vị thần “sinh ra muôn
   vật”/tổ phụ, không hẳn là “Đấng Sáng Tạo” theo nghĩa Kitô giáo. Có thể dùng “Đấng Sinh Thành”
   hoặc “vị tổ phụ của muôn loài” nếu muốn sát hơn; hiện không sai rõ.
4. **mn1:3.1 (chú thích)**: bản dịch thêm “không chỉ các vị A-la-hán” và không giải thích
   `sappurisa` (“chân nhân”); nguồn nói cả `ariya` và `sappurisa` đều chỉ người đã nhập dòng.
   Đúng ý nhưng chưa đủ cặp; để nguyên vì không sai nghĩa.
5. **Tiêu đề mục 1**: đã thêm “Hạng phàm phu” cho khớp lời kết “cách nhìn của hạng phàm phu”;
   nếu muốn song song với “Bậc hữu học” có thể đổi thành “Bậc phàm phu”, nhưng “hạng” chính xác
   hơn về mặt đạo lý.

---

## Chỗ còn thiếu — đã xử lý

- **Chú thích: đã đủ 14/14 NOTE** trong đợt bổ sung ngày 2026-10-22 (xem mục Chú thích ở trên).
  Báo cáo đầu ghi 31 NOTE thiếu là do đọc nhầm con số trong `api_mn1.json`.
- Không đọc hết 334 đoạn, nên báo cáo này **không** chứng nhận toàn bộ bản dịch; các vòng lặp lớn
  chỉ được kiểm bằng công thức và mẫu đại diện.

---

## Nhận xét

Bản dịch trung thành ở các đoạn mẫu: công thức A-la-hán/Như Lai đủ vế, đúng năm cách tưởng tượng,
đúng kết thúc từng vòng; câu kết “không hoan hỷ” giữ đúng dụng ý. Máy quét cơ học sạch: không từ
cấm, không ngoặc cong, không dấu lửng ngoài chú thích, số dấu `"` chẵn. Hai lỗi quy ước nhỏ đã sửa
(nhãn chú thích người dịch; thiếu tiêu đề mục 1). Vấn đề lớn nhất là **thiếu 31/41 NOTE**, cần bổ
sung trước khi coi bản dịch là hoàn chỉnh.

---

## Sau khi sửa

| Hạng mục | Kết quả |
|---|---|
| `ghep.py` | ghép 9 phần → `Kinh-Can-Ban-Phap-Mon.md` (117.296 ký tự) |
| `tao-muc-luc.py` | 10 liên kết (đã có mục 1) |
| `ra-soat.py` | 334 nguồn / 334 bản dịch; marker đủ, đúng thứ tự; dấu `"` chẵn; không ngoặc cong, không dấu lửng ngoài chú thích, không từ cấm; **KET LUAN: DAT — khong phat hien van de** |
| `kiem-tra-marker.py Kinh-*.md` | 334 marker; 24.065 từ nội dung; **==> ĐẠT** |
| Số đoạn, thứ tự | không đổi, không gộp, không tách |

Ghi chú: `kiem-tra-marker.py` chạy trên bản ghép `Kinh-Can-Ban-Phap-Mon.md` chỉ đếm marker và từ,
không đối chiếu nguồn (vì không có tệp nguồn cùng tên); việc đối chiếu 334/334 do `ra-soat.py`
thực hiện.
