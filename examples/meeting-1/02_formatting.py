"""Lesson 2 - formatting numbers and text: width, precision, alignment.

Run me:  python3 examples/meeting-1/02_formatting.py
No input needed. Then open the file and change the numbers.

THE TWO THINGS THAT CONFUSE EVERYONE:
  1. width is a MINIMUM - a small width does nothing at all
  2. print() hides the padding, because padding is spaces
"""

WIDTH = 72


def frame(title):
    print()
    print("=" * WIDTH)
    print(f"  {title}")
    print("=" * WIDTH)


# =====================================================================
frame("THE GRAMMAR")
# =====================================================================
print("""
    {value : [fill][align] [sign] [width] [,] [.precision] [type]}
                *     <  >  ^   +    20    ,     .10        f

    Everything after the colon is optional. Read :20.10f as
    "at least 20 characters wide, 10 digits after the point, fixed-point".
""")

# =====================================================================
frame("1. WIDTH IS A MINIMUM - that is why small widths do nothing")
# =====================================================================
value = 3.14159265358979
print('  "3.1415926536" already needs 12 characters, so:\n')
print(f"    {'spec':<12}{'len':>5}   result (quotes show the padding)")
print("    " + "-" * 52)
for spec in (".10f", "5.10f", "12.10f", "20.10f", "30.10f"):
    out = format(value, spec)
    note = "  <- width ignored" if len(out) == 12 and spec != ".10f" else ""
    print(f"    {'{:' + spec + '}':<12}{len(out):>5}   {out!r}{note}")
print("\n  Width never truncates a number. It only pads.")

# =====================================================================
frame("2. WHY IT LOOKS LIKE NOTHING HAPPENS")
# =====================================================================
print("  The padding is spaces, and print() shows them against the")
print("  background where you cannot see them.\n")
print(f"    print(f\"{{v:20.10f}}\")  ->{format(value, '20.10f')}")
print(f"    f\"{{v:20.10f}}\"         -> {format(value, '20.10f')!r}   <- quotes reveal it")
print("\n  IN THE REPL: leave off print() and the quotes show the padding.")

# =====================================================================
frame("3. WHAT WIDTH IS FOR: columns")
# =====================================================================
prices = [7.5, 1234.5, 89.125, 0.75, 45678.9]
print("  One value looks pointless. A column does not.\n")
print("    :.2f  (no width)        :10.2f  (width 10)")
print("    --------------------    --------------------")
for price in prices:
    print(f"    {format(price, '.2f'):<20}{price:10.2f}")
print("\n  The decimal points line up. That is the whole point, and it")
print("  only shows up across several lines.")

# =====================================================================
frame("4. ALIGNMENT INSIDE THE WIDTH")
# =====================================================================
value = 3.5
print(f"    {'spec':<12}result          meaning")
print("    " + "-" * 56)
for spec, meaning in [
    ("10.2f", "numbers default to RIGHT"),
    (">10.2f", "right, said explicitly"),
    ("<10.2f", "left"),
    ("^10.2f", "centre"),
    ("010.2f", "zero-filled"),
    ("+10.2f", "always show the sign"),
    ("*>10.2f", "any fill character you like"),
]:
    print(f"    {'{:' + spec + '}':<12}{format(value, spec)!r:<16}{meaning}")
print()
print(f"    {'{:10}':<12}{format('abc', '10')!r:<16}TEXT defaults to LEFT")
print("\n  That asymmetry is deliberate: text reads better left-aligned,")
print("  numbers compare better right-aligned.")

# =====================================================================
frame("5. A REAL REPORT NEEDS BOTH")
# =====================================================================
rows = [
    ("Bread 500g", "pcs", 6, 1.35),
    ("Sparkling water 1L", "bottle", 48, 0.65),
    ("Coffee 500g", "pack", 3, 7.99),
    ("Olive oil 750ml", "bottle", 12, 6.49),
]

print(f"  {'Product':<20}{'Unit':<8}{'Qty':>5}{'Price':>10}{'Total':>12}")
print("  " + "-" * 55)
for name, unit, quantity, price in rows:
    print(f"  {name:<20}{unit:<8}{quantity:>5}{price:>10.2f}{quantity * price:>12.2f}")
