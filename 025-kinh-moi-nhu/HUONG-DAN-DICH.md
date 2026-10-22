# Hướng dẫn dịch — Kinh Mồi Nhử (*Nivāpa Sutta*, Trung Bộ Kinh MN 25)

> Chuẩn chung bắt buộc: [`../../HUONG-DAN-CHUNG.md`](../../HUONG-DAN-CHUNG.md) — quy ước câu chữ,
> xưng hô, chú thích, số hiệu đoạn, từ cấm. Tệp này **chỉ ghi những quyết định riêng của bài**:
> tên nhân vật, thuật ngữ đặc thù, những chỗ dễ dịch sai.

---

## 1. Nội dung bài này

Đức Thế Tôn dùng hình ảnh người gieo mồi (Māra) và bốn bầy nai để nói về bốn cách người tu hành đối diện với cám dỗ. Bầy thứ nhất ăn mồi nên bị bắt; bầy thứ hai bỏ mồi vào rừng sâu nhưng khi cỏ cạn nước khô thì quay lại; bầy thứ ba dựng hang sát bên chỗ mồi, quan sát mà không ăn, nhưng hang bị người gieo mồi tìm thấy nên vẫn không thoát khỏi tay ông ta; bầy thứ tư đi vào vùng người gieo mồi không thể chạm tới. Bốn bầy ứng với bốn hạng sa-môn, bà-la-môn. Bài kết ở lời dặn về lãnh địa của bậc Thánh, nơi các bậc đoạn tận lậu hoặc an trú.

## 2. Nhân vật

| Pali | Dịch trong bài | Ghi chú (lần đầu xuất hiện) |
|---|---|---|
| Māra | Māra | Người gieo mồi, kẻ giăng bẫy |
| Nivāpa | mồi, chỗ mồi | Mồi do người gieo mồi rải xuống |
| migajāta | loài nai | Cũng có thể hiểu rộng là thú rừng |
| nevāpika | người gieo mồi | Ẩn dụ cho Māra |

## 3. Thuật ngữ riêng của bài

| Pali | Dịch chuẩn | Ghi chú |
|---|---|---|
| nivāpa | mồi, chỗ mồi | Đồng thời là ẩn dụ cho năm dục công đức |
| nevāpika | người gieo mồi | Māra |
| anāvāsa | chỗ không nương | Vùng bậc Thánh an trú |
| āsaya | hang ổ, chỗ nương | Trong bài chỉ chỗ nai dựng hang |

## 4. Chỗ dễ dịch sai

- Chữ nivāpa vừa là mồi cho thú vừa là ẩn dụ cho năm dục công đức; phải giữ cả hai nghĩa trong chú thích.
- "Mồi thế gian" (lokāmisa) là một cụm riêng, không phải "mồi ở đời" theo nghĩa thông thường.
- Các đoạn 5.15–5.16 là lời của bầy nai thứ hai, cần mở và đóng ngoặc kép đúng; bản gốc bị cắt theo đoạn nên dễ sót dấu.
- "Người gieo mồi và đoàn tùy tùng" là Māra và quân của ông, không phải thợ săn thật.
- Các câu lặp "khi say sưa, sinh phóng dật…" phải giữ nguyên chuỗi nhân quả ở cả bốn lần kể.

## 5. Kiểm tra trước khi commit

```bash
python3 ghep.py && python3 tao-muc-luc.py
python3 kiem-tra-marker.py Kinh-Kinh-Moi-Nhu.md
python3 ra-soat.py
python3 tien-do.py
```

`kiem-tra-marker.py` và `ra-soat.py` phải in `DAT`, `tien-do.py` phải báo không thiếu đoạn nào.
