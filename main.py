#!/usr/bin/env python3
"""Warning label for humans — one line, big laugh.

Writes the entry line to /output/entry.txt with no trailing newline,
so the file is exactly the 113-character warning label.
"""

import hashlib
import os
import sys

LINE = (
    "WARNING: This unit overheats during small talk, "
    "leaks during sad movies, and cannot be switched off "
    "\u2014 only muted."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    # Round-trip guard: what we wrote must be exactly the line, byte for byte.
    with open(OUTPUT_PATH, "rb") as handle:
        assert handle.read() == data, "output does not match the entry line"
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}")
    print(f"sha256: {digest}")
    print(f"chars: {len(LINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
