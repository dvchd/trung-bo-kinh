#!/usr/bin/env python3
"""Đồng nhất các công thức lặp giữa 152 bài.

Cùng một đoạn Pali đáng lẽ phải ra cùng một câu tiếng Việt ở mọi bài. Script này
gom các đoạn có PLI giống nhau, chọn cách dịch xuất hiện nhiều nhất làm chuẩn và
thay các cách dịch khác bằng chuẩn ấy.

Chỉ đụng vào những nhóm thoả hết các điều kiện sau, để tránh sửa oan:
  - PLI ngắn (dưới 200 ký tự), tức là công thức, không phải đoạn văn dài;
  - nhóm có ít nhất 5 bài;
  - cách dịch chuẩn chiếm ít nhất một nửa số lần xuất hiện;
  - bản dịch không chứa [Chú thích (chú thích riêng của từng bài phải giữ);
  - các cách dịch khác dài không quá gấp đôi chuẩn (loại trường hợp một bài
    khai triển đầy đủ peyyāla còn bài khác tóm lược).

Chạy thử: python3 cong-cu/dong-nhat-cong-thuc.py
Áp dụng: python3 cong-cu/dong-nhat-cong-thuc.py --apply
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_SEG_NGUON = re.compile(r'^##\s+(mn\d+:[\d\-]+\.\d+)\s*$')
RE_PLI = re.compile(r'^-\s+\*\*PLI\*\*:\s*(.*)$')
RE_SEG_DICH = re.compile(r'^<!--\s*seg:\s*(mn\d+:[\d\-]+\.\d+)\s*-->$')


def chuan_hoa(text):
    text = text.lower()
    text = re.sub(r'…pe…|\.\.\.|…', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def doc_nguon():
    pli = {}
    for ten in sorted(os.listdir(GOC)):
        if not re.match(r'^\d{3}-', ten):
            continue
        thu_muc = os.path.join(GOC, ten, 'nguon', 'sections')
        if not os.path.isdir(thu_muc):
            continue
        for tep in sorted(os.listdir(thu_muc)):
            if not tep.endswith('.md'):
                continue
            seg = None
            for dong in open(os.path.join(thu_muc, tep), encoding='utf-8'):
                m = RE_SEG_NGUON.match(dong.strip())
                if m:
                    seg = m.group(1)
                    continue
                m = RE_PLI.match(dong.strip())
                if m and seg and seg not in pli:
                    pli[seg] = m.group(1).strip()
    return pli


def doc_ban_dich():
    """{seg: (đường dẫn, nội dung)}"""
    dich = {}
    for ten in sorted(os.listdir(GOC)):
        if not re.match(r'^\d{3}-', ten):
            continue
        thu_muc = os.path.join(GOC, ten, 'ban-dich')
        if not os.path.isdir(thu_muc):
            continue
        for tep in sorted(os.listdir(thu_muc)):
            if not tep.endswith('.md'):
                continue
            duong_dan = os.path.join(thu_muc, tep)
            seg = None
            gom = []
            for dong in open(duong_dan, encoding='utf-8'):
                m = RE_SEG_DICH.match(dong.strip())
                if m:
                    if seg and gom:
                        dich[seg] = (duong_dan, ' '.join(gom).strip())
                    seg = m.group(1)
                    gom = []
                    continue
                if seg:
                    d = dong.strip()
                    if d and not d.startswith('<!--'):
                        gom.append(d)
            if seg and gom:
                dich[seg] = (duong_dan, ' '.join(gom).strip())
    return dich


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--min-bai', type=int, default=5)
    args = ap.parse_args()

    pli = doc_nguon()
    dich = doc_ban_dich()

    nhom = defaultdict(list)
    for seg, goc in pli.items():
        if seg not in dich:
            continue
        khoa = chuan_hoa(goc)
        if len(khoa) < 12 or len(khoa) > 200:
            continue
        nhom[khoa].append((seg, goc, dich[seg][1]))

    sua = []  # (seg, chuẩn, hiện tại, đường dẫn)
    bo_qua = 0
    for khoa, ds in nhom.items():
        bai = {x[0].split(':')[0] for x in ds}
        if len(bai) < args.min_bai:
            continue
        dem = Counter(x[2] for x in ds)
        chuan, so_chuan = dem.most_common(1)[0]
        if so_chuan * 2 < len(ds):
            bo_qua += 1
            continue
        if '[Chú thích' in chuan:
            bo_qua += 1
            continue
        for seg, _, vn in ds:
            if vn == chuan or '[Chú thích' in vn:
                continue
            if len(vn) > 2 * len(chuan) + 40:
                bo_qua += 1
                continue
            sua.append((seg, chuan, vn, dich[seg][0]))

    print('Đoạn PLI: %d | nhóm đủ điều kiện sửa: %d | chỗ sẽ thay: %d | bỏ qua: %d'
          % (len(pli), len({s for s, _, _, _ in sua}), len(sua), bo_qua))
    for seg, chuan, hien_tai, _ in sua[:8]:
        print('\n %s\n   cũ: %s\n   mới: %s' % (seg, hien_tai[:100], chuan[:100]))

    if not args.apply:
        print('\n(chạy lại với --apply để ghi)')
        return 0

    # ghi theo tệp
    theo_tep = defaultdict(list)
    for seg, chuan, _, duong_dan in sua:
        theo_tep[duong_dan].append((seg, chuan))

    so_tep = 0
    for duong_dan, danh_sach in theo_tep.items():
        noi_dung = open(duong_dan, encoding='utf-8').read()
        dong_list = noi_dung.split('\n')
        # dựng bản đồ vị trí marker -> chỉ số dòng
        vi_tri = {}
        for i, dong in enumerate(dong_list):
            m = RE_SEG_DICH.match(dong.strip())
            if m:
                vi_tri[m.group(1)] = i
        for seg, chuan in danh_sach:
            if seg not in vi_tri:
                continue
            i = vi_tri[seg] + 1
            # thay toàn bộ dòng văn bản của đoạn (bỏ qua dòng trống và chú thích)
            j = i
            while j < len(dong_list):
                d = dong_list[j].strip()
                if d.startswith('<!--') or RE_SEG_DICH.match(d):
                    break
                j += 1
            # đoạn văn nằm trong (i, j)
            khoang = [k for k in range(i, j) if dong_list[k].strip()]
            if not khoang:
                continue
            dong_list[khoang[0]] = chuan
            for k in khoang[1:]:
                dong_list[k] = ''
        open(duong_dan, 'w', encoding='utf-8').write('\n'.join(dong_list))
        so_tep += 1
    print('Đã sửa %d chỗ trong %d tệp.' % (len(sua), so_tep))
    return 0


if __name__ == '__main__':
    sys.exit(main())
