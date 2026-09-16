"""Exercise 2.12 - Approximate a definite integral by left rectangles.
Original: Lab 8, Task 2.

Practises: passing a function as an argument; checking a numerical method
against a known answer.

The archive's version is NOT an integrator - it computes
    (b - a) * sqrt(4a + sin(sqrt(a^3)))
which is a single rectangle spanning the whole interval (the n = 1 case).
"""

import math


def integrate_left(func, a, b, n):
    """Approximate the integral of func from a to b using n left rectangles.

    Height is taken from the LEFT edge of each strip, so the sample points
    are a, a+h, ..., a+(n-1)h  -  that is range(n), not range(n+1).
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        total += func(a + i * h)
    return total * h


def square(x):
    return x**2


def lab_function(x):
    """The integrand from the original lab statement."""
    return math.sqrt(4 * x + math.sin(math.sqrt(x**3)))


# --- check the method against an answer we know exactly ----------------
# The integral of x^2 from 0 to 1 is exactly 1/3.
print("Integral of x^2 from 0 to 1  (exact value 1/3 = 0.333333):")
for n in (1, 10, 100, 1000, 100000):
    approx = integrate_left(square, 0, 1, n)
    print(f"  n = {n:>6}  ->  {approx:.6f}   error {abs(approx - 1 / 3):.2e}")

print()
print("Left rectangles UNDERSHOOT a rising curve, so every value is below")
print("1/3 and the error shrinks roughly in proportion to 1/n.")

# --- the archive's single-rectangle version, for comparison ------------
print()
print("Integral of the lab function from 0 to 3:")
print(f"  n = 1     (the archive's formula) -> {integrate_left(lab_function, 0, 3, 1):.6f}")
print(f"  n = 100000                        -> {integrate_left(lab_function, 0, 3, 100000):.6f}")

# --- tests -------------------------------------------------------------
assert abs(integrate_left(square, 0, 1, 100000) - 1 / 3) < 1e-4
assert integrate_left(lambda x: 1, 0, 5, 10) == 5.0  # area of a 5x1 rectangle
print()
print("All tests passed.")
