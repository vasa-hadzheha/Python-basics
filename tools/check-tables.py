"""Check every markdown table has a consistent number of columns.

Usage, from the repository root:
    python3 tools/check-tables.py

A row with a missing final cell, or a raw "|" inside a cell, silently
renders as a broken or phantom column on GitHub - and you only notice by
looking. This catches both. Pipes escaped as \\| are not counted, which is
how you write a literal pipe inside a cell.
"""

import re
import sys
from pathlib import Path


def unescaped_pipes(line):
    """Count | characters that are not escaped with a backslash."""
    return len(re.findall(r"(?<!\\)\|", line))


def main():
    bad = []
    checked = 0
    for path in sorted(Path(".").rglob("*.md")):
        if ".git" in path.parts:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        block, start = [], None
        for number, line in enumerate(lines, 1):
            if line.strip().startswith("|"):
                start = number if start is None else start
                block.append((number, line))
            else:
                if len(block) >= 2:
                    checked += 1
                    counts = {unescaped_pipes(l) for _, l in block}
                    if len(counts) > 1:
                        bad.append((path, start, [(n, unescaped_pipes(l)) for n, l in block]))
                block, start = [], None

    print(f"checked {checked} tables")
    if bad:
        print(f"\n{len(bad)} RAGGED:")
        for path, start, detail in bad:
            print(f"  {path}: table starting line {start}")
            for number, count in detail:
                print(f"      line {number}: {count} pipes")
        sys.exit(1)
    print("every table has a consistent number of columns")


if __name__ == "__main__":
    main()
