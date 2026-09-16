"""Exercise 2.9 - Sort the odd-numbered rows of a square matrix ascending.
Original: Lab 7, Task 4.

Practises: in-place .sort() on a nested list.
"""

import random

random.seed(5)

n = int(input("Size of the square matrix: "))
m = [[random.randint(-20, 20) for j in range(n)] for i in range(n)]


def show(label, matrix):
    print(f"{label}:")
    for i, row in enumerate(matrix):
        print(f"  row {i} " + "".join(f"{cell:>6}" for cell in row))


show("Before", m)

# m[i] IS a list, so it has .sort(), and sorting it in place changes the
# matrix directly. Here the copy-vs-reference behaviour works FOR us.
#
# "Odd rows" is ambiguous again: we take odd INDEXES (1, 3, 5, ...).
# The archive's own comment notes range(0, n, 2) for 1-based counting.
for i in range(1, n, 2):
    m[i].sort()

show("After (odd INDEXES sorted ascending)", m)
