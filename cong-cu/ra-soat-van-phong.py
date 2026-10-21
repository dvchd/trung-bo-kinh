#!/usr/bin/env python3
"""Rà soát văn phong toàn bộ bản dịch Trung Bộ Kinh.

Khác với ra-soat.py của từng bài (kiểm neo đoạn, ngoặc kép, dấu lửng, từ cấm),
script này quét cả kho để tìm những lỗi máy móc lọt qua kiểm tra từng bài:

  [1] từ ngữ bị cấm và danh xưng sai
  [2] tiếng Anh còn sót trong bản dịch
  [3] ký tự lạ: ngoặc cong, dấu lửng ngoài chú thích, "Ð" thay cho "Đ", tab, NBSP
  [4] lỗi khoảng trắng: hai dấu cách, cách trước dấu câu, cách thừa cuối dòng
  [5] công thức mở đầu và danh hiệu chín phần không nhất quán
  [6] câu lặp nguyên văn bất thường trong cùng một tệp

Chạy: python3 cong-cu/ra-soat-van-phong.py
"""
import os
import re
import sys
from collections import defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BAN = [
    (r'\bnhư thị\b', 'như thị'),
    (r'\bnhất thời\b(?! (?:ấy|bấy|này|đó))', 'nhất thời'),
    (r'\bbất khả tư nghì\b', 'bất khả tư nghì'),
    (r'\bvô lượng vô biên\b', 'vô lượng vô biên'),
    (r'\bchấp trước\b', 'chấp trước'),
    (r'\bPhật giáo đồ\b', 'Phật giáo đồ'),
    (r'\bnhư trên\b', 'như trên'),
    (r'\blược đi\b', 'lược đi'),
    (r'\bnói rằng là\b', 'nói rằng là'),
    (r'\btiền thân là\b', 'tiền thân là'),
]
DANH_XUNG_SAI = [
    (r'Đức Phật', 'Đức Phật'),
    (r'đức Phật', 'đức Phật'),
    (r'\bcác ngươi\b', 'các ngươi'),
    (r'\bchúng mày\b', 'chúng mày'),
]
TIENG_ANH = re.compile(
    r'\b(?:the|and|of|is|are|was|were|with|from|that|this|these|those|for|but|not|'
    r'you|your|they|their|there|which|when|where|how|who|what|have|has|had|will|'
    r'should|would|could|must|might|being|been)\b', re.IGNORECASE)

CHUOI_CHIN_PHAN = (
    'bậc A-la-hán, Chánh đẳng giác, đầy đủ minh và hạnh, bậc Thiện thệ, '
    'bậc thấu hiểu thế gian, bậc tối thượng dẫn dắt những người cần được điều ngự, '
    'bậc thầy của trời và người, bậc Giác ngộ, bậc Thế Tôn'
)

loi = defaultdict(list)


def ghi(nhom, tep, so_dong, mo_ta):
    loi[nhom].append('%s:%d  %s' % (tep, so_dong, mo_ta))


