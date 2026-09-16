"""Exercise 3.1 - Largest of the negative numbers in a file.
Original: Lab 11, Task 1.

Run from the repository root:
    python3 exercise-bank/meeting-3/ex_3_01_largest_negative.py
"""

from pathlib import Path

SOURCE = Path("data/numbers.txt")

if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

values = []
skipped = []

with open(SOURCE, encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        # Bare .split() splits on ANY whitespace and drops empty pieces.
        # .split(' ') would yield '' for a double space -> float('') raises.
        for token in line.split():
            try:
                values.append(float(token))
            except ValueError:
                skipped.append((line_number, token))

print(f"Read {len(values)} numbers from {SOURCE}")
for line_number, token in skipped:
    print(f"  line {line_number}: skipped {token!r} - not a number")

negatives = [v for v in values if v < 0]

# THE GUARD: max([]) raises "ValueError: max() arg is an empty sequence".
# The archive calls max(s) unguarded, so it crashes on a file with no
# negative numbers.
if negatives:
    print(f"Negative numbers : {negatives}")
    print(f"Largest negative : {max(negatives)}")
else:
    print("There are no negative numbers in this file.")

# Proof the guard works - the same logic on data with no negatives:
empty = [v for v in [1.0, 2.0, 3.0] if v < 0]
print(f"\nSame code on all-positive data: ", end="")
print(max(empty) if empty else "handled cleanly, no crash")
