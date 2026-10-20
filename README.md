# Trung Bộ Kinh — bản dịch tiếng Việt hiện đại

> 152 bài kinh trong *Majjhima Nikāya* (Trung Bộ Kinh), dịch từ nguyên bản Pali, đối chiếu bản tiếng
> Anh của Bhikkhu Sujato, viết cho người Việt hiện đại không học Phật vẫn đọc hiểu được.

**Trạng thái: 1/152 bài đã dịch.** Mỗi bài hoàn thành được đánh dấu ✅ trong bảng mục lục bên dưới.

---

## Đọc thử trong mười phút

Nếu bạn chưa từng đọc kinh Pali, bắt đầu từ bốn bài này:

| Bài | Vì sao nên đọc |
|---|---|
| [Kinh Niệm Xứ](010-kinh-niem-xu/Kinh-Niem-Xu.md) | Bài kinh nền tảng về thiền tập, đọc được như một hướng dẫn thực hành |
| [Kinh Ví Dụ Con Rắn](022-kinh-vi-du-con-ran/Kinh-Vi-Du-Con-Ran.md) | Cảnh báo nổi tiếng: giáo pháp phải nắm đúng cách, như bắt rắn phải bắt đúng chỗ |
| [Kinh Dạy Rāhula](061-kinh-day-rahula/Kinh-Day-Rahula.md) | Đức Thế Tôn dạy con trai mình về nói thật — ngắn, ấm, rất cụ thể |
| [Kinh Căn Bản Pháp Môn](001-kinh-can-ban-phap-mon/Kinh-Can-Ban-Phap-Mon.md) | Bài mở đầu bộ kinh: tâm phàm phu nhận thức thế giới bằng những khái niệm nào |

