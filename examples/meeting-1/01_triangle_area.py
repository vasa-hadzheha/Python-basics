"""Lesson 1 - Heron's formula. (Original Lab 4, Task 1.)

Run me:  python3 examples/meeting-1/01_triangle_area.py
Values are hardcoded here so you can run it without typing anything.
Exercise 1.3 asks you to read them from the keyboard.
"""

import math  # 1. load the maths toolbox

a = 3.0  # 2. three side lengths, as floats
b = 4.0
c = 5.0

p = (a + b + c) / 2  # 3. the semi-perimeter: half the way round
#    "/" gives a float - good, we want 6.0 not 6

area = math.sqrt(p * (p - a) * (p - b) * (p - c))  # 4. Heron's formula

print("Semi-perimeter:", p)  # 5. show the intermediate value too -
print("Area:", area)  #    it makes the program explainable
