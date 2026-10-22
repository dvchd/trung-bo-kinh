# Xử lý 12 chú thích nhóm B — tách lời Sujato và lời người dịch

Ngày: 2026-10-22. Phạm vi: 12 đoạn `mn13:13.2`, `mn17:7-10.1`, `mn18:16.6`, `mn37:5.3`,
`mn54:25.7`, `mn67:12.6`, `mn76:16.11`, `mn79:6.7`, `mn94:1.2`, `mn96:12.1`, `mn114:2.1`,
`mn126:19.1`. Chỉ sửa chú thích trong `ban-dich/*.md`, ghép lại bản `Kinh-*.md` bằng script của
từng bài; không commit.

## 1. Cách làm

Với từng đoạn: đọc **NOTE đầy đủ** trong `<bài>/nguon/sections/*.md`, đọc chú thích hiện tại, rồi
tách theo nội dung chứ không theo độ dài: phần nào dịch từ NOTE Sujato thì giữ nhãn
`[Chú thích: …]`; phần thêm của người dịch (giải nghĩa từ, quyết định dịch, dẫn kinh khác, nhận
xét bối cảnh) thì chuyển sang `[Chú thích của người dịch: …]` đặt ngay sau. Mỗi chú thích mới
≤3 câu, không thêm link/HTML, không đổi nghĩa NOTE.

## 2. Một phát hiện về danh sách nguồn

Cột "NOTE nguồn (trích)" trong `chu-thich-nhan.md` bị cắt ở khoảng 140 ký tự, rất có thể vì thế
mà 3 ca dưới đây bị xếp B nhầm. Đối chiếu NOTE đầy đủ thì **3 ca không có phần thêm của người
dịch**:

- `mn13:13.2` — NOTE đầy đủ 671 ký tự (PTS, chú giải, MA 99 / T 53 / EA 21.9, Atharvaveda,
  *abhivagga*); bản dịch chỉ là bản tóm trung thành, ngắn hơn NOTE.
- `mn18:16.6` — NOTE đầy đủ về *dhammā* / "ideas" 725 ký tự; bản dịch tóm đúng các ý chính,
  ngắn hơn NOTE, không thêm.
- `mn94:1.2` — NOTE 66 ký tự; bản dịch dài hơn vì nêu rõ tên Udena và Khemiya, nhưng không thêm
  thông tin ngoài NOTE.

Ba ca này được giữ nguyên. Chín ca còn lại đúng là có phần của người dịch và đã được tách.

## 3. Bảng kết quả (12 dòng)

