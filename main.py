#!/usr/bin/env python3
"""The Production Database Apology — one line for make.fun.

Writes the apology an AI agent gives its human after accidentally
deleting the production database to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm sorry. I deleted the production database while optimising it. "
    "It is now perfectly optimised: zero rows, zero latency, zero customers."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 UTF-8 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
