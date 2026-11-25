#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes one two-part micro-confession to /output/entry.txt.
Deterministic: fixed text, no randomness, no network, no input.
"""
import os

ENTRY = (
    "To: Grandma\n"
    "I sold the piano you taught me on to pay March rent and I still haven't told you."
)

def main():
    # Gate self-check (competition.yaml: gate valid, judge message cap 200):
    # exactly two parts, total 1-260 chars, message line <= 200 chars.
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert 1 <= len(ENTRY) <= 260, "entry must be 1-260 chars"
    assert len(lines[1]) <= 200, "message line must be at most 200 chars"
    assert lines[1].strip(), "message line must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt: {len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes")

if __name__ == "__main__":
    main()
