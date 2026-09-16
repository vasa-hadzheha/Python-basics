"""Exercise 3.3 - Search a catalogue file, report once.
Original: Lab 11, Task 3.

Collect matches, THEN report. The archive prints inside the loop and had to
comment out its "nothing found" message with the note "IT LOOPS THE
MESSAGE" - because an else inside the loop fires per non-matching line.

Run from the repository root.
"""

from pathlib import Path

SOURCE = Path("data/songs.txt")
TARGET = Path("out/search_results.txt")

if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

query = input("Search for: ").strip()

if not query:
    print("An empty search would match every line. Give me something to look for.")
    raise SystemExit(0)

matches = []
total_lines = 0

with open(SOURCE, encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        line = line.strip()
        if not line:  # skip blanks
            continue
        total_lines += 1
        if query.lower() in line.lower():  # case-insensitive
            matches.append((line_number, line))

# Report AFTER the loop, so each message is printed exactly once.
print(f"\nSearched {total_lines} entries for {query!r}")

if not matches:
    print("  (nothing found)")
else:
    print(f"  {len(matches)} match(es):\n")
    print(f"  {'Line':>5}  {'Artist':<20}{'Title':<26}{'Year':>6}{'Length':>8}")
    print("  " + "-" * 66)
    for line_number, line in matches:
        artist, title, year, duration = line.split("|")
        print(f"  {line_number:>5}  {artist:<20}{title:<26}{year:>6}{duration:>8}")

    TARGET.parent.mkdir(exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        print(f"# search: {query}", file=f)
        for line_number, line in matches:
            print(f"{line_number}|{line}", file=f)
    print(f"\n  Written to {TARGET}")
