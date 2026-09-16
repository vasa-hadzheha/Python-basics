"""Lesson 2 - a piecewise function. (Original Lab 4, Task 4.)

    y = ln|x| - n    if x <= n
    y = cos(x * n)   if x > n

Run me:  python3 examples/meeting-1/02_piecewise.py
This one asks you to type two numbers. Try x=2, n=5.
"""

import math

x = float(input("Enter x: "))  # float: could be 2.5
n = float(input("Enter n: "))

if x == 0:
    # ln(0) is undefined, so refuse rather than crash.
    print("x must not be 0: ln|0| is undefined.")
elif x <= n:
    y = math.log(math.fabs(x)) - n  # math.fabs = absolute value
    print(f"y = {y:.6f}   (used the ln branch, because x <= n)")
else:
    y = math.cos(x * n)
    print(f"y = {y:.6f}   (used the cos branch, because x > n)")
