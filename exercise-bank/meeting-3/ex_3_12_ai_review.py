"""Exercise 3.12 - Code review of an AI-generated loader, plus a rewrite.

Run from the repository root:
    python3 exercise-bank/meeting-3/ex_3_12_ai_review.py

The generated code is clean, documented, uses `with`, and has error
handling. It is still wrong for our data in eight ways - and every one of
them is a DATA problem, not a Python problem. That is the pattern.
"""

import csv
from pathlib import Path

# =======================================================================
#  1. THE GENERATED CODE
# =======================================================================
GENERATED = '''
import csv

def load_prices(path):
    """Load product prices from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        A dictionary mapping product codes to prices.
    """
    prices = {}
    try:
        with open(path, 'r') as csvfile:                    # line 14
            reader = csv.DictReader(csvfile)                # line 15
            for row in reader:
                prices[int(row['ean'])] = float(row['unit_price'])   # line 17
    except Exception as e:                                  # line 18
        print(f"Error: {e}")                                # line 19
    return prices                                           # line 20
'''

# =======================================================================
#  2. THE REVIEW
# =======================================================================
REVIEW = [
    (
        "BLOCKER",
        15,
        "DictReader defaults to a comma delimiter",
        "data/products.csv is semicolon-separated. Every line parses as ONE "
        "column named 'ean;name;unit;category;unit_price;vat_rate', so line 17 "
        "raises KeyError on the first row. Note the error names 'unit_price', "
        "not 'ean': Python evaluates the right-hand side of an assignment first, "
        "so float(row['unit_price']) runs before the subscript on the left. Worth "
        "knowing when a traceback names an unexpected key. The AI had no way to "
        "know our delimiter - it assumed the US default.",
        "csv.DictReader(f, delimiter=';')",
    ),
    (
        "BLOCKER",
        17,
        "int(row['ean']) destroys the identifier",
        "A code like '0401234567890' becomes 401234567890: the leading zero is "
        "gone and the length drops from 13 to 12. Every lookup against another "
        "file then misses, silently. This is the single most frequent mistake in "
        "generated data code.",
        "keep it as a string: prices[row['ean'].strip()] = ...",
    ),
    (
        "BLOCKER",
        18,
        "except Exception as e: print(...) then return a PARTIAL dict",
        "This is the most dangerous line in the function. Any failure - wrong "
        "delimiter, missing file, one bad price on row 9,000 - is caught, printed "
        "to a terminal nobody is reading, and the function returns a dict "
        "containing however many rows it managed. The caller cannot distinguish "
        "'10 products' from 'the first 3 products, then it broke'. A crash would "
        "be strictly better than this.",
        "either let it raise, or return (prices, errors) so the caller can decide",
    ),
    (
        "MAJOR",
        14,
        "no encoding=, and no utf-8-sig",
        "Without encoding= the function behaves differently on Windows (cp1252) "
        "and Linux (utf-8), so it works on the author's machine and not on a "
        "colleague's. An Excel-exported CSV also carries a BOM, making the first "
        "column '\\ufeffean' - and then row['ean'] raises KeyError while the "
        "printed header looks perfectly normal.",
        "open(path, newline='', encoding='utf-8-sig')",
    ),
    (
        "MAJOR",
        14,
        "newline='' is missing",
        "The csv module requires it. Without it, a quoted field containing a "
        "newline is split across rows on Windows.",
        "add newline='' to the open() call",
    ),
    (
        "MAJOR",
        17,
        "float() with no handling for empty or non-numeric cells",
        "Combined with the bare except, one 'abc' or one empty cell silently "
        "truncates the whole result at that row.",
        "parse with a helper that returns None, then record the row as a reject",
    ),
    (
        "MAJOR",
        17,
        "duplicate eans overwrite silently",
        "If a code appears twice with different prices, the last one wins and "
        "nothing says so. Which price is correct? The function cannot know, and "
        "neither can the caller.",
        "detect duplicates and report them rather than picking arbitrarily",
    ),
    (
        "MINOR",
        20,
        "no count returned",
        "The caller cannot tell whether it loaded 10 rows or 2. len(prices) is "
        "not the answer either, because duplicates collapse.",
        "return the row count alongside the data",
    ),
    (
        "MINOR",
        "4-12",
        "the docstring is confidently wrong about failure",
        "It promises 'a dictionary mapping product codes to prices' with no "
        "mention that the dictionary may be silently incomplete. A docstring that "
        "overstates its guarantees is worse than none, because it stops the next "
        "reader from checking.",
        "document the failure behaviour explicitly",
    ),
    (
        "DESIGN",
        "-",
        "is dict[code] -> price even the right return value?",
        "It throws away name, unit, category and vat_rate. The first time you "
        "need a product name for a report, this function gets rewritten. The "
        "better request would have been: 'return a list of typed records, plus "
        "the rows you could not parse'.",
        "return a list of dicts, or a dict of code -> full record",
    ),
]

WIDTH = 78


