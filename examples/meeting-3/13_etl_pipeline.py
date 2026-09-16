"""Lesson 13 - a complete ETL pipeline, end to end.

    EXTRACT -> VALIDATE -> TRANSFORM -> LOAD -> REPORT

Reads   data/sales_raw.csv  (deliberately messy)
        data/products.csv   (the reference list)
Writes  out/clean_sales.csv
        out/rejects.csv
        out/sales.db
        a report on the terminal

Run me from the repository root:
    python3 examples/meeting-3/13_etl_pipeline.py

Every function here is small enough to review on its own. That is the point.
"""

import csv
import sqlite3
from datetime import date
from pathlib import Path

# --- configuration, all in one place ------------------------------------
# A reviewer should be able to see every tunable value without reading the code.
SALES_CSV = Path("data/sales_raw.csv")
PRODUCTS_CSV = Path("data/products.csv")
OUT_DIR = Path("out")
DELIMITER = ";"
ENCODING = "utf-8-sig"  # utf-8-sig: strips Excel's BOM
VALID_VAT_RATES = (0, 7, 19)
WIDTH = 72


# =======================================================================
#  helpers
# =======================================================================
def parse_decimal(raw):
    """'1,40' or ' 1.40 ' -> 1.4.  None if it is not a number."""
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


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


def parse_iso_date(raw):
    """'2026-01-05' -> date(2026, 1, 5).  None if it is not an ISO date."""
    if raw is None:
        return None
    try:
        return date.fromisoformat(str(raw).strip())
    except ValueError:
        return None


def is_valid_ean13(code):
    """True if code is exactly 13 digits. Identifiers stay strings."""
    return isinstance(code, str) and len(code) == 13 and code.isdigit()


def frame(title):
    """Print a framed heading, so the terminal output is scannable."""
    print("=" * WIDTH)
    print(f"  {title}")
    print("=" * WIDTH)


