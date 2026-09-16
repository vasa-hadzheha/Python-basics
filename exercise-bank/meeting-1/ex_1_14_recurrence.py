"""Exercise 1.14 - x0 = x1 = 1,  xi = x(i-1) + 2*x(i-2).  Find xn.
Original: Lab 5, Task 4 (the archive has both versions; here they are together).

Practises: rolling variables vs storing the whole history, and the
memory/information trade-off between them.

    n = 6  ->  1, 1, 3, 5, 11, 21, 43   ->  x6 = 43
"""

n = int(input("Which element? n = "))

if n < 0:
    print("n must be 0 or more.")
else:
    # --- Version A: rolling variables. Constant memory. -------------------
    if n <= 1:
        result_a = 1  # x0 and x1 are 1 by definition
    else:
        previous2 = 1  # x(i-2)
        previous1 = 1  # x(i-1)
        for _ in range(2, n + 1):
            current = previous1 + 2 * previous2
            # ORDER MATTERS: shift the window forward, oldest first.
            previous2 = previous1
            previous1 = current
        result_a = current

    # --- Version B: keep the whole sequence in a list. --------------------
    x = [1, 1]
    for i in range(2, n + 1):
        x.append(x[i - 1] + 2 * x[i - 2])
    result_b = x[n]

    print(f"Version A (rolling variables) : x{n} = {result_a}")
    print(f"Version B (list)              : x{n} = {result_b}")
    print(f"Sequence up to x{n}            : {x[: n + 1]}")
    print()
    print("Which to use for n = 1,000,000?")
    print("  Version A. It needs 3 numbers regardless of n.")
    print("  Version B would hold a million integers (~8 MB and growing),")
    print("  and those integers get very large, so it is far worse than that.")
    print("  Use B only when you actually need the whole sequence.")