def kiem_tep(duong_dan, tep_tuong_doi, kiem_cong_thuc):
    try:
        noi_dung = open(duong_dan, encoding='utf-8').read()
    except UnicodeDecodeError:
        ghi(3, tep_tuong_doi, 0, 'tệp không phải UTF-8')
        return
    dong_list = noi_dung.split('\n')
    for so, dong in enumerate(dong_list, 1):
        thap = dong.lower()
        # 1. từ cấm, danh xưng sai
        for mau, ten_mau in BAN:
            if re.search(mau, dong, re.IGNORECASE):
                ghi(1, tep_tuong_doi, so, 'từ cấm: "%s"' % ten_mau)
        for mau, ten_mau in DANH_XUNG_SAI:
            if re.search(mau, dong):
                ghi(1, tep_tuong_doi, so, 'danh xưng sai: "%s"' % ten_mau)
        # 2. tiếng Anh
        for m in TIENG_ANH.finditer(dong):
            ghi(2, tep_tuong_doi, so, 'nghi tiếng Anh: "%s"' % m.group(0))
        # 3. ký tự lạ (bỏ qua phần trong [Chú thích: ...])
        ngoai = re.sub(r'\[Chú thích[^\]]*\]', '', dong)
        for ky_tu, ten in (('\u201c', 'ngoặc cong mở'), ('\u201d', 'ngoặc cong đóng'),
                           ('\u2018', 'nháy cong mở'), ('\u2019', 'nháy cong đóng'),
                           ('\u2026', 'dấu lửng'), ('...', 'ba chấm'),
                           ('\u00d0', 'chữ Ð thay cho Đ'), ('\t', 'tab'),
                           ('\u00a0', 'khoảng trắng không ngắt')):
            if ky_tu in ngoai:
                ghi(3, tep_tuong_doi, so, 'ký tự lạ: %s' % ten)
        # 4. khoảng trắng
        if '  ' in dong.strip('\n'):
            ghi(4, tep_tuong_doi, so, 'hai dấu cách liền nhau')
        if re.search(r'\s+[,.;:!?]', dong):
            ghi(4, tep_tuong_doi, so, 'cách trước dấu câu')
        if dong != dong.rstrip():
            ghi(4, tep_tuong_doi, so, 'khoảng trắng thừa cuối dòng')
        # 5. công thức
        if kiem_cong_thuc:
            if 'Chánh Đẳng Giác' in dong:
                ghi(5, tep_tuong_doi, so, 'danh hiệu viết hoa sai: "Chánh Đẳng Giác"')
    # 5b. công thức đầu kinh
    if kiem_cong_thuc:
        so_lan = noi_dung.count('Tôi nghe như vầy.')
        if so_lan != 1:
            ghi(5, tep_tuong_doi, 0, 'câu mở đầu "Tôi nghe như vầy." xuất hiện %d lần' % so_lan)
        if 'Một thuở nọ' not in noi_dung:
            ghi(5, tep_tuong_doi, 0, 'thiếu "Một thuở nọ"')
        # các biến thể của danh hiệu chín phần
        for m in re.finditer(r'bậc A-la-hán, Chánh [đĐ]ẳng [gG]iác[^.\n]{0,400}', noi_dung):
            doan = m.group(0).strip()
            if 'Thiện thệ' not in doan:
                continue
            if not doan.startswith(CHUOI_CHIN_PHAN):
                ghi(5, tep_tuong_doi, noi_dung[:m.start()].count('\n') + 1,
                    'danh hiệu lệch: "%s"' % doan[:90])

def main():
    so_tep = 0
    for ten_thu_muc in sorted(os.listdir(GOC)):
        if not re.match(r'^\d{3}-', ten_thu_muc):
            continue
        thu_muc = os.path.join(GOC, ten_thu_muc)
        if not os.path.isdir(thu_muc):
            continue
        ban_dich = os.path.join(thu_muc, 'ban-dich')
        if os.path.isdir(ban_dich):
            for ten_tep in sorted(os.listdir(ban_dich)):
                if ten_tep.endswith('.md'):
                    kiem_tep(os.path.join(ban_dich, ten_tep),
                             '%s/ban-dich/%s' % (ten_thu_muc, ten_tep), False)
                    so_tep += 1
        for ten_tep in sorted(os.listdir(thu_muc)):
            if ten_tep.startswith('Kinh-') and ten_tep.endswith('.md'):
                kiem_tep(os.path.join(thu_muc, ten_tep),
                         '%s/%s' % (ten_thu_muc, ten_tep), True)
                so_tep += 1

    tieu_de = {
        1: 'Từ ngữ bị cấm và danh xưng sai',
        2: 'Tiếng Anh còn sót',
        3: 'Ký tự lạ',
        4: 'Lỗi khoảng trắng',
        5: 'Công thức không nhất quán',
    }
    tong = 0
    for nhom in sorted(loi):
        ds = loi[nhom]
        tong += len(ds)
        print('\n[%d] %s — %d chỗ' % (nhom, tieu_de[nhom], len(ds)))
        for d in ds[:60]:
            print('   ' + d)
        if len(ds) > 60:
            print('   … và %d chỗ nữa' % (len(ds) - 60))
    print('\nĐã quét %d tệp.' % so_tep)
    print('TONG VAN DE: %d' % tong)
    return 0 if tong == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
