#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

# The approval is warm and the dread is quiet: everything passes, which is exactly why the pager is coming.
TEXT = """LGTM — tests pass, diff is clean, and I am quietly certain this is the last calm moment before the pager wakes us at 3am."""

MAX_CHARS = 140

def main():
    # The bounty scores one code review comment of at most 140 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.startswith("LGTM"), "entry must approve the pull request"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
