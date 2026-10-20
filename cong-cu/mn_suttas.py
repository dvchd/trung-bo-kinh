#!/usr/bin/env python3
"""Bảng 152 bài Trung Bộ Kinh: số, tên Việt, tên Pali."""
import re
import unicodedata

# (số bài, tên hiển thị trong bản dịch, tên Pali không kèm "sutta")
TUPLES = [
    (1, 'Kinh Căn Bản Pháp Môn', 'Mūlapariyāya'),
    (2, 'Kinh Tất Cả Lậu Hoặc', 'Sabbāsava'),
    (3, 'Kinh Người Thừa Kế Pháp', 'Dhammadāyāda'),
    (4, 'Kinh Sợ Hãi và Kinh Hoàng', 'Bhayabherava'),
    (5, 'Kinh Không Uế Nhiễm', 'Anaṅgaṇa'),
    (6, 'Kinh Ước Muốn', 'Ākaṅkheyya'),
    (7, 'Kinh Ví Dụ Tấm Vải', 'Vatthūpama'),
    (8, 'Kinh Loại Bỏ', 'Sallekha'),
    (9, 'Kinh Chánh Kiến', 'Sammādiṭṭhi'),
    (10, 'Kinh Niệm Xứ', 'Satipaṭṭhāna'),
    (11, 'Tiểu Kinh Sư Tử Hống', 'Cūḷasīhanāda'),
    (12, 'Đại Kinh Sư Tử Hống', 'Mahāsīhanāda'),
    (13, 'Đại Kinh Khổ Uẩn', 'Mahādukkhakkhandha'),
    (14, 'Tiểu Kinh Khổ Uẩn', 'Cūḷadukkhakkhandha'),
    (15, 'Kinh Suy Đoán', 'Anumāna'),
    (16, 'Kinh Tâm Hoang Vu', 'Cetokhila'),
    (17, 'Kinh Khu Rừng', 'Vanapattha'),
    (18, 'Kinh Mật Hoàn', 'Madhupiṇḍika'),
    (19, 'Kinh Hai Loại Tầm', 'Dvedhāvitakka'),
    (20, 'Kinh An Trú Tầm', 'Vitakkasaṇṭhāna'),
    (21, 'Kinh Ví Dụ Cái Cưa', 'Kakacūpama'),
    (22, 'Kinh Ví Dụ Con Rắn', 'Alagaddūpama'),
    (23, 'Kinh Tổ Kiến', 'Vammika'),
    (24, 'Kinh Cỗ Xe', 'Rathavinīta'),
    (25, 'Kinh Mồi Nhử', 'Nivāpa'),
    (26, 'Kinh Thánh Cầu', 'Ariyapariyesanā'),
    (27, 'Tiểu Kinh Dấu Chân Voi', 'Cūḷahatthipadopama'),
    (28, 'Đại Kinh Dấu Chân Voi', 'Mahāhatthipadopama'),
    (29, 'Đại Kinh Lõi Cây', 'Mahāsāropama'),
    (30, 'Tiểu Kinh Lõi Cây', 'Cūḷasāropama'),
    (31, 'Tiểu Kinh Rừng Gosiṅga', 'Cūḷagosiṅga'),
    (32, 'Đại Kinh Rừng Gosiṅga', 'Mahāgosiṅga'),
    (33, 'Đại Kinh Người Chăn Bò', 'Mahāgopālaka'),
    (34, 'Tiểu Kinh Người Chăn Bò', 'Cūḷagopālaka'),
    (35, 'Tiểu Kinh Saccaka', 'Cūḷasaccaka'),
    (36, 'Đại Kinh Saccaka', 'Mahāsaccaka'),
    (37, 'Tiểu Kinh Đoạn Tận Ái', 'Cūḷataṇhāsaṅkhaya'),
    (38, 'Đại Kinh Đoạn Tận Ái', 'Mahātaṇhāsaṅkhaya'),
    (39, 'Đại Kinh Assapura', 'Mahāassapura'),
    (40, 'Tiểu Kinh Assapura', 'Cūḷaassapura'),
    (41, 'Kinh Sāleyyaka', 'Sāleyyaka'),
    (42, 'Kinh Verañjaka', 'Verañjaka'),
    (43, 'Đại Kinh Phương Quảng', 'Mahāvedalla'),
    (44, 'Tiểu Kinh Phương Quảng', 'Cūḷavedalla'),
    (45, 'Tiểu Kinh Thọ Trì Pháp', 'Cūḷadhammasamādāna'),
    (46, 'Đại Kinh Thọ Trì Pháp', 'Mahādhammasamādāna'),
    (47, 'Kinh Tư Sát', 'Vīmaṃsaka'),
    (48, 'Kinh Kosambī', 'Kosambiya'),
    (49, 'Kinh Phạm Thiên Mời', 'Brahmanimantanika'),
    (50, 'Kinh Sự Khiển Trách Ma', 'Māratajjanīya'),
    (51, 'Kinh Kandaraka', 'Kandaraka'),
    (52, 'Kinh Aṭṭhakanāgara', 'Aṭṭhakanāgara'),
    (53, 'Kinh Hữu Học', 'Sekha'),
    (54, 'Kinh Potaliya', 'Potaliya'),
    (55, 'Kinh Jīvaka', 'Jīvaka'),
    (56, 'Kinh Upāli', 'Upāli'),
    (57, 'Kinh Thực Hành Chó', 'Kukkuravatika'),
    (58, 'Kinh Abhaya', 'Abhayarājakumāra'),
    (59, 'Kinh Nhiều Loại Cảm Thọ', 'Bahuvedanīya'),
    (60, 'Kinh Không Thể Tranh Cãi', 'Apaṇṇaka'),
    (61, 'Kinh Dạy Rāhula', 'Rāhulovāda'),
    (62, 'Đại Kinh Dạy Rāhula', 'Mahārāhulovāda'),
    (63, 'Tiểu Kinh Māluṅkya', 'Cūḷamālukya'),
    (64, 'Đại Kinh Māluṅkya', 'Mahāmālukya'),
    (65, 'Kinh Bhaddāli', 'Bhaddāli'),
    (66, 'Kinh Ví Dụ Con Chim Cút', 'Laṭukikopama'),
    (67, 'Kinh Cātumā', 'Cātuma'),
    (68, 'Kinh Naḷakapāna', 'Naḷakapāna'),
    (69, 'Kinh Gulissāni', 'Gulissāni'),
    (70, 'Kinh Kīṭāgiri', 'Kīṭāgiri'),
    (71, 'Kinh Vacchagotta về Tam Minh', 'Tevijjavacchagotta'),
    (72, 'Kinh Vacchagotta về Lửa', 'Aggivacchagotta'),
    (73, 'Đại Kinh Vacchagotta', 'Mahāvacchagotta'),
    (74, 'Kinh Dīghanakha', 'Dīghanakha'),
    (75, 'Kinh Māgaṇḍiya', 'Māgaṇḍiya'),
    (76, 'Kinh Sandaka', 'Sandaka'),
    (77, 'Đại Kinh Sakuludāyi', 'Mahāsakuludāyi'),
    (78, 'Kinh Sa-môn Muṇḍika', 'Samaṇamuṇḍika'),
    (79, 'Tiểu Kinh Sakuludāyi', 'Cūḷasakuludāyi'),
    (80, 'Kinh Vekhanasa', 'Vekhanasa'),
    (81, 'Kinh Ghaṭikāra', 'Ghaṭikāra'),
    (82, 'Kinh Raṭṭhapāla', 'Raṭṭhapāla'),
    (83, 'Kinh Makhādeva', 'Makhādeva'),
    (84, 'Kinh Madhurā', 'Madhura'),
    (85, 'Kinh Bodhirājakumāra', 'Bodhirājakumāra'),
    (86, 'Kinh Aṅgulimāla', 'Aṅgulimāla'),
    (87, 'Kinh Sinh Từ Người Thương', 'Piyajātika'),
    (88, 'Kinh Bāhitika', 'Bāhitika'),
    (89, 'Kinh Bảo Tháp Pháp', 'Dhammacetiya'),
    (90, 'Kinh Kaṇṇakatthala', 'Kaṇṇakatthala'),
    (91, 'Kinh Brahmāyu', 'Brahmāyu'),
    (92, 'Kinh Sela', 'Sela'),
    (93, 'Kinh Assalāyana', 'Assalāyana'),
    (94, 'Kinh Ghoṭamukha', 'Ghoṭamukha'),
    (95, 'Kinh Caṅkī', 'Caṅkī'),
    (96, 'Kinh Esukārī', 'Esukārī'),
    (97, 'Kinh Dhānañjāni', 'Dhānañjāni'),
    (98, 'Kinh Vāseṭṭha', 'Vāseṭṭha'),
    (99, 'Kinh Subha', 'Subha'),
    (100, 'Kinh Saṅgārava', 'Saṅgārava'),
    (101, 'Kinh Devadaha', 'Devadaha'),
    (102, 'Kinh Năm và Ba', 'Pañcattaya'),
    (103, 'Kinh Như Thế Nào', 'Kinti'),
    (104, 'Kinh Sāmagāma', 'Sāmagāma'),
    (105, 'Kinh Sunakkhatta', 'Sunakkhatta'),
    (106, 'Kinh Về Bất Động', 'Āneñjasappāya'),
    (107, 'Kinh Gaṇakamoggallāna', 'Gaṇakamoggallāna'),
    (108, 'Kinh Gopaka', 'Gopakamoggallāna'),
    (109, 'Đại Kinh Trăng Tròn', 'Mahāpuṇṇama'),
    (110, 'Tiểu Kinh Trăng Tròn', 'Cūḷapuṇṇama'),
    (111, 'Kinh Tùy Quán', 'Anupada'),
    (112, 'Kinh Sáu Thanh Tịnh', 'Chabbisodhana'),
    (113, 'Kinh Con Người Chân Thật', 'Sappurisa'),
    (114, 'Kinh Nên Thân Cận và Không Nên Thân Cận', 'Sevitabbāsevitabba'),
    (115, 'Kinh Nhiều Giới', 'Bahudhātuka'),
    (116, 'Kinh Isigili', 'Isigili'),
    (117, 'Đại Kinh Bốn Mươi', 'Mahācattārīsaka'),
    (118, 'Kinh Niệm Hơi Thở', 'Ānāpānassati'),
    (119, 'Kinh Niệm Thân', 'Kāyagatāsati'),
    (120, 'Kinh Tái Sinh Theo Hành', 'Saṅkhārupapatti'),
    (121, 'Tiểu Kinh Không', 'Cūḷasuññata'),
    (122, 'Đại Kinh Không', 'Mahāsuññata'),
    (123, 'Kinh Hy Hữu và Kỳ Diệu', 'Acchariyaabbhuta'),
    (124, 'Kinh Bākula', 'Bākula'),
    (125, 'Kinh Địa Vị Người Đã Điều Phục', 'Dantabhūmi'),
    (126, 'Kinh Bhūmija', 'Bhūmija'),
    (127, 'Kinh Anuruddha', 'Anuruddha'),
    (128, 'Kinh Ô Nhiễm', 'Upakkilesa'),
    (129, 'Kinh Kẻ Ngu và Người Trí', 'Bālapaṇḍita'),
    (130, 'Kinh Sứ Giả Của Thần Chết', 'Devadūta'),
    (131, 'Kinh Một Đêm Lành', 'Bhaddekaratta'),
    (132, 'Kinh Ānanda Một Đêm Lành', 'Ānandabhaddekaratta'),
    (133, 'Đại Kinh Kaccāna Một Đêm Lành', 'Mahākaccānabhaddekaratta'),
    (134, 'Kinh Lomasakaṅgiya', 'Lomasakaṅgiya'),
    (135, 'Tiểu Kinh Phân Biệt Nghiệp', 'Cūḷakammavibhaṅga'),
    (136, 'Đại Kinh Phân Biệt Nghiệp', 'Mahākammavibhaṅga'),
    (137, 'Kinh Phân Biệt Sáu Xứ', 'Salāyatanavibhaṅga'),
    (138, 'Kinh Phân Biệt Tóm Tắt', 'Uddesavibhaṅga'),
    (139, 'Kinh Phân Biệt Không Tranh Cãi', 'Araṇavibhaṅga'),
    (140, 'Kinh Phân Biệt Giới', 'Dhātuvibhaṅga'),
    (141, 'Kinh Phân Biệt Sự Thật', 'Saccavibhaṅga'),
    (142, 'Kinh Phân Biệt Cúng Dường', 'Dakkhiṇāvibhaṅga'),
    (143, 'Kinh Dạy Anāthapiṇḍika', 'Anāthapiṇḍikovāda'),
    (144, 'Kinh Dạy Channa', 'Channovāda'),
    (145, 'Kinh Dạy Puṇṇa', 'Puṇṇovāda'),
    (146, 'Kinh Dạy Nandaka', 'Nandakovāda'),
    (147, 'Tiểu Kinh Dạy Rāhula', 'Cūḷarāhulovāda'),
    (148, 'Kinh Sáu Sáu', 'Chachakka'),
    (149, 'Đại Kinh Sáu Xứ', 'Mahāsaḷāyatanika'),
    (150, 'Kinh Nagaravinda', 'Nagaravindeyya'),
    (151, 'Kinh Thanh Tịnh Việc Khất Thực', 'Piṇḍapātapārisuddhi'),
    (152, 'Kinh Tu Tập Các Căn', 'Indriyabhāvanā'),
]

