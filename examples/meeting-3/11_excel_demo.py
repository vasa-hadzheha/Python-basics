"""Lesson 11 - reading and writing .xlsx with openpyxl.

openpyxl is NOT part of the standard library. This script creates its own
workbook so it needs no download, and skips itself with a clear message
if openpyxl is not installed.

    pip install openpyxl

Run me from the repository root:
    python3 examples/meeting-3/11_excel_demo.py
"""

from pathlib import Path

try:
    from openpyxl import Workbook, load_workbook
except ImportError:
    print("openpyxl is not installed - skipping this demo.")
    print("Install it with:  pip install openpyxl")
    raise SystemExit(0)  # exit code 0: not installed is not a failure

OUT = Path("out")
OUT.mkdir(exist_ok=True)
path = OUT / "products_demo.xlsx"

# --- write a workbook ---------------------------------------------------
workbook = Workbook()
sheet = workbook.active
sheet.title = "Products"

sheet.append(["ean", "name", "unit_price"])  # header
sheet.append(["4006381333931", "Bread 500g", 1.35])
sheet.append(["0401234567890", "Leading zero item", 2.00])

# Force the EAN column to Text, so Excel does not mangle it into 4.00638E+12
for row in sheet.iter_rows(min_row=2, min_col=1, max_col=1):
    for cell in row:
        cell.number_format = "@"  # "@" is Excel's Text format

workbook.save(path)
print(f"Wrote {path}")

# --- read it back -------------------------------------------------------
# data_only=True  : the cached RESULT of a formula, not the formula text.
#                   WARNING: a file written by a program (like this one)
#                   has no cached results, so formula cells read as None.
# read_only=True  : streams instead of loading the whole workbook.
workbook = load_workbook(path, read_only=True, data_only=True)
sheet = workbook["Products"]

rows = sheet.iter_rows(values_only=True)  # tuples, not Cell objects
header = [str(h).strip() for h in next(rows)]
products = [dict(zip(header, row)) for row in rows]  # zip pairs names with values
workbook.close()

print(f"\nRead back {len(products)} rows with header {header}")
for p in products:
    ean = p["ean"]
    print(f"  {ean!r:<18}{p['name']:<22}{p['unit_price']}")

print()
print("Note the second EAN kept its leading zero because we wrote the")
print("column as Text. Had it been written as a number, 0401234567890")
print("would have come back as 401234567890 - a 12-digit code that")
print("matches nothing.")
print()
print("Excel's other habits to watch for:")
print("  a 13-digit code in a General cell -> 4.00638E+12")
print("  something that looks like a date  -> 1-5 becomes 2026-01-05")
print("  part numbers like SEPT2, MAR1     -> converted to dates")
print()
print("The damage happens when a HUMAN opens a CSV in Excel and saves it.")
print("Checking len(code) == 13 catches it immediately.")

assert len(products) == 2
assert products[1]["ean"] == "0401234567890", "leading zero must survive"
print("\nAll tests passed.")
