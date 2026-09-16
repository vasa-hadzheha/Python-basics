"""Exercise 2.8 - Compute A.x and check whether A.x = b.
Original: Lab 7, Task 3.

Practises: nested loops with sum(); comparing float vectors properly.

The original archive author wrote "I do not understand the condition
'check whether Ax = b'". The answer is: compare element by element with a
tolerance, because these are floats. That was a good question to ask.
"""

import math

n = int(input("Number of matrix rows (n): "))
m = int(input("Vector dimension / matrix columns (m): "))

if n <= 0 or m <= 0:
    print("Both dimensions must be at least 1.")
else:
    x = [float(input(f"x[{j}] = ")) for j in range(m)]
    a = [[float(input(f"A[{i}][{j}] = ")) for j in range(m)] for i in range(n)]
    b = [float(input(f"b[{i}] = ")) for i in range(n)]

    print(f"Vector x = {x}")
    print("Matrix A:")
    for row in a:
        print("  " + "".join(f"{cell:>9.2f}" for cell in row))
    print(f"Vector b = {b}")

    # Row i of the product is the dot product of row i with x.
    # The matrix has m columns and x has m elements, so the indexes line up.
    result = []
    for i in range(n):
        result.append(sum(a[i][j] * x[j] for j in range(m)))

    print(f"A.x = {[round(v, 6) for v in result]}")

    # NEVER "result == b" for floats. Compare with a tolerance.
    eps = 1e-9
    equal = all(math.fabs(p - q) < eps for p, q in zip(result, b))

    print(f"A.x = b ?  {equal}")
    if not equal:
        print("Differences per element:")
        for i, (p, q) in enumerate(zip(result, b)):
            print(f"  row {i}: {p:.6f} vs {q:.6f}   diff {math.fabs(p - q):.2e}")
