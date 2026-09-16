"""Exercise 3.8 - Answer five business questions in SQL, not in Python.
[work-flavoured]

Build the database first:
    python3 examples/meeting-3/13_etl_pipeline.py

Then run from the repository root:
    python3 exercise-bank/meeting-3/ex_3_08_five_questions.py

THE KEY DISTINCTION: WHERE filters rows before grouping; HAVING filters
groups after. Questions 3 and 5 are impossible with WHERE, because the
condition is about a group total.
"""

import sqlite3
from pathlib import Path

DATABASE = Path("out/sales.db")

if not DATABASE.exists():
    print(f"x {DATABASE} not found.")
    print("  Build it first: python3 examples/meeting-3/13_etl_pipeline.py")
    raise SystemExit(1)

connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row  # so we can write row["country"]


def section(title):
    print()
    print("=" * 62)
    print(f"  {title}")
    print("=" * 62)


# --- 1 -----------------------------------------------------------------
section("1. Total gross revenue per country")
print(f"  {'Country':<10}{'Orders':>8}{'Gross':>12}")
print("  " + "-" * 30)
for row in connection.execute("""
    SELECT   country,
             COUNT(*)          AS orders,
             SUM(gross_amount) AS gross
    FROM     sale
    GROUP BY country
    ORDER BY gross DESC
"""):
    print(f"  {row['country']:<10}{row['orders']:>8}{row['gross']:>12.2f}")

# --- 2 -----------------------------------------------------------------
section("2. Top 3 products by units sold")
print(f"  {'Product':<24}{'Units':>8}{'Gross':>12}")
print("  " + "-" * 44)
for row in connection.execute("""
    SELECT   product_name,
             SUM(quantity)     AS units,
             SUM(gross_amount) AS gross
    FROM     sale
    GROUP BY ean
    ORDER BY units DESC
    LIMIT    3
"""):
    print(f"  {row['product_name']:<24}{row['units']:>8}{row['gross']:>12.2f}")

# --- 3: needs HAVING, not WHERE ----------------------------------------
section("3. Customers with more than one order")
print(f"  {'Customer':<20}{'Orders':>8}{'Gross':>12}")
print("  " + "-" * 40)
for row in connection.execute("""
    SELECT   customer,
             COUNT(*)          AS orders,
             SUM(gross_amount) AS gross
    FROM     sale
    GROUP BY customer
    HAVING   COUNT(*) > 1           -- HAVING: the condition is about the GROUP
    ORDER BY orders DESC, gross DESC
"""):
    print(f"  {row['customer']:<20}{row['orders']:>8}{row['gross']:>12.2f}")

# --- 4 -----------------------------------------------------------------
section("4. Average order value per category")
print(f"  {'Category':<18}{'Orders':>8}{'Avg gross':>12}")
print("  " + "-" * 38)
for row in connection.execute("""
    SELECT   category,
             COUNT(*)                   AS orders,
             ROUND(AVG(gross_amount), 2) AS avg_gross
    FROM     sale
    GROUP BY category
    ORDER BY avg_gross DESC
"""):
    print(f"  {row['category']:<18}{row['orders']:>8}{row['avg_gross']:>12.2f}")

# --- 5: also needs HAVING ----------------------------------------------
section("5. Days with gross revenue over 40.00")
print(f"  {'Date':<14}{'Orders':>8}{'Gross':>12}")
print("  " + "-" * 34)
rows = list(connection.execute("""
    SELECT   order_date,
             COUNT(*)          AS orders,
             SUM(gross_amount) AS gross
    FROM     sale
    GROUP BY order_date
    HAVING   SUM(gross_amount) > 40.00
    ORDER BY gross DESC
"""))
if not rows:
    print("  (no day exceeded 40.00)")
for row in rows:
    print(f"  {row['order_date']:<14}{row['orders']:>8}{row['gross']:>12.2f}")

# --- WHERE vs HAVING, demonstrated -------------------------------------
section("WHERE vs HAVING - the same query, two meanings")
a = connection.execute(
    "SELECT COUNT(*) FROM (SELECT ean FROM sale WHERE quantity > 15 GROUP BY ean)"
).fetchone()[0]
b = connection.execute(
    "SELECT COUNT(*) FROM (SELECT ean FROM sale GROUP BY ean HAVING SUM(quantity) > 15)"
).fetchone()[0]
print(f"  products with at least one SALE over 15 units : {a}")
print(f"  products whose TOTAL units exceed 15          : {b}")
print("  Different questions, different answers. WHERE = rows, HAVING = groups.")

connection.close()
