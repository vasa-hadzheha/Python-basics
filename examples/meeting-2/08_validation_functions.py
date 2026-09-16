"""Lesson 8 - small, single-purpose, testable functions.  [work-flavoured]

This is the real payoff of the lesson: each function answers ONE question,
so each can be reviewed and tested on its own.

Run me:  python3 examples/meeting-2/08_validation_functions.py
No input needed.
"""


def is_valid_ean13(code):
    """True if code is exactly 13 digits. Expects a string."""
    return isinstance(code, str) and len(code) == 13 and code.isdigit()


def parse_price(raw):
    """Turn '13,50' or ' 13.50 ' into 13.5. Return None if it is not a price.

    Returning None rather than raising lets the CALLER decide what a bad
    price means: skip the row, log it, or substitute zero. Not our job.
    """
    if raw is None:
        return None
    cleaned = str(raw).strip().replace(",", ".")
    try:
        value = float(cleaned)
    except ValueError:
        return None
    return value if value >= 0 else None


def describe(code, raw_price):
    """One-line human summary of a product row."""
    code_ok = "OK " if is_valid_ean13(code) else "BAD"
    price = parse_price(raw_price)
    price_text = f"{price:8.2f}" if price is not None else "       -"
    return f"[{code_ok}] {code:<15}{price_text}"


for code, price in [
    ("4006381333931", "13,50"),
    ("40063813339", "7.00"),  # too short
    ("4006381333931", "abc"),  # unparseable price
    ("4006381333931", "-5"),  # negative price
]:
    print(describe(code, price))

# --- tests: five asserts, one minute of work, real confidence -----------
assert is_valid_ean13("4006381333931") is True
assert is_valid_ean13("123") is False
assert is_valid_ean13("400638133893a") is False
assert is_valid_ean13(4006381333931) is False  # an int, not a string
assert parse_price("13,50") == 13.5
assert parse_price(" 13.50 ") == 13.5
assert parse_price("abc") is None
assert parse_price("-5") is None
assert parse_price(None) is None
print()
print("All tests passed.")
