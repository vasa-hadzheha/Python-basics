"""Exercise 1.11 - Count the zero digits in a whole number.
Original: Lab 5, Task 2.

Practises: % and // to walk through digits; edge cases.

Edge cases that matter here:
    n = 0     -> the loop body never runs, but the answer is 1
    n = -500  -> abs() first, or the loop misbehaves
    after the loop n is 0, so keep a copy if you want to print it
"""

n = int(input("Enter a whole number: "))

original = n  # the loop destroys n, so save it
n = abs(n)  # -104 has the same digits as 104

zero_count = 0

if n == 0:
    zero_count = 1  # the number 0 is a single zero digit
else:
    while n > 0:
        last_digit = n % 10  # peel off the rightmost digit
        if last_digit == 0:
            zero_count += 1
        n = n // 10  # drop it and continue

print(f"{original} contains {zero_count} zero digit(s)")

# Cross-check with string handling - shorter, and a good thing to know,
# but the point of the exercise was the % and // loop.
print(f"cross-check: {str(abs(original)).count('0')}")
