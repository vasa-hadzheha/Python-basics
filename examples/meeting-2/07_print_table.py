"""Lesson 7 - printing a table a human can actually read.

Keep this file. You will paste this pattern into real scripts for years.

Run me:  python3 examples/meeting-2/07_print_table.py
No input needed.
"""

# --- part 1: a plain numeric matrix --------------------------------------
table = [[1, -25, 300], [4000, 5, -6], [7, 88, 9]]

print("A numeric matrix, each cell right-aligned in 7 characters:")
for row in table:
    for cell in row:
        print(f"{cell:>7}", end="")  # end="" = do not start a new line yet
    print()  # now start one

print()
print("The same thing as the one-liner the original archive uses:")
print(*["".join(f"{cell:>7}" for cell in row) for row in table], sep="\n")

# --- part 2: a real report with headers ----------------------------------
headers = ["Product", "Unit", "Qty", "Price"]
rows = [
    ["Bread", "pcs", 6, 13.50],
    ["Milk", "pack", 10, 14.00],
    ["Cola", "can", 15, 11.99],
]

print()
print("A report: text left-aligned, numbers right-aligned.")
print(f"{headers[0]:<10}{headers[1]:<6}{headers[2]:>5}{headers[3]:>9}")
print("-" * 30)
for row in rows:
    print(f"{row[0]:<10}{row[1]:<6}{row[2]:>5}{row[3]:>9.2f}")
print("-" * 30)
print(f"{'TOTAL':<21}{sum(r[2] * r[3] for r in rows):>9.2f}")
