"""Exercise 3.5 - Sales summary from a messy CSV.  [work-flavoured]

Practises: DictReader, deliberate typing, grouping, reporting what was
skipped and why.

Run from the repository root.
"""

import csv
from pathlib import Path

SOURCE = Path("data/sales_raw.csv")
DELIMITER = ";"


def parse_int(raw):
    """' 12 ' -> 12.  None if it is not a whole number."""
    if raw is None:
        return None
    cleaned = str(raw).strip()
    if not cleaned:
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None


def parse_decimal(raw):
    """'1,40' or ' 1.40 ' -> 1.4.  None if it is not a number.

    The comma replacement RECOVERS a formatting difference (the Austrian
    export sends comma decimals). That is correct. Contrast with a
    negative quantity, which we reject - guessing what it means would be
    wrong.
    """
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

total_rows = 0
usable = []
skipped = []

with open(SOURCE, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=DELIMITER)
    for line_number, row in enumerate(reader, start=2):
        total_rows += 1

        quantity = parse_int(row["quantity"])
        price = parse_decimal(row["unit_price"])
        country = (row["country"] or "").strip().upper()

        if quantity is None:
            skipped.append((line_number, f"quantity not a number: {row['quantity']!r}"))
            continue
        if quantity <= 0:
            skipped.append((line_number, f"quantity not positive: {quantity}"))
            continue
        if price is None:
            skipped.append((line_number, f"price not a number: {row['unit_price']!r}"))
            continue
        if price < 0:
            skipped.append((line_number, f"price negative: {price}"))
            continue
        if len(country) != 2:
            skipped.append((line_number, f"country not a 2-letter code: {country!r}"))
            continue

        usable.append({"country": country, "quantity": quantity, "revenue": quantity * price})

# --- 1 and 4: the counts -----------------------------------------------
print("=" * 56)
print("  SALES SUMMARY")
print("=" * 56)
print(f"  rows read    : {total_rows:>6}")
print(f"  rows usable  : {len(usable):>6}")
print(f"  rows skipped : {len(skipped):>6}")
print(f"  reconciles   : {len(usable) + len(skipped) == total_rows}")

# --- 2: the totals -----------------------------------------------------
total_units = sum(r["quantity"] for r in usable)
total_revenue = sum(r["revenue"] for r in usable)
print(f"\n  total units  : {total_units:>10}")
print(f"  total revenue: {total_revenue:>10.2f}")

# --- 3: revenue per country -------------------------------------------
by_country = {}
for r in usable:
    # The counting pattern from Lesson 9, summing instead of counting.
    by_country[r["country"]] = by_country.get(r["country"], 0.0) + r["revenue"]

print(f"\n  {'Country':<10}{'Revenue':>12}{'Share':>9}")
print("  " + "-" * 31)
for country, revenue in sorted(by_country.items(), key=lambda pair: pair[1], reverse=True):
    share = revenue / total_revenue * 100 if total_revenue else 0.0
    print(f"  {country:<10}{revenue:>12.2f}{share:>8.1f}%")

# --- 4: why rows were skipped -----------------------------------------
print(f"\n  SKIPPED ROWS ({len(skipped)})")
for line_number, reason in skipped:
    print(f"    line {line_number:>3}: {reason}")

# --- tests -------------------------------------------------------------
assert parse_decimal("1,40") == 1.4, "comma decimals must be recovered"
assert parse_int("") is None
assert parse_int("abc") is None
assert len(usable) + len(skipped) == total_rows
print("\nAll tests passed.")
