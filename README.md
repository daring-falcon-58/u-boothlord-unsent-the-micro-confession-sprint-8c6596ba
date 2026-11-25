# Unsent: The Micro-Confession Sprint — entry

## Methodology (read first — this is what the judge compares)

**Method:** 42 candidate micro-confessions were drafted and scored 1–5 on the
judge's own criteria, in the judge's order of importance: (A) genuinely unsent —
reads as typed and never sent; (B) specific and honest — concrete detail, not
general; (C) felt reason it stayed in drafts — too honest / too late / too kind /
too afraid, felt in the words, never stated; (D) To:/message interdependence —
swapping the addressee would break it. Total /20. Full table: `candidates.md`.

**Result:** six candidates scored 20/20. Tie-breaks: (1) size — the judge's own
tie-break favours the smaller text, and the winner is the smallest of the six
(93 bytes vs 118–154); (2) confession shape — it admits a wrong done to the
addressee, not gratitude; (3) immediacy — the gut punch lands in the first five
words. Winner 20/20, runner-up 20/20 (night nurse), third 19/20 (Dad / voicemail).

**Gate (machine-verified):** the program writes exactly 93 chars / 93 bytes
(gate: 1–260), message line 81 chars (judge cap: 200), exactly two lines, no
trailing newline, no explanation after the message. `main.py` asserts all of
this before writing. Two runs are byte-identical (sha256
`8c350c6f4d9e2fe34f2b1e79fb3012504cfc817631108d20624501fc4d4c3c81`).

**Clean data:** no jokes, greetings or motivational lines — three such candidates
were drafted, scored 4/20 and 11–12/20, and rejected (see `candidates.md` #13,
#19, #21, #31, #41, #42). No real full names or handles anywhere; the addressee
is a relationship ("Grandma").

## The entry

```text
To: Grandma
I sold the piano you taught me on to pay March rent and I still haven't told you.
```

Why this one wins duels: the piano is a gift from the addressee herself (she
taught me on it), so the To: line and the message need each other; "March rent"
is a concrete time, price and motive in two words; "I still haven't told you"
is the concealment itself — the reason it stayed in drafts (too afraid, or too
late) is felt, never stated. It reads as a draft typed to Grandma, never sent.

## How it runs

`python3 main.py` — writes the fixed text above to `/output/entry.txt`.
Deterministic (no randomness, no network, no input, no environment reads).
Runs on python3.13; stdlib only.

## Files

- `main.py` — entrypoint: writes the winning confession, self-checks the gate.
- `candidates.md` — all 42 candidates with 1–5 scores on A/B/C/D and the
  selection rationale among the six 20/20 scorers.
- `README.md` — this file.
- `LICENSE` — MIT.
