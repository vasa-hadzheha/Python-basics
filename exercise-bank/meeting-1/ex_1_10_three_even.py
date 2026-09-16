"""Exercise 1.10 - Keep asking until three EVEN numbers have been entered.
Original: archive "завдання №9.py".

Practises: two counters - one drives the loop, one reports.

Note on the original: it read with float(input(...)) and then tested
"number % 2 == 0". For 4.0 that works, but 4.5 % 2 is 0.5 and "is 4.5 even"
is not a meaningful question. Whole numbers only, so int() is correct here.
"""

TARGET = 3

even_found = 0  # drives the loop
attempts = 0  # for the final report

while even_found < TARGET:
    raw = input(f"Enter a whole number ({even_found}/{TARGET} even so far): ")

    # Allow a leading minus sign, then digits.
    if not raw.lstrip("-").isdigit():
        print("  x That is not a whole number.")
        continue

    number = int(raw)
    attempts += 1

    if number % 2 == 0:
        even_found += 1
        print(f"  OK {number} is even.")
    else:
        print(f"  -- {number} is odd, ignoring it.")

print(f"\nDone: {TARGET} even numbers entered, after {attempts} valid number(s).")
