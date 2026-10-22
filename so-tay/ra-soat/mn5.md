# Rà soát MN 5 — Kinh Không Uế Nhiễm (*Anaṅgaṇa Sutta*)

Rà soát có giới hạn thời gian (≈15 phút), theo thứ tự `HUONG-DAN-CHUNG.md` → `HUONG-DAN-DICH.md`
→ quét tự động → đối chiếu PLI/EN ở các đoạn nghi ngờ. Không đọc trọn từng chữ, nhưng đã đọc
hết bản dịch (203 đoạn / 7 tệp) một lượt và mở nguồn cho ~45 đoạn có rủi ro.

---

## Đã kiểm gì

1. **Quét tự động toàn bộ `ban-dich/*.md`** (script tách theo `<!-- seg: -->`):
   - đoạn dịch > 400 ký tự ngoài chú thích: **5 chỗ** (29.1, 29.11, 32.1, 32.2, 33.2) — cả 5
     là danh sách Pali dài, đã đối chiếu và đúng, không cần cắt;
   - `[Chú thích: …]`: 21 NOTE trong `nguon/sections/` ↔ 20 chú thích trong bản dịch → **thiếu 1**
     (mn5:1.2), xem bảng dưới; một NOTE của 17.2 đã được đặt sau 18-20.2 (chỗ nội dung ấy thực
     sự liên quan: giảng Pháp cho tỳ-kheo-ni) — chấp nhận được;
   - từ cấm (`như thị`, `nhất thời`, `bất khả tư nghì`, `vô lượng vô biên`, `chấp trước`,
     `Phật giáo đồ`, `như trên`, `lược đi`, `nói rằng là`, `tiền thân là`): **0**;
   - `...`, `…` ngoài khối chú thích: **0**; ngoặc kép cong `“ ” ‘ ’`: **0**; `"Đức Phật"`: **0**;
     `ngươi/mày/các ông/v.v.`: **0**; số dấu `"` chẵn ở cả 7 tệp.
2. **Đối chiếu nghĩa với PLI/EN** ở các nhóm dễ sai:
   - bốn lần ví chậu đồng (4.3–4.8, 5.3–5.8, 6.3–6.8, 7.3–7.8) và hai ví chậu đồng ở 29.4–29.10 /
     30.4–30.10: đủ vế, đúng chiều (dơ → dơ thêm; sạch → dơ đi; sạch → sạch thêm), đúng ba mục
     `amanāpatā / pāṭikulyatā / jegucchatā` và ba mục đối xứng ở 30.9;
   - công thức năm vế `so sarāgo sadoso samoho sāṅgaṇo saṅkiliṭṭhacitto kālaṁ karissati` (4.2,
     4.8, 6.2, 6.8) và bản đảo (5.2, 5.8, 7.2, 7.8): giữ đủ 5 vế, không rút theo EN;
   - 12 nhóm ước muốn (10–17, 18-20, 21, 22-24, 25, 26-27): đúng chủ thể, đúng thứ tự
     y phục → bữa ăn → chỗ ở → thuốc men; các `…pe…` đã khai triển đủ ba đối tượng
     (tỳ-kheo-ni / nam cư sĩ / nữ cư sĩ);
   - các đoạn Sujato gộp (10.4, 11.4, 12.4, 13.4, 14.4, 15.4, 16.4, 17.3, 17.4, 18-20.2–4,
     21.3, 21.4, 22-24.2–4, 25.3, 25.4, 26-27.2–4): đều dịch thẳng từ PLI, không theo câu rút
     của EN (17.2 chỉ "các tỳ-kheo", đúng như `HUONG-DAN-DICH` dặn);
   - thuật ngữ riêng của bài: `aṅgaṇa` "vết nhơ", `pāṭikaṅkhaṁ` "có thể chắc rằng",
     `icchāvacara` "phạm vi ước muốn", `paṭipuggala` "người đồng hạng", `subhanimitta` "tướng
     đẹp", `eḷamūgā` "đần độn", `satthā` "bậc Đạo sư", `nāga` "long tượng" — dùng đúng, thống
     nhất toàn bài;
   - 31.5–31.12 (thợ bào vành bánh xe), 33.1 (tràng hoa `uppala / vassika / atimuttaka` →
     sen / lài / atimuttaka), 33.3–33.4 (lời tán thán qua lại): đúng nghĩa, không lệch chi tiết.
