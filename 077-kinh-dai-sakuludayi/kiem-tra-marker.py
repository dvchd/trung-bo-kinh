#!/usr/bin/env python3
"""Kiểm tra file bản dịch: đủ marker segment, đủ phủ, không lặp marker, không sót segment.

Dùng:  python3 kiem-tra-marker.py <file-ban-dich.md> [<file-nguon.md> ...]
Nếu không truyền file nguồn, script tự suy ra từ manifest.
"""
import re
import sys
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
SEG_RE = re.compile(r"<!--\s*seg:\s*(mn77:[\d.\-]+)\s*-->")


def markers_in(path):
    txt = open(path, encoding="utf-8").read()
    return SEG_RE.findall(txt)


def source_markers(path):
    txt = open(path, encoding="utf-8").read()
    return re.findall(r"^##\s+(mn77:[\d.\-]+)", txt, re.M)


def main():
    if len(sys.argv) < 2:
        print("Dùng: python3 kiem-tra-marker.py <file-ban-dich.md> [<file-nguon.md>]")
        return 2

    target = sys.argv[1]
    got = markers_in(target)

    sources = sys.argv[2:]
    if not sources:
        # Suy ra từ tên file: ban-dich/XX-ten.md -> nguon/sections/XX-ten.md
        name = os.path.basename(target)
        cand = os.path.join(BASE, "nguon", "sections", name)
        if os.path.exists(cand):
            sources = [cand]

    expect = []
    for s in sources:
        expect.extend(source_markers(s))

    print(f"== {target}")
    print(f"   marker trong bài dịch : {len(got)}")
    if expect:
        print(f"   segment trong nguồn   : {len(expect)}")

    errs = 0

    # 1. trùng marker
    seen = set()
    dups = sorted({m for m in got if m in seen or seen.add(m)})
    if dups:
        errs += len(dups)
        print(f"   [LỖI] marker lặp lại ({len(dups)}): {', '.join(dups[:12])}")

    if expect:
        missing = [m for m in expect if m not in got]
        extra = [m for m in got if m not in expect]
        if missing:
            errs += len(missing)
            print(f"   [LỖI] thiếu {len(missing)} segment: {', '.join(missing[:12])}")
        if extra:
            errs += len(extra)
            print(f"   [LỖI] marker lạ không có trong nguồn ({len(extra)}): {', '.join(extra[:12])}")

        # 2. thứ tự
        order = {m: i for i, m in enumerate(expect)}
        seen_o = [order[m] for m in got if m in order]
        bad = [(a, b) for a, b in zip(seen_o, seen_o[1:]) if b < a]
        if bad:
            errs += len(bad)
            print(f"   [LỖI] sai thứ tự tại {len(bad)} chỗ")

    # 3. marker không nằm riêng dòng
    txt = open(target, encoding="utf-8").read()
    inline = 0
    in_code = False
    for line in txt.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        s = line.strip()
        for m in SEG_RE.finditer(line):
            if not (s.startswith("<!-- seg:") or s == m.group(0)):
                inline += 1
    if inline:
        print(f"   [CẢNH BÁO] {inline} marker không nằm riêng một dòng (không bắt buộc, nhưng nên sửa)")

    # 4. nội dung rỗng
    body = SEG_RE.sub("\n", txt)
    body = re.sub(r"^#.*$", "", body, flags=re.M)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    words = len(re.findall(r"\w+", body, re.UNICODE))
    print(f"   số từ nội dung        : {words}")

    if errs:
        print(f"   ==> THẤT BẠI: {errs} lỗi")
        return 1
    print("   ==> ĐẠT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
