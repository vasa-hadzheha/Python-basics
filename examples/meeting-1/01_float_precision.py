"""Lesson 1 - why 0.1 + 0.2 is not 0.3, and how to SEE it.

Run me:  python3 examples/meeting-1/01_float_precision.py
No input needed.

Starts with the thing that hides the problem: a format spec that looks
like it asks for more digits but asks for more WIDTH.
"""

from decimal import Decimal

WIDTH = 70


def frame(title):
    print()
    print("=" * WIDTH)
    print(f"  {title}")
    print("=" * WIDTH)


# =====================================================================
frame("1. WHY YOU CANNOT SEE THE PROBLEM: width is not precision")
# =====================================================================
print("  In a format spec the number BEFORE the dot is the WIDTH,")
print("  and the number AFTER the dot is the PRECISION.\n")
print(f"  f\"{{0.1:10f}}\"    -> {f'{0.1:10f}'!r}")
print("                       width 10, and 6 decimals - the DEFAULT\n")
print(f"  f\"{{0.1:20f}}\"    -> {f'{0.1:20f}'!r}")
print("                       width 20, STILL 6 decimals - just more padding\n")
print("  Asking for width 100 changes nothing except the padding, which")
print("  is why 0.1 keeps looking like a clean 0.100000.\n")
print("  Add the DOT and you are asking for decimals:\n")
print(f"  f\"{{0.1:.20f}}\"   -> {f'{0.1:.20f}'!r}")
print(f"  f\"{{0.1:.30f}}\"   -> {f'{0.1:.30f}'!r}")
print(f"  f\"{{0.1:.55f}}\"   -> {f'{0.1:.55f}'!r}")
print()
print("  There it is. 0.1 was never exactly 0.1.")
print()
print("  spec      meaning")
print("  --------  -----------------------------------------")
print("  :10f      width 10, 6 decimals (default)")
print("  :.10f     10 decimals, no minimum width")
print("  :20.10f   width 20 AND 10 decimals")
print("  :.2f      2 decimals - what you want for money")

# =====================================================================
frame("2. WHAT IS ACTUALLY STORED")
# =====================================================================
for value in (0.1, 0.2, 0.3):
    print(f"  you type {value!s:<5} -> stored as {Decimal(value)}")

# =====================================================================
frame("3. WHY: 0.1 HAS NO EXACT BINARY FORM")
# =====================================================================


def to_binary(x, bits=50):
    """Write the fractional part of x in base 2, bit by bit."""
    whole = int(x)
    frac = x - whole
    bits_out = []
    for _ in range(bits):
        frac *= 2
        bit = int(frac)
        bits_out.append(str(bit))
        frac -= bit
    return f"{whole}." + "".join(bits_out)


print("  A computer stores numbers in base 2, using only halves,")
print("  quarters, eighths ... Some decimals fit. Some never do.\n")
print("  1/10 in DECIMAL = 0.1                exact")
print("  1/3  in DECIMAL = 0.3333333...       never ends")
print("  1/10 in BINARY  = 0.000110011001...  never ends\n")
print(f"  0.1 in binary = {to_binary(0.1)[:40]}...")
print("                     ^^^^ '0011' repeating, forever\n")
print("  A float has room for 53 binary digits, so the repeating")
print("  pattern is CUT OFF. The stored value is very slightly wrong.")
print("  It is the same reason you cannot write 1/3 exactly on paper.")

# =====================================================================
frame("4. SO THE SUM IS GENUINELY A DIFFERENT NUMBER")
# =====================================================================
print(f"  0.1 + 0.2 produces  {Decimal(0.1 + 0.2)}")
print(f"  0.3       is        {Decimal(0.3)}")
print()
print("  They first differ at the 17th decimal place, so:")
print(f"    0.1 + 0.2 == 0.3   ->  {0.1 + 0.2 == 0.3}")
print()
print("  How far apart? Exactly ONE step - look at the last hex digit:")
print(f"    (0.1 + 0.2).hex() = {(0.1 + 0.2).hex()}")
print(f"    (0.3).hex()       = {(0.3).hex()}")
print("                                        ^ 4 vs 3")
print("  They are adjacent floats. There is no value in between.")

# =====================================================================
frame("5. SOME DECIMALS ARE EXACT - THE POWERS OF TWO")
# =====================================================================
for value in (0.5, 0.25, 0.125, 0.75, 2.5, 0.1, 0.3):
    exact = Decimal(value) == Decimal(str(value))
    mark = "exact" if exact else "NOT exact"
    print(f"  {value!s:<7} {mark:<10} {Decimal(value)}")
print()
print("  0.5 = 1/2, 0.25 = 1/4, 0.125 = 1/8 - all powers of two, so binary")
print("  represents them perfectly. 0.1 = 1/10 and 10 is not a power of two.")

# =====================================================================
frame("6. WHAT TO DO ABOUT IT")
# =====================================================================
import math

print("  (a) Never compare floats with == . Use a tolerance:\n")
print(f"      0.1 + 0.2 == 0.3                        -> {0.1 + 0.2 == 0.3}")
print(f"      abs((0.1 + 0.2) - 0.3) < 1e-9           -> {abs((0.1 + 0.2) - 0.3) < 1e-9}")
print(f"      math.isclose(0.1 + 0.2, 0.3)            -> {math.isclose(0.1 + 0.2, 0.3)}")
print()
print("  (b) For DISPLAY, round to the decimals you mean:\n")
print(f"      f\"{{0.1 + 0.2:.2f}}\"  -> {f'{0.1 + 0.2:.2f}'}   <- always do this for money")
print()
print("  (c) For MONEY that must be exact to the cent, use Decimal:\n")
a, b = Decimal("0.1"), Decimal("0.2")
print(f"      Decimal('0.1') + Decimal('0.2')  -> {a + b}")
print(f"      ... == Decimal('0.3')            -> {a + b == Decimal('0.3')}")
print("      Note the QUOTES: Decimal('0.1') is exact,")
print(f"      but Decimal(0.1) inherits the broken float: {Decimal(0.1)}")
print()
print("  (d) Or store money as whole cents in an int, and divide only")
print("      when you print it. Banks do this.")
print()
print("  This is NOT a Python bug. Every language using IEEE 754 doubles")
print("  behaves identically - C, Java, JavaScript, Excel, SQL.")
print("=" * WIDTH)

# --- tests -----------------------------------------------------------
assert 0.1 + 0.2 != 0.3
assert math.isclose(0.1 + 0.2, 0.3)
assert abs((0.1 + 0.2) - 0.3) < 1e-9
assert f"{0.1 + 0.2:.2f}" == "0.30"
assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
assert Decimal(0.1) != Decimal("0.1"), "Decimal(float) keeps the float error"
assert f"{0.1:20f}" == "            0.100000", "width, not precision"
assert f"{0.1:.20f}" == "0.10000000000000000555", "the dot means precision"
assert Decimal(0.5) == Decimal("0.5"), "powers of two are exact"
print()
print("All tests passed.")
