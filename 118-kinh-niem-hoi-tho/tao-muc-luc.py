#!/usr/bin/env python3
"""Chèn / cập nhật \'## Mục lục\' trong Kinh-Niem-Hoi-Tho.md (anchor kiểu GitHub)."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(BASE, 'Kinh-Niem-Hoi-Tho.md')
START = '\n## Trung Bộ Kinh — bài kinh số 118: Kinh Niệm Hơi Thở\n'

def slug(t):
    t = t.strip().lower()
    t = re.sub(r'[^\w\s-]', '', t, flags=re.UNICODE)   # bo dau cham, ngoac, em dash...
    return t.replace(' ', '-')                        # moi khoang trang -> mot '-'

def text_of(h):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', h)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    return t.strip()

src = open(DOC, encoding='utf-8').read()

# 1. bỏ mục lục cũ
i = src.find('\n## Mục lục\n')
if i >= 0:
    j = src.find(START, i)
    src = src[:i] + '\n' + src[j:] if j >= 0 else src[:i]

# 2. thu thap tieu de tu '## Truong Bo Kinh' tro di, dung truoc '## Bảng thuật ngữ'
body = src[src.index(START):]
body = body.split('\n## Bảng thuật ngữ')[0]
heads = re.findall(r'^(#{2,3})\s+(.+)$', body, re.M)

lines = ['## Mục lục', '', '- [Lời giới thiệu](#lời-giới-thiệu)']
for hashes, h in heads:
    t = text_of(h)
    a = slug(t)
    if len(hashes) == 2:
        lines.append('- [**%s**](#%s)' % (t, a))
    else:
        lines.append('  - [%s](#%s)' % (t, a))
lines += ['', '---', '']
toc = '\n'.join(lines) + '\n'

src = src.replace(START, '\n' + toc + START.lstrip('\n'), 1)
open(DOC, 'w', encoding='utf-8').write(src)
print('muc luc: %d lien ket' % sum(1 for l in lines if '](' in l))
