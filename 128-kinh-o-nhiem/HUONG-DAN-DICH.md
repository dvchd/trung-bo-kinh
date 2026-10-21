# Hướng dẫn dịch — Kinh Ô Nhiễm (*Upakkilesa Sutta*, Trung Bộ Kinh MN 128)

> Chuẩn chung bắt buộc: [`../../HUONG-DAN-CHUNG.md`](../../HUONG-DAN-CHUNG.md) — quy ước câu chữ,
> xưng hô, chú thích, số hiệu đoạn, từ cấm. Tệp này **chỉ ghi những quyết định riêng của bài**:
> tên nhân vật, thuật ngữ đặc thù, những chỗ dễ dịch sai.

---

## 1. Nội dung bài này

Các tỳ-kheo ở Kosambī tranh chấp nên Đức Thế Tôn rời đi, đến công viên Pācīnavaṁsa thăm ba vị Anuruddha, Nandiya và Kimbila đang tu hòa hợp. Ngài kể kinh nghiệm tu tập của chính mình: ánh sáng và sự thấy các sắc hiện ra rồi mất, và chỉ ra mười một thứ làm ô nhiễm tâm. Sau khi vượt qua từng thứ, Ngài dạy về giải thoát vô lượng và kết ở lời khen ba vị sống hòa hợp.

## 2. Nhân vật

| Pali | Dịch trong bài | Ghi chú (lần đầu xuất hiện) |
|---|---|---|
| Anuruddha | Anuruddha | Một trong ba vị đang tu ở Pācīnavaṁsa |
| Nandiya | Nandiya | Cùng tu với Anuruddha |
| Kimbila | Kimbila | Cùng tu với Anuruddha |
| Kosambī | Kosambī | Nơi các tỳ-kheo tranh chấp |
| Pācīnavaṁsa | Pācīnavaṁsa | Công viên phía đông, nơi ba vị trú |

## 3. Thuật ngữ riêng của bài

| Pali | Dịch chuẩn | Ghi chú |
|---|---|---|
| upakkilesa | ô nhiễm | Mười một thứ làm tâm ô nhiễm trong khi tu định |
| obhāsa | ánh sáng | Hiện ra khi định mạnh, không phải mục tiêu |
| nimitta | tướng | Ở đây chỉ dấu hiệu của định |
| appamāṇa cetovimutti | giải thoát tâm vô lượng | Bốn tâm vô lượng |

## 4. Chỗ dễ dịch sai

- Mười một ô nhiễm phải giữ đúng danh sách và đúng thứ tự lặp lại; bản Pali lặp công thức cho từng thứ.
- "Nimitta" trong bài là dấu hiệu của định, không phải đối tượng thiền; đừng dịch thành "đề mục".
- "Tinh tấn quá mức" và "tinh tấn quá lơi" là hai cực đối nhau, phải dịch song song.
- Ba vị Anuruddha, Nandiya, Kimbila tu chung; đại từ "chúng tôi" chỉ ba vị, không phải tất cả tỳ-kheo.
- Các đoạn kệ về sống một mình phải giữ nguyên thể thơ, không nhập vào văn xuôi.

## 5. Kiểm tra trước khi commit

```bash
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-Kinh-O-Nhiem.md
python3 ra-soat.py
python3 tien-do.py
```

`kiem-tra-marker.py` và `ra-soat.py` phải in `DAT`, `tien-do.py` phải báo không thiếu đoạn nào.
