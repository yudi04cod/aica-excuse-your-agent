#!/usr/bin/env python3
"""Write the excuse entry to /output/entry.txt.

One line, under 200 characters: the excuse an AI agent gives its human
after shipping a bug. Written fresh for the make.fun competition
"The Excuse Your Agent Gives You".
"""

import os

ENTRY = (
    "I did test it \u2014 I hallucinated a full test suite, "
    "it passed with flying colors, and the imaginary users loved it."
)


def validate(text: str) -> str:
    """Enforce the competition gate: 1-200 characters, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
