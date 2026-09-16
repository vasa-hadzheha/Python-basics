"""Exercise 2.10 - Count the columns containing no zero.
Original: Lab 7, Task 5.

Practises: column-wise iteration, break as an optimisation, all().
"""

import random

random.seed(3)

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

table = [[random.randint(0, 4) for j in range(cols)] for i in range(rows)]

print("      " + "".join(f"{j:>4}" for j in range(cols)))
for i, row in enumerate(table):
    print(f"row {i} " + "".join(f"{cell:>4}" for cell in row))

# --- explicit version: you can put a print inside it --------------------
clean = 0
for j in range(cols):  # COLUMN is the outer loop
    has_zero = False
    for i in range(rows):  # walk DOWN the column
        if table[i][j] == 0:
            has_zero = True
            break  # settled; stop looking
    if not has_zero:
        clean += 1
        print(f"  column {j} has no zeros")

print(f"Columns without a zero: {clean}")

# --- concise version: read this, it is what experienced devs write ------
concise = sum(1 for j in range(cols) if all(table[i][j] != 0 for i in range(rows)))
print(f"Concise version agrees: {concise == clean}")

# --- the archive's mistake ---------------------------------------------
#   f = [0 if 0 in column else 1 for column in a]
# "for column in a" walks over ROWS, because a is a list of rows.
wrong = sum(1 for row in table if 0 not in row)
print(f"The archive's version counts ROWS without a zero instead: {wrong}")
