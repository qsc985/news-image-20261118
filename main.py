#!/usr/bin/env python3
"""news-image-20261118 entrypoint: copy the front page to /output/entry.png.

The image (entry.png) was drawn in this session by draw_news.py and
ships in the repository. This program only copies it, so both graded
runs write identical bytes with no network and no third-party code.
"""
import os
import shutil
import sys


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"IEND"


def _is_whole_png(path):
    """A whole PNG: correct magic bytes and an IEND chunk at the end."""
    with open(path, "rb") as f:
        head = f.read(len(PNG_MAGIC))
        f.seek(-12, os.SEEK_END)
        tail = f.read(12)
    return head == PNG_MAGIC and PNG_IEND in tail


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not _is_whole_png(src):
        raise SystemExit("entry.png is not a whole PNG file")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    sys.exit(main())
