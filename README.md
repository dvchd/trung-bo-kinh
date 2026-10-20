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
| 17 | Kinh Khu Rừng | *Vanapattha* | — |
| 18 | Kinh Mật Hoàn | *Madhupiṇḍika* | — |
| 19 | [Kinh Hai Loại Tầm](019-kinh-hai-loai-tam/Kinh-Hai-Loai-Tam.md) | *Dvedhāvitakka* | ✅ |
| 20 | [Kinh An Trú Tầm](020-kinh-an-tru-tam/Kinh-An-Tru-Tam.md) | *Vitakkasaṇṭhāna* | ✅ |
| 21 | [Kinh Ví Dụ Cái Cưa](021-kinh-vi-du-cai-cua/Kinh-Vi-Du-Cai-Cua.md) | *Kakacūpama* | ✅ |
| 22 | [Kinh Ví Dụ Con Rắn](022-kinh-vi-du-con-ran/Kinh-Vi-Du-Con-Ran.md) | *Alagaddūpama* | ✅ |
| 23 | Kinh Tổ Kiến | *Vammika* | — |
| 24 | Kinh Cỗ Xe | *Rathavinīta* | — |
| 25 | Kinh Mồi Nhử | *Nivāpa* | — |
| 26 | [Kinh Thánh Cầu](026-kinh-thanh-cau/Kinh-Thanh-Cau.md) | *Ariyapariyesanā* | ✅ |
| 27 | [Tiểu Kinh Dấu Chân Voi](027-kinh-tieu-dau-chan-voi/Kinh-Tieu-Dau-Chan-Voi.md) | *Cūḷahatthipadopama* | ✅ |
| 28 | [Đại Kinh Dấu Chân Voi](028-kinh-dai-dau-chan-voi/Kinh-Dai-Dau-Chan-Voi.md) | *Mahāhatthipadopama* | ✅ |
| 29 | [Đại Kinh Lõi Cây](029-kinh-dai-loi-cay/Kinh-Dai-Loi-Cay.md) | *Mahāsāropama* | ✅ |
| 30 | [Tiểu Kinh Lõi Cây](030-kinh-tieu-loi-cay/Kinh-Tieu-Loi-Cay.md) | *Cūḷasāropama* | ✅ |
| 31 | Tiểu Kinh Rừng Gosiṅga | *Cūḷagosiṅga* | — |
| 32 | Đại Kinh Rừng Gosiṅga | *Mahāgosiṅga* | — |
| 33 | Đại Kinh Người Chăn Bò | *Mahāgopālaka* | — |
| 34 | Tiểu Kinh Người Chăn Bò | *Cūḷagopālaka* | — |
| 35 | [Tiểu Kinh Saccaka](035-kinh-tieu-saccaka/Kinh-Tieu-Saccaka.md) | *Cūḷasaccaka* | ✅ |
| 36 | [Đại Kinh Saccaka](036-kinh-dai-saccaka/Kinh-Dai-Saccaka.md) | *Mahāsaccaka* | ✅ |
| 37 | [Tiểu Kinh Đoạn Tận Ái](037-kinh-tieu-doan-tan-ai/Kinh-Tieu-Doan-Tan-Ai.md) | *Cūḷataṇhāsaṅkhaya* | ✅ |
| 38 | [Đại Kinh Đoạn Tận Ái](038-kinh-dai-doan-tan-ai/Kinh-Dai-Doan-Tan-Ai.md) | *Mahātaṇhāsaṅkhaya* | ✅ |
| 39 | [Đại Kinh Assapura](039-kinh-dai-assapura/Kinh-Dai-Assapura.md) | *Mahāassapura* | ✅ |
| 40 | [Tiểu Kinh Assapura](040-kinh-tieu-assapura/Kinh-Tieu-Assapura.md) | *Cūḷaassapura* | ✅ |
| 41 | Kinh Sāleyyaka | *Sāleyyaka* | — |
| 42 | Kinh Verañjaka | *Verañjaka* | — |
| 43 | [Đại Kinh Phương Quảng](043-kinh-dai-phuong-quang/Kinh-Dai-Phuong-Quang.md) | *Mahāvedalla* | ✅ |
| 44 | [Tiểu Kinh Phương Quảng](044-kinh-tieu-phuong-quang/Kinh-Tieu-Phuong-Quang.md) | *Cūḷavedalla* | ✅ |
| 45 | Tiểu Kinh Thọ Trì Pháp | *Cūḷadhammasamādāna* | — |
| 46 | Đại Kinh Thọ Trì Pháp | *Mahādhammasamādāna* | — |
| 47 | Kinh Tư Sát | *Vīmaṃsaka* | — |
| 48 | [Kinh Kosambī](048-kinh-kosambi/Kinh-Kosambi.md) | *Kosambiya* | ✅ |
| 49 | Kinh Phạm Thiên Mời | *Brahmanimantanika* | — |
| 50 | Kinh Sự Khiển Trách Ma | *Māratajjanīya* | — |
| 51 | Kinh Kandaraka | *Kandaraka* | — |
| 52 | Kinh Aṭṭhakanāgara | *Aṭṭhakanāgara* | — |
| 53 | Kinh Hữu Học | *Sekha* | — |
| 54 | [Kinh Potaliya](054-kinh-potaliya/Kinh-Potaliya.md) | *Potaliya* | ✅ |
| 55 | Kinh Jīvaka | *Jīvaka* | — |
| 56 | Kinh Upāli | *Upāli* | — |
| 57 | Kinh Thực Hành Chó | *Kukkuravatika* | — |
| 58 | Kinh Abhaya | *Abhayarājakumāra* | — |
| 59 | Kinh Nhiều Loại Cảm Thọ | *Bahuvedanīya* | — |
| 60 | Kinh Không Thể Tranh Cãi | *Apaṇṇaka* | — |
| 61 | [Kinh Dạy Rāhula](061-kinh-day-rahula/Kinh-Day-Rahula.md) | *Rāhulovāda* | ✅ |
| 62 | [Đại Kinh Dạy Rāhula](062-kinh-dai-day-rahula/Kinh-Dai-Day-Rahula.md) | *Mahārāhulovāda* | ✅ |
| 63 | Tiểu Kinh Māluṅkya | *Cūḷamālukya* | — |
| 64 | [Đại Kinh Māluṅkya](064-kinh-dai-malunkya/Kinh-Dai-Malunkya.md) | *Mahāmālukya* | ✅ |
| 65 | Kinh Bhaddāli | *Bhaddāli* | — |
| 66 | Kinh Ví Dụ Con Chim Cút | *Laṭukikopama* | — |
| 67 | Kinh Cātumā | *Cātuma* | — |
| 68 | Kinh Naḷakapāna | *Naḷakapāna* | — |
| 69 | Kinh Gulissāni | *Gulissāni* | — |
| 70 | [Kinh Kīṭāgiri](070-kinh-kitagiri/Kinh-Kitagiri.md) | *Kīṭāgiri* | ✅ |
| 71 | Kinh Vacchagotta về Tam Minh | *Tevijjavacchagotta* | — |
| 72 | Kinh Vacchagotta về Lửa | *Aggivacchagotta* | — |
| 73 | Đại Kinh Vacchagotta | *Mahāvacchagotta* | — |
| 74 | Kinh Dīghanakha | *Dīghanakha* | — |
| 75 | Kinh Māgaṇḍiya | *Māgaṇḍiya* | — |
| 76 | Kinh Sandaka | *Sandaka* | — |
| 77 | Đại Kinh Sakuludāyi | *Mahāsakuludāyi* | — |
| 78 | Kinh Sa-môn Muṇḍika | *Samaṇamuṇḍika* | — |
| 79 | Tiểu Kinh Sakuludāyi | *Cūḷasakuludāyi* | — |
| 80 | Kinh Vekhanasa | *Vekhanasa* | — |
| 81 | Kinh Ghaṭikāra | *Ghaṭikāra* | — |
| 82 | Kinh Raṭṭhapāla | *Raṭṭhapāla* | — |
| 83 | Kinh Makhādeva | *Makhādeva* | — |
| 84 | Kinh Madhurā | *Madhura* | — |
| 85 | Kinh Bodhirājakumāra | *Bodhirājakumāra* | — |
| 86 | [Kinh Aṅgulimāla](086-kinh-angulimala/Kinh-Angulimala.md) | *Aṅgulimāla* | ✅ |
| 87 | Kinh Sinh Từ Người Thương | *Piyajātika* | — |
| 88 | Kinh Bāhitika | *Bāhitika* | — |
| 89 | Kinh Bảo Tháp Pháp | *Dhammacetiya* | — |
| 90 | Kinh Kaṇṇakatthala | *Kaṇṇakatthala* | — |
| 91 | Kinh Brahmāyu | *Brahmāyu* | — |
| 92 | Kinh Sela | *Sela* | — |
| 93 | Kinh Assalāyana | *Assalāyana* | — |
| 94 | Kinh Ghoṭamukha | *Ghoṭamukha* | — |
| 95 | Kinh Caṅkī | *Caṅkī* | — |
| 96 | Kinh Esukārī | *Esukārī* | — |
| 97 | Kinh Dhānañjāni | *Dhānañjāni* | — |
| 98 | Kinh Vāseṭṭha | *Vāseṭṭha* | — |
| 99 | Kinh Subha | *Subha* | — |
| 100 | Kinh Saṅgārava | *Saṅgārava* | — |
| 101 | Kinh Devadaha | *Devadaha* | — |
| 102 | Kinh Năm và Ba | *Pañcattaya* | — |
| 103 | Kinh Như Thế Nào | *Kinti* | — |
| 104 | Kinh Sāmagāma | *Sāmagāma* | — |
| 105 | Kinh Sunakkhatta | *Sunakkhatta* | — |
| 106 | Kinh Về Bất Động | *Āneñjasappāya* | — |
| 107 | Kinh Gaṇakamoggallāna | *Gaṇakamoggallāna* | — |
| 108 | Kinh Gopaka | *Gopakamoggallāna* | — |
| 109 | Đại Kinh Trăng Tròn | *Mahāpuṇṇama* | — |
| 110 | Tiểu Kinh Trăng Tròn | *Cūḷapuṇṇama* | — |
| 111 | Kinh Tùy Quán | *Anupada* | — |
| 112 | Kinh Sáu Thanh Tịnh | *Chabbisodhana* | — |
| 113 | Kinh Con Người Chân Thật | *Sappurisa* | — |
| 114 | Kinh Nên Thân Cận và Không Nên Thân Cận | *Sevitabbāsevitabba* | — |
| 115 | Kinh Nhiều Giới | *Bahudhātuka* | — |
| 116 | Kinh Isigili | *Isigili* | — |
| 117 | Đại Kinh Bốn Mươi | *Mahācattārīsaka* | — |
| 118 | [Kinh Niệm Hơi Thở](118-kinh-niem-hoi-tho/Kinh-Niem-Hoi-Tho.md) | *Ānāpānassati* | ✅ |
| 119 | Kinh Niệm Thân | *Kāyagatāsati* | — |
| 120 | Kinh Tái Sinh Theo Hành | *Saṅkhārupapatti* | — |
| 121 | Tiểu Kinh Không | *Cūḷasuññata* | — |
| 122 | Đại Kinh Không | *Mahāsuññata* | — |
| 123 | Kinh Hy Hữu và Kỳ Diệu | *Acchariyaabbhuta* | — |
| 124 | Kinh Bākula | *Bākula* | — |
| 125 | Kinh Địa Vị Người Đã Điều Phục | *Dantabhūmi* | — |
| 126 | Kinh Bhūmija | *Bhūmija* | — |
| 127 | Kinh Anuruddha | *Anuruddha* | — |
| 128 | Kinh Ô Nhiễm | *Upakkilesa* | — |
| 129 | Kinh Kẻ Ngu và Người Trí | *Bālapaṇḍita* | — |
| 130 | Kinh Sứ Giả Của Thần Chết | *Devadūta* | — |
| 131 | [Kinh Một Đêm Lành](131-kinh-mot-dem-lanh/Kinh-Mot-Dem-Lanh.md) | *Bhaddekaratta* | ✅ |
| 132 | Kinh Ānanda Một Đêm Lành | *Ānandabhaddekaratta* | — |
| 133 | Đại Kinh Kaccāna Một Đêm Lành | *Mahākaccānabhaddekaratta* | — |
| 134 | Kinh Lomasakaṅgiya | *Lomasakaṅgiya* | — |
| 135 | Tiểu Kinh Phân Biệt Nghiệp | *Cūḷakammavibhaṅga* | — |
| 136 | Đại Kinh Phân Biệt Nghiệp | *Mahākammavibhaṅga* | — |
| 137 | Kinh Phân Biệt Sáu Xứ | *Salāyatanavibhaṅga* | — |
| 138 | Kinh Phân Biệt Tóm Tắt | *Uddesavibhaṅga* | — |
| 139 | Kinh Phân Biệt Không Tranh Cãi | *Araṇavibhaṅga* | — |
| 140 | Kinh Phân Biệt Giới | *Dhātuvibhaṅga* | — |
| 141 | Kinh Phân Biệt Sự Thật | *Saccavibhaṅga* | — |
| 142 | Kinh Phân Biệt Cúng Dường | *Dakkhiṇāvibhaṅga* | — |
| 143 | Kinh Dạy Anāthapiṇḍika | *Anāthapiṇḍikovāda* | — |
| 144 | Kinh Dạy Channa | *Channovāda* | — |
| 145 | Kinh Dạy Puṇṇa | *Puṇṇovāda* | — |
| 146 | Kinh Dạy Nandaka | *Nandakovāda* | — |
| 147 | Tiểu Kinh Dạy Rāhula | *Cūḷarāhulovāda* | — |
| 148 | Kinh Sáu Sáu | *Chachakka* | — |
| 149 | Đại Kinh Sáu Xứ | *Mahāsaḷāyatanika* | — |
| 150 | Kinh Nagaravinda | *Nagaravindeyya* | — |
| 151 | Kinh Thanh Tịnh Việc Khất Thực | *Piṇḍapātapārisuddhi* | — |
| 152 | Kinh Tu Tập Các Căn | *Indriyabhāvanā* | — |
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
