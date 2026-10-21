#!/usr/bin/env python3
"""Kiểm tra tính nhất quán của các công thức lặp giữa 152 bài.

Cùng một đoạn Pali (ví dụ toàn bộ khuôn "Tôi nghe như vầy…" hoặc khuôn thiền-na)
xuất hiện ở nhiều bài. Người đọc sẽ thấy đó là hai bản dịch khác nhau nếu mỗi
bài dịch một kiểu. Script này:

1. đọc PLI của từng đoạn trong nguon/sections/*.md,
2. đọc bản dịch của từng đoạn trong ban-dich/*.md,
3. nhóm các đoạn có PLI giống nhau (đã chuẩn hoá),
4. in ra những nhóm có bản dịch tiếng Việt không thống nhất.

Chạy: python3 cong-cu/ra-soat-cong-thuc.py [--min N] [--top N]
  --min  số bài tối thiểu để coi là công thức lặp (mặc định 3)
  --top  số nhóm in ra (mặc định 40)
"""
import argparse
import os
import re
import sys
from collections import defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_SEG_NGUON = re.compile(r'^##\s+(mn\d+:[\d\-]+\.\d+)\s*$')
RE_PLI = re.compile(r'^-\s+\*\*PLI\*\*:\s*(.*)$')
RE_SEG_DICH = re.compile(r'^<!--\s*seg:\s*(mn\d+:[\d\-]+\.\d+)\s*-->$')


def chuan_hoa(text):
    text = text.lower()
    text = re.sub(r'…pe…|\.\.\.|…', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def doc_nguon():
    """Trả về {seg: PLI}."""
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
            seg_hien_tai = None
            for dong in open(os.path.join(thu_muc, tep), encoding='utf-8'):
                m = RE_SEG_NGUON.match(dong.strip())
                if m:
                    seg_hien_tai = m.group(1)
                    continue
                m = RE_PLI.match(dong.strip())
                if m and seg_hien_tai and seg_hien_tai not in pli:
                    pli[seg_hien_tai] = m.group(1).strip()
    return pli


def doc_ban_dich():
    """Trả về {seg: đoạn tiếng Việt}."""
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
            seg_hien_tai = None
            gom = []
            for dong in open(os.path.join(thu_muc, tep), encoding='utf-8'):
                m = RE_SEG_DICH.match(dong.strip())
                if m:
                    if seg_hien_tai and gom:
                        dich[seg_hien_tai] = ' '.join(gom).strip()
                    seg_hien_tai = m.group(1)
                    gom = []
                    continue
                if seg_hien_tai:
                    d = dong.strip()
                    if d and not d.startswith('<!--'):
                        gom.append(d)
            if seg_hien_tai and gom:
                dich[seg_hien_tai] = ' '.join(gom).strip()
    return dich


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min', type=int, default=3)
    ap.add_argument('--top', type=int, default=40)
    ap.add_argument('--day-du', action='store_true', help='in cả nhóm đã thống nhất')
    args = ap.parse_args()

    pli = doc_nguon()
    dich = doc_ban_dich()
    print('Đoạn có PLI: %d | đoạn có bản dịch: %d' % (len(pli), len(dich)))

    nhom = defaultdict(list)
    for seg, goc in pli.items():
        if seg not in dich:
            continue
        khoa = chuan_hoa(goc)
        if len(khoa) < 25:
            continue
        bai = seg.split(':')[0]
        nhom[khoa].append((bai, seg, goc, dich[seg]))

    lech = []
    for khoa, ds in nhom.items():
        bai = {x[0] for x in ds}
        if len(bai) < args.min:
            continue
        bien_the = defaultdict(list)
        for _, seg, _, vn in ds:
            bien_the[re.sub(r'\s+', ' ', vn).strip()].append(seg)
        if len(bien_the) > 1:
            lech.append((len(bai), len(ds), len(bien_the), ds[0][2], bien_the))

    lech.sort(key=lambda x: -(x[0] * (x[2] - 1)))
    print('Nhóm công thức lặp (≥%d bài) có bản dịch lệch: %d' % (args.min, len(lech)))
    for so_bai, so_lan, so_bien_the, goc, bien_the in lech[:args.top]:
        print('\n--- PLI: %s' % goc[:110])
        print('    %d bài, %d đoạn, %d cách dịch' % (so_bai, so_lan, so_bien_the))
        for vn, ds in sorted(bien_the.items(), key=lambda x: -len(x[1]))[:4]:
            print('    [%d] %s: %s' % (len(ds), ','.join(ds[:4]), vn[:150]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
