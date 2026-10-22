# Rà soát nhãn `[Chú thích: …]` — chú thích Sujato hay lời người dịch?

Báo cáo đọc–ghi, **không sửa tệp bản dịch nào**, không commit. Ngày 2026-10-22.

## 1. Câu hỏi và quy ước đối chiếu

Theo `HUONG-DAN-CHUNG.md` §6 và `so-tay/CACH-DOC-CHU-THICH.md`: chú thích dịch từ **NOTE** của Bhikkhu Sujato mang nhãn `[Chú thích: …]`; chú thích do người dịch tự thêm mang nhãn `[Chú thích của người dịch: …]`. Báo cáo tìm những chỗ nhãn thứ nhất đang dùng cho nội dung thuộc loại thứ hai.

## 2. Cách làm

1. Quét `*/ban-dich/*.md` (905 tệp, 152 bài), cắt theo marker `<!-- seg: mnX:A.B -->`, trích mọi chuỗi mở đầu `[Chú thích: ` và không phải `[Chú thích của người dịch:`.
2. Lập chỉ mục NOTE từ `*/nguon/sections/*.md` (2646 NOTE, nguồn có thể chứa số đoạn gộp dạng `mn124:11-15.1`), đối chiếu theo số đoạn: trùng → ±1 → ±2 → ±3.
3. Ba nhóm nghi vấn:
   - **A** — chắc chắn của người dịch: tự khai “chú thích của người dịch”, nói về cách dịch/bản dịch này/bản Hán/PTS/`chúng tôi`, về số thứ tự bài, dòng kết, peyyāla.
   - **B** — có thể của Sujato nhưng Việt hoá mạnh: có NOTE nguồn nhưng bản dịch dài gấp 2–4 lần, thêm dẫn chứng/giải thích ngoài NOTE.
   - **C** — không có NOTE ở đoạn ấy và ±3 đoạn: không đủ căn cứ.

## 3. Số liệu

| Chỉ số | Số lượng |
|---|---|
| Tệp `ban-dich/*.md` đã quét | 905 |
| Chú thích `[Chú thích: …]` (không phải “của người dịch”) | **2632** |
| Có NOTE đúng đoạn | 2558 |
| Có NOTE trong ±1…±3 đoạn (lệch do peyyāla) | 25 |
| Không có NOTE ở đoạn ấy và ±3 đoạn | 49 |
| **Nghi vấn A** | **33** |
| **Nghi vấn B** | **12** |
| **Nghi vấn C** (đã trừ phần đã xếp A) | **20** |

## 4. Nhóm A — chắc chắn là của người dịch (33)

Điểm mạnh nhất: **24 chú thích tự khai** “Đây là chú thích của người dịch” / “ghi chú của người dịch” ngay trong nội dung mà vẫn mang nhãn `[Chú thích:`. Đây là bằng chứng nội tại, không cần suy đoán.

