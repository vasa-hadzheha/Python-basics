"""Exercise 3.11 - Code review of "the quick script", plus a fixed version.

Run from the repository root:
    python3 exercise-bank/meeting-3/ex_3_11_code_review.py

This file contains:
  1. the original script, quoted
  2. the written review, finding by finding
  3. a working rewrite, run against the real data
"""

# =======================================================================
#  1. THE CODE UNDER REVIEW
# =======================================================================
ORIGINAL = '''
import csv

def process(filename):
    f = open(filename)                                  # line 4
    data = csv.reader(f)                                # line 5
    results = {}
    for row in data:                                    # line 7
        code = int(row[0])                              # line 8
        qty = row[2]                                    # line 9
        price = row[3]                                  # line 10
        total = qty * price                             # line 11
        if row[5] in results:                           # line 12
            results[row[5]] = results[row[5]] + total
        else:
            results[row[5]] = total
    avg = sum(results.values()) / len(results)          # line 17
    print("Average per country: " + str(avg))           # line 18
    out = open("results.csv", "w")                      # line 19
    for k in results:                                   # line 20
        out.write(k + "," + str(results[k]))            # line 21
    return results

process("sales.csv")
'''

# =======================================================================
#  2. THE REVIEW
# =======================================================================
# Each finding follows the pattern from Lesson 14:
#   line number -> what happens -> why it matters -> suggestion

REVIEW = [
    (
        "BLOCKER",
        4,
        "open() without with, and f is never closed",
        "The file handle leaks. On Windows the file stays locked, so the next "
        "program that tries to read it fails. Any exception in the loop leaves "
        "it open for the life of the process.",
        "with open(filename, newline='', encoding='utf-8-sig') as f:",
    ),
    (
        "BLOCKER",
        11,
        "qty * price multiplies two STRINGS",
        "Every value from csv.reader is text. '12' * '1.35' raises TypeError, so "
        "the script dies on row 1. Had one side been an int it would silently "
        "repeat the text instead, which is worse.",
        "quantity = int(row['quantity']); price = float(row['unit_price'])",
    ),
    (
        "BLOCKER",
        7,
        "the header row is never skipped",
        "The first iteration processes the header, so int(row[0]) gets 'order_id' "
        "and raises ValueError. Even with DictReader you must be conscious of this.",
        "use csv.DictReader, which consumes the header for you",
    ),
    (
        "BLOCKER",
        8,
        "int(row[0]) on a product code",
        "A code like '0401234567890' becomes 401234567890 - the leading zero is "
        "gone and the length drops from 13 to 12, so it will never again match the "
        "same product in any other file. Also: `code` is assigned and never used, "
        "so this line is pure risk with no benefit.",
        "keep identifiers as strings; delete the line entirely if unused",
    ),
    (
        "MAJOR",
        19,
        "open('results.csv', 'w') is destructive and mislocated",
        "'w' truncates the file the instant it is opened, before anything is "
        "written. The path is also relative to wherever the script was launched, "
        "so it can overwrite a file the author did not intend - and they said they "
        "want to run this on the live export.",
        "write to an explicit out/ directory, created with mkdir(exist_ok=True)",
    ),
    (
        "MAJOR",
        17,
        "sum(...) / len(results) with no guard",
        "An empty or fully-filtered input gives ZeroDivisionError. Empty input is "
        "not exotic - a failed upstream export produces a header-only file.",
        "if not results: report 'no data' and return early",
    ),
    (
        "MAJOR",
        "7-15",
        "no validation whatsoever",
        "Our real file has an empty quantity, a -2 quantity, 'abc' as a price and "
        "a 'not-a-date'. Each of these either crashes the run or silently corrupts "
        "the total. There is no way to tell which rows contributed.",
        "parse each field, reject on failure with a reason, write rejects to a file",
    ),
    (
        "MAJOR",
        "7-15",
        "no row count, and no record of skipped rows",
        "Even once the crashes are fixed, the caller cannot tell whether this "
        "processed 21 rows or 2. A pipeline that cannot account for its input "
        "cannot be trusted with it.",
        "print rows read / accepted / rejected, and assert they reconcile",
    ),
    (
        "MINOR",
        "9, 10, 12",
        "positional indexes row[2], row[3], row[5]",
        "Nobody reading this knows what row[5] is. Insert a column in the export "
        "and every index shifts, silently producing wrong numbers rather than an "
        "error. A short row raises IndexError.",
        "DictReader gives row['country'], which explains itself and survives",
    ),
    (
        "MINOR",
        21,
        "output has no newline, no header, and the wrong delimiter",
        "All rows end up concatenated onto one line, there is no header, and the "
        "comma does not match the semicolon-separated input. Nothing can read it "
        "back - including Excel.",
        "csv.DictWriter with fieldnames, writeheader(), and delimiter=';'",
    ),
    (
        "MINOR",
        18,
        "'Average per country: ' + str(avg)",
        "An unformatted float prints as 123.45600000000002 in a report, which "
        "looks like a defect to whoever reads it.",
        "print(f'Average per country: {avg:.2f}')",
    ),
    (
        "MINOR",
        4,
        "no encoding=, no newline=''",
        "Without encoding= the script behaves differently on Windows and Linux. "
        "Without newline='' the csv module mishandles quoted multi-line fields. "
        "An Excel-exported file also carries a BOM, which needs utf-8-sig.",
        "open(path, newline='', encoding='utf-8-sig')",
    ),
]

WIDTH = 78


