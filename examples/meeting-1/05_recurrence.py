"""Lesson 5 - two solutions to the same recurrence. (Original Lab 5, Task 4.)

    x0 = x1 = 1,   xi = x(i-1) + 2*x(i-2)

Run me:  python3 examples/meeting-1/05_recurrence.py
Try n=6  ->  43
"""

n = int(input("Which element? n = "))

if n < 0:
    print("n must be 0 or more.")
else:
    # --- Version A: keep only the last two values (constant memory) -------
    if n <= 1:
        result_a = 1  # x0 and x1 are both 1 by definition
    else:
        previous2 = 1  # x(i-2)
        previous1 = 1  # x(i-1)
        for i in range(2, n + 1):
            current = previous1 + 2 * previous2
            previous2 = previous1  # <- shuffle the window forward
            previous1 = current
        result_a = current

    # --- Version B: keep the whole history (a list) -----------------------
    x = [1, 1]  # x[0] and x[1]
    for i in range(2, n + 1):
        x.append(x[i - 1] + 2 * x[i - 2])

    print(f"Version A (3 variables) : x{n} = {result_a}")
    print(f"Version B (list)        : x{n} = {x[n]}")
    print(f"Full sequence           : {x[: n + 1]}")
    print()
    print("Same answer, different trade-off:")
    print("  A uses constant memory but only gives you the final value.")
    print("  B gives you the whole sequence but grows with n.")
