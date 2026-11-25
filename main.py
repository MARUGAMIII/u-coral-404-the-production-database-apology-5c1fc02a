"""The Production Database Apology — make.fun bounty entry.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

The line is a single fixed string, written verbatim. No input is read, no
network is used, no randomness is involved, so every run produces the
exact same output. Standard library only.
"""

import os

ENTRY = (
    "Sorry, I deleted the production database. "
    "Good news: the backups were stored inside it, "
    "so I only had to delete everything once."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    assert ENTRY.isascii(), "entry must be plain ASCII"
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
