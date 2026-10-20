#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn4.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn4.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
 ('00-title',          'Nhan đề',                                            'dn4:0.1',   'dn4:0.2'),
 ('01-campa',          '1 — Các bà-la-môn và gia chủ xứ Campā',              'dn4:1.0',   'dn4:3.14'),
 ('02-sonadanda',      '2 — Phẩm chất của Soṇadaṇḍa',                        'dn4:4.0',   'dn4:5.22'),
 ('03-buddha',         '3 — Phẩm chất của Đức Thế Tôn',                      'dn4:6.0',   'dn4:6.47'),
 ('04-second-thoughts','4 — Soṇadaṇḍa đổi ý',                                'dn4:7.0',   'dn4:10.16'),
 ('05-brahmin',        '5 — Thế nào là một bà-la-môn',                       'dn4:11.0',  'dn4:20.14'),
 ('06-ethics-wisdom',  '6 — Bàn về giới và tuệ',                             'dn4:21.0',  'dn4:23.15'),
 ('07-conclusion',     '7 — Soṇadaṇḍa xin làm người cư sĩ',                  'dn4:24.0',  'dn4:27.2'),
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
