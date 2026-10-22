# Dành cho người đọc kỹ thuật và người đóng góp

Trang này dành cho người muốn **sửa bản dịch, kiểm tra, hoặc dựng thêm bài** — không cần đọc nếu bạn
chỉ muốn đọc kinh. Quay lại [README](README.md) để bắt đầu đọc.

---

## 1. Kho này được tổ chức thế nào

```
.
├── README.md                  ← trang cho người đọc
├── DONG-GOP.md                ← trang này
├── LICENSE
├── HUONG-DAN-CHUNG.md         ← quy ước dịch chung cho cả 152 bài
├── so-tay/                    ← (bổ sung sau khi dịch xong phần lớn)
├── cong-cu/                   ← script cấp kho
└── 001-kinh-can-ban-phap-mon/ … 152-kinh-tu-tap-cac-can/
```

Mỗi thư mục bài kinh:

| Mục | Nội dung |
|---|---|
| `Kinh-*.md` | **Bản dịch hoàn chỉnh** — tệp duy nhất người đọc cần |
| `README.md` | Giới thiệu bài, bối cảnh, liên kết tới các bài khác |
| `ban-dich/` | Bản dịch chia theo đoạn, mỗi đoạn một tệp — **nguồn của bản hoàn chỉnh** |
| `nguon/` | Pali, bản dịch Anh của Sujato và chú thích, tách theo đoạn |
| `ghep.py` | Ghép `ban-dich/` thành `Kinh-*.md` |
| `tao-muc-luc.py` | Chèn mục lục có anchor kiểu GitHub vào bản hoàn chỉnh |
| `kiem-tra-marker.py` | Kiểm tra đủ và đúng thứ tự số hiệu đoạn |
| `ra-soat.py` | Rà soát toàn bài: số hiệu đoạn, thuật ngữ, định dạng |
| `tien-do.py` | Báo cáo tiến độ dịch |
| `ra-soat/` | Báo cáo rà soát của từng vòng |

Nguyên tắc: **`ban-dich/` là nguồn, `Kinh-*.md` là sản phẩm.** Không sửa trực tiếp tệp hoàn chỉnh —
sửa trong `ban-dich/` rồi ghép lại, nếu không lần ghép sau sẽ ghi đè.

## 2. Sửa một câu

```bash
cd 02-kinh-sa-mon-qua/
# 1. tìm câu cần sửa bằng số hiệu đoạn
grep -rn "mn2:14.3" ban-dich/
# 2. sửa tệp tương ứng trong ban-dich/
# 3. ghép lại và chèn mục lục
python3 ghep.py && python3 tao-muc-luc.py
# 4. kiểm tra
python3 kiem-tra-marker.py && python3 ra-soat.py
```

`ra-soat.py` phải in ra `KET LUAN: DAT` trước khi commit.

## 3. Bộ kiểm tra cấp kho

| Script | Kiểm gì |
|---|---|
| `python3 cong-cu/ra-soat-toan-bo.py` | 753 tệp: đủ neo đoạn, ngoặc kép cân và không cong, từ bị cấm, dấu lửng ngoài chú thích |
| `python3 cong-cu/ra-soat-van-phong.py` | 1057 tệp: văn phong, tiếng Anh sót, ký tự lạ, danh hiệu chín phần lệch dạng |
| `python3 cong-cu/ra-soat-cong-thuc.py` | báo cáo đoạn Pali đang được dịch khác nhau giữa các bài |

Kiểm tra riêng từng bài: chạy `ra-soat.py` trong thư mục bài đó. Hiện **152/152 bài đạt**.

## 4. Quy ước dịch

Đọc [`HUONG-DAN-CHUNG.md`](HUONG-DAN-CHUNG.md) trước khi sửa bất cứ câu nào. Những điểm dễ vi phạm nhất:

- Người kể chuyện luôn là **"Đức Thế Tôn"**, không dùng "Đức Phật" trong lời kể.
- Không dùng: *như thị, nhất thời, bất khả tư nghì, vô lượng vô biên, chấp trước, Phật giáo đồ, như
  trên, lược đi, nói rằng là, tiền thân là*.
- `sīla` = **giới**, `paññā` = **tuệ** — không thay bằng "giới hạnh"/"trí tuệ" tùy chỗ.
- Chín danh hiệu của Đức Thế Tôn phải đúng **một dạng** trong cả 152 bài.
- Chỗ Pali viết tắt bằng *peyyāla* (`…pe…`) thì **phải dịch mở rộng**, không giữ dấu lược.

## 5. Dựng một bài mới

```bash
python3 cong-cu/tao-bai.py 35
```

Script tải dữ liệu từ SuttaCentral, dựng thư mục `35-…`, sinh các tệp khung và script. Sau đó làm theo
`HUONG-DAN-DICH.md` trong thư mục vừa tạo.

## 6. Đóng góp

- **Báo lỗi dịch**: mở issue, ghi số hiệu đoạn (`mn4:12.3`) và câu hiện tại.
- **Đề nghị cách dịch khác**: kèm lý do và, nếu có, chỗ tương ứng trong bản Pali/Anh ở `nguon/`.
- **Bản dịch phái sinh**: được phép không điều kiện — bản dịch thuộc CC0, không bắt buộc ghi nguồn.

## 7. Giấy phép

- Bản dịch tiếng Việt: **CC0 1.0** (phạm vi công cộng) — xem [`LICENSE`](LICENSE).
- Mã nguồn (các tệp `.py`): **MIT**.
- Nguyên bản Pali: phạm vi công cộng.
- Bản dịch tiếng Anh của Bhikkhu Sujato: CC0.

## 8. Quy ước viết

- **Commit message viết tiếng Việt có dấu**, ví dụ: `Thêm 13: bảng từ Hán-Việt`, không viết
  `Them 13: bang tu Han-Viet`. Lịch sử commit trước đây đã được sửa lại cho đúng quy ước này.
- **Tên tệp và tên thư mục giữ ASCII không dấu** (`01-kinh-pham-vong`, `Kinh-Pham-Vong.md`) để đường
  dẫn ổn định trên mọi hệ điều hành và mọi trình duyệt. Đây là lựa chọn có chủ ý, không phải lỗi.
- **Nội dung trong tệp `.md` phải có dấu đầy đủ** — bản dịch, sổ tay, README. Bộ kiểm tra không tự
  phát hiện được lỗi này, nên người sửa phải tự đọc lại.
- **Chú thích trong tệp `.py` cũng viết có dấu.** Riêng dòng in ra màn hình (`print`) giữ ASCII
  không dấu (`KET LUAN: DAT`) để máy đọc được và không lỗi mã hoá khi chuyển hướng output.
