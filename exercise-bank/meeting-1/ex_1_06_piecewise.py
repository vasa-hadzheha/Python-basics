"""Exercise 1.6 - A piecewise function.
Original: Lab 4, Task 4.

    y = ln|x| - n     if x <= n
    y = cos(x * n)    if x > n

Practises: if/else, math.log, math.fabs, guarding a domain.
"""

import math

x = float(input("Enter x: "))
n = float(input("Enter n: "))

if x == 0:
    # ln|0| is undefined. Refuse clearly instead of crashing with ValueError.
    print("x must not be 0: ln|0| is undefined.")
elif x <= n:
    # One branch covers both "x < n" and "x = n" from the original statement,
    # because the formula is the same for each.
    y = math.log(math.fabs(x)) - n
    print(f"y = ln|{x}| - {n} = {y:.6f}")
else:
    y = math.cos(x * n)
    print(f"y = cos({x} * {n}) = {y:.6f}")
