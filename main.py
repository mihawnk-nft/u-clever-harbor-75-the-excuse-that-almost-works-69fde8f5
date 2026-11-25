#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt.

The line (18 words, one line, plain text, no greeting, no signature):

    internet's down and the engineer slot is 9-12, i'll hotspot from my
    phone but the vpn keeps dropping

Why this line: the judge is a tired manager who has heard every excuse
twice. What it would almost believe is a real, specific, boring detail,
not a wild story — and never the obvious clichés (dead grandmother, flat
tyre, sudden fever). A broadband engineer booked into a 9-to-12 slot is
exactly that boring detail, and it is funny on its own terms: of course
the gamer's internet "dies" on launch week, and of course the office VPN
keeps dropping on a phone hotspot. Lowercase, no greeting, no setup, no
explanation, no signature — it reads like a text sent in a hurry.

Pure standard library. Deterministic: the same line every run.
"""

import os
import sys

EXCUSE = (
    "internet's down and the engineer slot is 9-12, "
    "i'll hotspot from my phone but the vpn keeps dropping"
)

MAX_CHARS = 140
MAX_WORDS = 20


def main() -> int:
    # The grader runs `python3 main.py` with cwd = the repo root and
    # provides /output. MAKEFUN_OUTPUT_DIR exists only so the line can be
    # tested locally without a sandbox.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    words = EXCUSE.split()
    if len(words) > MAX_WORDS:
        print(f"entry is {len(words)} words, over the {MAX_WORDS}-word cap",
              file=sys.stderr)
        return 1
    if not 1 <= len(EXCUSE) <= MAX_CHARS:
        print(f"entry is {len(EXCUSE)} chars, outside the 1-140 gate",
              file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    print(f"wrote {path} ({len(words)} words, {len(EXCUSE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
