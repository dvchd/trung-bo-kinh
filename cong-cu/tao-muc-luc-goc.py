#!/usr/bin/env python3
"""Sinh bảng mục lục 152 bài trong README gốc, kèm trạng thái dịch."""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mn_suttas import thong_tin  # noqa: E402

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(GOC, 'README.md')

dong = []
so_xong = 0
for n in range(1, 153):
    info = thong_tin(n)
    d = os.path.join(GOC, info['thu_muc'])
    tep = glob.glob(os.path.join(d, 'Kinh-*.md'))
    if tep:
        so_xong += 1
        ten = '[%s](%s/%s)' % (info['ten'], info['thu_muc'], os.path.basename(tep[0]))
        trang_thai = '✅'
    else:
        ten = info['ten']
        trang_thai = '—'
    dong.append('| %d | %s | *%s* | %s |' % (n, ten, info['pali'], trang_thai))

bang = '\n'.join([
    '| # | Bài kinh | Tên Pali | Đã dịch |',
    '|---|---|---|---|',
] + dong)

src = open(README, encoding='utf-8').read()
if '<!-- BAT DAU MUC LUC -->' not in src:
    src = src.replace(
        '<!-- Bảng mục lục đầy đủ do cong-cu/tao-muc-luc-goc.py sinh ra; sẽ cập nhật khi các bài hoàn thành. -->\n\nBảng mục lục đang được hoàn thiện cùng tiến độ dịch.',
        '<!-- BAT DAU MUC LUC -->\n<!-- KET THUC MUC LUC -->')
    src = re.sub(r'\*\*Trạng thái: đang dịch\.\*\*[^\n]*',
                 '**Trạng thái: %d/152 bài đã dịch.** Mỗi bài hoàn thành được đánh dấu ✅ trong bảng mục lục bên dưới.' % so_xong,
                 src)
src = re.sub(r'<!-- BAT DAU MUC LUC -->.*?<!-- KET THUC MUC LUC -->',
             '<!-- BAT DAU MUC LUC -->\n' + bang + '\n<!-- KET THUC MUC LUC -->',
             src, flags=re.S)
open(README, 'w', encoding='utf-8').write(src)
print('muc luc: %d/152 bai da dich' % so_xong)
