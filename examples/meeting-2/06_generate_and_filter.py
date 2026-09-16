"""Lesson 6 - generate an array by a rule, then filter it.
Original: Lab 6, Task 2.

Run me:  python3 examples/meeting-2/06_generate_and_filter.py
Try n=5.
"""

import math

n = int(input("How many elements? "))

if n <= 0:
    print("n must be at least 1.")
else:
    b = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            b.append(1 + 0.5 + 1 / i)  # even i
        else:
            b.append(math.factorial(i) / 2 + 3)  # odd i

    print("Array B:")
    for index, value in enumerate(b):
        print(f"  b[{index}] = {value:.4f}")

    # The product of the elements at ODD INDEXES (1, 3, 5, ...).
    #
    # The original lab says "elements with odd numbers", which is ambiguous:
    #   odd INDEX    (0-based) -> range(1, len(b), 2) -> b[1], b[3], ...
    #   odd POSITION (1-based) -> range(0, len(b), 2) -> b[0], b[2], ...
    # We state which one we mean, because the code cannot be ambiguous.
    product = 1.0
    picked = []
    for index in range(1, len(b), 2):
        product *= b[index]
        picked.append(index)

    print(f"Odd indexes used: {picked}")
    print(f"Product of odd-indexed elements = {product:.6f}")
