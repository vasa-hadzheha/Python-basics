"""Lesson 11 - a typed, validated CSV loader.

This is the pattern for every CSV you will ever load.

Run me from the repository root:
    python3 examples/meeting-3/11_load_products.py
"""

import csv

REQUIRED_COLUMNS = {"ean", "name", "unit", "category", "unit_price", "vat_rate"}


def parse_decimal(raw):
    """'1,35' or ' 1.35 ' -> 1.35.  None if it is not a number."""
    if raw is None:
        return None
    cleaned = raw.strip().replace(",", ".")  # accept both decimal separators
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def load_products(path):
    """Read products.csv into typed dicts.

    Returns (good_rows, problems). Never raises on bad DATA - a bad row
    becomes a problem report so the caller decides what to do. A missing
    COLUMN does raise, because there is no sensible way to continue.
    """
    good, problems = [], []

    # newline=""      : required by the csv module
    # utf-8-sig       : strips Excel's BOM, so the first column is "ean"
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")

        # Check the header BEFORE processing a single row.
        header = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - header
        if missing:
            raise ValueError(f"{path}: missing column(s): {sorted(missing)}")

        # start=2 because line 1 is the header, so the number in a problem
        # report is the line you can open in an editor and look at.
        for line_number, row in enumerate(reader, start=2):
            ean = (row["ean"] or "").strip()
            name = (row["name"] or "").strip()
            price = parse_decimal(row["unit_price"])
            vat = parse_decimal(row["vat_rate"])

            # One continue per failure: a row gets at most one reason.
            if len(ean) != 13 or not ean.isdigit():
                problems.append((line_number, ean, f"bad EAN: {ean!r}"))
                continue
            if not name:
                problems.append((line_number, ean, "empty name"))
                continue
            if price is None or price < 0:
                problems.append((line_number, ean, f"bad price: {row['unit_price']!r}"))
                continue
            if vat is None or vat not in (0, 7, 19):
                problems.append((line_number, ean, f"bad VAT rate: {row['vat_rate']!r}"))
                continue

            good.append(
                {
                    "ean": ean,  # str - an identifier
                    "name": name,
                    "unit": row["unit"].strip(),
                    "category": row["category"].strip(),
                    "unit_price": price,  # float - money
                    "vat_rate": int(vat),  # int - a code
                    "gross_price": round(price * (1 + vat / 100), 2),
                }
            )

    return good, problems


products, problems = load_products("data/products.csv")

print(f"Loaded {len(products)} products, {len(problems)} problem(s)")
for line_number, ean, reason in problems:
    print(f"  line {line_number}: {reason}")

print(f"\n{'EAN':<15}{'Name':<22}{'Net':>8}{'VAT':>5}{'Gross':>9}")
print("-" * 59)
for p in products[:5]:
    print(
        f"{p['ean']:<15}{p['name']:<22}{p['unit_price']:>8.2f}"
        f"{p['vat_rate']:>4}%{p['gross_price']:>9.2f}"
    )

# --- the danger of treating a code as a number --------------------------
print()
print("Why 'ean' stays a string:")
code = "0401234567890"
print(f"  as text   : {code!r}  ({len(code)} characters)")
print(f"  as int    : {int(code)}  ({len(str(int(code)))} characters)")
print("  The leading zero is gone and every join on this code now fails.")

# --- tests --------------------------------------------------------------
assert parse_decimal("1,35") == 1.35
assert parse_decimal(" 1.35 ") == 1.35
assert parse_decimal("") is None
assert parse_decimal("abc") is None
assert len(products) == 10
assert all(isinstance(p["ean"], str) and len(p["ean"]) == 13 for p in products)
print("\nAll tests passed.")