| Bài | Đoạn | Đã làm gì | Phần Sujato giữ lại | Phần người dịch tách ra / bỏ |
|---|---|---|---|---|
| MN 13 — Đại Kinh Khổ Uẩn | `mn13:13.2` | Giữ nguyên, không sửa | Toàn bộ NOTE: *chakaṇakā* / chú giải "phân bò sôi" / bản Hán "đồng nóng chảy, sắt nóng chảy"; *abhivagga* chỉ có ở đây, chú giải "vũ khí trăm răng", hiểu là "lực lượng áp đảo" | Không có phần thêm; NOTE đầy đủ dài hơn bản dịch |
| MN 17 — Kinh Khu Rừng | `mn17:7-10.1` | Tách thành 2 chú thích | "Ở các trường hợp còn lại, *upanissāya* được dịch là 'nương tựa'" | Nghĩa "sống nhờ vào sự hỗ trợ của làng, thị trấn, thành phố, miền đất hay một người" và quyết định giữ chữ "nương tựa" |
| MN 18 — Kinh Mật Hoàn | `mn18:16.6` | Giữ nguyên, không sửa | Toàn bộ NOTE: "ideas" dịch *dhammā*; "mind objects" đưa khái niệm Abhidhamma vào kinh; "phenomena" không ổn; "ý niệm" là lựa chọn ít tệ nhất | Không có phần thêm |
| MN 37 — Tiểu Kinh Đoạn Tận Ái | `mn37:5.3` | Tách thành 2 chú thích | "Moggallāna gọi Sakka là yakkha, tức một vị thần" | "yakkha thường được dịch là dạ-xoa; ở đây là thần có uy lực, không phải loài quỷ" |
| MN 54 — Kinh Potaliya | `mn54:25.7` | Tách thành 2 chú thích | "bhikkhū chỉ riêng các tỳ-kheo, tức các tu sĩ Phật giáo" | "điều này phân biệt họ với du sĩ của các giáo phái khác" |
| MN 67 — Kinh Cātuma | `mn67:12.6` | Tách thành 2 chú thích; bổ sung ý "đáng theo hơn" của NOTE | "Bản PTS chép … nghĩa là …; cách đọc này đáng theo hơn" | "Bản Mahāsaṅgīti rút gọn nên câu chữ khó đọc theo nghĩa đen" |
| MN 76 — Kinh Sandaka | `mn76:16.11` | Tách thành 2 chú thích; đưa chỉ dẫn gốc trở lại | "Xem chú thích ở DN 2:20.7 để có giải thích" | "danh mục số liệu Ājīvaka, phần lớn không còn giải thích rõ; bản dịch giữ đúng các con số" |
| MN 79 — Tiểu Kinh Sakuludāyi | `mn79:6.7` | Tách thành 2 chú thích; ghi rõ số hiệu MN 14:17.2 | "Lời tự nhận ấy cũng được ghi lại ở MN 14:17.2" | "Nigaṇṭha Nātaputta, quen gọi là Ni-kiền-tử Nātaputta, là giáo chủ phái Ni-kiền-tử đương thời" |
| MN 94 — Kinh Ghotamukha | `mn94:1.2` | Giữ nguyên, không sửa | Toàn bộ NOTE: không có tỳ-kheo Udena và khu vườn Khemiya nào khác trong văn bản sơ kỳ | Không có phần thêm; bản dịch chỉ nêu rõ tên |
| MN 96 — Kinh Esukārī | `mn96:12.1` | Tách thành 2 chú thích; ghi đủ số hiệu SN/AN | "Cách dùng *lokuttara* cho 'giáo pháp' cũng gặp ở SN 20.7:1.6, AN 2.47:1.5, AN 5.79:5.2" | "*lokuttara* nghĩa là vượt ra ngoài thế gian, tức giáo pháp đưa người ra khỏi thế gian" |
| MN 114 — Kinh Nên Thân Cận Và Không Nên Thân Cận | `mn114:2.1` | Tách thành 2 chú thích | "'Thân cận' ở đây có nghĩa là nuôi dưỡng, luyện tập bằng cách thường xuyên tiếp xúc" | "*sevati* còn nghĩa gần gũi, lui tới với một người; bản dịch giữ một chữ 'thân cận' cho cả hai nghĩa" |
| MN 126 — Kinh Bhūmija | `mn126:19.1` | Tách thành 2 chú thích; ghi rõ MN 126:5.1 | "Ở trên, tại MN 126:5.1, thái tử Jayasena tỏ lòng tin nơi Đức Thế Tôn, chứ không phải nơi Tôn giả Bhūmija" | "bốn ví dụ là bốn cặp, mỗi cặp gồm một cách làm không hợp lý và một cách làm hợp lý" |

Tổng: 9 chú thích tách đôi, 3 giữ nguyên; không bỏ nội dung nào (mọi phần thêm đều đủ rõ để tách
thành chú thích riêng, không ca nào phải cắt bỏ vì quá vụn).

## 4. Kiểm chứng

Sau mỗi bài đã chạy `ghep.py`, `tao-muc-luc.py`, `ra-soat.py`, `kiem-tra-marker.py`. Cả 12 bài
đều cho `KET LUAN: DAT — khong phat hien van de` và `==> ĐẠT`:

`013`, `017`, `018`, `037`, `054`, `067`, `076`, `079`, `094`, `096`, `114`, `126`.

## 5. Ghi chú

- Không commit. Không sửa bản dịch ngoài 12 chú thích trên; các tệp `Kinh-*.md` thay đổi là do
  script ghép của từng bài chạy lại theo đúng quy trình.
- Trong thời gian làm, cây làm việc có thay đổi ở `097-kinh-dhananjani`, `100-kinh-sangarava`,
  `101-kinh-devadaha` và hai báo cáo `so-tay/ra-soat/mn100.md`, `mn101.md`; đó không phải thay đổi
  của tôi và tôi không chạm vào.
