"""Lesson 8 - a piecewise function wrapped in a def.
Original: Lab 8, Task 1 - which contains a real operator-precedence bug.

Run me:  python3 examples/meeting-2/08_piecewise_function.py
Try a=1, b=1.
"""

import math


def f(x, y):
    """Return f(x, y) as defined in Lab 8, Task 1.

    x > 0 and y > 0  ->  x^3 + sqrt(x^2 + y^4)
    x > 0 and y < 0  ->  (x^2 - 2x + sqrt(x)) / x^(3/5)
    otherwise        ->  sin(x * y)
    """
    if x > 0 and y > 0:
        return x**3 + math.sqrt(x**2 + y**4)
    elif x > 0 and y < 0:
        return (x**2 - 2 * x + math.sqrt(x)) / x ** (3 / 5)
    else:
        return math.sin(x * y)


a = float(input("a = "))
b = float(input("b = "))

print(f"f(a, b) = {f(a, b):.6f}")
print(f"f(2, a) = {f(2, a):.6f}")

u = f(a, b) + f(2, a) + 2  # called three times, defined once
print(f"U = {u:.6f}")

# --- the archive's bug, demonstrated ------------------------------------
print()
print("The original archive wrote  (x**2 + y**4) ** 1/2  for a square root.")
print("'**' binds tighter than '/', so Python computes (expr ** 1) / 2:")
value = 1.0**2 + 1.0**4
print(f"  (x**2 + y**4)       = {value}")
print(f"  ... ** 1/2  gives   = {value**1 / 2}   <- the archive's answer")
print(f"  ... ** 0.5  gives   = {value**0.5}   <- an actual square root")
print("No error, a plausible number, wrong result. A classic review find.")
