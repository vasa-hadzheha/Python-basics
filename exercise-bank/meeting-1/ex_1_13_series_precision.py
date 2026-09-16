"""Exercise 1.13 - Sum a series until the terms stop mattering.
Original: Lab 5, Task 3.

    ln(1 - x) = -( x + x^2/2 + x^3/3 + ... )    valid for |x| < 1

Practises: while driven by precision rather than by a count; the guard
that stops it hanging.

THE BUG IN THE ORIGINAL: it has no |x| < 1 check. For x = 1.5 the terms
GROW, "fabs(term) > eps" is never false, and the program hangs forever.
"""

import math

x = float(input("x (must satisfy |x| < 1): "))
eps = float(input("precision eps (e.g. 0.000001): "))

if math.fabs(x) >= 1:
    print("Refused: the series only converges for |x| < 1.")
    print("With |x| >= 1 the terms grow and the loop would never end.")
elif eps <= 0:
    print("Refused: eps must be greater than 0, or the loop never ends.")
else:
    total = 0.0
    k = 1
    term = x  # the first term
    terms_used = 0

    while math.fabs(term) > eps:
        total -= term  # the series is negated
        k += 1
        term = (x**k) / k  # the next term
        terms_used += 1

    reference = math.log(1 - x)
    difference = math.fabs(total - reference)

    print(f"Series sum    = {total:.10f}   ({terms_used} terms)")
    print(f"math.log(1-x) = {reference:.10f}")
    print(f"Difference    = {difference:.2e}")

    if difference < eps * 10:
        print("The identity holds to the requested precision.")
    else:
        print("The identity does NOT hold to the requested precision.")
