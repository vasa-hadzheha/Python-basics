"""Lesson 5 - "for" instead of a hand-rolled counter. (Original Lab 5, Task 1.)

    ln|a^n| + ln|a^(n-1)| + ... + ln|a^1|

Run me:  python3 examples/meeting-1/05_sum_of_logs.py
Try a=2, n=3  ->  4.158883
"""

import math

a = float(input("Enter a non-zero real number a: "))
n = int(input("Enter a natural number n: "))

if a == 0:
    print("a must not be zero: ln(0) is undefined.")
elif n < 1:
    print("n must be at least 1.")
else:
    total = 0.0
    for power in range(n, 0, -1):  # n, n-1, ..., 1  (counting down)
        total += math.log(math.fabs(a**power))

    # n is untouched, so we can still report it:
    print(f"Sum of {n} terms = {total:.6f}")

    # Cross-check against the closed form: ln|a^k| = k*ln|a|,
    # so the whole sum is (1+2+...+n) * ln|a| = n(n+1)/2 * ln|a|.
    expected = (n * (n + 1) / 2) * math.log(math.fabs(a))
    print(f"Closed-form check = {expected:.6f}")
