#!/usr/bin/env python3
"""Sinh mục lục 152 bài trong README gốc, chia theo ba phần và mười lăm phẩm."""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mn_suttas import thong_tin  # noqa: E402

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(GOC, 'README.md')

# Ba phần, mười lăm phẩm theo thứ tự truyền thống của Trung Bộ Kinh.
PHAN = [
    ('Phần một — Mūlapaṇṇāsa (1–50)', [
        ('Mūlapariyāyavagga', 'Phẩm Căn Bản', 1, 10),
        ('Sīhanādavagga', 'Phẩm Sư Tử Hống', 11, 20),
        ('Opammavagga', 'Phẩm Ví Dụ', 21, 30),
        ('Mahāyamakavagga', 'Đại Song Đôi', 31, 40),
        ('Cūḷayamakavagga', 'Tiểu Song Đôi', 41, 50),
    ]),
    ('Phần hai — Majjhimapaṇṇāsa (51–100)', [
        ('Gahapativagga', 'Phẩm Gia Chủ', 51, 60),
        ('Bhikkhuvagga', 'Phẩm Tỳ-kheo', 61, 70),
        ('Paribbājakavagga', 'Phẩm Du Sĩ Ngoại Đạo', 71, 80),
        ('Rājavagga', 'Phẩm Vua', 81, 90),
        ('Brāhmaṇavagga', 'Phẩm Bà-la-môn', 91, 100),
    ]),
    ('Phần ba — Uparipaṇṇāsa (101–152)', [
        ('Devadahavagga', 'Phẩm Devadaha', 101, 110),
        ('Anupadavagga', 'Phẩm Theo Thứ Tự', 111, 120),
        ('Suññatavagga', 'Phẩm Không', 121, 130),
        ('Vibhaṅgavagga', 'Phẩm Phân Tích', 131, 140),
        ('Saḷāyatanavagga', 'Phẩm Sáu Xứ', 141, 152),
    ]),
]


def dong_mot_bai(n):
    info = thong_tin(n)
    d = os.path.join(GOC, info['thu_muc'])
    tep = glob.glob(os.path.join(d, 'Kinh-*.md'))
    if tep:
        ten = '[%s](%s/%s)' % (info['ten'], info['thu_muc'], os.path.basename(tep[0]))
    else:
        ten = info['ten']
    return '| %d | %s | *%s* |' % (n, ten, info['pali'])


so_xong = sum(1 for n in range(1, 153)
              if glob.glob(os.path.join(GOC, thong_tin(n)['thu_muc'], 'Kinh-*.md')))

dong = ['Ba phần, mười lăm phẩm, theo thứ tự truyền thống của bộ kinh.']
for ten_phan, vaggas in PHAN:
    dong += ['', '### ' + ten_phan]
    for pali, vi, a, b in vaggas:
        dong += ['', '#### %s — %s (%d–%d)' % (pali, vi, a, b), '',
                 '| # | Bài kinh | Tên Pali |', '|---|---|---|']
        dong += [dong_mot_bai(n) for n in range(a, b + 1)]

bang = '\n'.join(dong)

src = open(README, encoding='utf-8').read()
if '<!-- BAT DAU MUC LUC -->' not in src:
    src = src.replace(
        '<!-- Bảng mục lục đầy đủ do cong-cu/tao-muc-luc-goc.py sinh ra; sẽ cập nhật khi các bài hoàn thành. -->\n\nBảng mục lục đang được hoàn thiện cùng tiến độ dịch.',
        '<!-- BAT DAU MUC LUC -->\n<!-- KET THUC MUC LUC -->')
src = re.sub(r'\*\*Trạng thái: \d+/152 bài đã dịch\*\*',
             '**Trạng thái: %d/152 bài đã dịch**' % so_xong, src)
src = re.sub(r'<!-- BAT DAU MUC LUC -->.*?<!-- KET THUC MUC LUC -->',
             '<!-- BAT DAU MUC LUC -->\n' + bang + '\n<!-- KET THUC MUC LUC -->',
             src, flags=re.S)
open(README, 'w', encoding='utf-8').write(src)
print('muc luc: %d/152 bai da dich, %d pham' % (so_xong, sum(len(v) for _, v in PHAN)))