3. **Kiểm tra máy** sau khi sửa: `ghep.py`, `tao-muc-luc.py`, `ra-soat.py` → **KET LUAN: DAT**;
   `kiem-tra-marker.py Kinh-Khong-Ue-Nhiem.md` → 203 marker, **==> ĐẠT**.

---

## Đã sửa: 2 chỗ

| Đoạn | Trước | Sau | Lý do |
|---|---|---|---|
| mn5:1.2 | (không có chú thích) | thêm `[Chú thích: Đức Thế Tôn không xuất hiện trong bài kinh này, nhưng Ngài vẫn được nhắc đến để tỏ lòng kính trọng, cho thấy những sự việc kể ở đây diễn ra khi Ngài còn tại thế.]` | `nguon/sections/01-phan-1.md` có **NOTE** cho đúng đoạn 1.2 nhưng bản dịch bỏ sót (21 NOTE nguồn ↔ 20 chú thích). Nội dung là của Sujato, không phải lời người dịch; người kể nên dùng "Đức Thế Tôn", không dùng "Đức Phật". |
| 00-gioi-thieu.md (dòng 13) | "mặc y **vá** từ vải rách nhặt được" | "mặc y **may** từ vải rách nhặt được" | Cùng một cụm `paṁsukūlika… lūkhacīvaradharo` mà thân bài (29.1, 29.11) dịch "mặc y may từ vải rách nhặt được"; phần giới thiệu để "y vá" là lệch thuật ngữ trong cùng một ấn bản. Không đổi nghĩa. |

Ngoài hai chỗ trên, **không sửa câu chữ nào**: các đoạn nghi ngờ còn lại khi mở PLI ra đều đúng.

---

## Những chỗ đã kiểm và thấy đúng (đáng ghi lại)

- 2.7–2.10: bốn câu "trong hai người đều (không) có vết nhơ…" đúng cấu trúc
  `imesaṁ dvinnaṁ puggalānaṁ … sataṁ` — không phải câu so sánh hai hạng người khác nhau.
- 4.1 / 5.1: `pāṭikaṅkhaṁ` dịch "có thể chắc rằng" (không phải "đáng mong đợi"), đúng như
  `HUONG-DAN-DICH` §3; vế ba động từ `chandaṁ janessati / vāyamissati / vīriyaṁ ārabhissati`
  giữ đủ.
- 6.1 vs 7.1: cặp đối xứng `subhanimittaṁ manasi karissati` / `na manasi karissati` và
  `anuddhaṁsessati` / `nānuddhaṁsessati` ("làm vấy bẩn" / "không làm vấy bẩn") — đúng chiều,
  không lẫn phủ định.
- 9.1: `Aṅgaṇaṁ aṅgaṇanti … vuccati` dịch thoát thành "người ta vẫn nói đến chữ 'vết nhơ'",
  giữ được lối chơi chữ rồi 9.2 hỏi lại "chữ ấy là tên gọi cho cái gì".
- 12.2 / 12.3: `sappaṭipuggalo … no appaṭipuggalo` không bị hiểu thành "kẻ thù"; 13.2 có thêm
  "tức Đức Thế Tôn" đúng như `HUONG-DAN-DICH` dặn cho lần đầu chữ `satthā`, và nhịp "hỏi đi hỏi
  lại" được giữ.
- 14.2 / 15.2: `purakkhatvā`, `bhattāya`, `aggāsanaṁ aggodakaṁ aggapiṇḍaṁ` dịch đúng nghĩa
  "đi đầu", "để dùng bữa", "chỗ ngồi / nước uống / miếng ăn tốt nhất", không thành hạng mục lễ vật.
- 16.2: người nói lời tùy hỷ là vị vừa dùng bữa xong (`bhuttāvī anumodeyyaṁ`), không phải thí chủ.
- 29.5 vs 30.5: `ahi / kukkura / manussakuṇapa` và `sālīnaṁ odanaṁ vicitakāḷakaṁ anekasūpaṁ
  anekabyañjanaṁ` — đủ ba xác, và "cơm trắng nấu từ gạo sāli, đã nhặt hết hạt đen, cùng nhiều
  món canh và nhiều món ăn", không rút gọn.