Các bài còn lại xem ở [mục lục đầy đủ](#mục-lục-152-bài).

---

## Bắt đầu từ đâu

1. **Muốn hiểu Phật giáo là gì** — đọc [Kinh Căn Bản Pháp Môn](001-kinh-can-ban-phap-mon/Kinh-Can-Ban-Phap-Mon.md)
   rồi [Kinh Tất Cả Lậu Hoặc](002-kinh-tat-ca-lau-hoac/Kinh-Tat-Ca-Lau-Hoac.md). Hai bài mở đầu bộ
   kinh trả lời: tâm nhận thức sai thế nào, và làm sao gột sạch những ô nhiễm ấy.
2. **Muốn thực hành** — [Kinh Niệm Xứ](010-kinh-niem-xu/Kinh-Niem-Xu.md) và
   [Kinh Niệm Hơi Thở](118-kinh-niem-hoi-tho/Kinh-Niem-Hoi-Tho.md) là hai bản hướng dẫn thiền đầy đủ
   nhất trong bộ.
3. **Muốn đọc như truyện** — các bài có cốt truyện rõ: [Kinh Aṅgulimāla](086-kinh-angulimala/Kinh-Angulimala.md)
   (kẻ giết người đổi đời), [Kinh Thánh Cầu](026-kinh-thanh-cau/Kinh-Thanh-Cau.md) (Đức Thế Tôn kể lại
   cuộc đời mình), Kinh Dạy Channa.

---

## Về bản dịch này

- **Dịch từ Pali**, không dịch lại từ bản tiếng Anh. Bản Anh của Bhikkhu Sujato (CC0) dùng để đối
  chiếu từng đoạn, phát hiện chỗ hiểu sai.
- **Mỗi đoạn nguồn là một đoạn dịch**, có neo `mnN:X.Y` trong tệp nguồn — trích dẫn hay báo lỗi đều
  tra ngược được tới SuttaCentral.
- **Văn phong**: tiếng Việt hiện đại, câu ngắn, chủ động; thuật ngữ Phật học giữ nhưng giải thích ở
  lần đầu xuất hiện; không dùng lối Hán-Việt cổ.
- **Quy ước đầy đủ**: [`HUONG-DAN-CHUNG.md`](HUONG-DAN-CHUNG.md).
- Các chỗ Sujato có chú thích đáng giữ thì bản dịch có `[Chú thích: …]` ngay sau đoạn liên quan.

---

## Cấu trúc kho

```
001-kinh-can-ban-phap-mon/     một bài kinh
├── Kinh-Can-Ban-Phap-Mon.md   bản dịch hoàn chỉnh (ghép từ ban-dich/)
├── ban-dich/                  từng đoạn, mỗi tệp một phần
├── nguon/                     Pali gốc, bản Anh Sujato, chú thích, segment
├── README.md                  giới thiệu bài
├── ghep.py                    ghép ban-dich/ thành Kinh-*.md
├── tao-muc-luc.py             chèn mục lục vào Kinh-*.md
├── kiem-tra-marker.py         kiểm tra đủ/đúng neo đoạn
├── ra-soat.py                 rà soát từ cấm, ngoặc, công thức lặp
└── tien-do.py                 báo tiến độ dịch
cong-cu/                       công cụ dùng chung
mau/                           khuôn để sinh bài mới
```

Muốn sửa một câu: tìm neo `mnN:X.Y` trong `Kinh-*.md`, sửa tệp tương ứng trong `ban-dich/`, chạy
`python3 ghep.py && python3 tao-muc-luc.py`, rồi `python3 kiem-tra-marker.py` và `python3 ra-soat.py`
phải in `DAT`. Chi tiết: [`DONG-GOP.md`](DONG-GOP.md).

---

## Mục lục 152 bài

<!-- BAT DAU MUC LUC -->
| # | Bài kinh | Tên Pali | Đã dịch |
|---|---|---|---|
| 1 | [Kinh Căn Bản Pháp Môn](001-kinh-can-ban-phap-mon/Kinh-Can-Ban-Phap-Mon.md) | *Mūlapariyāya* | ✅ |
| 2 | [Kinh Tất Cả Lậu Hoặc](002-kinh-tat-ca-lau-hoac/Kinh-Tat-Ca-Lau-Hoac.md) | *Sabbāsava* | ✅ |
| 3 | Kinh Người Thừa Kế Pháp | *Dhammadāyāda* | — |
| 4 | [Kinh Sợ Hãi và Kinh Hoàng](004-kinh-so-hai-va-kinh-hoang/Kinh-So-Hai-Va-Kinh-Hoang.md) | *Bhayabherava* | ✅ |
| 5 | Kinh Không Uế Nhiễm | *Anaṅgaṇa* | — |
| 6 | Kinh Ước Muốn | *Ākaṅkheyya* | — |
| 7 | [Kinh Ví Dụ Tấm Vải](007-kinh-vi-du-tam-vai/Kinh-Vi-Du-Tam-Vai.md) | *Vatthūpama* | ✅ |
| 8 | Kinh Loại Bỏ | *Sallekha* | — |
| 9 | [Kinh Chánh Kiến](009-kinh-chanh-kien/Kinh-Chanh-Kien.md) | *Sammādiṭṭhi* | ✅ |
| 10 | [Kinh Niệm Xứ](010-kinh-niem-xu/Kinh-Niem-Xu.md) | *Satipaṭṭhāna* | ✅ |
| 11 | Tiểu Kinh Sư Tử Hống | *Cūḷasīhanāda* | — |
| 12 | [Đại Kinh Sư Tử Hống](012-kinh-dai-su-tu-hong/Kinh-Dai-Su-Tu-Hong.md) | *Mahāsīhanāda* | ✅ |
| 13 | [Đại Kinh Khổ Uẩn](013-kinh-dai-kho-uan/Kinh-Dai-Kho-Uan.md) | *Mahādukkhakkhandha* | ✅ |
| 14 | Tiểu Kinh Khổ Uẩn | *Cūḷadukkhakkhandha* | — |
| 15 | Kinh Suy Đoán | *Anumāna* | — |
| 16 | Kinh Tâm Hoang Vu | *Cetokhila* | — |
| 17 | [Kinh Khu Rừng](017-kinh-khu-rung/Kinh-Khu-Rung.md) | *Vanapattha* | ✅ |
| 18 | [Kinh Mật Hoàn](018-kinh-mat-hoan/Kinh-Mat-Hoan.md) | *Madhupiṇḍika* | ✅ |
| 19 | [Kinh Hai Loại Tầm](019-kinh-hai-loai-tam/Kinh-Hai-Loai-Tam.md) | *Dvedhāvitakka* | ✅ |
| 20 | [Kinh An Trú Tầm](020-kinh-an-tru-tam/Kinh-An-Tru-Tam.md) | *Vitakkasaṇṭhāna* | ✅ |
| 21 | [Kinh Ví Dụ Cái Cưa](021-kinh-vi-du-cai-cua/Kinh-Vi-Du-Cai-Cua.md) | *Kakacūpama* | ✅ |
| 22 | [Kinh Ví Dụ Con Rắn](022-kinh-vi-du-con-ran/Kinh-Vi-Du-Con-Ran.md) | *Alagaddūpama* | ✅ |
| 23 | [Kinh Tổ Kiến](023-kinh-to-kien/Kinh-To-Kien.md) | *Vammika* | ✅ |
| 24 | [Kinh Cỗ Xe](024-kinh-co-xe/Kinh-Co-Xe.md) | *Rathavinīta* | ✅ |
| 25 | [Kinh Mồi Nhử](025-kinh-moi-nhu/Kinh-Moi-Nhu.md) | *Nivāpa* | ✅ |
| 26 | [Kinh Thánh Cầu](026-kinh-thanh-cau/Kinh-Thanh-Cau.md) | *Ariyapariyesanā* | ✅ |
| 27 | [Tiểu Kinh Dấu Chân Voi](027-kinh-tieu-dau-chan-voi/Kinh-Tieu-Dau-Chan-Voi.md) | *Cūḷahatthipadopama* | ✅ |
| 28 | [Đại Kinh Dấu Chân Voi](028-kinh-dai-dau-chan-voi/Kinh-Dai-Dau-Chan-Voi.md) | *Mahāhatthipadopama* | ✅ |
| 29 | [Đại Kinh Lõi Cây](029-kinh-dai-loi-cay/Kinh-Dai-Loi-Cay.md) | *Mahāsāropama* | ✅ |
| 30 | [Tiểu Kinh Lõi Cây](030-kinh-tieu-loi-cay/Kinh-Tieu-Loi-Cay.md) | *Cūḷasāropama* | ✅ |
| 31 | [Tiểu Kinh Rừng Gosiṅga](031-kinh-tieu-rung-gosinga/Kinh-Tieu-Rung-Gosinga.md) | *Cūḷagosiṅga* | ✅ |
| 32 | [Đại Kinh Rừng Gosiṅga](032-kinh-dai-rung-gosinga/Kinh-Dai-Rung-Gosinga.md) | *Mahāgosiṅga* | ✅ |
| 33 | [Đại Kinh Người Chăn Bò](033-kinh-dai-nguoi-chan-bo/Kinh-Dai-Nguoi-Chan-Bo.md) | *Mahāgopālaka* | ✅ |
| 34 | [Tiểu Kinh Người Chăn Bò](034-kinh-tieu-nguoi-chan-bo/Kinh-Tieu-Nguoi-Chan-Bo.md) | *Cūḷagopālaka* | ✅ |
| 35 | [Tiểu Kinh Saccaka](035-kinh-tieu-saccaka/Kinh-Tieu-Saccaka.md) | *Cūḷasaccaka* | ✅ |
| 36 | [Đại Kinh Saccaka](036-kinh-dai-saccaka/Kinh-Dai-Saccaka.md) | *Mahāsaccaka* | ✅ |
| 37 | [Tiểu Kinh Đoạn Tận Ái](037-kinh-tieu-doan-tan-ai/Kinh-Tieu-Doan-Tan-Ai.md) | *Cūḷataṇhāsaṅkhaya* | ✅ |
| 38 | [Đại Kinh Đoạn Tận Ái](038-kinh-dai-doan-tan-ai/Kinh-Dai-Doan-Tan-Ai.md) | *Mahātaṇhāsaṅkhaya* | ✅ |
| 39 | [Đại Kinh Assapura](039-kinh-dai-assapura/Kinh-Dai-Assapura.md) | *Mahāassapura* | ✅ |
| 40 | [Tiểu Kinh Assapura](040-kinh-tieu-assapura/Kinh-Tieu-Assapura.md) | *Cūḷaassapura* | ✅ |
| 41 | [Kinh Sāleyyaka](041-kinh-saleyyaka/Kinh-Saleyyaka.md) | *Sāleyyaka* | ✅ |
| 42 | [Kinh Verañjaka](042-kinh-veranjaka/Kinh-Veranjaka.md) | *Verañjaka* | ✅ |
| 43 | [Đại Kinh Phương Quảng](043-kinh-dai-phuong-quang/Kinh-Dai-Phuong-Quang.md) | *Mahāvedalla* | ✅ |
| 44 | [Tiểu Kinh Phương Quảng](044-kinh-tieu-phuong-quang/Kinh-Tieu-Phuong-Quang.md) | *Cūḷavedalla* | ✅ |
| 45 | [Tiểu Kinh Thọ Trì Pháp](045-kinh-tieu-tho-tri-phap/Kinh-Tieu-Tho-Tri-Phap.md) | *Cūḷadhammasamādāna* | ✅ |
| 46 | [Đại Kinh Thọ Trì Pháp](046-kinh-dai-tho-tri-phap/Kinh-Dai-Tho-Tri-Phap.md) | *Mahādhammasamādāna* | ✅ |
| 47 | [Kinh Tư Sát](047-kinh-tu-sat/Kinh-Tu-Sat.md) | *Vīmaṃsaka* | ✅ |
| 48 | [Kinh Kosambī](048-kinh-kosambi/Kinh-Kosambi.md) | *Kosambiya* | ✅ |
| 49 | [Kinh Phạm Thiên Mời](049-kinh-pham-thien-moi/Kinh-Pham-Thien-Moi.md) | *Brahmanimantanika* | ✅ |
| 50 | [Kinh Sự Khiển Trách Ma](050-kinh-su-khien-trach-ma/Kinh-Su-Khien-Trach-Ma.md) | *Māratajjanīya* | ✅ |
| 51 | Kinh Kandaraka | *Kandaraka* | — |
| 52 | Kinh Aṭṭhakanāgara | *Aṭṭhakanāgara* | — |
| 53 | [Kinh Hữu Học](053-kinh-huu-hoc/Kinh-Huu-Hoc.md) | *Sekha* | ✅ |
| 54 | [Kinh Potaliya](054-kinh-potaliya/Kinh-Potaliya.md) | *Potaliya* | ✅ |
| 55 | [Kinh Jīvaka](055-kinh-jivaka/Kinh-Jivaka.md) | *Jīvaka* | ✅ |
| 56 | [Kinh Upāli](056-kinh-upali/Kinh-Upali.md) | *Upāli* | ✅ |
| 57 | [Kinh Thực Hành Chó](057-kinh-thuc-hanh-cho/Kinh-Thuc-Hanh-Cho.md) | *Kukkuravatika* | ✅ |
| 58 | [Kinh Abhaya](058-kinh-abhaya/Kinh-Abhaya.md) | *Abhayarājakumāra* | ✅ |
| 59 | Kinh Nhiều Loại Cảm Thọ | *Bahuvedanīya* | — |
| 60 | [Kinh Không Thể Tranh Cãi](060-kinh-khong-the-tranh-cai/Kinh-Khong-The-Tranh-Cai.md) | *Apaṇṇaka* | ✅ |
| 61 | [Kinh Dạy Rāhula](061-kinh-day-rahula/Kinh-Day-Rahula.md) | *Rāhulovāda* | ✅ |
| 62 | [Đại Kinh Dạy Rāhula](062-kinh-dai-day-rahula/Kinh-Dai-Day-Rahula.md) | *Mahārāhulovāda* | ✅ |
| 63 | [Tiểu Kinh Māluṅkya](063-kinh-tieu-malunkya/Kinh-Tieu-Malunkya.md) | *Cūḷamālukya* | ✅ |
| 64 | [Đại Kinh Māluṅkya](064-kinh-dai-malunkya/Kinh-Dai-Malunkya.md) | *Mahāmālukya* | ✅ |
| 65 | [Kinh Bhaddāli](065-kinh-bhaddali/Kinh-Bhaddali.md) | *Bhaddāli* | ✅ |
| 66 | [Kinh Ví Dụ Con Chim Cút](066-kinh-vi-du-con-chim-cut/Kinh-Vi-Du-Con-Chim-Cut.md) | *Laṭukikopama* | ✅ |
| 67 | Kinh Cātumā | *Cātuma* | — |
| 68 | [Kinh Naḷakapāna](068-kinh-nalakapana/Kinh-Nalakapana.md) | *Naḷakapāna* | ✅ |
| 69 | Kinh Gulissāni | *Gulissāni* | — |
| 70 | [Kinh Kīṭāgiri](070-kinh-kitagiri/Kinh-Kitagiri.md) | *Kīṭāgiri* | ✅ |
| 71 | [Kinh Vacchagotta về Tam Minh](071-kinh-vacchagotta-ve-tam-minh/Kinh-Vacchagotta-Ve-Tam-Minh.md) | *Tevijjavacchagotta* | ✅ |
| 72 | [Kinh Vacchagotta về Lửa](072-kinh-vacchagotta-ve-lua/Kinh-Vacchagotta-Ve-Lua.md) | *Aggivacchagotta* | ✅ |
| 73 | Đại Kinh Vacchagotta | *Mahāvacchagotta* | — |
| 74 | [Kinh Dīghanakha](074-kinh-dighanakha/Kinh-Dighanakha.md) | *Dīghanakha* | ✅ |
| 75 | [Kinh Māgaṇḍiya](075-kinh-magandiya/Kinh-Magandiya.md) | *Māgaṇḍiya* | ✅ |
| 76 | Kinh Sandaka | *Sandaka* | — |
| 77 | [Đại Kinh Sakuludāyi](077-kinh-dai-sakuludayi/Kinh-Dai-Sakuludayi.md) | *Mahāsakuludāyi* | ✅ |
| 78 | [Kinh Sa-môn Muṇḍika](078-kinh-sa-mon-mundika/Kinh-Sa-Mon-Mundika.md) | *Samaṇamuṇḍika* | ✅ |
| 79 | [Tiểu Kinh Sakuludāyi](079-kinh-tieu-sakuludayi/Kinh-Tieu-Sakuludayi.md) | *Cūḷasakuludāyi* | ✅ |
| 80 | [Kinh Vekhanasa](080-kinh-vekhanasa/Kinh-Vekhanasa.md) | *Vekhanasa* | ✅ |
| 81 | [Kinh Ghaṭikāra](081-kinh-ghatikara/Kinh-Ghatikara.md) | *Ghaṭikāra* | ✅ |
| 82 | [Kinh Raṭṭhapāla](082-kinh-ratthapala/Kinh-Ratthapala.md) | *Raṭṭhapāla* | ✅ |
| 83 | [Kinh Makhādeva](083-kinh-makhadeva/Kinh-Makhadeva.md) | *Makhādeva* | ✅ |
| 84 | [Kinh Madhurā](084-kinh-madhura/Kinh-Madhura.md) | *Madhura* | ✅ |
| 85 | [Kinh Bodhirājakumāra](085-kinh-bodhirajakumara/Kinh-Bodhirajakumara.md) | *Bodhirājakumāra* | ✅ |
| 86 | [Kinh Aṅgulimāla](086-kinh-angulimala/Kinh-Angulimala.md) | *Aṅgulimāla* | ✅ |
| 87 | [Kinh Sinh Từ Người Thương](087-kinh-sinh-tu-nguoi-thuong/Kinh-Sinh-Tu-Nguoi-Thuong.md) | *Piyajātika* | ✅ |
| 88 | [Kinh Bāhitika](088-kinh-bahitika/Kinh-Bahitika.md) | *Bāhitika* | ✅ |
| 89 | [Kinh Bảo Tháp Pháp](089-kinh-bao-thap-phap/Kinh-Bao-Thap-Phap.md) | *Dhammacetiya* | ✅ |
| 90 | [Kinh Kaṇṇakatthala](090-kinh-kannakatthala/Kinh-Kannakatthala.md) | *Kaṇṇakatthala* | ✅ |
| 91 | [Kinh Brahmāyu](091-kinh-brahmayu/Kinh-Brahmayu.md) | *Brahmāyu* | ✅ |
| 92 | [Kinh Sela](092-kinh-sela/Kinh-Sela.md) | *Sela* | ✅ |
| 93 | [Kinh Assalāyana](093-kinh-assalayana/Kinh-Assalayana.md) | *Assalāyana* | ✅ |
| 94 | [Kinh Ghoṭamukha](094-kinh-ghotamukha/Kinh-Ghotamukha.md) | *Ghoṭamukha* | ✅ |
| 95 | [Kinh Caṅkī](095-kinh-canki/Kinh-Canki.md) | *Caṅkī* | ✅ |
| 96 | [Kinh Esukārī](096-kinh-esukari/Kinh-Esukari.md) | *Esukārī* | ✅ |
| 97 | [Kinh Dhānañjāni](097-kinh-dhananjani/Kinh-Dhananjani.md) | *Dhānañjāni* | ✅ |
| 98 | [Kinh Vāseṭṭha](098-kinh-vasettha/Kinh-Vasettha.md) | *Vāseṭṭha* | ✅ |
| 99 | [Kinh Subha](099-kinh-subha/Kinh-Subha.md) | *Subha* | ✅ |
| 100 | [Kinh Saṅgārava](100-kinh-sangarava/Kinh-Sangarava.md) | *Saṅgārava* | ✅ |
| 101 | [Kinh Devadaha](101-kinh-devadaha/Kinh-Devadaha.md) | *Devadaha* | ✅ |
| 102 | [Kinh Năm và Ba](102-kinh-nam-va-ba/Kinh-Nam-Va-Ba.md) | *Pañcattaya* | ✅ |
| 103 | [Kinh Như Thế Nào](103-kinh-nhu-the-nao/Kinh-Nhu-The-Nao.md) | *Kinti* | ✅ |
| 104 | [Kinh Sāmagāma](104-kinh-samagama/Kinh-Samagama.md) | *Sāmagāma* | ✅ |
| 105 | Kinh Sunakkhatta | *Sunakkhatta* | — |
| 106 | Kinh Về Bất Động | *Āneñjasappāya* | — |
| 107 | [Kinh Gaṇakamoggallāna](107-kinh-ganakamoggallana/Kinh-Ganakamoggallana.md) | *Gaṇakamoggallāna* | ✅ |
| 108 | Kinh Gopaka | *Gopakamoggallāna* | — |
| 109 | Đại Kinh Trăng Tròn | *Mahāpuṇṇama* | — |
| 110 | Tiểu Kinh Trăng Tròn | *Cūḷapuṇṇama* | — |
| 111 | Kinh Tùy Quán | *Anupada* | — |
| 112 | Kinh Sáu Thanh Tịnh | *Chabbisodhana* | — |
| 113 | Kinh Con Người Chân Thật | *Sappurisa* | — |
| 114 | Kinh Nên Thân Cận và Không Nên Thân Cận | *Sevitabbāsevitabba* | — |
| 115 | Kinh Nhiều Giới | *Bahudhātuka* | — |
| 116 | Kinh Isigili | *Isigili* | — |
| 117 | [Đại Kinh Bốn Mươi](117-kinh-dai-bon-muoi/Kinh-Dai-Bon-Muoi.md) | *Mahācattārīsaka* | ✅ |
| 118 | [Kinh Niệm Hơi Thở](118-kinh-niem-hoi-tho/Kinh-Niem-Hoi-Tho.md) | *Ānāpānassati* | ✅ |
| 119 | [Kinh Niệm Thân](119-kinh-niem-than/Kinh-Niem-Than.md) | *Kāyagatāsati* | ✅ |
| 120 | Kinh Tái Sinh Theo Hành | *Saṅkhārupapatti* | — |
| 121 | [Tiểu Kinh Không](121-kinh-tieu-khong/Kinh-Tieu-Khong.md) | *Cūḷasuññata* | ✅ |
| 122 | [Đại Kinh Không](122-kinh-dai-khong/Kinh-Dai-Khong.md) | *Mahāsuññata* | ✅ |
| 123 | Kinh Hy Hữu và Kỳ Diệu | *Acchariyaabbhuta* | — |
| 124 | Kinh Bākula | *Bākula* | — |
| 125 | [Kinh Địa Vị Người Đã Điều Phục](125-kinh-dia-vi-nguoi-da-dieu-phuc/Kinh-Dia-Vi-Nguoi-Da-Dieu-Phuc.md) | *Dantabhūmi* | ✅ |
| 126 | Kinh Bhūmija | *Bhūmija* | — |
| 127 | Kinh Anuruddha | *Anuruddha* | — |
| 128 | Kinh Ô Nhiễm | *Upakkilesa* | — |
| 129 | [Kinh Kẻ Ngu và Người Trí](129-kinh-ke-ngu-va-nguoi-tri/Kinh-Ke-Ngu-Va-Nguoi-Tri.md) | *Bālapaṇḍita* | ✅ |
| 130 | [Kinh Sứ Giả Của Thần Chết](130-kinh-su-gia-cua-than-chet/Kinh-Su-Gia-Cua-Than-Chet.md) | *Devadūta* | ✅ |
| 131 | [Kinh Một Đêm Lành](131-kinh-mot-dem-lanh/Kinh-Mot-Dem-Lanh.md) | *Bhaddekaratta* | ✅ |
| 132 | Kinh Ānanda Một Đêm Lành | *Ānandabhaddekaratta* | — |
| 133 | Đại Kinh Kaccāna Một Đêm Lành | *Mahākaccānabhaddekaratta* | — |
| 134 | Kinh Lomasakaṅgiya | *Lomasakaṅgiya* | — |
| 135 | [Tiểu Kinh Phân Biệt Nghiệp](135-kinh-tieu-phan-biet-nghiep/Kinh-Tieu-Phan-Biet-Nghiep.md) | *Cūḷakammavibhaṅga* | ✅ |
| 136 | [Đại Kinh Phân Biệt Nghiệp](136-kinh-dai-phan-biet-nghiep/Kinh-Dai-Phan-Biet-Nghiep.md) | *Mahākammavibhaṅga* | ✅ |
| 137 | [Kinh Phân Biệt Sáu Xứ](137-kinh-phan-biet-sau-xu/Kinh-Phan-Biet-Sau-Xu.md) | *Salāyatanavibhaṅga* | ✅ |
| 138 | Kinh Phân Biệt Tóm Tắt | *Uddesavibhaṅga* | — |
| 139 | [Kinh Phân Biệt Không Tranh Cãi](139-kinh-phan-biet-khong-tranh-cai/Kinh-Phan-Biet-Khong-Tranh-Cai.md) | *Araṇavibhaṅga* | ✅ |
| 140 | [Kinh Phân Biệt Giới](140-kinh-phan-biet-gioi/Kinh-Phan-Biet-Gioi.md) | *Dhātuvibhaṅga* | ✅ |
| 141 | [Kinh Phân Biệt Sự Thật](141-kinh-phan-biet-su-that/Kinh-Phan-Biet-Su-That.md) | *Saccavibhaṅga* | ✅ |
| 142 | [Kinh Phân Biệt Cúng Dường](142-kinh-phan-biet-cung-duong/Kinh-Phan-Biet-Cung-Duong.md) | *Dakkhiṇāvibhaṅga* | ✅ |
| 143 | [Kinh Dạy Anāthapiṇḍika](143-kinh-day-anathapindika/Kinh-Day-Anathapindika.md) | *Anāthapiṇḍikovāda* | ✅ |
| 144 | [Kinh Dạy Channa](144-kinh-day-channa/Kinh-Day-Channa.md) | *Channovāda* | ✅ |
| 145 | Kinh Dạy Puṇṇa | *Puṇṇovāda* | — |
| 146 | [Kinh Dạy Nandaka](146-kinh-day-nandaka/Kinh-Day-Nandaka.md) | *Nandakovāda* | ✅ |
| 147 | [Tiểu Kinh Dạy Rāhula](147-kinh-tieu-day-rahula/Kinh-Tieu-Day-Rahula.md) | *Cūḷarāhulovāda* | ✅ |
| 148 | [Kinh Sáu Sáu](148-kinh-sau-sau/Kinh-Sau-Sau.md) | *Chachakka* | ✅ |
| 149 | Đại Kinh Sáu Xứ | *Mahāsaḷāyatanika* | — |
| 150 | Kinh Nagaravinda | *Nagaravindeyya* | — |
| 151 | Kinh Thanh Tịnh Việc Khất Thực | *Piṇḍapātapārisuddhi* | — |
| 152 | [Kinh Tu Tập Các Căn](152-kinh-tu-tap-cac-can/Kinh-Tu-Tap-Cac-Can.md) | *Indriyabhāvanā* | ✅ |
<!-- KET THUC MUC LUC -->

---

## Giấy phép

- **Văn bản dịch**: CC0 1.0 — không cần ghi công, dùng thoải mái.
- **Mã nguồn**: MIT.
- Bản Pali: phạm vi công cộng. Bản tiếng Anh của Bhikkhu Sujato: CC0.

Chi tiết: [`LICENSE`](LICENSE).

---

## Góp ý và báo lỗi

Mở issue ở repo gốc, ghi rõ số bài và neo đoạn (`mn1:2.3`) cùng câu cần sửa. Mọi góp ý về nghĩa,
văn phong, thuật ngữ đều được hoan nghênh.
