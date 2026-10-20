# Hướng dẫn dịch — Kinh Māgaṇḍiya (*Māgaṇḍiya Sutta*, Trung Bộ Kinh MN 75)

> Chuẩn chung bắt buộc: [`../../HUONG-DAN-CHUNG.md`](../../HUONG-DAN-CHUNG.md) — quy ước câu chữ,
> xưng hô, chú thích, số hiệu đoạn, từ cấm. Tệp này **chỉ ghi những quyết định riêng của bài**:
> tên nhân vật, thuật ngữ đặc thù, những chỗ dễ dịch sai.

---

## 1. Nội dung bài này

Du sĩ Māgaṇḍiya, người tu khổ hạnh, đến nhà lửa của một bà-la-môn dòng Bhāradvāja, thấy chỗ nghỉ của Đức Thế Tôn và buông lời sỉ nhục Ngài là kẻ giết thai nhi. Đức Thế Tôn đến gặp, hỏi lại, rồi giảng rằng sáu giác quan ưa thích đối tượng của chúng, và người tu cần điều phục sự ưa thích ấy; Ngài kể lại đời sống dục lạc của mình trước khi xuất gia để cho thấy mình đã hiểu rõ năm dục công đức. Bài kinh dùng hình ảnh người bệnh phong gãi vết thương, người bệnh bị lôi đến hố than và người mù bẩm sinh tìm tấm vải trắng để phá tan hiểu lầm của Māgaṇḍiya về "sức khỏe" và "Niết-bàn". Cuối cùng Māgaṇḍiya xin xuất gia, chịu bốn tháng thử thách và chứng quả A-la-hán.

## 2. Nhân vật

| Pali | Dịch trong bài | Ghi chú (lần đầu xuất hiện) |
|---|---|---|
| Māgaṇḍiya | Māgaṇḍiya | Du sĩ tu khổ hạnh, sau xuất gia và chứng quả A-la-hán |
| Bhāradvāja | Bhāradvāja | Dòng họ bà-la-môn chủ nhà lửa |
| Kammāsadhamma | Kammāsadhamma | Thị trấn xứ Kuru |
| āvuso | này hiền giả | Cách Māgaṇḍiya gọi Đức Thế Tôn, không dùng "bạch Thế Tôn" |

## 3. Thuật ngữ riêng của bài

| Pali | Dịch chuẩn | Ghi chú |
|---|---|---|
| kāmaguṇa | năm dục công đức | Năm thứ đáng ưa do mắt, tai, mũi, lưỡi, thân đem lại |
| ārogyaparamā | sức khỏe là lợi ích tối thượng | Câu kệ Māgaṇḍiya hiểu lầm là sức khỏe thân xác |
| upadhi | thân này, cơ sở tái sinh | Trong bài chỉ nền tảng của khổ |
| cātumāsāni | bốn tháng thử thách | Thủ tục cho người từng tu giáo phái khác |

## 4. Chỗ dễ dịch sai

- "Kẻ giết thai nhi" (moghapurisa) là lời sỉ nhục của Māgaṇḍiya, không phải nhận định của người kể; phải đặt trong ngoặc kép của lời dẫn.
- "Sức khỏe là lợi ích tối thượng" (ārogyaparamā lābhā) là câu kệ Đức Thế Tôn nói về sức khỏe của tâm, không phải lời khen thân xác; Māgaṇḍiya hiểu sai và bài kinh khai thác chính chỗ hiểu sai ấy.
- "Āvuso" của Māgaṇḍiya phải dịch "này hiền giả", không "bạch Thế Tôn".
- Các đoạn 8.x bị cắt giữa lời nói: ngoặc kép phải mở ở đoạn trước và đóng ở đoạn sau, mỗi tệp vẫn chẵn dấu.
- "Vatta" trong câu về bốn tháng thử thách là thủ tục, không phải "hạnh nguyện".

## 5. Kiểm tra trước khi commit

```bash
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-Magandiya.md
python3 ra-soat.py
python3 tien-do.py
```

`kiem-tra-marker.py` và `ra-soat.py` phải in `DAT`, `tien-do.py` phải báo không thiếu đoạn nào.
