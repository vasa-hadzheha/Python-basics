"""Exercise 3.2 - Replace zeros with the file maximum, write the result.
Original: Lab 11, Task 2.

The exercise is really about OUTPUT FORMAT: if you cannot read your own
output back in, the format is wrong.

Run from the repository root.
"""

from pathlib import Path

SOURCE = Path("data/numbers_with_zeros.txt")
TARGET = Path("out/replaced.txt")

if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

values = []
with open(SOURCE, encoding="utf-8") as f:
    for line in f:
        values.extend(float(token) for token in line.split())

if not values:
    print("The file is empty - nothing to do.")
    raise SystemExit(0)

largest = max(values)
replaced = [largest if value == 0 else value for value in values]

TARGET.parent.mkdir(exist_ok=True)  # writing does not create the folder

# ONE VALUE PER LINE. The archive writes str(the_list), producing
# "[5.0, 22.0, 12.0, ...]" on a single line - a file that nothing can read
# back except eval(), which must never be pointed at a data file.
with open(TARGET, "w", encoding="utf-8") as f:
    for value in replaced:
        f.write(f"{value:g}\n")

print(f"Read           : {len(values)} values")
print(f"Largest value  : {largest:g}")
print(f"Zeros replaced : {values.count(0)}")
print(f"Wrote          : {TARGET}")

# --- the round-trip test, which is the point of the exercise -----------
with open(TARGET, encoding="utf-8") as f:
    readback = [float(line) for line in f]

print(f"\nRead back      : {len(readback)} values")
print(f"Round-trips    : {readback == replaced}")
assert readback == replaced, "output format must be re-readable"
