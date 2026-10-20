#!/usr/bin/env python3
"""Dựng khung một bài Trung Bộ Kinh mới.

    python3 cong-cu/tao-bai.py 1        # chỉ bài 1
    python3 cong-cu/tao-bai.py --tat-ca  # cả 152 bài (bỏ qua bài đã có)

Việc làm:
- Tải api_mnN.json từ SuttaCentral (bilara, bản Sujato).
- Chia nguồn thành các tệp trong nguon/sections/.
- Sinh nguon/tao-sections.py, ghep.py, tao-muc-luc.py, kiem-tra-marker.py,
  ra-soat.py, tien-do.py cho bài đó.
- Sinh HUONG-DAN-DICH.md và README.md khung.
"""
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'cong-cu'))
from mn_suttas import thong_tin  # noqa: E402

MAU = os.path.join(ROOT, 'mau')
API = 'https://suttacentral.net/api/bilarasuttas/mn%d/sujato'
CHUNK = 50


def bo_dau(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()


def slug_ngan(s, limit=28):
    s = bo_dau(s).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:limit].rstrip('-')


def tai_api(n):
    for lan in range(3):
        try:
            with urllib.request.urlopen(API % n, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if lan == 2:
                raise
            print('  loi tai (lan %d): %s' % (lan + 1, e))
            time.sleep(2 * (lan + 1))


def chia_khoi(d, tag):
    """Trả về [(ten_tep, nhan, key_dau, key_cuoi)]."""
    k = d['keys_order']
    tieu_de = [x for x in k if x.startswith(tag + ':0.')]
    con = [x for x in k if x not in tieu_de]
    khoi = [('00-title', 'Nhan đề', tieu_de[0], tieu_de[-1])] if tieu_de else []
    if not con:
        return khoi

    head = [x for x in con if re.match(r'^%s:\d+\.0$' % re.escape(tag), x)]
    if head:
        vi_tri = {x: i for i, x in enumerate(con)}
        if vi_tri[head[0]] > 0:
            khoi.append(('01-mo-dau', 'Mở đầu', con[0], con[vi_tri[head[0]] - 1]))
        for j, h in enumerate(head):
            cuoi = con[vi_tri[head[j + 1]] - 1] if j + 1 < len(head) else con[-1]
            nhan = (d['translation_text'].get(h) or '').strip() or ('Phần %d' % (j + 1))
            khoi.append(('%02d-%s' % (len(khoi), slug_ngan(nhan, 24) or ('phan-%d' % (len(khoi)))),
                         nhan, h, cuoi))
        return khoi

    so = 0
    for i in range(0, len(con), CHUNK):
        so += 1
        phan = con[i:i + CHUNK]
        khoi.append(('%02d-phan-%d' % (so, so), 'Phần %d' % so, phan[0], phan[-1]))
    return khoi


def doc_mau(ten):
    return open(os.path.join(MAU, ten), encoding='utf-8').read()


def ghi(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)


def tao_sections_py(tag, khoi):
    t = doc_mau('tao-sections.py')
    t = t.replace('dn4', tag)
    dong = '\n'.join(
        "  ('%s', %r, '%s', '%s')," % (ten, nhan, k0, k1)
        for ten, nhan, k0, k1 in khoi)
    t = re.sub(r'FILES = \[.*?\n\]', 'FILES = [\n' + dong + '\n]', t, flags=re.S)
    t = re.sub(r'FILES= \[.*?\n\]', 'FILES = [\n' + dong + '\n]', t, flags=re.S)
    return t


def tao_ghep(ten_tep, khoi):
    t = doc_mau('ghep.py')
    t = t.replace('Kinh-Sonadanda', ten_tep)
    order = 'ORDER = [\n'
    dong = ["'%s'" % b[0] for b in khoi]
    for i in range(0, len(dong), 4):
        order += '    ' + ', '.join(dong[i:i + 4]) + ',\n'
    order += ']'
    t = re.sub(r'ORDER = \[.*?\n\]', order, t, flags=re.S)
    return t


def tao_muc_luc(ten_tep, so, ten):
    t = doc_mau('tao-muc-luc.py')
    t = t.replace('Kinh-Sonadanda', ten_tep)
    start = '## Trung Bộ Kinh — bài kinh số %d: %s\n' % (so, ten)
    t = re.sub(r'\nSTART = .*', lambda m: '\nSTART = ' + repr(start), t)
    return t


def tao_ra_soat(tag, so):
    t = doc_mau('ra-soat.py')
    t = t.replace('dn4', tag)
    t = t.replace('DN 4', 'MN %d' % so)
    t = re.sub(r'PINNED = \[.*?\n\]', 'PINNED = []', t, flags=re.S)
    t = re.sub(r"NAMES = \[.*?\n\s*'Gotama.*?\]", "NAMES = ['Đức Thế Tôn', 'Như Lai']", t, flags=re.S)
    return t


def tao_huong_dan(info):
    t = doc_mau('HUONG-DAN-DICH.md')
    for k, v in [('{{TEN_KINH}}', info['ten']), ('{{PALI}}', info['pali']),
                 ('{{N}}', str(info['so'])), ('{{SLUG_PASCAL}}', info['ten_tep']) ]:
        t = t.replace(k, v)
    return t


def tao_readme(info, so_doan):
    return f"""# {info['ten']} — *{info['pali']} Sutta*

> Bài kinh số {info['so']} trong Trung Bộ Kinh (*Majjhima Nikāya*), kinh tạng Pali.

**Đọc bản dịch hoàn chỉnh: [`{info['ten_tep']}.md`]({info['ten_tep']}.md)**

---

## Về bài kinh

<!-- Người dịch viết 3–6 câu: bài nói về ai, việc gì, kết thúc thế nào. -->

## Con số

| | |
|---|---|
| Đoạn văn (segment) | **{so_doan}** — khớp 100% với nguồn SuttaCentral |
| Nguồn Pali | SuttaCentral, bản *Mahāsaṅgīti Tipiṭaka* |
| Bản đối chiếu | Bhikkhu Sujato (CC0) |

## Cấu trúc

<!-- Liệt kê các tệp trong ban-dich/ kèm một dòng nội dung, sau khi dịch xong. -->

## Cách đọc và góp ý

- Bản dịch chia đoạn theo từng segment của SuttaCentral; mỗi đoạn có neo `mn{info['so']}:X.Y` trong
  tệp nguồn, nên trích dẫn hay báo lỗi đều tra được.
- Báo lỗi: mở issue ở repo gốc, ghi rõ `mn{info['so']}:X.Y` và câu cần sửa.

## Giấy phép

Văn bản dịch: CC0 1.0 (không cần ghi công). Xem [`../LICENSE`](../LICENSE).
"""


def tao_bai(n, ep=False):
    info = thong_tin(n)
    d = os.path.join(ROOT, info['thu_muc'])
    if os.path.isdir(d) and not ep:
        print('bai %d da co, bo qua' % n)
        return False
    tag = 'mn%d' % n
    print('=== bai %d: %s (%s)' % (n, info['ten'], tag))
    api = tai_api(n)
    ghi(os.path.join(d, 'nguon', 'api_%s.json' % tag), json.dumps(api, ensure_ascii=False))
    khoi = chia_khoi(api, tag)
    ghi(os.path.join(d, 'nguon', 'tao-sections.py'), tao_sections_py(tag, khoi))
    os.makedirs(os.path.join(d, 'nguon', 'sections'), exist_ok=True)
    subprocess.run([sys.executable, 'tao-sections.py'], cwd=os.path.join(d, 'nguon'), check=True)
    so_doan = sum(1 for x in api['keys_order'])
    for ten, noi_dung in [
        ('ghep.py', tao_ghep(info['ten_tep'], khoi)),
        ('tao-muc-luc.py', tao_muc_luc(info['ten_tep'], n, info['ten'])),
        ('kiem-tra-marker.py', doc_mau('kiem-tra-marker.py').replace('dn4', tag)),
        ('ra-soat.py', tao_ra_soat(tag, n)),
        ('tien-do.py', doc_mau('tien-do.py').replace('dn4', tag)),
    ]:
        ghi(os.path.join(d, ten), noi_dung)
    ghi(os.path.join(d, 'HUONG-DAN-DICH.md'), tao_huong_dan(info))
    ghi(os.path.join(d, 'README.md'), tao_readme(info, so_doan))
    os.makedirs(os.path.join(d, 'ban-dich'), exist_ok=True)
    os.makedirs(os.path.join(d, 'ra-soat'), exist_ok=True)
    print('   %d doan -> %s' % (so_doan, info['thu_muc']))
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    if sys.argv[1] == '--tat-ca':
        for n in range(1, 153):
            try:
                tao_bai(n)
            except Exception as e:  # noqa: BLE001
                print('   [LOI] bai %d: %s' % (n, e))
        return 0
    for a in sys.argv[1:]:
        tao_bai(int(a), ep=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
