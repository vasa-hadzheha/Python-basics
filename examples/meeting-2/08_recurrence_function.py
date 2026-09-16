"""Lesson 8 - one function, evaluated at several points.
Original: Lab 8, Task 3.

    a[0] = 9, a[1] = 35, a[i] = sin(a[i-1] + cos(a[i-2]))

Run me:  python3 examples/meeting-2/08_recurrence_function.py
No input needed.
"""

import math


def g(n):
    """Return the nth term of a[i] = sin(a[i-1] + cos(a[i-2])), a[0]=9, a[1]=35."""
    if n < 0:
        # Refuse an impossible request rather than return nonsense.
        raise ValueError("n must be 0 or more")

    a = [9.0, 35.0]
    if n <= 1:
        return a[n]

    for i in range(2, n + 1):
        a.append(math.sin(a[i - 1] + math.cos(a[i - 2])))
    return a[n]


print(f"g(0)  = {g(0):.6f}")
print(f"g(1)  = {g(1):.6f}")
print(f"g(7)  = {g(7):.6f}")
print(f"g(9)  = {g(9):.6f}")
print(f"S = g(7) + g(9) = {g(7) + g(9):.6f}")

# The archive version returned "el", the loop's last value. For n <= 1 the
# loop never runs, so "el" does not exist -> UnboundLocalError. Returning
# a[n] is both correct and clearer about intent.
print()
try:
    print(f"g(-1) -> {g(-1)}")
except ValueError as error:
    print(f"g(-1) raised ValueError as designed: {error}")
