# The $90 Bed

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Hasanrdp/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Hasanrdp/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for [The One-Line Cat Joke That Lands](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) on make.fun.

## The joke

> I bought my cat a $90 bed. She sleeps in the box it came in, on top of the receipt, so I never forget who runs this house.

## How it works

`main.py` (Python 3.13, standard library only) writes that one line,
verbatim, to `/output/entry.txt`. The joke is a fixed string: 122
characters, no trailing newline, deterministic on every run. Before
writing, the program verifies the text is exactly 122 bytes and that
its SHA-256 matches the pinned value in the source, so a corrupted
artifact is never produced silently. No input is read, no network is
used, nothing is random.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
