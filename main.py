#!/usr/bin/env python3
"""The One-Line Laugh entry: write one funny line to /output/entry.txt."""

import os

LINE = "The Wi-Fi only drops when I'm about to win \u2014 my router has a gambling problem."


def main():
    # Gate: one sentence, 1-200 characters, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
