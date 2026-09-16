"""Exercise 3.4 - Pair negatives from line 1 with positives from line 2.
Original: archive Checker/.

Practises: line-indexed parsing, and zip() instead of two near-identical
branches.

THE ARCHIVE'S BUG: its else branch loops "for i in range(len(x))" and
indexes y[i]. When y is the shorter list that raises IndexError. zip()
cannot have this bug, because it stops at the shorter sequence.

Run from the repository root.
"""

from pathlib import Path

SOURCE = Path("data/points.txt")

if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

x_values = []
y_values = []

with open(SOURCE, encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        numbers = [float(token) for token in line.split()]
        if line_number == 1:
            x_values = [v for v in numbers if v < 0]  # negatives from line 1
        elif line_number == 2:
            y_values = [v for v in numbers if v > 0]  # positives from line 2

print(f"x (negatives from line 1): {x_values}")
print(f"y (positives from line 2): {y_values}")

# zip stops at the shorter list automatically - no length branching needed.
points = list(zip(x_values, y_values))

print(f"\nPaired {len(points)} point(s) "
      f"(limited by the shorter list: {min(len(x_values), len(y_values))})")
for i, (x, y) in enumerate(points, start=1):
    print(f"  Point {i} = ({x:g}, {y:g})")

unused_x = len(x_values) - len(points)
unused_y = len(y_values) - len(points)
if unused_x or unused_y:
    print(f"\nUnpaired: {unused_x} x-value(s), {unused_y} y-value(s)")
    print("Reporting the leftovers matters - silently dropping them is data loss.")

# --- tests -------------------------------------------------------------
assert list(zip([1, 2, 3], [9, 8])) == [(1, 9), (2, 8)], "zip stops at the shorter"
assert list(zip([], [1, 2])) == []
print("\nAll tests passed.")
