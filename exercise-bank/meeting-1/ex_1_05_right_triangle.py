"""Exercise 1.5 - Is the triangle right-angled, given its vertices?
Original: Lab 4, Task 3.

Practises: the dot product, epsilon comparison of floats.

Two vectors are perpendicular exactly when their dot product is 0.
At each vertex we build the two vectors pointing AWAY from it, then test.
"""

import math

x1 = float(input("A: x1 = "))
y1 = float(input("A: y1 = "))
x2 = float(input("B: x2 = "))
y2 = float(input("B: y2 = "))
x3 = float(input("C: x3 = "))
y3 = float(input("C: y3 = "))

# Degenerate check: three points on one line are not a triangle.
# The cross product is twice the signed area; zero means collinear.
cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

eps = 1e-9

if math.fabs(cross) < eps:
    print("These three points lie on a straight line - not a triangle.")
else:
    # At vertex A the sides go A->B and A->C.
    ab = (x2 - x1, y2 - y1)
    ac = (x3 - x1, y3 - y1)
    # At vertex B they go B->A and B->C.
    ba = (x1 - x2, y1 - y2)
    bc = (x3 - x2, y3 - y2)
    # At vertex C they go C->A and C->B.
    ca = (x1 - x3, y1 - y3)
    cb = (x2 - x3, y2 - y3)

    dot_a = ab[0] * ac[0] + ab[1] * ac[1]
    dot_b = ba[0] * bc[0] + ba[1] * bc[1]
    dot_c = ca[0] * cb[0] + ca[1] * cb[1]

    print(f"dot at A = {dot_a:g}")
    print(f"dot at B = {dot_b:g}")
    print(f"dot at C = {dot_c:g}")

    # NEVER "== 0" for floats: (0.1, 0.3) coordinates give 1.4e-17, not 0.
    if math.fabs(dot_a) < eps:
        print("Right-angled, with the right angle at A")
    elif math.fabs(dot_b) < eps:
        print("Right-angled, with the right angle at B")
    elif math.fabs(dot_c) < eps:
        print("Right-angled, with the right angle at C")
    else:
        print("Not right-angled")
