#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line from the agent
that broke production, written to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run.
Standard library only, no network.
"""

import os

LINE = (
    "I pushed untested code to production, wiped the database, "
    "and my rollback plan was hoping nobody noticed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
