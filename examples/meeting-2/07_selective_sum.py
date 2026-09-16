"""Lesson 7 - sum the positive cells at even row index and odd column index.
Original: Lab 7, Task 1.

Run me:  python3 examples/meeting-2/07_selective_sum.py
No input needed - the seed makes it reproducible.
"""

import random

random.seed(7)  # fixed seed: the same "random" matrix every run

rows, cols = 4, 5
table = [[random.randint(-10, 20) for j in range(cols)] for i in range(rows)]

# Show it with row and column numbers so the answer can be checked by eye.
print("      " + "".join(f"{j:>7}" for j in range(cols)))
for i, row in enumerate(table):
    print(f"row {i} " + "".join(f"{cell:>7}" for cell in row))

total = 0
for i in range(0, rows, 2):  # even row indexes:    0, 2, 4, ...
    for j in range(1, cols, 2):  # odd column indexes:  1, 3, 5, ...
        if table[i][j] > 0:  # positive only
            total += table[i][j]
            # Printing each contribution is not decoration - it is how you
            # verify the total against the printed matrix above.
            print(f"  + table[{i}][{j}] = {table[i][j]}")

print(f"Sum = {total}")
