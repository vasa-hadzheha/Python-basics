"""Lesson 10 - largest of the negative numbers in a file.
Original: Lab 11, Task 1.

Run me from the repository root:
    python3 examples/meeting-3/10_largest_negative.py
"""

values = []

with open("data/numbers.txt", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        # Bare .split() splits on ANY whitespace and discards empty pieces.
        # split(' ') would produce '' for a double space, and float('')
        # raises ValueError. The archive uses split(' ') and gets away with
        # it only because its test file is tidy.
        for token in line.split():
            try:
                values.append(float(token))
            except ValueError:
                print(f"  line {line_number}: skipping {token!r} - not a number")

print(f"Read {len(values)} numbers")

negatives = [v for v in values if v < 0]

# max([]) raises ValueError. The archive calls max(s) unguarded, so the
# same script crashes on a file with no negative numbers.
if negatives:
    print(f"Negative numbers   : {negatives}")
    print(f"Largest negative   : {max(negatives)}")
else:
    print("There are no negative numbers in the file.")
