"""Exercise 3.7 - Load a CSV into SQLite with constraints that make bad
data impossible.  [work-flavoured]

THE LESSON: validation in Python protects one script. A constraint
protects the data from every program that ever touches the table.

Run from the repository root.
"""

import csv
import sqlite3
from pathlib import Path

SOURCE = Path("data/products.csv")
DATABASE = Path("out/shop.db")

# DROP first, so the script can be re-run.
SCHEMA = """
DROP TABLE IF EXISTS product;
CREATE TABLE product (
    ean        TEXT    PRIMARY KEY,                       -- no duplicates, zeros kept
    name       TEXT    NOT NULL CHECK (length(name) > 0),
    unit       TEXT    NOT NULL,
    category   TEXT    NOT NULL,
    unit_price REAL    NOT NULL CHECK (unit_price >= 0),
    vat_rate   INTEGER NOT NULL CHECK (vat_rate IN (0, 7, 19))
);
"""

COLUMNS = ["ean", "name", "unit", "category", "unit_price", "vat_rate"]

if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

DATABASE.parent.mkdir(exist_ok=True)

with open(SOURCE, newline="", encoding="utf-8-sig") as f:
    rows = [
        (
            r["ean"].strip(),  # TEXT
            r["name"].strip(),
            r["unit"].strip(),
            r["category"].strip(),
            float(r["unit_price"]),  # REAL
            int(r["vat_rate"]),  # INTEGER
        )
        for r in csv.DictReader(f, delimiter=";")
    ]

connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row
try:
    connection.executescript(SCHEMA)
    # executemany, not a loop of execute(): minutes vs under a second at 40k rows.
    connection.executemany(
        f"INSERT INTO product ({', '.join(COLUMNS)}) VALUES (?, ?, ?, ?, ?, ?)", rows
    )
    connection.commit()  # WITHOUT THIS, NOTHING IS SAVED
except Exception:
    connection.rollback()  # all or nothing
    raise

count = connection.execute("SELECT COUNT(*) FROM product").fetchone()[0]
print(f"Loaded {len(rows)} rows into {DATABASE}; table now holds {count}")

# --- prove the constraints work ----------------------------------------
print("\n" + "=" * 62)
print("  THE CONSTRAINTS REFUSE BAD DATA")
print("=" * 62)

bad_rows = [
    ("duplicate ean", ("4006381333931", "Copy", "pcs", "bakery", 1.35, 7)),
    ("negative price", ("1111111111111", "Cheap", "pcs", "bakery", -1.00, 7)),
    ("invalid vat rate", ("2222222222222", "Odd VAT", "pcs", "bakery", 1.00, 13)),
    ("empty name", ("3333333333333", "", "pcs", "bakery", 1.00, 7)),
]

for label, values in bad_rows:
    try:
        connection.execute(
            f"INSERT INTO product ({', '.join(COLUMNS)}) VALUES (?, ?, ?, ?, ?, ?)", values
        )
        connection.commit()
        print(f"  x {label:<20} WAS ACCEPTED - the constraint is missing!")
    except sqlite3.IntegrityError as error:
        print(f"  + {label:<20} refused: {error}")

final = connection.execute("SELECT COUNT(*) FROM product").fetchone()[0]
print(f"\nTable still holds {final} rows - nothing bad got in.")

# --- leading zeros survive because ean is TEXT -------------------------
connection.execute(
    f"INSERT INTO product ({', '.join(COLUMNS)}) VALUES (?, ?, ?, ?, ?, ?)",
    ("0401234567890", "Leading zero item", "pcs", "grocery", 2.00, 7),
)
connection.commit()
stored = connection.execute(
    "SELECT ean FROM product WHERE name = ?", ("Leading zero item",)
).fetchone()["ean"]
print(f"\nStored a code with a leading zero: {stored!r} ({len(stored)} chars)")
assert stored == "0401234567890", "TEXT must preserve the leading zero"

assert final == 10
connection.close()
print("\nAll tests passed.")
