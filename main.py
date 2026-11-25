#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke, one line.

Writes a single joke about office life (under 200 characters) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set). Pure stdlib,
deterministic: the same line on every run.
"""

import os
import sys

# Original joke: the office printer's suspicious sense of timing.
# The twist lands on the human, not the machine: lying to a printer
# to get it to behave is the most office thing anyone can do.
LINE = "The printer only jams on urgent documents, so now I label everything 'not urgent' and lie to a machine."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not text:
        print("line is empty", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"line is {len(text)} chars, outside 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
