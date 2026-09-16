"""Exercise 1.8 - Sum of the first 17 even numbers, two ways.
Original: archive "SUM завдання №5.py".

Practises: the accumulator pattern; while vs for.
"""

COUNT = 17

# --- Version 1: while, with a hand-rolled counter (the original style) ----
total_while = 0
value = 2
i = 1
while i <= COUNT:
    total_while += value
    value += 2
    i += 1

# --- Version 2: for, letting range() produce the even numbers -------------
# range(start, stop, step): 2, 4, 6, ..., 34.  Stop is 2*COUNT + 1 because
# range excludes its upper bound.
total_for = 0
for value in range(2, 2 * COUNT + 1, 2):
    total_for += value

# --- Version 3: the one-liner you will see in real code -------------------
total_builtin = sum(range(2, 2 * COUNT + 1, 2))

# --- Cross-check against the closed form ---------------------------------
# The sum of the first n even numbers is n * (n + 1).
expected = COUNT * (COUNT + 1)

print(f"while loop  : {total_while}")
print(f"for loop    : {total_for}")
print(f"sum(range()): {total_builtin}")
print(f"formula n(n+1): {expected}")
print()
print("All four agree:", total_while == total_for == total_builtin == expected)
