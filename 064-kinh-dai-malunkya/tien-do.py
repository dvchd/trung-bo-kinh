#!/usr/bin/env python3
"""Báo cáo tiến độ dịch: so sánh tập marker nguồn vs bản dịch."""
import re, glob, os, sys

SRC = re.compile(r'^##\s+(mn64:\d+(?:\.\d+)+)', re.M)
OUT = re.compile(r'<!--\s*seg:\s*(mn64:\d+(?:\.\d+)+)\s*-->')

def segs(path, rx):
    """Tập segment id xuất hiện trong file (khử trùng lặp)."""
    return set(m.group(1) for m in rx.finditer(open(path, encoding='utf-8').read()))

src_dir, out_dir = 'nguon/sections', 'ban-dich'
src = {os.path.basename(f): segs(f, SRC) for f in sorted(glob.glob(f'{src_dir}/*.md'))}
done = {os.path.basename(f): segs(f, OUT) for f in sorted(glob.glob(f"{out_dir}/*.md"))}

ts = sum(len(v) for v in src.values())
td = sum(len(done.get(k, set())) for k in src)
print(f'Tổng nguồn : {ts} segment / {len(src)} file')
print(f'Đã dịch    : {td} segment / {len([k for k in src if done.get(k)])} file')
print(f'Còn lại    : {ts - td} segment')
print()

ok = part = none = bad = 0
for k in sorted(src):
    s, d = src[k], done.get(k, set())
    if not d:
        st, note = '--  ', f'chưa có (cần {len(s)})'
        none += 1
    elif d == s:
        st, note = 'OK  ', f'{len(d)}/{len(s)}'
        ok += 1
    else:
        miss, extra = s - d, d - s
        bits = []
        if miss: bits.append(f'thiếu {len(miss)}')
        if extra: bits.append(f'thừa {len(extra)}')
        st = '!!  '
        note = f'{len(d)}/{len(s)} ' + ', '.join(bits)
        if extra: bad += 1
        else: part += 1
    print(f'{st}{k:36s} {note}')

print()
print(f'Hoàn chỉnh: {ok} | Thiếu segment: {part} | Có marker lạ: {bad} | Chưa làm: {none}')
sys.exit(0 if part == 0 and none == 0 and bad == 0 else 1)
