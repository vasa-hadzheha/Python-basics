"""Lesson 3 - guard first, compute second. (Original Lab 4, Task 1 extended.)

Run me:  python3 examples/meeting-1/03_triangle_validated.py
Try 3 4 5  (area 6), then 1 2 50 (not a triangle), then 0 4 5 (bad input).
"""

import math

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

# Guard first, compute second. If the data is bad, say so and stop.
if a <= 0 or b <= 0 or c <= 0:
    print("A side length must be positive.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("These lengths cannot form a triangle.")
else:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Area = {area:.4f}")