def print_review():
    print("=" * WIDTH)
    print("  CODE REVIEW: AI-generated load_prices()")
    print("=" * WIDTH)
    print("  It looks good: typed, documented, uses `with`, has error handling.")
    print("  It will not work on our files, and the way it fails is worse than")
    print("  crashing. Note that all eight defects are DATA problems, not Python")
    print("  problems - the AI has never seen our files and cannot know that our")
    print("  exports are semicolon-separated or that our codes have leading zeros.")
    print()

    for severity in ("BLOCKER", "MAJOR", "MINOR", "DESIGN"):
        items = [f for f in REVIEW if f[0] == severity]
        if not items:
            continue
        print("-" * WIDTH)
        print(f"  {severity}  ({len(items)})")
        print("-" * WIDTH)
        for _, line, what, why, suggestion in items:
            print(f"  line {line}: {what}")
            print(f"      why    : {why}")
            print(f"      suggest: {suggestion}")
            print()

    print("=" * WIDTH)
    print(f"  {len(REVIEW)} findings")
    print("=" * WIDTH)


# =======================================================================
#  3. THE REWRITE
# =======================================================================
def parse_decimal(raw):
    """Text -> float, or None if it will not convert. Accepts '1,35'."""
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def load_products(path, delimiter=";"):
    """Load products from a CSV into a dict keyed by EAN.

    Returns (products, problems, rows_read):
        products   dict of ean (str) -> full record
        problems   list of (line_number, ean, reason) for unusable rows
        rows_read  number of data rows seen

    EANs are kept as STRINGS so leading zeros survive.

    Raises:
        FileNotFoundError  if path does not exist
        ValueError         if a required column is missing

    Never raises on a bad row: it becomes a problem report instead, so the
    caller decides whether to halt, log or continue. The returned dict is
    always complete with respect to the rows that passed - it is never
    silently truncated.
    """
    required = {"ean", "name", "unit", "category", "unit_price", "vat_rate"}
    products, problems = {}, []
    rows_read = 0

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)

        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing column(s) {sorted(missing)}")

        for line_number, row in enumerate(reader, start=2):
            rows_read += 1
            ean = (row["ean"] or "").strip()
            price = parse_decimal(row["unit_price"])
            vat = parse_decimal(row["vat_rate"])

            if len(ean) != 13 or not ean.isdigit():
                problems.append((line_number, ean, f"ean is not 13 digits: {ean!r}"))
                continue
            if ean in products:
                # Reported, not silently overwritten.
                problems.append((line_number, ean, f"duplicate ean {ean}"))
                continue
            if price is None or price < 0:
                problems.append((line_number, ean, f"bad price: {row['unit_price']!r}"))
                continue
            if vat is None or int(vat) not in (0, 7, 19):
                problems.append((line_number, ean, f"bad vat_rate: {row['vat_rate']!r}"))
                continue

            # A full record, not just the price - so the next requirement
            # does not mean rewriting this function.
            products[ean] = {
                "ean": ean,
                "name": row["name"].strip(),
                "unit": row["unit"].strip(),
                "category": row["category"].strip(),
                "unit_price": price,
                "vat_rate": int(vat),
            }

    return products, problems, rows_read


def main():
    print_review()

    source = Path("data/products.csv")
    if not source.exists():
        print(f"\nx {source} not found - run this from the repository root.")
        return

    print()
    print("=" * WIDTH)
    print("  THE REWRITE, RUN ON THE REAL FILE")
    print("=" * WIDTH)

    products, problems, rows_read = load_products(source)
    print(f"  rows read  : {rows_read}")
    print(f"  loaded     : {len(products)}")
    print(f"  problems   : {len(problems)}")
    print(f"  reconciles : {len(products) + len(problems) == rows_read}")

    for line_number, ean, reason in problems:
        print(f"    line {line_number}: {reason}")

    print(f"\n  {'EAN':<15}{'Name':<22}{'Price':>8}")
    print("  " + "-" * 45)
    for record in list(products.values())[:4]:
        print(f"  {record['ean']:<15}{record['name']:<22}{record['unit_price']:>8.2f}")

    # --- what the generated version actually does on our file ----------
    print()
    print("=" * WIDTH)
    print("  WHAT THE GENERATED VERSION DOES ON THIS FILE")
    print("=" * WIDTH)

    def generated_load_prices(path):
        """The AI's version, verbatim, so we can watch it fail."""
        prices = {}
        try:
            with open(path, "r") as csvfile:
                reader = csv.DictReader(csvfile)  # no delimiter
                for row in reader:
                    prices[int(row["ean"])] = float(row["unit_price"])
        except Exception as e:
            print(f"  Error: {e}")
        return prices

    result = generated_load_prices(source)
    print(f"  returned {len(result)} prices")
    print("  It printed one error line and returned an EMPTY dict. A caller that")
    print("  does not check len() would report zero revenue and never know why.")

    # --- and the leading-zero problem, concretely ----------------------
    print()
    print("  The leading-zero problem, concretely:")
    code = "0401234567890"
    print(f"    as text : {code!r}  ({len(code)} chars)")
    print(f"    as int  : {int(code)}   ({len(str(int(code)))} chars)")
    print("    Any join on this code now misses that product, silently.")

    # --- tests ---------------------------------------------------------
    assert len(products) == 10
    assert len(products) + len(problems) == rows_read
    assert all(isinstance(k, str) and len(k) == 13 for k in products)
    assert parse_decimal("1,35") == 1.35
    assert parse_decimal("") is None
    assert result == {}, "the generated version returns nothing on our file"
    print("\n  All tests passed.")


if __name__ == "__main__":
    main()
