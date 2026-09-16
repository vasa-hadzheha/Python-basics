"""Exercise 1.3 - Triangle area from three side lengths.
Original: Lab 4, Task 1.

Practises: if/elif/else, the triangle inequality, math.sqrt.
"""

import math

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

# Cheapest check first: a length cannot be zero or negative.
if a <= 0 or b <= 0 or c <= 0:
    print("A side length must be greater than 0.")

# Then the relationship between the values: the triangle inequality.
# Each side must be shorter than the sum of the other two.
elif a + b <= c or a + c <= b or b + c <= a:
    print("These three lengths cannot form a triangle.")

else:
    p = (a + b + c) / 2  # semi-perimeter
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))  # Heron's formula
    print(f"Semi-perimeter = {p:.4f}")
    print(f"Area           = {area:.4f}")
