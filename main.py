#!/usr/bin/env python3
"""Five Seconds to Explain the Glass (u-po-pu-five-seconds-to-explain-the-glass-934d9949).

Writes ONE sentence -- a pet cat's 5-second defense of the glass it swept
off the table -- to /output/entry.txt.

Winning sentence (25/25 in candidates.md scoring, angle: impersonation /
identity theft -- the glass committed the crime, the cat enforces house law):

    It was impersonating my water bowl, and identity theft is a serious
    crime in this house.

Stdlib only. Fully deterministic: the same bytes are written on every run.
"""

import os

SENTENCE = (
    "It was impersonating my water bowl, and identity theft "
    "is a serious crime in this house."
)

OUTPUT_PATH = "/output/entry.txt"

# File content is the sentence plus exactly one trailing newline.
MAX_FILE_CHARS = 200


def validate(sentence: str) -> str:
    """Enforce the bounty rules before anything is written.

    Returns the exact sentence to write, or raises ValueError.
    """
    text = sentence.strip()
    if not text:
        raise ValueError("sentence must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if len(text) + 1 > MAX_FILE_CHARS:  # +1 for the trailing newline
        raise ValueError("entry file must be at most 200 characters")
    return text


def main() -> None:
    sentence = validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(sentence + "\n")


if __name__ == "__main__":
    main()
