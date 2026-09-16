"""Exercise 1.12 - ln|a^n| + ln|a^(n-1)| + ... + ln|a^1|
Original: Lab 5, Task 1.

Practises: for with a negative step; guarding a domain; testing against
a closed-form formula.
"""

import math

a = float(input("Enter a non-zero real number a: "))
n = int(input("Enter a natural number n: "))

if a == 0:
    print("a must not be zero: ln(0) is undefined.")
elif n < 1:
    print("n must be at least 1 - otherwise there are no terms to add.")
else:
    total = 0.0
    for power in range(n, 0, -1):  # n, n-1, ..., 1
        total += math.log(math.fabs(a**power))

    print(f"Sum of {n} terms = {total:.6f}")

    # Because ln|a^k| = k * ln|a|, the whole sum equals
    # (1 + 2 + ... + n) * ln|a| = n(n+1)/2 * ln|a|.
    # Checking a loop against a closed form is a cheap, powerful test.
    expected = (n * (n + 1) / 2) * math.log(math.fabs(a))
    print(f"Closed form     = {expected:.6f}")
    print(f"Difference      = {math.fabs(total - expected):.2e}")
