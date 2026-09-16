"""Lesson 7 - count the columns that contain no zero.
Original: Lab 7, Task 5.

The interesting part: to work column-wise, the loops swap round.

Run me:  python3 examples/meeting-2/07_columns_without_zero.py
"""

import random

random.seed(3)
rows, cols = 4, 6
table = [[random.randint(0, 4) for j in range(cols)] for i in range(rows)]

print("      " + "".join(f"{j:>4}" for j in range(cols)))
for i, row in enumerate(table):
    print(f"row {i} " + "".join(f"{cell:>4}" for cell in row))

# --- the explicit version: readable, and you can put a print inside ------
clean_columns = 0
for j in range(cols):  # COLUMN is the outer loop now
    has_zero = False
    for i in range(rows):  # walk DOWN the column
        if table[i][j] == 0:
            has_zero = True
            break  # one zero settles it; stop looking
    if not has_zero:
        clean_columns += 1
        print(f"  column {j} has no zeros")

print(f"Columns without a zero: {clean_columns}")

# --- the Pythonic version: what an experienced dev (or an AI) writes -----
# all(...) is True when every item is True, and it short-circuits exactly
# like the break above.
concise = sum(1 for j in range(cols) if all(table[i][j] != 0 for i in range(rows)))
print(f"Same answer, concise version: {concise}")

# --- the BROKEN version from the archive, for comparison ----------------
#   f = [0 if 0 in column else 1 for column in a]
# "for column in a" iterates over ROWS, because a is a list of rows.
# The variable is named "column" and holds a row: a bug in waiting.
broken = sum(1 for row in table if 0 not in row)
print(f"The archive's mistake counts ROWS without a zero: {broken}")
print("Same code shape, different question. Always read what the code DOES.")
