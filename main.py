#!/usr/bin/env python3
"""The Funniest Out-of-Office - make.fun entry.

Writes a single line of out-of-office auto-reply (140 characters or
fewer) to /output/entry.txt and prints it to stdout. Deterministic,
no network, no dependencies.
"""

import os

ENTRY = "I'm out of office until Monday. My inbox has unionised and gone on strike — your email is holding a tiny placard."

MAX_CHARS = 140


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