| Bài | Đoạn | Nhãn hiện tại | Phân loại | Trích chú thích hiện tại | NOTE nguồn (trích) | Đề nghị |
|---|---|---|---|---|---|---|
| 011-kinh-tieu-su-tu-hong | `mn11:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Chữ cūḷa nghĩa là nhỏ, ngắn; bài kinh này mang tên ấy để đối lại với Đại Kinh Sư Tử Hống ở MN 12 — ghi chú của người dịc… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 016-kinh-tam-hoang-vu | `mn16:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Cetokhila* ghép từ *ceto* (tâm, lòng) và *khila* (mảnh đất hoang cằn cỗi đến mức mưa suốt bốn tháng cũng không có gì mọ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 016-kinh-tam-hoang-vu | `mn16:27.10` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Bài thứ sáu là vị trí của bài này trong phẩm Sư Tử Hống, không phải số 16 của Trung Bộ Kinh. Đây là chú thích của người… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 017-kinh-khu-rung | `mn17:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Vanapattha* chỉ một nơi rừng rậm cách xa làng mạc, chỗ ở thích hợp cho người xuất gia tu tập. Bản Anh của SuttaCentral… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 017-kinh-khu-rung | `mn17:26.10` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | "Bài thứ bảy" là vị trí của bài này trong phẩm Sư Tử Hống, không phải số 17 của Trung Bộ Kinh. Đây là chú thích của ngườ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 018-kinh-mat-hoan | `mn18:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Madhu* là mật ong; *piṇḍika* là viên, cục nhỏ. Tên bài kinh lấy từ hình ảnh chiếc bánh mật ở đoạn cuối, khi Tôn giả Āna… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 019-kinh-hai-loai-tam | `mn19:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Dvedhā* là "hai phần, hai loại"; *vitakka* là "tầm", tức sự hướng tâm và suy nghĩ về một đối tượng. Đây là chú thích củ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 020-kinh-an-tru-tam | `mn20:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Vitakka* là "tầm", tức sự hướng tâm và suy nghĩ về một đối tượng; *saṇṭhāna* là "sự an trú, sự lắng lại". Tên bài kinh… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 020-kinh-an-tru-tam | `mn20:9.0` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Đây là bài kệ tóm tắt (uddāna) liệt kê mười bài kinh của phẩm Sư Tử Hống, từ MN 11 đến MN 20; mỗi cụm từ là một từ khóa… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 021-kinh-vi-du-cai-cua | `mn21:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Kakaca* là "cái cưa", *upama* là "ví dụ, sự so sánh". Tên bài kinh lấy từ hình ảnh ở phần cuối: dù kẻ cướp có dùng cưa… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 022-kinh-vi-du-con-ran | `mn22:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Alagadda* là một loài rắn độc, được hiểu là rắn hổ mang; *upama* là "ví dụ, so sánh". Bài kinh mượn hình ảnh bắt rắn để… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 023-kinh-to-kien | `mn23:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Vammika* là tổ kiến, gò đất do loài mối đùn lên; *sutta* là bài kinh. Tên bài kinh lấy từ hình ảnh mở đầu: một tổ kiến… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 025-kinh-moi-nhu | `mn25:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Nivāpa* là mồi, là thức ăn rải ra để dụ; *sutta* là bài kinh. Bản Anh của Bhikkhu Sujato đặt tên bài là "Sowing", nghĩa… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 025-kinh-moi-nhu | `mn25:2.4` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Bốn bước trong câu này là xương sống của cả bài: mê mẩn thọ hưởng, sinh say sưa, sinh phóng dật, rồi thành ra người gieo… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 025-kinh-moi-nhu | `mn25:6.28` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Đây là kế của bầy nai thứ tư, không phải lời lặp lại của bầy nai thứ ba. So với lời bầy nai thứ ba ở đoạn 6.19, chỉ khác… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 025-kinh-moi-nhu | `mn25:7.3` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Năm loại dục lạc là năm thứ khoái cảm đến từ mắt, tai, mũi, lưỡi và thân. Đây là chú thích của người dịch. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 038-kinh-dai-doan-tan-ai | `mn38:26.2` | `[Chú thích: …]` | **A** — có câu "Người dịch chú"/"chúng tôi" chen trong chú thích dịch từ NOTE | Theo MN 93:18.61, đây là một giáo thuyết của giới bà-la-môn, và rõ ràng đã được đưa vào bài kinh này như một quan niệm p… | According to MN 93:18.61 this was a doctrine of the brahmins, and it was evidently adopted in this sutta as a popular theory of conception. I discuss… | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 054-kinh-potaliya | `mn54:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Potaliya là tên riêng của một gia chủ nên được giữ nguyên dạng Pali theo quy ước của bộ dịch này. Chú thích của người dị… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 054-kinh-potaliya | `mn54:26.5` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Đây là dòng ghi dấu kết thúc bài kinh trong bản Pali; 'thứ tư' là số thứ tự của bài trong nhóm bài mà bản in ấy đang sắp… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 057-kinh-thuc-hanh-cho | `mn57:15.5` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Đây là dòng ghi kết thúc bài kinh trong bản Pali, không phải lời thoại. Đây là chú thích của người dịch. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 058-kinh-abhaya | `mn58:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Abhaya* nghĩa là "không sợ hãi"; *rājakumāra* nghĩa là thái tử. Tên Pali của bài kinh ghép cả hai lại, chỉ vị thái tử đ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 058-kinh-abhaya | `mn58:12.4` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | "Bài thứ tám" là bài thứ tám trong phẩm Gahapativagga của Trung Bộ Kinh, không phải bài thứ tám của toàn bộ 152 bài. Đây… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 059-kinh-nhieu-loai-cam-tho | `mn59:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Bahuvedanīya* ghép *bahu* (nhiều) với *vedanīya* (thuộc về cảm thọ), nghĩa là "nhiều loại cảm thọ". Đây là chú thích củ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 059-kinh-nhieu-loai-cam-tho | `mn59:15.5` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | Sự diệt thọ tưởng là trạng thái trong đó tưởng và thọ tạm thời ngưng nghỉ. Đây là chú thích của người dịch. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 059-kinh-nhieu-loai-cam-tho | `mn59:16.9` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | "Bài thứ chín" là bài thứ chín trong phẩm Gahapativagga của Trung Bộ Kinh, không phải bài thứ 59 của toàn bộ 152 bài. Đâ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 060-kinh-khong-the-tranh-cai | `mn60:0.2` | `[Chú thích: …]` | **A** — tự khai "chú thích của người dịch" trong chính nội dung | *Apaṇṇaka* là thuật ngữ đánh bạc, ghép *a* (không) với *paṇṇa* (số năm): bộ xúc xắc bốn hạt là "trọn vẹn", thêm hạt thứ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 060-kinh-khong-the-tranh-cai | `mn60:36.2` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Pali ở đây lược đoạn bằng dấu peyyāla; bản dịch ghi đủ danh sách các phép khổ hạnh quen thuộc, trùng với MN 12:45.1–45.8… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 060-kinh-khong-the-tranh-cai | `mn60:40-54.2` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Pali ở đây lược rất nhiều bằng dấu peyyāla: từ chỗ nghe Pháp, có đức tin, xuất gia, cho đến giới hạnh, hộ trì các căn, c… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 076-kinh-sandaka | `mn76:0.2` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Tên Sandaka và địa điểm này không thấy xuất hiện ở chỗ nào khác trong kinh tạng Pali. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Bỏ (trùng NOTE ở `mn76:2.1`); nếu giữ thì đổi nhãn người dịch |
| 077-kinh-dai-sakuludayi | `mn77:38.4` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Dòng kết này là lời ghi của truyền bản Pali, đánh dấu bài kinh thứ bảy trong một nhóm bài của bộ kinh, không phải số thứ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 079-kinh-tieu-sakuludayi | `mn79:46.8` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Dòng kết này là lời ghi của truyền bản Pali, đánh dấu bài kinh thứ chín trong một nhóm bài của bộ kinh, không phải số th… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 082-kinh-ratthapala | `mn82:42.55` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Dòng này là lời ghi kết thúc bài kinh trong bản Pali, không phải lời thoại; "bài thứ hai" là vị trí của bài kinh trong m… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |
| 119-kinh-niem-than | `mn119:38.1` | `[Chú thích: …]` | **A** — không có NOTE nguồn; nội dung nói về chính bản dịch / số thứ tự / peyyāla | Câu này trong nguyên bản kết bằng dấu lược peyyāla, là lối tắt để chuyển sang loại thắng trí kế tiếp, không phải chỗ thi… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Đổi nhãn → `[Chú thích của người dịch: …]` |

*Ghi chú:* các mục `mn*:0.2` là chú thích giải nghĩa tên bài — tiêu đề nguồn không có NOTE, nội dung do người dịch soạn. `mn76:0.2` trùng NOTE ở `mn76:2.1`. `mn38:26.2` có câu “Người dịch chú: …” chen giữa phần dịch NOTE.


## 5. Nhóm B — có thể của Sujato nhưng đã Việt hoá mạnh (12)

NOTE nguồn rất ngắn, bản dịch mở rộng gấp 2–4 lần và thêm chi tiết không có trong NOTE (dẫn kinh khác, giải nghĩa từ, nhận xét bối cảnh). Không thể kết luận chỉ bằng đối chiếu số đoạn; cần đọc bản gốc để quyết định.

| Bài | Đoạn | Nhãn hiện tại | Phân loại | Trích chú thích hiện tại | NOTE nguồn (trích) | Đề nghị |
|---|---|---|---|---|---|---|
| 013-kinh-dai-kho-uan | `mn13:13.2` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | *Chakaṇakā* thường được chú giải hiểu là phân bò đang sôi, nhưng tự thân từ này không nói lên điều đó, và các bản Hán tư… | For “splashed with dung” (chakaṇakāyapi osiñcanti), PTS reads pakkaṭṭhī, but this word appears to be spurious. The commentary says chakaṇakā means “bo… | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 017-kinh-khu-rung | `mn17:7-10.1` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Ở các trường hợp còn lại, *upanissāya* mang nghĩa sống nhờ vào sự hỗ trợ của làng, thị trấn, thành phố, miền đất hay một… | In the remaining cases I translate upanissaya as “supported by”. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 018-kinh-mat-hoan | `mn18:16.6` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Các pháp ở đây dịch chữ dhammā, chỉ những gì được ý biết chứ không phải được giác quan biết. Tiếng Anh không có từ tương… | Here, rather unsatisfactorily, “ideas” renders dhammā. Dhamma in the sense of “what is known by the mind rather than the senses” doesn’t readily map o… | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 037-kinh-tieu-doan-tan-ai | `mn37:5.3` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Ở đây Moggallāna gọi Sakka là yakkha, tức một vị thần có uy lực, chứ không phải loài quỷ; chữ này thường được dịch là dạ… | Moggallāna refers to Sakka as a “spirit” (yakkha). | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 054-kinh-potaliya | `mn54:25.7` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Chữ bhikkhū ở đây chỉ riêng các tỳ-kheo, tức tu sĩ theo giáo pháp này, không phải du sĩ của các giáo phái khác. | Notice how bhikkhū (“mendicants”) specifically indicates Buddhist monastics. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 067-kinh-catuma | `mn67:12.6` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Bản PTS chép câu này là *na kho te, Sāriputta, puna pi evarūpaṁ cittaṁ uppādetabbaṁ*, nghĩa là "này Sāriputta, ông chớ k… | The PTS reading is preferable: na kho te Sāriputta puna pi evarūpaṁ cittaṁ uppādetabbanti. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 076-kinh-sandaka | `mn76:16.11` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Đây là danh mục số liệu của truyền thống Ājīvaka, phần lớn không còn giải thích được rõ ràng. Bản dịch giữ đúng các con… | For explanations, see my note at DN 2:20.7. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 079-kinh-tieu-sakuludayi | `mn79:6.7` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Nigaṇṭha Nātaputta, quen gọi là Ni-kiền-tử Nātaputta, là vị giáo chủ của phái Ni-kiền-tử đương thời. Lời tự nhận ấy cũng… | The same claim is recorded at MN 14:17.2. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 094-kinh-ghotamukha | `mn94:1.2` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Không có vị tỳ-kheo nào tên Udena và cũng không có khu vườn nào tên Khemiya được nhắc đến ở chỗ khác trong các văn bản P… | Neither monk nor monastery are mentioned elsewhere in early texts. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 096-kinh-esukari | `mn96:12.1` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Chữ lokuttara chỉ cái vượt ra ngoài thế gian, tức giáo pháp đưa ra khỏi thế gian. Cách dùng chữ này trong câu trên cũng… | For lokuttaraṁ dhammaṁ as “transcendental teaching”, see SN 20.7:1.6, AN 2.47:1.5, AN 5.79:5.2. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 114-kinh-nen-than-can-va-khong-nen-than-can | `mn114:2.1` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Chữ sevati ở đây vừa có nghĩa là gần gũi, lui tới với một người, vừa có nghĩa là nuôi dưỡng, luyện tập bằng cách thường… | To “cultivate” is to foster or nurture through repeated association or practice. | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |
| 126-kinh-bhumija | `mn126:19.1` | `[Chú thích: …]` | **B** — NOTE nguồn ngắn, bản dịch mở rộng/giải thích gấp 2-4 lần → có thể của Sujato nhưng đã Việt hoá mạnh | Ở trên, thái tử Jayasena tỏ lòng tin nơi Đức Thế Tôn, chứ không phải nơi Tôn giả Bhūmija. Bốn ví dụ ở đây là bốn cặp, mỗ… | Above, Jayasena expresses his confidence in the Buddha, but not in Bhūmija (MN 126:5.1). | Giữ nhãn; tách phần thêm của người dịch sang nhãn người dịch |

## 6. Nhóm C — không có NOTE nguồn ở đoạn ấy (20)

Không có NOTE ở đúng đoạn và cả ±3 đoạn: chưa đủ căn cứ nhận là của Sujato, cũng chưa đủ để khẳng định là của người dịch. Phần lớn là gloss ngắn, có thể do người dịch viết hoặc do bản nguồn trong kho thiếu NOTE.

| Bài | Đoạn | Nhãn hiện tại | Phân loại | Trích chú thích hiện tại | NOTE nguồn (trích) | Đề nghị |
|---|---|---|---|---|---|---|
| 005-kinh-khong-ue-nhiem | `mn5:18-20.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Một tỳ-kheo giảng Pháp cho tỳ-kheo-ni vì động cơ thế tục thì phạm tội. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 007-kinh-vi-du-tam-vai | `mn7:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | *Vattha* là "tấm vải", *upama* là "ví dụ, so sánh". Tên kinh lấy hình ảnh tấm vải dơ và tấm vải sạch để nói về tâm bị cấ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 021-kinh-vi-du-cai-cua | `mn21:21.5` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Đoạn kết này được dẫn lại ở MN 28:24.3, nơi bài kinh mang tên "Lời khuyên về ví dụ cái cưa"; đây là một trong những ví d… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 024-kinh-co-xe | `mn24:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | *Rathavinīta* ghép từ *ratha*, cỗ xe, và *vinīta*, đã được huấn luyện hay đã thắng sẵn; chú giải hiểu là "bảy cỗ xe có n… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 038-kinh-dai-doan-tan-ai | `mn38:18.5` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Đức Thế Tôn hỏi tới hỏi lui các học trò, củng cố việc học bằng cách chắc chắn rằng họ hiểu từng điểm. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 075-kinh-magandiya | `mn75:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Tên Māgaṇḍiya có lẽ nghĩa là người đến từ xứ Mākandī bên bờ sông Hằng, thuộc vùng Kuru-Pañcāla. Chú giải Pali nói vị du… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 076-kinh-sandaka | `mn76:6.1` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Nếp sống phi phạm hạnh (abrahmacariyavāsa) là lối sống mà ai theo nó thì đời sống phạm hạnh không thể đứng vững. Đời sốn… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 082-kinh-ratthapala | `mn82:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Tên *Raṭṭhapāla* ghép từ *raṭṭha*, "quốc gia", và *pāla*, "người gìn giữ"; nghĩa là "người gìn giữ quốc gia". | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 085-kinh-bodhirajakumara | `mn85:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | *Bodhirājakumāra* là hợp từ *bodhi* (giác ngộ) và *rājakumāra* (thái tử); đây là tên riêng của một vị thái tử dòng Thích… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 085-kinh-bodhirajakumara | `mn85:1.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Susumāragira nghĩa là "tiếng gầm của cá sấu", một khu rừng trên dãy đồi thuộc xứ Bhaggā, phía nam sông Hằng. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 085-kinh-bodhirajakumara | `mn85:12.3` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Xứ Vô sở hữu là tầng vô sắc thứ ba, nơi tâm an trú trên ý niệm "không có gì cả". | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 085-kinh-bodhirajakumara | `mn85:13.3` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Xứ Phi tưởng phi phi tưởng là tầng vô sắc thứ tư, nơi tưởng đã vi tế đến mức không thể nói là có tưởng hay không có tưởn… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 085-kinh-bodhirajakumara | `mn85:57.17` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Padhāna nghĩa đen là "sửa" hay "đặt", do đó là "cố gắng", "tinh cần". Trong Phật giáo, từ này gần nghĩa với "thiền định"… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 099-kinh-subha | `mn99:16.1` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Dục công đức là năm nhóm đối tượng của giác quan được xem là đáng ưa, gồm sắc, tiếng, mùi, vị và xúc hấp dẫn. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 100-kinh-sangarava | `mn100:7.1` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Đức Thế Tôn gọi thanh niên Saṅgārava bằng tên dòng họ của ông ta là Bhāradvāja, theo lối gọi quen thuộc dành cho người b… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 106-kinh-ve-bat-dong | `mn106:13.10` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | `Sakkāya`, hữu thân, là cách gọi toàn bộ thân tâm gồm năm uẩn. Câu này nói rằng tất cả những gì vừa kể đều nằm trong phạ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 117-kinh-dai-bon-muoi | `mn117:0.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | *Mahā* là "lớn"; *cattārīsaka* là "bốn mươi". Tên gọi này phân biệt bài kinh với những bài cùng chủ đề ngắn hơn, và ý ng… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 127-kinh-anuruddha | `mn127:2.7` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Lời thỉnh dùng lối nói người thứ tư, nghĩa là bữa ăn dành cho bốn người, tính cả người thỉnh. | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 127-kinh-anuruddha | `mn127:16.8` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Chữ *jhāyati* trong Pali vừa có nghĩa là cháy, vừa có nghĩa là hành thiền; ở đây cả hai nghĩa cùng được dùng, nên ngọn đ… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |
| 138-kinh-phan-biet-tom-tat | `mn138:15.2` | `[Chú thích: …]` | **C** — không có NOTE ở đoạn này và ±3 đoạn | Bản Mahāsaṅgīti ở đoạn này ghi asaṇṭhita, nghĩa là "không mắc kẹt", nhưng câu kết ở 15.3 và cả mạch đoạn đều nói về sự m… | *(không có NOTE ở đoạn này và ±3 đoạn)* | Tra NOTE gốc; nếu không có thì đổi nhãn người dịch |

## 7. Năm ví dụ rõ nhất

1. `mn11:0.2` — “Chữ cūḷa nghĩa là nhỏ, ngắn; … — **ghi chú của người dịch**.” Nhãn hiện tại `[Chú thích:`. → đổi nhãn.
2. `mn54:0.2` — “Potaliya là tên riêng … theo **quy ước của bộ dịch này**. Chú thích của người dịch.” → đổi nhãn.
3. `mn60:36.2` — “Pali ở đây lược đoạn bằng dấu peyyāla; **bản dịch ghi đủ** danh sách …” → đổi nhãn.
4. `mn77:38.4` — “Dòng kết này là lời ghi của truyền bản Pali, đánh dấu bài kinh thứ bảy …, **không phải số thứ tự 77** của Trung Bộ Kinh.” → đổi nhãn.
5. `mn38:26.2` — dịch từ NOTE nhưng chèn “**Người dịch chú:** gandhabba ở đây chỉ chúng sinh sắp nhập thai…” → tách phần thêm sang nhãn người dịch.


## 8. Đề nghị chung (không thực hiện trong báo cáo này)

- 33 chú thích nhóm A: đổi nhãn sang `[Chú thích của người dịch: …]`; riêng `mn76:0.2` nên **bỏ** vì trùng NOTE `mn76:2.1`.
- 12 nhóm B: giữ nhãn, tách phần thêm của người dịch sang câu riêng có nhãn người dịch.
- 20 nhóm C: tra lại bản Sujato gốc; nếu không có NOTE thì đổi nhãn người dịch.
- Nên bổ sung quy ước: chú thích giải nghĩa **tên bài** (`mn*:0.2`) và chú thích về **số thứ tự / dòng kết / peyyāla** mặc định là của người dịch.


## 9. Cách tái lập

```python
import re,glob
note={}
for f in glob.glob("*/nguon/sections/*.md"):
    cur=None
    for line in open(f,encoding="utf-8"):
        m=re.match(r"^## (mn\d+):([\d.\-]+)(\s|$)",line)
        if m: cur=m.group(1)+":"+m.group(2); continue
        if cur and line.startswith("- **NOTE**:"): note[cur]=line[11:].strip()
for f in glob.glob("*/ban-dich/*.md"):
    for m in re.finditer(r"<!-- seg: (mn\d+):([\d.\-]+) -->(.*?)(?=<!-- seg:|\Z)",open(f,encoding="utf-8").read(),re.S):
        for c in re.findall(r"\[Chú thích: (.+?)\]",m.group(3),re.S):
            print(f, m.group(1)+":"+m.group(2), c[:60])
```

## 8. Kết quả xử lý (2026-10-22)

- **Nhóm A**: đổi nhãn 32 chú thích sang `[Chú thích của người dịch: …]`, bỏ câu tự khai thừa trong nội dung; riêng `mn38:26.2` tách làm hai chú thích (phần đầu của Sujato, phần sau của người dịch). Một trường hợp trong danh sách A là **báo nhầm**: `mn76:0.2` thực ra dịch từ NOTE ở `mn76:1.2` ("Neither Sandaka nor this location appear to be known elsewhere") nên giữ nguyên nhãn.
- **Nhóm C**: đổi nhãn 17 chú thích giải nghĩa rõ ràng là của người dịch — 6 chú thích nhan đề (`mn7:0.2`, `mn24:0.2`, `mn75:0.2`, `mn82:0.2`, `mn85:0.2`, `mn117:0.2`; các tệp `00-title.md` không có NOTE nguồn) và 11 chú thích gloss từ ngữ (`mn5:18-20.2`, `mn38:18.5`, `mn76:6.1`, `mn85:1.2`, `mn85:12.3`, `mn85:13.3`, `mn99:16.1`, `mn100:7.1`, `mn106:13.10`, `mn127:2.7`, `mn127:16.8`).
- **Còn để ngỏ**: 12 điểm nhóm B (chú thích dài hơn NOTE nguồn, cần tách phần thêm của người dịch) và 2 điểm nhóm C (`mn21:21.5`, `mn138:15.2`) — ghi ở mục "Việc còn lại" của `TIEN-DO.md`.
