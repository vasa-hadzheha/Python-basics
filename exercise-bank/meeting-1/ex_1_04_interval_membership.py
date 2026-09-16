"""Exercise 1.4 - Does the number lie in [1; 2] intersected with (c; d)?
Original: Lab 4, Task 2.

Practises: chained comparisons, "and", inclusive vs exclusive bounds.

Note the bracket styles:
    [1; 2]  square  -> ends INCLUDED  -> use <=
    (c; d)  round   -> ends EXCLUDED  -> use <
"""

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

if c >= d:
    # (c; d) is empty when c >= d, so nothing can be in the intersection.
    print(f"The interval (c; d) = ({c}; {d}) is empty - nothing can belong to it.")
else:
    # Python lets us chain, which reads like the mathematics:
    if 1 <= a <= 2 and c < a < d:
        print("a belongs to the interval")
    else:
        print("a does not belong to the interval")

    if 1 <= b <= 2 and c < b < d:
        print("b belongs to the interval")
    else:
        print("b does not belong to the interval")

# A nice piece of reasoning from the original solution:
# c and d can NEVER belong to the open interval (c; d), because
# "c < c" and "d < d" are both false by definition. So there is no
# need to test them at all.
print("c and d can never belong to (c; d) - no test needed.")
