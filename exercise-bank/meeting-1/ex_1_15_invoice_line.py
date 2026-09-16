"""Exercise 1.15 - One invoice line, fully validated.  [work-flavoured]

Practises: everything from Meeting 1, on a realistic task.

THE KEY LESSON: a product code is TEXT, not a number.
    int("0401234567890")  ->  401234567890
The leading zero is gone, the length is wrong, and the code will never
again match the same product in another file. Identifiers stay strings.
"""

SEPARATOR = "-" * 42
VALID_VAT_RATES = (0, 7, 19)

# --- product code: exactly 13 digits, kept as a string -------------------
while True:
    code = input("Product code (13 digits): ").strip()  # strip: pasted values
    if len(code) == 13 and code.isdigit():  #   carry stray spaces
        break
    print(f"  x Must be exactly 13 digits (you gave {len(code)} characters).")

# --- quantity: a whole number greater than 0 -----------------------------
while True:
    raw = input("Quantity (whole number): ").strip()
    try:
        quantity = int(raw)
    except ValueError:
        print("  x Not a whole number.")
        continue
    if quantity > 0:
        break
    print("  x Quantity must be greater than 0.")

# --- unit price: a decimal greater than 0 --------------------------------
while True:
    raw = input("Unit price: ").strip().replace(",", ".")  # accept 13,50
    try:
        price = float(raw)
    except ValueError:
        print("  x Not a number.")
        continue
    if price > 0:
        break
    print("  x Price must be greater than 0.")

# --- VAT rate: one of a fixed set ----------------------------------------
while True:
    raw = input(f"VAT rate {VALID_VAT_RATES} in percent: ").strip()
    try:
        vat_rate = int(raw)
    except ValueError:
        print("  x Not a whole number.")
        continue
    if vat_rate in VALID_VAT_RATES:  # "in" tests membership in one go
        break
    print(f"  x Must be one of {VALID_VAT_RATES}.")

# --- the arithmetic ------------------------------------------------------
net = quantity * price
vat_amount = net * vat_rate / 100
gross = net + vat_amount

# --- the report ---------------------------------------------------------
print()
print(SEPARATOR)
print("  INVOICE LINE")
print(SEPARATOR)
print(f"  {'Product code':<15}{code:>20}")
print(f"  {'Quantity':<15}{quantity:>20}")
print(f"  {'Unit price':<15}{price:>20.2f}")
print(f"  {'Net amount':<15}{net:>20.2f}")
print(f"  {f'VAT ({vat_rate}%)':<15}{vat_amount:>20.2f}")
print(f"  {'Gross amount':<15}{gross:>20.2f}")
print(SEPARATOR)
