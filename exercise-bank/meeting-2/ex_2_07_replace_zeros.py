"""Exercise 2.7 - Replace every zero in A with the matching element of B.
Original: Lab 7, Task 2.

Practises: two matrices walked in step.
"""

import random

random.seed(11)

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

print("Enter matrix A (type some zeros to see the replacement):")
a = [
    [float(input(f"a[{i}][{j}] = ")) for j in range(cols)]  #
    for i in range(rows)
]

b = [[float(random.randint(1, 100)) for j in range(cols)] for i in range(rows)]


def show(label, matrix):
    print(f"{label}:")
    for row in matrix:
        print("  " + "".join(f"{cell:>9.2f}" for cell in row))


show("Matrix A (before)", a)
show("Matrix B", b)

replaced = 0
for i in range(rows):
    for j in range(cols):
        # These are floats. A value TYPED as 0 is exactly 0.0, so == works.
        # A value that was COMPUTED to nearly zero would not match; for that
        # you would need math.fabs(a[i][j]) < eps. We mean exact zero here.
        if a[i][j] == 0:
            a[i][j] = b[i][j]
            replaced += 1

show("Matrix A (after)", a)
print(f"Replaced {replaced} zero(s).")
