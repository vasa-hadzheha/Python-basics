"""Exercise 2.6 - Sum positive cells at even row / odd column index.
Original: Lab 7, Task 1.

Practises: double loops with a range step; verifying a total by eye.
"""

import random

random.seed(7)  # fixed seed so the matrix is the same every run

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

table = [[random.randint(-10, 20) for j in range(cols)] for i in range(rows)]

print("      " + "".join(f"{j:>7}" for j in range(cols)))
for i, row in enumerate(table):
    print(f"row {i} " + "".join(f"{cell:>7}" for cell in row))

total = 0
for i in range(0, rows, 2):  # even row indexes
    for j in range(1, cols, 2):  # odd column indexes
        if table[i][j] > 0:
            total += table[i][j]
            print(f"  + table[{i}][{j}] = {table[i][j]}")

print(f"Sum = {total}")
