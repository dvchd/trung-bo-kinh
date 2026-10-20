#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_mn146.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_mn146.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
  ('00-title', 'Nhan đề', 'mn146:0.1', 'mn146:0.2'),
  ('01-phan-1', 'Phần 1', 'mn146:1.1', 'mn146:6.21'),
  ('02-phan-2', 'Phần 2', 'mn146:6.22', 'mn146:8.13'),
  ('03-phan-3', 'Phần 3', 'mn146:8.14', 'mn146:10.16'),
  ('04-phan-4', 'Phần 4', 'mn146:10.17', 'mn146:16.10'),
  ('05-phan-5', 'Phần 5', 'mn146:16.11', 'mn146:19-20.19'),
  ('06-phan-6', 'Phần 6', 'mn146:19-20.20', 'mn146:23.1'),
  ('07-phan-7', 'Phần 7', 'mn146:23.2', 'mn146:26.14'),
  ('08-phan-8', 'Phần 8', 'mn146:26.15', 'mn146:27.8'),
]

# Đoạn PLI không có EN: Sujato gộp câu. Nếu PLI trùng khớp tuyệt đối với một
# đoạn phía trước thì mượn lại EN của đoạn đó.
exact = {}
for x in k:
    if norm(r.get(x)):
        exact.setdefault(norm(p.get(x)), x)

def en_for(x):
    v = norm(r.get(x))
    if v: return v, None
    t = exact.get(norm(p.get(x)))
    if t and POS[t] < POS[x]: return norm(r.get(t)), t
    return '', None

seen = set(); stats = {'copied': 0, 'empty': 0}
for name, label, k0, k1 in FILES:
    ks = [x for x in k[POS[k0]:POS[k1] + 1] if x not in seen]
    seen |= set(ks)
    out = ['# %s  (%d đoạn)' % (label, len(ks)), '']
    for x in ks:
        line = '## ' + x
        rf = (ref.get(x) or '').strip()
        if rf: line += '  `%s`' % rf
        out.append(line)
        pl = norm(p.get(x))
        if pl: out.append('- **PLI**: ' + pl)
        en, src = en_for(x)
        if en:
            tag = '- **EN**: ' + en
            if src: tag += '  (= %s)' % src
            out.append(tag)
            if src: stats['copied'] += 1
        elif pl:
            out.append('- **EN**: (Sujato gộp đoạn này vào câu trước — dịch trực tiếp từ PLI)')
            stats['empty'] += 1
        cm = norm(c.get(x))
        if cm: out.append('- **NOTE**: ' + cm)
        out.append('')
    open(os.path.join(HERE, 'sections', name + '.md'), 'w', encoding='utf-8').write('\n'.join(out))

print('xong:', len(FILES), 'file |', len(seen), 'đoạn | EN mượn lại:', stats['copied'], '| EN trống:', stats['empty'])
