"""Exercise 2.15 - Find duplicate and invalid product codes.  [work-flavoured]

Practises: the counting pattern, dict comprehensions, sets.

WHY THIS MATTERS: a duplicate key breaks a join. Join two tables on a code
that appears three times on one side and you get three times the rows you
expected - and every total downstream is silently inflated. Checking for
duplicates BEFORE joining is the highest-value validation in data work.
"""

codes = [
    "4006381333931",
    "4009900484147",
    "4006381333931",
    "40099004841",  # too short
    "4311501676851",
    "4006381333931",
    "4311501676851",
    "400990048414X",  # contains a letter
    "",  # empty
]


def is_valid_ean13(code):
    """True if code is exactly 13 digits. Expects a string."""
    return isinstance(code, str) and len(code) == 13 and code.isdigit()


def count_occurrences(values):
    """How many times each value appears. The counting pattern."""
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


counts = count_occurrences(codes)

# A dict comprehension with a filter.
duplicates = {code: n for code, n in counts.items() if n > 1}
invalid = [code for code in counts if not is_valid_ean13(code)]

print(f"Total codes         : {len(codes)}")
print(f"Unique codes        : {len(counts)}")  # or len(set(codes))
print(f"Duplicated codes    : {len(duplicates)}")
print(f"Invalid codes       : {len(invalid)}")

print("\nDuplicates (highest count first):")
for code, n in sorted(duplicates.items(), key=lambda pair: pair[1], reverse=True):
    print(f"  {code:<18}appears {n} times")

print("\nInvalid codes:")
for code in invalid:
    reason = "empty" if not code else f"{len(code)} chars, digits-only={code.isdigit()}"
    print(f"  {code!r:<18}{reason}")

print("\nA set is the fastest way to de-duplicate anything:")
print(f"  len(set(codes)) = {len(set(codes))}")

# --- tests -------------------------------------------------------------
assert count_occurrences(["a", "b", "a"]) == {"a": 2, "b": 1}
assert count_occurrences([]) == {}
assert is_valid_ean13("4006381333931")
assert not is_valid_ean13("400990048414X")
assert not is_valid_ean13("")
assert counts["4006381333931"] == 3
print("\nAll tests passed.")
