"""Exercise 2.16 - Reconcile a supplier price list against our own.
[work-flavoured] This is the real job, in miniature.

Practises: keying a list of dicts by id BEFORE comparing; set operations on
dict keys; comparing money with a tolerance.

THE KEY IDEA: build a dict keyed by code first. Then membership is a lookup,
not a nested loop.
    nested loops : 40,000 x 40,000 = 1.6 BILLION comparisons
    dict lookups : 40,000
This is the single most valuable performance idea in the course.
"""

import math

# Half a cent: two prices closer than this are "the same price".
PRICE_TOLERANCE = 0.005

supplier = [
    {"code": "4006381333931", "name": "Bread 500g", "price": 13.50},
    {"code": "4009900484147", "name": "Milk 1L", "price": 14.00},
    {"code": "4311501676851", "name": "Salt 1kg", "price": 7.20},
    {"code": "5000112637922", "name": "Cola 330ml", "price": 11.99},
]

ours = [
    {"code": "4006381333931", "name": "Bread 500g", "price": 13.50},
    {"code": "4009900484147", "name": "Milk 1L", "price": 13.80},
    {"code": "4311501676851", "name": "Salt 1kg", "price": 7.20},
    {"code": "9999999999999", "name": "Old item", "price": 3.00},
]


def key_by(rows, field):
    """Turn a list of dicts into a dict keyed by one field."""
    return {row[field]: row for row in rows}


def same_price(a, b):
    """True if two prices agree to within half a cent.

    NEVER use == on money read from a file: a price that arrived as
    13.499999999999998 would report as a change.
    """
    return math.fabs(a - b) < PRICE_TOLERANCE


def percent_change(old, new):
    """Percentage change from old to new. None if old is 0."""
    if old == 0:  # ZeroDivisionError on real data is a matter of when, not if
        return None
    return (new - old) / old * 100


supplier_by_code = key_by(supplier, "code")
ours_by_code = key_by(ours, "code")

# Dict keys behave as sets, so these three lines are an INNER JOIN and two
# LEFT JOIN-with-no-match checks.
in_both = supplier_by_code.keys() & ours_by_code.keys()
only_supplier = supplier_by_code.keys() - ours_by_code.keys()
only_ours = ours_by_code.keys() - supplier_by_code.keys()

unchanged = []
changed = []
for code in sorted(in_both):
    old = ours_by_code[code]["price"]
    new = supplier_by_code[code]["price"]
    if same_price(old, new):
        unchanged.append(code)
    else:
        changed.append((code, old, new))

WIDTH = 74
print("=" * WIDTH)
print("  PRICE LIST RECONCILIATION")
print("=" * WIDTH)
print(f"  supplier rows: {len(supplier)}    our rows: {len(ours)}")
print(f"  matched: {len(in_both)}    unchanged: {len(unchanged)}    changed: {len(changed)}")
print(f"  new: {len(only_supplier)}    discontinued: {len(only_ours)}")

print("-" * WIDTH)
print("  PRICE CHANGES")
if not changed:
    print("  (none)")
for code, old, new in changed:
    pct = percent_change(old, new)
    pct_text = f"{pct:+7.2f}%" if pct is not None else "      -"
    name = supplier_by_code[code]["name"]
    print(f"  {code}  {name:<14}{old:>8.2f} -> {new:>8.2f}  {new - old:>+8.2f}  {pct_text}")

print("-" * WIDTH)
print("  NEW PRODUCTS (supplier only)")
if not only_supplier:
    print("  (none)")
for code in sorted(only_supplier):
    p = supplier_by_code[code]
    print(f"  {code}  {p['name']:<14}{p['price']:>8.2f}")

print("-" * WIDTH)
print("  DISCONTINUED (ours only)")
if not only_ours:
    print("  (none)")
for code in sorted(only_ours):
    p = ours_by_code[code]
    print(f"  {code}  {p['name']:<14}{p['price']:>8.2f}")

print("-" * WIDTH)
print("  UNCHANGED")
print(f"  {', '.join(sorted(unchanged)) or '(none)'}")
print("=" * WIDTH)

# --- tests -------------------------------------------------------------
assert key_by([{"c": "x", "v": 1}], "c") == {"x": {"c": "x", "v": 1}}
assert same_price(13.50, 13.499999999999998)
assert not same_price(13.50, 13.80)
assert percent_change(10, 12) == 20.0
assert percent_change(0, 5) is None
assert len(in_both) == 3
assert only_supplier == {"5000112637922"}
assert only_ours == {"9999999999999"}
assert [c for c, _, _ in changed] == ["4009900484147"]
print("All tests passed.")