- 29.10 / 30.10: `jighacchitānampi na bhottukamyatā assa, pageva suhitānaṁ` — đúng phép đảo
  ("người đói cũng không muốn ăn, huống chi người no" / "người no cũng muốn ăn, huống chi người đói").
- 31.9–31.10: `vaṅka / jimha / dosa` → "cong / vênh / khuyết" nhất quán ở cả lời ước và lời kể;
  `suddhā assa sāre patiṭṭhitā` dịch "trong sạch và vững chắc tận phần lõi" đúng như dặn (không
  thành "an trú trong lõi đạo").
- 32.1 vs 32.2: danh sách xấu/đối xứng đảo đúng chiều `okkamane pubbaṅgamā, paviveke
  nikkhittadhurā` ↔ `okkamane nikkhittadhurā, paviveke pubbaṅgamā`.
- Lời kể gọi "Đức Thế Tôn", không có "Đức Phật"; bài không có lời nào của Đức Thế Tôn nên không
  xuất hiện "các ông"; Sāriputta gọi chúng tăng là "này các vị", các vị gọi lại "thưa Tôn giả" —
  nhất quán suốt bài.

---

## Điểm chưa chắc

1. **mn5:1.5** — `Āvusoti … paccassosuṁ` dịch "Thưa Tôn giả". Cùng một chữ `āvuso` mà 1.4 lại
   dịch "Này các hiền giả"; nhưng toàn bài mọi lời hướng đến Sāriputta (kể cả của Moggallāna) đều
   dùng "thưa Tôn giả", nên giữ cho thống nhất, không sửa.
2. **mn5:31.7 / 31.8** — `purāṇayānakāraputto` dịch "trước đây là con trai người thợ đóng xe"
   (nghe như ông ta đã thôi làm con). Có thể hiểu là "con trai một người thợ đóng xe trước kia";
   nhưng EN của Sujato cũng đọc "who was formerly of the wainwrights" nên chưa đủ chắc để đổi.
3. **mn5:30.9** — ba mục `manāpatā / appāṭikulyatā / ajegucchatā` dịch "ưa thích / dễ chịu /
   không ghê tởm". Đúng nghĩa nhưng không song song với 29.9 ("không ưa thích / ghê tởm / gớm
   ghiếc"); nếu muốn đối xứng từng chữ thì `appāṭikulyatā` nên là "không ghê tởm". Chỉ là mức độ
   song hành, không sai nghĩa.
4. **mn5:12.2, 13.2, 15.2** — có thêm "chỉ", "chính", "tức Đức Thế Tôn" so với PLI. Đây là những
   trợ từ làm rõ nhấn mạnh (`mameva`, `ahameva`) hoặc theo đúng dặn của `HUONG-DAN-DICH`; không
   phải thêm ý.
5. **mn5:3.1, 31.1** — "Khi nghe vậy" cho `Atha kho`. PLI chỉ có "Rồi"; "khi nghe vậy" là suy ra
   từ mạch, tự nhiên trong tiếng Việt, nhưng đúng nguyên tắc "không thêm" thì có thể bỏ.
6. **Note 17.2** (giảng Pháp cho tỳ-kheo-ni phạm tội) đặt sau 18-20.2 thay vì sau 17.2 như vị trí
   NOTE trong nguồn. Đặt sau 17.2 sẽ tối nghĩa vì câu 17.2 đã dịch theo PLI chỉ nói "các tỳ-kheo";
   giữ chỗ hiện tại.
7. **31.6 chú thích** lược phần dẫn chứng `Tha-ap 150:1.1` và `Bṛhatsaṁhitā 10.17` (bỏ link là
   đúng quy ước, nhưng bỏ luôn tên chứng liệu là mất một chút thông tin). Không sửa vì đây là
   lựa chọn tóm lược hợp lệ.

---

## Kết quả kiểm tra

```
python3 ghep.py && python3 tao-muc-luc.py && python3 ra-soat.py
  → KET LUAN: DAT — khong phat hien van de
python3 kiem-tra-marker.py Kinh-Khong-Ue-Nhiem.md
  → marker trong bài dịch: 203 / ==> ĐẠT
```

Tệp ghép `Kinh-Khong-Ue-Nhiem.md`: 203 đoạn, 7 phần; chú thích 5 + 5 + 2 + 9 = 21, khớp đủ 21
NOTE của nguồn. Không commit.
