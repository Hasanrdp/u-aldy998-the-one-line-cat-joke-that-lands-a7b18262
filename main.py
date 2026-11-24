"""The One-Line Cat Joke That Lands.

Writes a single one-line joke about cats to /output/entry.txt.

The joke is a fixed string, written verbatim. The program checks it
before writing: exactly 122 bytes, UTF-8, and its sha256 must match
the pinned value below. If the check fails, it writes nothing and
exits non-zero, so a bad artifact can never be produced silently.

No input is read, no network is used, no randomness is involved:
every run writes the same 122 bytes.
"""

import hashlib
import os
import sys

JOKE = (
    "I bought my cat a $90 bed. She sleeps in the box it came in, "
    "on top of the receipt, so I never forget who runs this house."
)

EXPECTED_BYTES = 122
EXPECTED_SHA256 = "03570d1924b960d178854812526e96b31a076127c3b30a7eac079e5177538324"


def main() -> int:
    text = JOKE
    data = text.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        print(f"refusing: joke is {len(data)} bytes, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        print("refusing: joke sha256 does not match the pinned value",
              file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200) or not text.strip():
        print("refusing: joke fails the 1-200 character gate", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
