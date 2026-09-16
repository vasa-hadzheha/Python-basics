"""Lesson 10 - search a catalogue file.
Original: Lab 11, Task 3.

Collect matches, THEN report. The archive prints inside the loop and had to
comment out its "nothing found" message because an else inside the loop
fires once per non-matching line.

Run me from the repository root:
    python3 examples/meeting-3/10_search_catalogue.py
"""

QUERY = "1975"

matches = []
with open("data/songs.txt", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        line = line.strip()
        if not line:  # skip blank lines
            continue
        if QUERY.lower() in line.lower():  # case-insensitive
            matches.append((line_number, line))

print(f"{len(matches)} match(es) for {QUERY!r}:")
for line_number, line in matches:
    artist, title, year, duration = line.split("|")
    print(f"  line {line_number}: {artist} - {title} ({year}, {duration})")

if not matches:
    print("  (nothing found)")  # printed ONCE, after the loop
