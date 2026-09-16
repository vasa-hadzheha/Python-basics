"""Exercise 3.10 - An idempotent load: running it twice must not double
the data.  [work-flavoured]

WHY THIS MATTERS: a scheduled job WILL run twice. Someone reruns it after
a failure, or a retry fires. A load that is not idempotent turns that into
duplicated revenue in every downstream report.

"Can this safely run twice?" is a standing review question.

Run from the repository root - several times, and watch the count.
"""

import csv
import sqlite3
from pathlib import Path

SOURCE = Path("data/products.csv")
DATABASE = Path("out/incremental.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS product (
    ean        TEXT PRIMARY KEY,          -- the key that makes upsert possible
    name       TEXT NOT NULL,
    unit       TEXT NOT NULL,
    category   TEXT NOT NULL,
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    vat_rate   INTEGER NOT NULL CHECK (vat_rate IN (0, 7, 19))
);
"""

# ON CONFLICT DO UPDATE is the modern upsert, and it is what you want in
# production. Unlike INSERT OR REPLACE it does NOT delete and re-insert
# the row, so columns you do not supply keep their existing values.
# "excluded" refers to the row you tried to insert.
UPSERT = """
INSERT INTO product (ean, name, unit, category, unit_price, vat_rate)
VALUES (?, ?, ?, ?, ?, ?)
ON CONFLICT(ean) DO UPDATE SET
    name       = excluded.name,
    unit       = excluded.unit,
    category   = excluded.category,
    unit_price = excluded.unit_price,
    vat_rate   = excluded.vat_rate
"""


def read_products(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [
            (
                r["ean"].strip(),
                r["name"].strip(),
                r["unit"].strip(),
                r["category"].strip(),
                float(r["unit_price"]),
                int(r["vat_rate"]),
            )
            for r in csv.DictReader(f, delimiter=";")
        ]


def load(database, rows):
    """Upsert rows. Returns (rows_before, rows_after)."""
    connection = sqlite3.connect(database)
    try:
        connection.executescript(SCHEMA)
        before = connection.execute("SELECT COUNT(*) FROM product").fetchone()[0]
        connection.executemany(UPSERT, rows)
        connection.commit()
        after = connection.execute("SELECT COUNT(*) FROM product").fetchone()[0]
        return before, after
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

DATABASE.parent.mkdir(exist_ok=True)
DATABASE.unlink(missing_ok=True)  # start clean so the demo is repeatable

rows = read_products(SOURCE)
print(f"Source file holds {len(rows)} products\n")

print("=" * 58)
print("  RUNNING THE SAME LOAD THREE TIMES")
print("=" * 58)
print(f"  {'Run':<8}{'Rows before':>14}{'Rows after':>14}")
print("  " + "-" * 36)
for run_number in (1, 2, 3):
    before, after = load(DATABASE, rows)
    print(f"  {run_number:<8}{before:>14}{after:>14}")
    assert after == len(rows), "an idempotent load must not grow the table"

print("\n  The count never grows. The load is idempotent.")

# --- now change a price and reload --------------------------------------
print("\n" + "=" * 58)
print("  A CHANGED PRICE IS PICKED UP, NOT DUPLICATED")
print("=" * 58)

connection = sqlite3.connect(DATABASE)
old_price = connection.execute(
    "SELECT unit_price FROM product WHERE ean = ?", ("4006381333931",)
).fetchone()[0]
connection.close()

changed = [
    (ean, name, unit, cat, 9.99 if ean == "4006381333931" else price, vat)
    for ean, name, unit, cat, price, vat in rows
]
before, after = load(DATABASE, changed)

connection = sqlite3.connect(DATABASE)
new_price = connection.execute(
    "SELECT unit_price FROM product WHERE ean = ?", ("4006381333931",)
).fetchone()[0]
total = connection.execute("SELECT COUNT(*) FROM product").fetchone()[0]
connection.close()

print(f"  price before  : {old_price}")
print(f"  price after   : {new_price}")
print(f"  row count     : {total}  (unchanged)")

assert new_price == 9.99, "the update must be applied"
assert total == len(rows), "the update must not add a row"

print("\n  Updated in place. No duplicate.")
print("\n" + "=" * 58)
print("  INSERT OR REPLACE vs ON CONFLICT DO UPDATE")
print("=" * 58)
print("  INSERT OR REPLACE deletes the row and inserts a new one, so any")
print("  column you do not supply reverts to its default. Use it only when")
print("  you are supplying every column. Otherwise prefer ON CONFLICT.")
print("\nAll tests passed.")
