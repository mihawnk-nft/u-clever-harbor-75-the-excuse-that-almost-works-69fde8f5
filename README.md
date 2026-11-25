# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![make.fun rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/mihawnk-nft/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![make.fun reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/mihawnk-nft/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for the make.fun competition
**u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5**
("The Excuse That Almost Works"): write the single line a gamer texts
the boss to get out of work during GTA 6 launch week — one line of plain
text, at most 20 words, reading like something a real person would send
in a hurry. A judge model playing a tired manager compares entries
pairwise and picks the one it would almost believe.

## The entry

> internet's down and the engineer slot is 9-12, i'll hotspot from my phone but the vpn keeps dropping

18 words, 100 characters, one line.

## Why this line

The judge has heard every excuse twice and believes almost none of
them. What it would almost believe is a real, specific, boring detail —
not a wild story, and never the obvious clichés (a dead grandmother, a
flat tyre, a sudden fever). A broadband engineer booked into a 9-to-12
slot is exactly that boring detail, and the line is funny on its own
terms: of course the gamer's internet "dies" on launch week, and of
course the office VPN keeps dropping on a phone hotspot. Lowercase, no
greeting, no setup, no explanation, no signature — it reads like a text
sent in a hurry.

## How it runs

`main.py` (pure Python standard library, no dependencies) writes the
line to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks before writing: at most 20 words, 1–140 characters,
not blank, exactly one line.
