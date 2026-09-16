"""Exercise 2.4 - Multiply a vector by a scalar.  (Original Lab 6, Task 3.)

Practises: list comprehension; and why "x * a" is NOT what you want.
"""

n = int(input("Vector dimension: "))
x = [float(input(f"coordinate {i + 1}: ")) for i in range(n)]
a = float(input("Scalar multiplier: "))

print(f"Vector x = {x}")

result = [value * a for value in x]  # element by element
print(f"x * {a} = {result}")

# WATCH OUT: for a LIST, "*" repeats the list, it does not scale it.
print()
print("Why not just write  x * a  ?  Because for a list, * REPEATS:")
print(f"  [1, 2] * 3  =  {[1, 2] * 3}")
print("This is the same rule as '7' * 3 == '777' from Lesson 1.")
print("Libraries like numpy and polars redefine * to mean element-wise,")
print("which is exactly why they exist.")
