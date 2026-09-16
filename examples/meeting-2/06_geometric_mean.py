"""Lesson 6 - geometric mean of n numbers. (Original Lab 6, Task 1.)

Run me:  python3 examples/meeting-2/06_geometric_mean.py
Try n=3 with 2, 4, 8  ->  4.0
"""

n = int(input("How many numbers? "))

if n <= 0:
    # 1/n would be a ZeroDivisionError, and "the mean of no numbers"
    # is not a question with an answer.
    print("You need at least one number.")
else:
    x = [float(input(f"x{i + 1}: ")) for i in range(n)]

    print(f"Sequence: {x}")

    product = 1.0  # products start at 1, NOT 0
    for value in x:
        product *= value
    print(f"Product = {product}")

    if product > 0:
        geometric_mean = product ** (1 / n)
        print(f"Geometric mean = {geometric_mean:.6f}")
    else:
        # (-8) ** (1/3) does not raise - it returns a COMPLEX number.
        # Without this guard you would silently print (1+1.73j) in a report.
        print("No real geometric mean: the product is not positive.")
