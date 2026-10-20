#!/usr/bin/env python3
"""Rà soát toàn bộ bản dịch MN 30.

Dung:  python3 ra-soat.py [--drift]
"""
import sys, os, re, glob, difflib, json

BASE = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(BASE, 'ban-dich')
NGUON = os.path.join(BASE, 'nguon', 'sections')

SEG = re.compile(r'<!--\s*seg:\s*(mn30:[\d.\-]+)\s*-->')

# Câu/công thức phải xuất hiện đúng số lần, đúng nguyên văn
PINNED = []

BANNED = ['như thị', 'nhất thời', 'bất khả tư nghì', 'vô lượng vô biên',
          'chấp trước', 'Phật giáo đồ', 'như trên', 'lược đi', '...']

def read(p):
    return open(p, encoding='utf-8').read()

def strip_comments(t):
    return re.sub(r'<!--.*?-->', '', t, flags=re.S)

def strip_notes(t):
    return re.sub(r'\[[^\]]*\]', '', t)

def main():
    EXCLUDE = ('00-gioi-thieu', 'bang-thuat-ngu', 'nguon-tham-khao')
    files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(BAN, '*.md'))
                   if not os.path.basename(p).startswith(EXCLUDE))
    problems = []
    print('=' * 68)
    print('RA SOAT BAN DICH MN 30 — %d tep' % len(files))

    # 1. marker
    src_keys = []
    for p in sorted(glob.glob(os.path.join(NGUON, '*.md'))):
        src_keys += re.findall(r'^##\s+(mn30:[\d.\-]+)', read(p), re.M)
    got = []
    for f in files:
        got += SEG.findall(read(os.path.join(BAN, f)))
    print('\n[1] Marker')
    print('    nguon %d | ban dich %d' % (len(src_keys), len(got)))
    if len(set(got)) != len(got):
        d = [k for k in set(got) if got.count(k) > 1]
        problems.append('marker lap: %s' % d[:10]); print('    [LOI] lap:', d[:10])
    miss = [k for k in src_keys if k not in got]
    extra = [k for k in got if k not in src_keys]
    if miss: problems.append('thieu marker %d' % len(miss)); print('    [LOI] thieu:', miss[:12])
    if extra: problems.append('marker la %d' % len(extra)); print('    [LOI] la:', extra[:12])
    order = {k: i for i, k in enumerate(src_keys)}
    seq = [order[k] for k in got if k in order]
    bad = [i for i in range(1, len(seq)) if seq[i] < seq[i-1]]
    if bad: problems.append('sai thu tu %d' % len(bad)); print('    [LOI] sai thu tu tai', len(bad), 'cho')
    if not (miss or extra or bad):
        print('    OK — du, dung thu tu, khong lap')

    # 2. dấu ngoặc kép
    print('\n[2] Can bang dau ngoac kep "')
    for f in files:
        body = strip_comments(read(os.path.join(BAN, f)))
        body = strip_notes(body)
        n = body.count('"')
        if n % 2:
            problems.append('%s: le dau "' % f); print('    [LOI] %-32s %d dau "' % (f, n))
    if not any('le dau' in p for p in problems):
        print('    OK — moi tep chan')

    # 3. ngoặc cong
    print('\n[3] Dau ngoac cong (curly quotes)')
    curl = [f for f in files if re.search(r'[\u201c\u201d\u2018\u2019]', read(os.path.join(BAN, f)))]
    if curl:
        problems.append('curly quotes: %s' % curl); print('    [LOI]', curl)
    else:
        print('    OK — khong co')

    # 4. dấu ... ngoài chú thích
    print('\n[4] Dau … ngoai [Chú thích]')
    hits = []
    for f in files:
        body = strip_comments(read(os.path.join(BAN, f)))
        for ln in strip_notes(body).split('\n'):
            if '…' in ln or '...' in ln:
                hits.append('%s: %s' % (f, ln.strip()[:70]))
    if hits:
        problems.append('%d dong co … ngoai chu thich' % len(hits))
        for h in hits[:10]: print('    [LOI]', h)
        if len(hits) > 10: print('    ... va %d dong nua' % (len(hits) - 10))
    else:
        print('    OK — khong co')

    # 5. từ cấm
    print('\n[5] Tu ngu can tranh')
    found = False
    for b in BANNED:
        for f in files:
            body = strip_comments(read(os.path.join(BAN, f)))
            if b in body:
                problems.append('tu cam "%s" trong %s' % (b, f))
                print('    [LOI] "%s" trong %s' % (b, f)); found = True
    if not found: print('    OK — khong co')

    # 6. công thức pin
    print('\n[6] Cong thuc lap bat buoc')
    for text, expect, pli in PINNED:
        n = sum(strip_comments(read(os.path.join(BAN, f))).count(text) for f in files)
        ok = 'OK ' if n == expect else 'LOI'
        print('    [%s] %-2d/%-2d  %s' % (ok, n, expect, text[:56]))
        if n != expect:
            problems.append('cong thuc "%s": %d/%d' % (text[:30], n, expect))

    # 7. doan gop (marker lien nhau khong co chu — hop le khi gop cau)
    print('\n[7] Doan dich rong')
    empty = []
    for f in files:
        txt = read(os.path.join(BAN, f))
        for m in SEG.finditer(txt):
            after = txt[m.end():m.end() + 400]
            body = re.split(r'<!--\s*seg:', after)[0].strip()
            if body.startswith('#'):      # segment tieu de — khong tinh
                continue
            body = re.sub(r'^#.*$', '', body, flags=re.M).strip()
            if len(re.findall(r'\w+', body, re.UNICODE)) < 3:
                empty.append('%s %s' % (f, m.group(1)))
    if empty:
        print('    [INFO] %d marker gop chung voi doan sau (hop le): %s' % (len(empty), empty[:8]))
    else:
        print('    OK — khong co')

    # 8. bảng markdown
    print('\n[8] Bang markdown — so cot')
    for f in files:
        lines = read(os.path.join(BAN, f)).split('\n')
        tbl = []
        for ln in lines:
            if ln.strip().startswith('|'):
                tbl.append(ln.count('|'))
            else:
                if len(set(tbl)) > 1:
                    problems.append('%s: bang lech cot' % f); print('    [LOI] %s lech cot' % f)
                tbl = []

    # 9. drift công thức
    if '--drift' in sys.argv:
        print('\n[9] Phat hien lech cong thuc (cau tuong tu nhung khac chu)')
        sents = []
        for f in files:
            body = strip_comments(read(os.path.join(BAN, f)))
            body = strip_notes(body)
            for s in re.split(r'(?<=[.!?])\s+|\n+', body):
                s = s.strip()
                if len(s.split()) >= 6:
                    sents.append((f, s))
        NAMES = ['Đức Thế Tôn', 'Như Lai']
        def canon(t):
            for n in NAMES:
                t = t.replace(n, '@')
            t = re.sub(r'\b(một|hai|ba|bốn|năm|sáu|bảy|tám)\b', '#', t)
            return t
        groups = {}
        for f, s in sents:
            groups.setdefault(' '.join(canon(s).split()[:5]).lower(), []).append((f, s))
        n = 0
        for k, v in groups.items():
            if len(v) < 2: continue
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    a, b = v[i][1], v[j][1]
                    if a == b: continue
                    r = difflib.SequenceMatcher(None, canon(a), canon(b)).ratio()
                    if r >= 0.985: continue
                    if 0.55 < r < 0.985:
                        n += 1
                        if n <= 12:
                            print('    [~] %.2f  %s' % (r, a[:64]))
                            print('                %s' % b[:64])
        print('    tong cap lech: %d (can ra tay)' % n)

    print('\n' + '=' * 68)
    if problems:
        print('KET LUAN: %d van de' % len(problems))
        for p in problems: print('  -', p)
        return 1
    print('KET LUAN: DAT — khong phat hien van de')
    return 0

if __name__ == '__main__':
    sys.exit(main())