print("  " + "-" * 55)
total = sum(q * p for _, _, q, p in rows)
print(f"  {'TOTAL':<43}{total:>12.2f}")
print("\n  Text columns use :<20 and :<8. Number columns use :>5 and")
print("  :>10.2f. Every column is a width.")

# =====================================================================
frame("6. LONG TEXT BREAKS A TABLE - unless you truncate it")
# =====================================================================
long_name = "Sparkling mineral water 1 litre glass bottle"
print(f"  the name is {len(long_name)} characters long\n")
print(f"    {'{:<20}':<12}{long_name:<20}|   <- overflows, column ruined")
print(f"    {'{:<20.20}':<12}{long_name:<20.20}|   <- width AND max length")
print("\n  :<20.20 means 'at least 20 wide, at most 20 characters'.")
print("  For text, precision is a MAXIMUM LENGTH - unlike for numbers.")

# =====================================================================
frame("7. THE OTHER TYPE LETTERS")
# =====================================================================
value = 1234.5678
print("  floats:")
for spec, meaning in [
    (".2f", "fixed point - use this"),
    (",.2f", "thousands separator"),
    (".2e", "scientific notation"),
    (".4g", "general: shortest sensible form"),
    (".1%", "as a percentage (multiplies by 100!)"),
]:
    print(f"    {'{:' + spec + '}':<10}{format(value, spec)!r:<18}{meaning}")

print("\n  integers:")
for number, spec, meaning in [
    (255, "d", "decimal"),
    (1234567, ",d", "with thousands separators"),
    (255, "b", "binary"),
    (255, "08b", "binary, zero-padded to 8 digits"),
    (255, "x", "hexadecimal"),
    (255, "#x", "hexadecimal with the 0x prefix"),
]:
    shown = f"{number:>9}"
    print(f"    {'{:' + spec + '}':<10}{format(number, spec)!r:<18}{meaning}  (from{shown})")

# =====================================================================
frame("8. WIDTH FROM A VARIABLE")
# =====================================================================
column_width = 18
decimals = 3
print(f"  column_width = {column_width}, decimals = {decimals}\n")
print(f"    f\"{{value:{{column_width}}.{{decimals}}f}}\"")
print(f"    -> {f'{value:{column_width}.{decimals}f}'!r}")
print("\n  Nested braces let you compute the layout - handy when the width")
print("  depends on the longest value in your data:")
names = ["Bread", "Sparkling water 1L", "Coffee"]
needed = max(len(n) for n in names)
print(f"\n    longest name is {needed} characters, so use :<{needed}")
for name in names:
    print(f"    |{name:<{needed}}|")

# =====================================================================
frame("9. A ROUNDING GOTCHA WORTH KNOWING")
# =====================================================================
print("  Python rounds HALF TO EVEN, and float storage nudges some values:\n")
for v in (0.125, 0.135, 89.125, 2.675):
    print(f"    f\"{{{v}:.2f}}\"  -> {format(v, '.2f')}")
print("\n  0.125 -> 0.12 (down) but 0.135 -> 0.14 (up). Not a typo.")
print("  Fine for display. NOT fine when a total must match an invoice.")
print("  For that, use Decimal with an explicit rounding mode:\n")
from decimal import ROUND_HALF_UP, Decimal

for v in ("0.125", "2.675"):
    rounded = Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"    Decimal({v!r}).quantize(Decimal('0.01'), ROUND_HALF_UP) -> {rounded}")
print("=" * WIDTH)

# --- tests -----------------------------------------------------------
assert format(3.14159265358979, "5.10f") == "3.1415926536", "small width is ignored"
assert len(format(3.14159265358979, "20.10f")) == 20
assert format(3.5, "<10.2f") == "3.50      "
assert format(3.5, ">10.2f") == "      3.50"
assert format(3.5, "^10.2f") == "   3.50   "
assert format(3.5, "010.2f") == "0000003.50"
assert format("abc", "10") == "abc       ", "text defaults to left"
assert format(3.5, "10.2f") == "      3.50", "numbers default to right"
assert format("a very long name", ".6") == "a very", "text precision truncates"
assert format(1234.5678, ",.2f") == "1,234.57"
assert format(255, "08b") == "11111111"
assert f"{1234.5678:{10}.{1}f}" == "    1234.6", "nested width works"
assert format(0.125, ".2f") == "0.12", "half to even"
assert str(Decimal("0.125").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)) == "0.13"
print()
print("All tests passed.")
