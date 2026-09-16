"""Lesson 9 - a warehouse stock database built from dicts and functions.
Original: Lab 9, Task 1.

Three deliberate improvements over the archive version:
  1. ship_goods refuses to go negative (the archive lets stock hit -993)
  2. no input() inside the functions, so they are testable and schedulable
  3. they return a message instead of printing it

Run me:  python3 examples/meeting-2/09_warehouse.py
No input needed.
"""


def receive_goods(stock, name, unit, quantity):
    """Add quantity to stock[name], creating the product if it is new.

    Returns (stock, message). Does not print - the caller decides that.
    """
    if quantity <= 0:
        return stock, f"x Quantity must be positive, got {quantity}"

    if name in stock:
        stock[name]["quantity"] += quantity
        return stock, f"+ Received {quantity} {unit} of {name} (now {stock[name]['quantity']})"

    stock[name] = {"unit": unit, "quantity": quantity}
    return stock, f"+ New product {name}: {quantity} {unit}"


def ship_goods(stock, name, quantity):
    """Remove quantity from stock[name]. Refuses to go negative."""
    if name not in stock:
        return stock, f"x No such product: {name}"

    available = stock[name]["quantity"]
    if quantity > available:
        return stock, f"x Cannot ship {quantity} of {name}: only {available} in stock"

    stock[name]["quantity"] -= quantity
    return stock, f"- Shipped {quantity} of {name} ({stock[name]['quantity']} left)"


def show_stock(stock):
    """Print the stock as an aligned table."""
    print(f"{'Product':<12}{'Unit':<8}{'Qty':>6}")
    print("-" * 26)
    for name, details in sorted(stock.items()):
        print(f"{name:<12}{details['unit']:<8}{details['quantity']:>6}")
    print("-" * 26)
    print(f"{'TOTAL':<20}{sum(d['quantity'] for d in stock.values()):>6}")


stock = {
    "Bread": {"unit": "pcs", "quantity": 6},
    "Milk": {"unit": "pack", "quantity": 10},
    "Salt": {"unit": "pack", "quantity": 13},
}

print("BEFORE")
show_stock(stock)
print()

for action in [
    ("receive", "Bread", "pcs", 24),
    ("receive", "Chocolate", "bar", 50),
    ("ship", "Milk", 4),
    ("ship", "Milk", 999),  # refused: not enough stock
    ("ship", "Caviar", 1),  # refused: unknown product
    ("receive", "Bread", "pcs", -5),  # refused: negative quantity
]:
    if action[0] == "receive":
        stock, message = receive_goods(stock, action[1], action[2], action[3])
    else:
        stock, message = ship_goods(stock, action[1], action[2])
    print(message)

print()
print("AFTER")
show_stock(stock)

# --- the archive's bug, demonstrated ------------------------------------
print()
print("The archive's del_good does  stock[name]['quantity'] -= count  with")
print("no check. Shipping 999 units of which you have 6 would leave:")
print(f"  6 - 999 = {6 - 999} units in stock")
print("No error, no warning - just an impossible number in every report.")

# --- tests --------------------------------------------------------------
test_stock = {"X": {"unit": "pcs", "quantity": 5}}
_, msg = ship_goods(test_stock, "X", 10)
assert test_stock["X"]["quantity"] == 5, "refused shipment must not change stock"
assert msg.startswith("x")
_, msg = ship_goods(test_stock, "X", 5)
assert test_stock["X"]["quantity"] == 0
_, msg = receive_goods(test_stock, "Y", "kg", 3)
assert test_stock["Y"] == {"unit": "kg", "quantity": 3}
print()
print("All tests passed.")
