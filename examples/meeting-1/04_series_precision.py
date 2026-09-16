"""Lesson 4 - loop until precise enough. (Original Lab 5, Task 3.)

    ln(1 - x) = -( x + x^2/2 + x^3/3 + ... )    for |x| < 1

Run me:  python3 examples/meeting-1/04_series_precision.py
Try x=0.5 and eps=0.000001.  Then try x=1.5 and see the guard refuse it.
"""

import math

x = float(input("x (between -1 and 1): "))
eps = float(input("precision, e.g. 0.000001: "))

if math.fabs(x) >= 1:
    # Without this guard the terms GROW instead of shrinking and the
    # loop below never ends. The original archive version omits it.
    print("The series only converges for |x| < 1.")
elif eps <= 0:
    print("Precision must be greater than 0.")
else:
    total = 0.0
    k = 1
    term = x  # the first term
    passes = 0

    while math.fabs(term) > eps:  # stop when terms stop mattering
        total -= term  # the series is negated
        k += 1
        term = (x**k) / k  # build the next term
        passes += 1

    print(f"Series result : {total:.8f}   ({passes} terms used)")
    print(f"math.log(1-x) : {math.log(1 - x):.8f}")
    print(f"Difference    : {math.fabs(total - math.log(1 - x)):.2e}")
