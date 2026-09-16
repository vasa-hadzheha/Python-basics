"""Exercise 3.9 - Produce a plain-text report you could paste into an email.
[work-flavoured]

Build the database first:
    python3 examples/meeting-3/13_etl_pipeline.py

Run from the repository root.
"""

import sqlite3
from datetime import datetime
from pathlib import Path

DATABASE = Path("out/sales.db")
TARGET = Path("out/monthly_report.txt")
WIDTH = 64

if not DATABASE.exists():
    print(f"x {DATABASE} not found.")
    print("  Build it first: python3 examples/meeting-3/13_etl_pipeline.py")
    raise SystemExit(1)


def section(f, title):
    """One helper, so every heading looks identical.

    Consistency is what makes a generated report look deliberate rather
    than accidental.
    """
    print(file=f)
    print("=" * WIDTH, file=f)
    print(f" {title}", file=f)
    print("=" * WIDTH, file=f)


connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row

TARGET.parent.mkdir(exist_ok=True)

with open(TARGET, "w", encoding="utf-8") as f:
    # --- header ---------------------------------------------------------
    print("=" * WIDTH, file=f)
    print(" SALES REPORT", file=f)
    print("=" * WIDTH, file=f)
    print(f" Generated : {datetime.now():%Y-%m-%d %H:%M}", file=f)
    print(f" Source    : {DATABASE}", file=f)

    totals = connection.execute("""
        SELECT COUNT(*)          AS orders,
               MIN(order_date)    AS first_day,
               MAX(order_date)    AS last_day,
               SUM(quantity)      AS units,
               SUM(net_amount)    AS net,
               SUM(vat_amount)    AS vat,
               SUM(gross_amount)  AS gross
        FROM   sale
    """).fetchone()

    # A report that does not say how much data it covers cannot be checked.
    print(f" Period    : {totals['first_day']} to {totals['last_day']}", file=f)
    print(f" Orders    : {totals['orders']}", file=f)

    # --- by country -----------------------------------------------------
    section(f, "REVENUE BY COUNTRY")
    print(f" {'Country':<12}{'Orders':>8}{'Units':>8}{'Net':>12}{'Gross':>12}", file=f)
    print(" " + "-" * (WIDTH - 2), file=f)
    for row in connection.execute("""
        SELECT   country, COUNT(*) AS orders, SUM(quantity) AS units,
                 SUM(net_amount) AS net, SUM(gross_amount) AS gross
        FROM     sale GROUP BY country ORDER BY gross DESC
    """):
        print(
            f" {row['country']:<12}{row['orders']:>8}{row['units']:>8}"
            f"{row['net']:>12.2f}{row['gross']:>12.2f}",
            file=f,
        )

    # --- by category ----------------------------------------------------
    section(f, "REVENUE BY CATEGORY")
    print(f" {'Category':<18}{'Orders':>8}{'Units':>8}{'Gross':>12}", file=f)
    print(" " + "-" * (WIDTH - 2), file=f)
    for row in connection.execute("""
        SELECT   category, COUNT(*) AS orders, SUM(quantity) AS units,
                 SUM(gross_amount) AS gross
        FROM     sale GROUP BY category ORDER BY gross DESC
    """):
        print(
            f" {row['category']:<18}{row['orders']:>8}{row['units']:>8}{row['gross']:>12.2f}",
            file=f,
        )

    # --- grand total ----------------------------------------------------
    section(f, "GRAND TOTAL")
    print(f" {'Units sold':<22}{totals['units']:>16}", file=f)
    print(f" {'Net amount':<22}{totals['net']:>16.2f}", file=f)
    print(f" {'VAT':<22}{totals['vat']:>16.2f}", file=f)
    print(" " + "-" * (WIDTH - 2), file=f)
    print(f" {'Gross amount':<22}{totals['gross']:>16.2f}", file=f)

    # --- the self-check -------------------------------------------------
    difference = abs((totals["net"] + totals["vat"]) - totals["gross"])
    print(file=f)
    print(f" Self-check: net + VAT == gross ... {difference < 0.005}", file=f)
    print("=" * WIDTH, file=f)

connection.close()

print(f"Wrote {TARGET}\n")
print(TARGET.read_text(encoding="utf-8"))
