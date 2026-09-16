"""Exercise 1.2 - Rectangle report.

Practises: input(), float(), f-string alignment.
"""

a = float(input("Side a: "))
b = float(input("Side b: "))

area = a * b
perimeter = 2 * (a + b)

# :<10 = left-align in 10 chars.  :>10.2f = right-align in 10, two decimals.
print(f"{'Area':<10}: {area:>10.2f}")
print(f"{'Perimeter':<10}: {perimeter:>10.2f}")
