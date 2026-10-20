#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_mn10.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_mn10.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
  ('00-title', 'Nhan đề', 'mn10:0.1', 'mn10:0.2'),
  ('01-mo-dau', 'Mở đầu', 'mn10:1.1', 'mn10:5.5'),
  ('02-1-2-the-postures', '1.2. The Postures', 'mn10:6.0', 'mn10:7.5'),
  ('03-1-3-situational-awarenes', '1.3. Situational Awareness', 'mn10:8.0', 'mn10:9.3'),
  ('04-1-4-focusing-on-the-repu', '1.4. Focusing on the Repulsive', 'mn10:10.0', 'mn10:11.3'),
  ('05-1-5-focusing-on-the-elem', '1.5. Focusing on the Elements', 'mn10:12.0', 'mn10:13.3'),
  ('06-1-6-the-charnel-ground-c', '1.6. The Charnel Ground Contemplations', 'mn10:14.0', 'mn10:31.6'),
  ('07-2-observing-the-feelings', '2. Observing the Feelings', 'mn10:32.0', 'mn10:33.5'),
  ('08-3-observing-the-mind', '3. Observing the Mind', 'mn10:34.0', 'mn10:37.5'),
  ('09-4-2-the-aggregates', '4.2. The Aggregates', 'mn10:38.0', 'mn10:39.5'),
  ('10-4-3-the-sense-fields', '4.3. The Sense Fields', 'mn10:40.0', 'mn10:41.5'),
  ('11-4-4-the-awakening-factor', '4.4. The Awakening Factors', 'mn10:42.0', 'mn10:43.5'),
  ('12-4-5-the-truths', '4.5. The Truths', 'mn10:44.0', 'mn10:47.6'),
  ('13-phan-12', 'Phần 12', 'mn10:48.0', 'mn10:48.4'),
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
