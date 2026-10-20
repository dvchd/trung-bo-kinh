# Hướng dẫn dịch — Kinh Căn Bản Pháp Môn (*Mūlapariyāya Sutta*, Trung Bộ Kinh MN 1)

> Chuẩn chung bắt buộc: [`../../HUONG-DAN-CHUNG.md`](../../HUONG-DAN-CHUNG.md) — quy ước câu chữ,
> xưng hô, chú thích, số hiệu đoạn, từ cấm. Tệp này **chỉ ghi những quyết định riêng của bài**:
> tên nhân vật, thuật ngữ đặc thù, những chỗ dễ dịch sai.

---

## 1. Nội dung bài này

Tại rừng Subhaga gần Ukkaṭṭhā, Đức Thế Tôn dạy các tỳ-kheo "pháp môn về cội nguồn của mọi pháp". Bài
kinh không kể chuyện: nó lần lượt đặt hai mươi bốn đối tượng nhận thức — bốn đại, các loại chúng sinh
và chư thiên, bốn xứ thiền vô sắc, sáu đối tượng của giác quan, tính nhất thể, tính đa dạng, tất cả và
Niết-bàn — trước bốn hạng người. Với mỗi đối tượng, phàm phu nhận thức rồi tưởng tượng và thích thú;
bậc hữu học biết trực tiếp nhưng không tưởng tượng; bậc A-la-hán cũng vậy, không còn tham sân si; Như
Lai thấy rõ thích thú là cội nguồn của khổ. Kết thúc, các tỳ-kheo nghe xong không hoan hỷ.

## 2. Nhân vật

| Pali | Dịch trong bài | Ghi chú (lần đầu xuất hiện) |
|---|---|---|
| Bhagavā | Đức Thế Tôn | mn1:1.2 |
| bhikkhū | các tỳ-kheo | mn1:1.3 |
| puthujjana | phàm phu | mn1:3.1 |
| sekkha | bậc hữu học | mn1:27.1 |
| arahant | bậc A-la-hán | mn1:51.1 |
| Tathāgata | Như Lai | mn1:147.1 |

## 3. Thuật ngữ riêng của bài

| Pali | Dịch chuẩn | Ghi chú |
|---|---|---|
| sañjānāti | nhận thức | phân biệt đối tượng bằng tri giác và khái niệm |
| maññati | tưởng tượng | thêm "của tôi", ngã mạn, tà kiến vào đối tượng |
| abhinandati | thích thú | ưa thích, bám vào |
| abhijānāti | biết trực tiếp | hiểu bằng trí tuệ, không qua suy luận |
| pariññāta | hiểu biết trọn vẹn | đã liễu tri |
| nandī | thích thú | ở cuối kinh: cội nguồn của khổ |
| Nibbāna | Niết-bàn | vẫn nằm trong danh sách "mọi pháp" |

## 4. Chỗ dễ dịch sai

- **Các đoạn viết tắt**: từ mn1:28.1 đến mn1:49.1, rồi lặp lại ở các vòng sau, Pali chỉ ghi "Āpaṁ
  …pe…" (nước, v.v.). Bản dịch viết đủ cả bốn câu của khuôn cho từng đối tượng, đúng như cách bản Pali
  muốn người tụng đọc hiểu.
- **Năm cách tưởng tượng**: "pathaviṁ maññati / pathaviyā maññati / pathavito maññati / pathaviṁ meti
  maññati / pathaviṁ abhinandati" — lần lượt là coi là, coi ở trong, coi phát xuất từ, coi là của tôi,
  và ưa thích. Không được gộp cả năm thành một động từ.
- **Câu kết mn1:194.9**: "Na te bhikkhū bhagavato bhāsitaṁ abhinandunti" — các tỳ-kheo **không hoan hỷ**,
  không phải "không hiểu". Đây là chi tiết cố ý của kinh, đừng làm dịu đi.
- **Niết-bàn trong danh sách**: Niết-bàn được nêu như một đối tượng nhận thức, không phải một ngoại lệ
  siêu hình; phàm phu cũng "nhận thức Niết-bàn là Niết-bàn" rồi tưởng tượng về nó.

## 5. Kiểm tra trước khi commit

```bash
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-Can-Ban-Phap-Mon.md
python3 ra-soat.py
python3 tien-do.py
```

`kiem-tra-marker.py` và `ra-soat.py` phải in `DAT`, `tien-do.py` phải báo không thiếu đoạn nào.
