"""Lesson 3 - is the triangle right-angled? (Original Lab 4, Task 3.)

Two vectors are perpendicular exactly when their dot product is zero.

Run me:  python3 examples/meeting-1/03_right_triangle.py
No input needed. Change the coordinates and re-run.
"""

import math

x1, y1 = 0.0, 0.0  # <- assigning several variables on one line
x2, y2 = 4.0, 0.0
x3, y3 = 0.0, 3.0

# Vectors along the sides, written as (dx, dy)
ab = (x2 - x1, y2 - y1)
ac = (x3 - x1, y3 - y1)
bc = (x3 - x2, y3 - y2)

# Dot product: multiply matching components, add them up.
# Zero means the two vectors are perpendicular.
dot_at_a = ab[0] * ac[0] + ab[1] * ac[1]
dot_at_b = -ab[0] * bc[0] + -ab[1] * bc[1]
dot_at_c = ac[0] * bc[0] + ac[1] * bc[1]

eps = 1e-9  # 1e-9 is shorthand for 0.000000001

print(f"dot at A = {dot_at_a}")
print(f"dot at B = {dot_at_b}")
print(f"dot at C = {dot_at_c}")

if math.fabs(dot_at_a) < eps or math.fabs(dot_at_b) < eps or math.fabs(dot_at_c) < eps:
    print("Right-angled triangle")
else:
    print("Not right-angled")
