"""Exercise 2.11 - Order the rows by the sum of their positive even elements.
Original: Lab 7, Task 6.

Practises: sorting by a computed key, and why a magic sentinel is a bug.
"""

import random

random.seed(13)

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

table = [[random.randint(-5, 20) for j in range(cols)] for i in range(rows)]


def even_positive_sum(row):
    """Sum of the elements of row that are both positive and even."""
    return sum(value for value in row if value > 0 and value % 2 == 0)


print("Original matrix, with each row's score:")
for i, row in enumerate(table):
    print(f"  row {i} " + "".join(f"{c:>5}" for c in row) + f"   score={even_positive_sum(row)}")

# The clean way: sort by a computed key. No mutation, no sentinel.
ordered = sorted(table, key=even_positive_sum)

print("\nRows ordered by score, smallest first:")
for row in ordered:
    print("  " + "".join(f"{c:>5}" for c in row) + f"   score={even_positive_sum(row)}")

# --- why the archive's approach is fragile -----------------------------
# It repeatedly takes the row with the smallest score, then overwrites that
# score with 10000000 so it cannot be picked again:
#
#     g.append(a[h.index(min(h))])
#     h[h.index(min(h))] = 10000000
#
# It works - until a row genuinely scores above 10,000,000, at which point
# the ordering silently breaks. A magic sentinel that can collide with real
# data is a real bug class. sorted(key=...) cannot have this problem.
print()
print("Note: the archive marks used rows with the sentinel 10000000.")
print("Any row scoring above that value would silently break the order.")
