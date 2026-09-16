"""Lesson 4 - peel a number apart digit by digit. (Original Lab 5, Task 2.)

Run me:  python3 examples/meeting-1/04_count_zeros.py
Try 1020 (-> 2), 0 (-> 1), -500 (-> 2), 7 (-> 0).
"""

n = int(input("Enter a whole number: "))
original = n  # keep a copy: the loop below destroys n
n = abs(n)  # handle negatives: -104 has the same digits as 104

zero_count = 0

if n == 0:
    # Edge case: the number 0 has one digit, and it is a zero.
    zero_count = 1
else:
    while n > 0:
        last_digit = n % 10  # peel off the rightmost digit
        if last_digit == 0:
            zero_count += 1
        n = n // 10  # drop that digit and carry on

print(f"{original} contains {zero_count} zero(s)")