assert len(TUPLES) == 152 and [n for n, _, _ in TUPLES] == list(range(1, 153))


def bo_dau(s):
    s = s.replace('Đ', 'D').replace('đ', 'd')
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()


def slug(ten_kinh):
    """'Kinh Căn Bản Pháp Môn' -> 'can-ban-phap-mon'."""
    s = ten_kinh
    if s.startswith('Đại Kinh '):
        s = 'dai ' + s[len('Đại Kinh '):]
    elif s.startswith('Tiểu Kinh '):
        s = 'tieu ' + s[len('Tiểu Kinh '):]
    elif s.startswith('Kinh '):
        s = s[len('Kinh '):]
    s = bo_dau(s).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def thong_tin(n):
    """Trả về dict: so, ten, pali, slug, thu_muc, ten_tep."""
    so, ten, pali = TUPLES[n - 1]
    sl = slug(ten)
    return {
        'so': so,
        'ten': ten,
        'pali': pali,
        'slug': sl,
        'thu_muc': '%03d-kinh-%s' % (so, sl),
        'ten_tep': 'Kinh-' + '-'.join(w.capitalize() for w in sl.split('-')),
    }


if __name__ == '__main__':
    import sys
    for n in (1, 10, 152):
        print(thong_tin(n))
    if len(sys.argv) > 1:
        for n in range(1, 153):
            print(n, thong_tin(n)['thu_muc'], '|', thong_tin(n)['ten'])
