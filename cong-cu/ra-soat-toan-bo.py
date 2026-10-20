#!/usr/bin/env python3
"""Rà soát toàn bộ 152 bản dịch: từ cấm, ngoặc kép cong, ba chấm ngoài chú thích, ký hiệu chưa dịch."""
import glob
import os
import re
import sys

SKIP = {'00-gioi-thieu', 'bang-thuat-ngu', 'nguon-tham-khao'}
BANNED = ['như thị', 'nhất thời', 'bất khả tư nghì', 'vô lượng vô biên', 'chấp trước',
          'Phật giáo đồ', 'như trên', 'lược đi', 'nói rằng là', 'tiền thân là']
problems = []
da_quet = 0

for n in range(1, 153):
    ds = glob.glob('%03d-*/' % n)
    if not ds:
        problems.append(('THIEU THU MUC', n, '', '', 0))
        continue
    d = os.path.join(ds[0], 'ban-dich')
    for f in sorted(glob.glob(d + '/*.md')):
        base = os.path.basename(f)
        if base[:-3] in SKIP:
            continue
        da_quet += 1
        t = open(f, encoding='utf-8').read()
        rel = f.split('/')[0]
        for w in BANNED:
            c = len(re.findall(re.escape(w), t, re.I))
            if c:
                problems.append(('TU CAM', rel, base, w, c))
        if re.search(r'[\u201c\u201d\u2018\u2019]', t):
            problems.append(('NGOAC KEP CONG', rel, base, '', 0))
        for m in re.finditer(r'[^\[\]]*?\.\.\.', t):
            seg = t[max(0, m.start() - 40):m.end()]
            if 'Chú thích' not in seg:
                problems.append(('BA CHAM', rel, base, seg[-50:].replace('\n', ' '), 1))
        for tok in ('TODO', 'XXX', 'FIXME', '???'):
            if tok in t:
                problems.append(('CHUA DICH', rel, base, tok, 1))

print('so tep da quet:', da_quet)
for p in problems[:40]:
    print(' ', p)
print('TONG VAN DE:', len(problems))
sys.exit(0 if not problems else 1)
