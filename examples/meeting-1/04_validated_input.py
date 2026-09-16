"""Lesson 4 - "while True" plus "break": ask until the answer is usable.

This is the pattern you will genuinely reuse at work.

Run me:  python3 examples/meeting-1/04_validated_input.py
Try typing abc, then -5, then 3.5.
"""

while True:
    raw = input("Enter a positive number: ")
    if raw.replace(".", "", 1).isdigit():  # digits, with at most one dot
        value = float(raw)
        if value > 0:
            break  # good input - leave the loop
    print("  x That is not a positive number. Try again.")

print(f"Thank you. You entered {value}")