# =======================================================================
#  EXTRACT
# =======================================================================
def load_products(path):
    """Read the reference product list into a dict keyed by EAN.

    Keyed by EAN because we are about to look products up 20 times - or
    40,000 times on a real file. A dict lookup is O(1); scanning a list
    each time is O(n), and nested loops are how a 5-second job becomes a
    5-hour job. (Exercise 2.16.)
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found - run this from the repository root")

    with open(path, newline="", encoding=ENCODING) as f:
        reader = csv.DictReader(f, delimiter=DELIMITER)
        return {
            row["ean"].strip(): {
                "name": row["name"].strip(),
                "category": row["category"].strip(),
                "vat_rate": int(row["vat_rate"]),
            }
            for row in reader
        }


def extract_sales(path):
    """Read the raw sales file as a list of (line_number, row) pairs.

    line_number starts at 2 because line 1 is the header - so the number
    in an error message is the line you can open in an editor and look at.
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found - run this from the repository root")

    with open(path, newline="", encoding=ENCODING) as f:
        reader = csv.DictReader(f, delimiter=DELIMITER)

        # Check the header BEFORE reading rows. If a supplier renamed a
        # column, fail once with a clear message - not 40,000 KeyErrors.
        required = {"order_id", "order_date", "ean", "quantity", "unit_price", "customer", "country"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing column(s) {sorted(missing)}")

        return list(enumerate(reader, start=2))


# =======================================================================
#  VALIDATE + TRANSFORM
# =======================================================================
def validate_and_transform(raw_rows, products):
    """Turn raw text rows into typed records.

    Returns (clean, rejects). Never raises on bad data and never prints:
    a bad row becomes a reject with a reason, so nothing is lost silently
    and the caller decides what to do about it.
    """
    clean = []
    rejects = []
    seen_order_ids = set()

    for line_number, row in raw_rows:
        order_id = parse_int(row.get("order_id"))
        order_date = parse_iso_date(row.get("order_date"))
        ean = (row.get("ean") or "").strip()
        quantity = parse_int(row.get("quantity"))
        unit_price = parse_decimal(row.get("unit_price"))
        customer = (row.get("customer") or "").strip()
        country = (row.get("country") or "").strip().upper()

        def reject(reason):
            rejects.append(
                {
                    "line": line_number,
                    "order_id": row.get("order_id", ""),
                    "ean": ean,
                    "reason": reason,
                }
            )

        # One "continue" per failure, so a row produces at most one reason.
        # Cheapest and most fundamental checks first.
        if order_id is None:
            reject(f"order_id is not a whole number: {row.get('order_id')!r}")
            continue
        if order_id in seen_order_ids:
            reject(f"duplicate order_id {order_id}")
            continue
        if order_date is None:
            reject(f"order_date is not an ISO date: {row.get('order_date')!r}")
            continue
        if not is_valid_ean13(ean):
            reject(f"ean is not 13 digits: {ean!r}")
            continue
        if ean not in products:
            # A referential-integrity failure: the code is well formed but
            # names no product we know. This is what a FOREIGN KEY checks.
            reject(f"ean {ean} is not in the product list")
            continue
        if quantity is None:
            reject(f"quantity is not a whole number: {row.get('quantity')!r}")
            continue
        if quantity <= 0:
            reject(f"quantity must be positive, got {quantity}")
            continue
        if unit_price is None:
            reject(f"unit_price is not a number: {row.get('unit_price')!r}")
            continue
        if unit_price < 0:
            reject(f"unit_price must not be negative, got {unit_price}")
            continue
        if not country or len(country) != 2:
            reject(f"country is not a 2-letter code: {country!r}")
            continue

        seen_order_ids.add(order_id)

        product = products[ean]
        vat_rate = product["vat_rate"]
        net = round(quantity * unit_price, 2)
        vat_amount = round(net * vat_rate / 100, 2)

        clean.append(
            {
                "order_id": order_id,
                "order_date": order_date.isoformat(),  # store dates as ISO text
                "ean": ean,  # str: leading zeros survive
                "product_name": product["name"],
                "category": product["category"],
                "quantity": quantity,
                "unit_price": unit_price,
                "vat_rate": vat_rate,
                "net_amount": net,
                "vat_amount": vat_amount,
                "gross_amount": round(net + vat_amount, 2),
                "customer": customer,
                "country": country,
            }
        )

    return clean, rejects


# =======================================================================
#  LOAD
# =======================================================================
SCHEMA = """
DROP TABLE IF EXISTS sale;
CREATE TABLE sale (
    order_id     INTEGER PRIMARY KEY,
    order_date   TEXT    NOT NULL,
    ean          TEXT    NOT NULL,
    product_name TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    quantity     INTEGER NOT NULL CHECK (quantity > 0),
    unit_price   REAL    NOT NULL CHECK (unit_price >= 0),
    vat_rate     INTEGER NOT NULL CHECK (vat_rate IN (0, 7, 19)),
    net_amount   REAL    NOT NULL,
    vat_amount   REAL    NOT NULL,
    gross_amount REAL    NOT NULL,
    customer     TEXT    NOT NULL,
    country      TEXT    NOT NULL CHECK (length(country) = 2)
);
"""

COLUMNS = [
    "order_id", "order_date", "ean", "product_name", "category",
    "quantity", "unit_price", "vat_rate", "net_amount", "vat_amount",
    "gross_amount", "customer", "country",
]


def write_csv(path, rows, fieldnames):
    """Write rows to a CSV. Writes a header even when there are no rows."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=DELIMITER)
        writer.writeheader()
        writer.writerows(rows)


def load_to_sqlite(path, rows):
    """Load clean rows into SQLite.

    The CHECK and PRIMARY KEY constraints repeat the checks we already did
    in Python. That repetition is deliberate: validation protects this one
    script, a constraint protects the data from every script, forever.
    """
    connection = sqlite3.connect(path)
    try:
        connection.executescript(SCHEMA)
        placeholders = ", ".join("?" for _ in COLUMNS)
        connection.executemany(
            f"INSERT INTO sale ({', '.join(COLUMNS)}) VALUES ({placeholders})",
            [tuple(row[c] for c in COLUMNS) for row in rows],
        )
        connection.commit()  # without this, nothing is saved
    except Exception:
        connection.rollback()  # all or nothing
        raise
    finally:
        connection.close()


# =======================================================================
#  REPORT
# =======================================================================
def report(connection, raw_count, clean_count, reject_count):
    """Print the run summary and a few aggregate tables."""
    frame("RUN SUMMARY")
    print(f"  rows read     : {raw_count:>6}")
    print(f"  rows accepted : {clean_count:>6}")
    print(f"  rows rejected : {reject_count:>6}")
    print(f"  {'-' * 30}")
    print(f"  reconciles    : {clean_count + reject_count == raw_count}")
    rate = clean_count / raw_count * 100 if raw_count else 0.0
    print(f"  acceptance    : {rate:>5.1f}%")

    print()
    frame("REVENUE BY COUNTRY")
    print(f"  {'Country':<10}{'Orders':>8}{'Units':>8}{'Net':>12}{'Gross':>12}")
    print("  " + "-" * 50)
    for row in connection.execute("""
        SELECT   country,
                 COUNT(*)            AS orders,
                 SUM(quantity)       AS units,
                 SUM(net_amount)     AS net,
                 SUM(gross_amount)   AS gross
        FROM     sale
        GROUP BY country
        ORDER BY gross DESC
    """):
        print(f"  {row['country']:<10}{row['orders']:>8}{row['units']:>8}"
              f"{row['net']:>12.2f}{row['gross']:>12.2f}")

    print()
    frame("TOP PRODUCTS BY GROSS REVENUE")
    print(f"  {'Product':<22}{'Category':<16}{'Units':>8}{'Gross':>12}")
    print("  " + "-" * 58)
    for row in connection.execute("""
        SELECT   product_name, category,
                 SUM(quantity)     AS units,
                 SUM(gross_amount) AS gross
        FROM     sale
        GROUP BY ean
        ORDER BY gross DESC
        LIMIT    5
    """):
        print(f"  {row['product_name']:<22}{row['category']:<16}"
              f"{row['units']:>8}{row['gross']:>12.2f}")

    print()
    frame("GRAND TOTAL")
    totals = connection.execute("""
        SELECT COUNT(*)          AS orders,
               SUM(quantity)     AS units,
               SUM(net_amount)   AS net,
               SUM(vat_amount)   AS vat,
               SUM(gross_amount) AS gross
        FROM   sale
    """).fetchone()
    print(f"  orders {totals['orders']}   units {totals['units']}")
    print(f"  net {totals['net']:.2f}   VAT {totals['vat']:.2f}   gross {totals['gross']:.2f}")
    # An arithmetic self-check: net + VAT must equal gross.
    difference = abs((totals["net"] + totals["vat"]) - totals["gross"])
    print(f"  net + VAT == gross : {difference < 0.005}")


# =======================================================================
#  the pipeline, as one readable sequence
# =======================================================================
def main():
    OUT_DIR.mkdir(exist_ok=True)

    # EXTRACT
    products = load_products(PRODUCTS_CSV)
    raw_rows = extract_sales(SALES_CSV)
    print(f"Extracted {len(raw_rows)} sales rows and {len(products)} reference products\n")

    # VALIDATE + TRANSFORM
    clean, rejects = validate_and_transform(raw_rows, products)

    # LOAD
    write_csv(OUT_DIR / "clean_sales.csv", clean, COLUMNS)
    write_csv(OUT_DIR / "rejects.csv", rejects, ["line", "order_id", "ean", "reason"])
    database = OUT_DIR / "sales.db"
    load_to_sqlite(database, clean)

    # REPORT
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    try:
        report(connection, len(raw_rows), len(clean), len(rejects))
    finally:
        connection.close()

    if rejects:
        print()
        frame(f"REJECTED ROWS ({len(rejects)})")
        for r in rejects:
            print(f"  line {r['line']:>3}  order {r['order_id']:<6}  {r['reason']}")
        print()
        print(f"  Written to {OUT_DIR / 'rejects.csv'} - nothing was dropped silently.")

    print()
    print(f"Outputs: {OUT_DIR}/clean_sales.csv, {OUT_DIR}/rejects.csv, {database}")


if __name__ == "__main__":
    main()
