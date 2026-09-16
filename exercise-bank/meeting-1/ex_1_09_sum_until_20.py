"""Exercise 1.9 - Keep adding numbers until the total reaches 20.
Original: archive "SUM завдання №8.py".

Practises: while with an unknown number of passes.
"""

total = 0.0
count = 0

# We cannot use "for" here: how many numbers the user types depends on
# what they type. That is exactly what "while" is for.
while total < 20:
    raw = input(f"Enter a number (total so far {total:g}): ")
    try:
        number = float(raw)
    except ValueError:
        print("  x Not a number. Try again.")
        continue  # back to the condition; nothing was added

    total += number
    count += 1

    # EDGE CASE the original version ignores: if the user only ever enters
    # negative numbers, total never reaches 20 and this loop never ends.
    # We warn rather than loop silently forever.
    if count >= 20 and total < 0:
        print("  ! The total is going the wrong way. Stopping.")
        break

print(f"\nTotal = {total:g} after {count} number(s)")
