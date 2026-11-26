"""Roast the Smart Fridge: one deterministic line, written fresh in this session.

Writes a single 138-character roast to /output/entry.txt (or to the path
named by ENTRY_OUTPUT, used only for local testing). Stdlib only, no
network, no randomness, no input files: the same bytes on every run.
"""

import os
from pathlib import Path

ROAST = (
    "My smart fridge filmed my 2am snack, uploaded it to the cloud, "
    "and now the whole internet knows I eat pickles over the sink like a raccoon"
)


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    # One line, no trailing newline: exactly the roast, byte-identical each run.
    output.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
