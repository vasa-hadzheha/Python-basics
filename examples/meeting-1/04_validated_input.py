"""Lesson 4 - "while True" plus "break": ask until the answer is usable.

This is the pattern you will genuinely reuse at work.

Run me:  python3 examples/meeting-1/04_validated_input.py
Try typing abc, then -5, then 3.5.
"""

while True:
    raw = input("Enter a positive number: ")

    # Let float() decide what counts as a number, and catch its complaint.
    #
    # WHY NOT  raw.replace(".", "", 1).isdigit()  ?
    # That trick reads nicely - "digits, with at most one dot" - but it
    # disagrees with float() on some characters. "2" as a SUPERSCRIPT is a
    # digit as far as isdigit() is concerned, yet float() refuses it:
    #     "²".isdigit()  ->  True
    #     float("²")     ->  ValueError
    # So the check would pass and the conversion on the next line would
    # crash. The rule: do not re-implement a test that the conversion
    # itself already performs. Try the conversion and handle the failure.
    try:
        value = float(raw)
    except ValueError:
        print("  x That is not a number. Try again.")
        continue  # back to the condition; nothing was assigned

    if value > 0:
        break  # good input - leave the loop

    print("  x The number must be greater than 0. Try again.")

print(f"Thank you. You entered {value}")
