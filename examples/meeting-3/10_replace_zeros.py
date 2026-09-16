"""Lesson 10 - replace every zero with the file's maximum, write the result.
Original: Lab 11, Task 2.

Run me from the repository root:
    python3 examples/meeting-3/10_replace_zeros.py
"""

from pathlib import Path

values = []
with open("data/numbers_with_zeros.txt", encoding="utf-8") as f:
    for line in f:
        values.extend(float(token) for token in line.split())

if not values:
    print("The file is empty - nothing to do.")
else:
    largest = max(values)
    replaced = [largest if v == 0 else v for v in values]

    Path("out").mkdir(exist_ok=True)  # writing does not create the folder
    with open("out/replaced.txt", "w", encoding="utf-8") as f:
        for value in replaced:
            f.write(f"{value:g}\n")  # ONE VALUE PER LINE

    print(f"Largest value  : {largest:g}")
    print(f"Zeros replaced : {values.count(0)}")
    print(f"Wrote {len(replaced)} values to out/replaced.txt")

    # The archive writes  f.write(str(new_list))  which produces
    # "[5.0, 22.0, 12.0, ...]" on one line. It is a file, but nothing can
    # read it back except eval(), which you must never point at data.
    #
    # THE TEST FOR ANY OUTPUT FORMAT: can you read it back in?
    with open("out/replaced.txt", encoding="utf-8") as f:
        readback = [float(line) for line in f]
    print(f"Read back {len(readback)} values; identical: {readback == replaced}")
