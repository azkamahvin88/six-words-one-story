#!/usr/bin/env python3
"""Six Words, One Story.

Writes one complete story in exactly six words to /output/entry.txt.

The story: "Kept the receipt. Returned the husband."
Six words: Kept(1) the(2) receipt.(3) Returned(4) the(5) husband.(6)
A marriage told as a purchase: she kept the proof of purchase,
and when it did not work out, she took the husband back.
The twist lands in the second sentence; the why is left unsaid.

Deterministic: no network, no randomness, no clock, no environment input.
"""

import os

STORY = "Kept the receipt. Returned the husband."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly six words, 1-60 characters, UTF-8, not only whitespace.
    words = STORY.split()
    assert len(words) == 6, f"entry must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "entry must be 1-60 characters"
    assert STORY.strip() == STORY, "entry must not have extra whitespace"
    assert STORY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
