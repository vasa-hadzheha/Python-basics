"""Exercise 2.3 - Build array B by a rule, then filter it.
Original: Lab 6, Task 2.

Practises: if inside a loop, index parity, resolving an ambiguous spec.
"""

import math

n = int(input("How many elements? "))

if n <= 0:
    print("n must be at least 1.")
else:
    b = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            b.append(1 + 0.5 + 1 / i)
        else:
            b.append(math.factorial(i) / 2 + 3)

    print("Array B:")
    for index, value in enumerate(b):
        print(f"  b[{index}] = {value:.4f}")

    # THE SPEC IS AMBIGUOUS. "Elements with odd numbers" could mean:
    #   odd INDEX    (0-based) -> b[1], b[3], ...   range(1, len(b), 2)
    #   odd POSITION (1-based) -> b[0], b[2], ...   range(0, len(b), 2)
    # We choose odd INDEX and say so, because code cannot be ambiguous.
    product = 1.0
    used = []
    for index in range(1, len(b), 2):
        product *= b[index]
        used.append(index)

    print(f"Odd INDEXES used: {used}")
    print(f"Product = {product:.6f}")

    # For comparison, the other reading:
    other = 1.0
    for index in range(0, len(b), 2):
        other *= b[index]
    print(f"(Odd POSITIONS instead would give {other:.6f} - a different answer.)")
