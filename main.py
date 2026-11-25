#!/usr/bin/env python3
"""One Line, One Chill — write exactly one line of horror to entry.txt.

Deterministic: the same bytes are written on every run.
Standard library only. No network.
"""

import os
from pathlib import Path

LINE = (
    "The baby monitor plays my daughter's lullaby at 3 a.m. every night "
    "in a voice that isn't hers, and she hums along in her sleep."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce: non-empty, a single line, at most 200 Unicode code points."""
    if not line:
        raise ValueError("line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def output_dir() -> Path:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(env) if env else Path("/output")


def main() -> None:
    validate(LINE)
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    data = (LINE + "\n").encode("utf-8")
    out_path.write_bytes(data)
    print(f"wrote {len(data)} bytes, {len(LINE)} characters to {out_path}")


if __name__ == "__main__":
    main()
