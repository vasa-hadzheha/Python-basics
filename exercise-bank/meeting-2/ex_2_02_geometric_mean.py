"""Exercise 2.2 - Geometric mean of n numbers.  (Original Lab 6, Task 1.)

Practises: building a list from input, the product accumulator, guards.
"""

n = int(input("How many numbers? "))

if n <= 0:
    # 1/n would raise ZeroDivisionError, and "the mean of no numbers" has
    # no answer anyway. Refuse before dividing.
    print("You need at least one number.")
else:
    x = [float(input(f"x{i + 1}: ")) for i in range(n)]
    print(f"Sequence: {x}")

    product = 1.0  # products start at 1, NOT 0
    for value in x:
        product *= value
    print(f"Product = {product}")

    if product > 0:
        print(f"Geometric mean = {product ** (1 / n):.6f}")
    else:
        # (-8) ** (1/3) does NOT raise - it returns the complex number
        # (1+1.73j). Without this guard a complex number ends up in a report.
        print("No real geometric mean: the product is not positive.")
