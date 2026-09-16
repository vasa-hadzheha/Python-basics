"""Lesson 1 - Values and types.

Run me:  python3 examples/meeting-1/01_types.py
No input needed. Read the code, predict each line, then compare.
"""

# --- the four types -------------------------------------------------------
quantity = 10          # int    - a whole number
price = 13.50          # float  - a decimal number
product = "Bread"      # str    - text
available = True       # bool   - True or False

print("quantity :", quantity, type(quantity))
print("price    :", price, type(price))
print("product  :", product, type(product))
print("available:", available, type(available))

print("-" * 50)

# --- "10" is not 10 -------------------------------------------------------
print('10 + 10     =', 10 + 10)        # 20   -> arithmetic
print('"10" + "10" =', "10" + "10")    # 1010 -> text joined together

print("-" * 50)

# --- the arithmetic operators --------------------------------------------
print("7 / 2  =", 7 / 2)     # 3.5  division ALWAYS gives a float
print("7 // 2 =", 7 // 2)    # 3    floor division - remainder thrown away
print("7 % 2  =", 7 % 2)     # 1    modulo - only the remainder
print("2 ** 8 =", 2**8)      # 256  power

print("-" * 50)

# --- taking a number apart with % and // ---------------------------------
n = 407
print(f"{n} % 10  = {n % 10}   <- the last digit")
print(f"{n} // 10 = {n // 10}  <- everything except the last digit")

print("-" * 50)

# --- even or odd ---------------------------------------------------------
for value in (10, 7, 0, -3):
    print(f"{value:>3} % 2 = {value % 2}  ->", "even" if value % 2 == 0 else "odd")

print("-" * 50)

# --- conversion ----------------------------------------------------------
print('int("42")   =', int("42"))
print('float("3.14")=', float("3.14"))
print("str(42)     =", repr(str(42)))
print("int(3.99)   =", int(3.99), " <- CHOPS the decimals, does not round")
print("round(3.99) =", round(3.99), "    <- this rounds")

print("-" * 50)

# --- the float trap ------------------------------------------------------
import math

print("0.1 + 0.2        =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 =", 0.1 + 0.2 == 0.3, " <- surprising, but correct")

eps = 0.000001
print("fabs((0.1+0.2) - 0.3) < eps =", math.fabs((0.1 + 0.2) - 0.3) < eps, "<- the fix")
