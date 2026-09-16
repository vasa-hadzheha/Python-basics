"""Lesson 12 - load a CSV into SQLite, then answer questions with SQL.

Run me from the repository root:
    python3 examples/meeting-3/12_csv_to_sqlite.py
"""

import csv
import sqlite3

SCHEMA = """
CREATE TABLE product (
    ean        TEXT PRIMARY KEY,
    name       TEXT NOT NULL,
    unit       TEXT NOT NULL,
    category   TEXT NOT NULL,
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    vat_rate   INTEGER NOT NULL CHECK (vat_rate IN (0, 7, 19))
);
"""

connection = sqlite3.connect(":memory:")  # a throwaway database
connection.row_factory = sqlite3.Row  # rows behave like dicts
connection.executescript(SCHEMA)

# --- load ---------------------------------------------------------------
with open("data/products.csv", newline="", encoding="utf-8-sig") as f:
    rows = [
        (
            r["ean"].strip(),  # TEXT - leading zeros survive
            r["name"].strip(),
            r["unit"].strip(),
            r["category"].strip(),
            float(r["unit_price"]),  # REAL
            int(r["vat_rate"]),  # INTEGER
        )
        for r in csv.DictReader(f, delimiter=";")
    ]

# executemany, not a loop of execute(): on 40,000 rows that is the
# difference between minutes and under a second.
connection.executemany("INSERT INTO product VALUES (?, ?, ?, ?, ?, ?)", rows)
connection.commit()  # WITHOUT THIS, NOTHING IS SAVED
print(f"Loaded {len(rows)} products")

# --- query --------------------------------------------------------------
print("\nProducts per category, dearest first:")
query = """
    SELECT   category,
             COUNT(*)                  AS product_count,
             ROUND(AVG(unit_price), 2) AS avg_price,
             ROUND(MAX(unit_price), 2) AS max_price
    FROM     product
    GROUP BY category
    ORDER BY avg_price DESC
"""
print(f"{'Category':<16}{'Count':>7}{'Avg':>9}{'Max':>9}")
print("-" * 41)
for row in connection.execute(query):
    # row_factory=sqlite3.Row lets us use column NAMES, not positions.
    # row[3] would break the moment someone adds a column.
    print(
        f"{row['category']:<16}{row['product_count']:>7}"
        f"{row['avg_price']:>9.2f}{row['max_price']:>9.2f}"
    )

# --- a parameterised query ---------------------------------------------
# ALWAYS parameters, never an f-string. The (?, ?) placeholders make SQL
# injection impossible and handle quoting for free.
print("\nGrocery items over 1.00:")
for row in connection.execute(
    "SELECT name, unit_price FROM product "
    "WHERE category = ? AND unit_price > ? ORDER BY unit_price DESC",
    ("grocery", 1.00),
):
    print(f"  {row['name']:<22}{row['unit_price']:>8.2f}")

# --- WHERE filters rows; HAVING filters groups -------------------------
print("\nCategories whose total value exceeds 2.00:")
for row in connection.execute("""
    SELECT   category, ROUND(SUM(unit_price), 2) AS total
    FROM     product
    GROUP BY category
    HAVING   SUM(unit_price) > 2.00
    ORDER BY total DESC
"""):
    print(f"  {row['category']:<16}{row['total']:>8.2f}")

# --- what an f-string in SQL would allow -------------------------------
print()
print("Why parameters and not f-strings:")
malicious = "'; DROP TABLE product; --"
print(f"  If a user typed {malicious!r} into a name search,")
print("  an f-string query would delete the table. A parameter just")
print("  looks for a product with that literal name and finds none:")
found = connection.execute("SELECT COUNT(*) FROM product WHERE name = ?", (malicious,)).fetchone()
print(f"  rows found: {found[0]}, table intact: ", end="")
print(connection.execute("SELECT COUNT(*) FROM product").fetchone()[0] == 10)

connection.close()