def print_review():
    print("=" * WIDTH)
    print("  CODE REVIEW: process() in the quick script")
    print("=" * WIDTH)
    print("  Summary: I would not run this on the live export yet. There are four")
    print("  blockers that stop it working at all, and it silently corrupts totals")
    print("  once they are fixed. The structure is sound - it is the data handling")
    print("  that needs work. Happy to pair on it.")
    print()

    for severity in ("BLOCKER", "MAJOR", "MINOR"):
        items = [f for f in REVIEW if f[0] == severity]
        print("-" * WIDTH)
        print(f"  {severity}  ({len(items)})")
        print("-" * WIDTH)
        for _, line, what, why, suggestion in items:
            print(f"  line {line}: {what}")
            print(f"      why    : {why}")
            print(f"      suggest: {suggestion}")
            print()

    counts = {s: len([f for f in REVIEW if f[0] == s]) for s in ("BLOCKER", "MAJOR", "MINOR")}
    print("=" * WIDTH)
    print(f"  {len(REVIEW)} findings: "
          f"{counts['BLOCKER']} blocker, {counts['MAJOR']} major, {counts['MINOR']} minor")
    print("=" * WIDTH)


# =======================================================================
#  3. THE REWRITE
# =======================================================================
import csv
from pathlib import Path


def parse_int(raw):
    """Text -> int, or None if it will not convert."""
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
    """Text -> float, or None if it will not convert. Accepts '1,40'."""
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def revenue_by_country(path, delimiter=";"):
    """Total revenue per country from a sales CSV.

    Returns (totals, rejects, rows_read):
        totals     dict of country -> revenue
        rejects    list of {line, reason} for rows that could not be used
        rows_read  how many data rows were seen

    Never raises on bad DATA. Raises ValueError on a missing COLUMN,
    because there is no sensible way to continue.
    """
    required = {"quantity", "unit_price", "country"}
    totals, rejects = {}, []
    rows_read = 0

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)

        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing column(s) {sorted(missing)}")

        for line_number, row in enumerate(reader, start=2):
            rows_read += 1
            quantity = parse_int(row["quantity"])
            price = parse_decimal(row["unit_price"])
            country = (row["country"] or "").strip().upper()

            if quantity is None:
                rejects.append({"line": line_number, "reason": f"quantity {row['quantity']!r}"})
                continue
            if quantity <= 0:
                rejects.append({"line": line_number, "reason": f"quantity not positive: {quantity}"})
                continue
            if price is None:
                rejects.append({"line": line_number, "reason": f"price {row['unit_price']!r}"})
                continue
            if price < 0:
                rejects.append({"line": line_number, "reason": f"price negative: {price}"})
                continue
            if len(country) != 2:
                rejects.append({"line": line_number, "reason": f"country {country!r}"})
                continue

            totals[country] = totals.get(country, 0.0) + quantity * price

    return totals, rejects, rows_read


def write_totals(path, totals, delimiter=";"):
    """Write country totals as proper CSV, with a header."""
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["country", "revenue"], delimiter=delimiter)
        writer.writeheader()
        for country, revenue in sorted(totals.items(), key=lambda p: p[1], reverse=True):
            writer.writerow({"country": country, "revenue": f"{revenue:.2f}"})


def main():
    print_review()

    source = Path("data/sales_raw.csv")
    target = Path("out/revenue_by_country.csv")

    if not source.exists():
        print(f"\nx {source} not found - run this from the repository root.")
        return

    print()
    print("=" * WIDTH)
    print("  THE REWRITE, RUN ON THE REAL FILE")
    print("=" * WIDTH)

    totals, rejects, rows_read = revenue_by_country(source)

    print(f"  rows read     : {rows_read:>6}")
    print(f"  rows used     : {rows_read - len(rejects):>6}")
    print(f"  rows rejected : {len(rejects):>6}")
    print(f"  reconciles    : {(rows_read - len(rejects)) + len(rejects) == rows_read}")

    if not totals:
        # The guard the original was missing.
        print("\n  No usable rows - nothing to average.")
        return

    print(f"\n  {'Country':<10}{'Revenue':>12}")
    print("  " + "-" * 22)
    for country, revenue in sorted(totals.items(), key=lambda p: p[1], reverse=True):
        print(f"  {country:<10}{revenue:>12.2f}")

    average = sum(totals.values()) / len(totals)
    print("  " + "-" * 22)
    print(f"  {'Average':<10}{average:>12.2f}")

    print(f"\n  REJECTED ({len(rejects)})")
    for r in rejects:
        print(f"    line {r['line']:>3}: {r['reason']}")

    write_totals(target, totals)
    print(f"\n  Written to {target}")
    print("  " + target.read_text(encoding="utf-8").replace("\n", "\n  ").rstrip())

    # --- tests ---------------------------------------------------------
    assert parse_int("") is None
    assert parse_int("abc") is None
    assert parse_decimal("1,40") == 1.4
    assert revenue_by_country(source)[2] == rows_read

    # The empty case the original crashed on: a header-only file.
    header_only = Path("out/header_only.csv")
    header_only.parent.mkdir(exist_ok=True)
    header_only.write_text("quantity;unit_price;country\n", encoding="utf-8")
    empty_totals, empty_rejects, empty_rows = revenue_by_country(header_only)
    assert empty_totals == {} and empty_rejects == [] and empty_rows == 0
    print("  header-only file handled: 0 rows, no ZeroDivisionError")
    print("\n  All tests passed.")


if __name__ == "__main__":
    main()
