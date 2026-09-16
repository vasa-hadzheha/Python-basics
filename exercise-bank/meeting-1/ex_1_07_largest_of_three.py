"""Exercise 1.7 - The largest of three numbers.
Original: archive "Aditional exercises/new.py" - which contains a real bug.

Practises: comparing several values correctly, and NOT shadowing built-ins.

THE BUG IN THE ORIGINAL
-----------------------
    def max(number_1, number_2, number_3):
        if number_1 > number_2 > number_3:   return number_1
        elif number_2 > number_1 > number_3: return number_2
        else:                                return number_3

Try it with (1, 5, 3):
    1 > 5 > 3 ?  No.
    5 > 1 > 3 ?  5 > 1 yes, but 1 > 3 no  -> No.
    falls through to else -> returns 3.   WRONG, the answer is 5.

A chained comparison "a > b > c" demands a TOTAL ordering of all three
values, which only covers a fraction of the possible arrangements.
The fix: compare each candidate against BOTH others.

Two further problems with the original:
  * naming it "max" shadows Python's own built-in max()
  * using ">" rather than ">=" means ties are handled by accident
"""


def largest_of_three(first, second, third):
    """Return the largest of three numbers."""
    if first >= second and first >= third:
        return first
    elif second >= first and second >= third:
        return second
    else:
        return third


x = int(input("First number:  "))
y = int(input("Second number: "))
z = int(input("Third number:  "))

print(f"Largest (our function) : {largest_of_three(x, y, z)}")
print(f"Largest (built-in max) : {max(x, y, z)}")

# Proof that the original is broken, on every arrangement of 1, 3, 5:
print()
print("Checking our function against the built-in on all 6 orderings of 1,3,5:")
for a, b, c in [(1, 3, 5), (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1)]:
    ours = largest_of_three(a, b, c)
    print(f"  ({a}, {b}, {c}) -> {ours}   {'OK' if ours == 5 else 'WRONG'}")
