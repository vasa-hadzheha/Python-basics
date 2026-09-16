"""Exercise 3.6 - Validate a product file into clean rows and rejects.
[work-flavoured]

Practises: header checking, one reason per reject, reconciliation.

Run from the repository root.
"""

import csv
from pathlib import Path

SOURCE = Path("data/products.csv")
CLEAN = Path("out/products_clean.csv")
REJECTS = Path("out/products_rejects.csv")
DELIMITER = ";"
REQUIRED = {"ean", "name", "unit", "category", "unit_price", "vat_rate"}
VALID_VAT_RATES = (0, 7, 19)

CLEAN_COLUMNS = ["ean", "name", "unit", "category", "unit_price", "vat_rate", "gross_price"]
REJECT_COLUMNS = ["line", "ean", "reason"]


def parse_decimal(raw):
    """Text -> float, or None if it will not convert."""
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def validate_products(path):
    """Return (clean, rejects, total_rows).

    Raises on a missing COLUMN (a broken file), never on a bad ROW.
    """
    clean, rejects = [], []
    total = 0
    seen_eans = set()

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=DELIMITER)

        # Header first: one clear error, not 40,000 KeyErrors.
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing column(s) {sorted(missing)}")

        for line_number, row in enumerate(reader, start=2):
            total += 1
            ean = (row["ean"] or "").strip()
            name = (row["name"] or "").strip()
            price = parse_decimal(row["unit_price"])
            vat = parse_decimal(row["vat_rate"])

            def reject(reason):
                rejects.append({"line": line_number, "ean": ean, "reason": reason})

            # One continue per failure: at most one reason per row.
            if len(ean) != 13 or not ean.isdigit():
                reject(f"ean is not 13 digits: {ean!r}")
                continue
            if ean in seen_eans:
                reject(f"duplicate ean {ean}")
                continue
            if not name:
                reject("name is empty")
                continue
            if price is None:
                reject(f"unit_price is not a number: {row['unit_price']!r}")
                continue
            if price <= 0:
                reject(f"unit_price must be greater than 0, got {price}")
                continue
            if vat is None or int(vat) not in VALID_VAT_RATES:
                reject(f"vat_rate must be one of {VALID_VAT_RATES}, got {row['vat_rate']!r}")
                continue

            seen_eans.add(ean)
            clean.append({
                "ean": ean,
                "name": name,
                "unit": row["unit"].strip(),
                "category": row["category"].strip(),
                "unit_price": price,
                "vat_rate": int(vat),
                "gross_price": round(price * (1 + vat / 100), 2),
            })

    return clean, rejects, total


def write_csv(path, rows, fieldnames):
    """Write rows to CSV. Writes a header even when rows is empty."""
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=DELIMITER)
        writer.writeheader()
        writer.writerows(rows)


if not SOURCE.exists():
    print(f"x {SOURCE} not found - run this from the repository root.")
    raise SystemExit(1)

clean, rejects, total = validate_products(SOURCE)
write_csv(CLEAN, clean, CLEAN_COLUMNS)
write_csv(REJECTS, rejects, REJECT_COLUMNS)

print("=" * 52)
print("  PRODUCT FILE VALIDATION")
print("=" * 52)
print(f"  rows read     : {total:>5}")
print(f"  rows accepted : {len(clean):>5}  -> {CLEAN}")
print(f"  rows rejected : {len(rejects):>5}  -> {REJECTS}")
print(f"  reconciles    : {len(clean) + len(rejects) == total}")

if rejects:
    print("\n  REJECTED")
    for r in rejects:
        print(f"    line {r['line']:>3}  {r['ean']:<15}{r['reason']}")

# --- prove the validator catches each planted problem -------------------
print("\n" + "=" * 52)
print("  SELF-TEST ON DELIBERATELY BROKEN ROWS")
print("=" * 52)

BROKEN = Path("out/products_broken.csv")
BROKEN.parent.mkdir(exist_ok=True)
BROKEN.write_text(
    "ean;name;unit;category;unit_price;vat_rate\n"
    "4006381333931;Good row;pcs;bakery;1.35;7\n"
    "40063813;Short ean;pcs;bakery;1.35;7\n"
    "4009900484147;;pcs;dairy;1.40;7\n"
    "4311501676851;Bad price;pack;grocery;abc;19\n"
    "5000112637922;Zero price;can;drinks;0;19\n"
    "4008400403021;Bad vat;bar;confectionery;2.49;13\n"
    "4006381333931;Duplicate ean;pcs;bakery;1.35;7\n",
    encoding="utf-8",
)

broken_clean, broken_rejects, broken_total = validate_products(BROKEN)
print(f"  rows read     : {broken_total}")
print(f"  rows accepted : {len(broken_clean)}")
print(f"  rows rejected : {len(broken_rejects)}")
for r in broken_rejects:
    print(f"    line {r['line']:>3}  {r['reason']}")

assert len(broken_clean) == 1, "only the good row should survive"
assert len(broken_rejects) == 6
assert broken_clean[0]["name"] == "Good row"
assert len(clean) == 10 and len(rejects) == 0, "the real file is clean"
print("\nAll tests passed.")
