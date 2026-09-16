"""Exercise 2.13 - The cook's product directory.  (Original Lab 9, Task 2.)

Practises: a list of dicts; search functions that take arguments instead of
calling input() themselves.

Difference from the archive: the archive reads from the keyboard INSIDE
add_product(), which makes it untestable and unusable from a scheduled job.
Here the functions are pure: data in, result out.
"""


def add_product(products, name, unit, quantity, price):
    """Top up an existing product, or append a new one.

    Returns (products, message).
    """
    if quantity <= 0:
        return products, f"x Quantity must be positive, got {quantity}"
    if price < 0:
        return products, f"x Price cannot be negative, got {price}"

    for product in products:
        if product["name"].lower() == name.lower():
            product["quantity"] += quantity
            return products, f"+ Topped up {product['name']}: now {product['quantity']} {product['unit']}"

    products.append({"name": name, "unit": unit, "quantity": quantity, "price": price})
    return products, f"+ Added new product {name}: {quantity} {unit} @ {price:.2f}"


def search_by_name(products, query):
    """Every product whose name contains query, ignoring case."""
    return [p for p in products if query.lower() in p["name"].lower()]


def search_by_price(products, low, high):
    """Every product whose price is between low and high, inclusive."""
    return [p for p in products if low <= p["price"] <= high]


def show(label, products):
    print(f"\n{label}")
    if not products:  # an empty list is falsy - Lesson 3
        print("  (nothing found)")
        return
    print(f"  {'Name':<14}{'Unit':<8}{'Qty':>6}{'Price':>9}{'Value':>10}")
    print("  " + "-" * 47)
    for p in sorted(products, key=lambda p: p["name"]):
        value = p["quantity"] * p["price"]
        print(f"  {p['name']:<14}{p['unit']:<8}{p['quantity']:>6}{p['price']:>9.2f}{value:>10.2f}")
    total = sum(p["quantity"] * p["price"] for p in products)
    print("  " + "-" * 47)
    print(f"  {'TOTAL':<28}{'':>9}{total:>10.2f}")


products = [
    {"name": "Milk", "unit": "pack", "quantity": 10, "price": 14.00},
    {"name": "Bread", "unit": "pcs", "quantity": 6, "price": 13.50},
    {"name": "Salt", "unit": "pack", "quantity": 13, "price": 7.00},
    {"name": "Cola", "unit": "can", "quantity": 15, "price": 11.99},
]

show("Starting directory", products)

for args in [
    ("Milk", "pack", 5, 14.00),  # tops up
    ("milk", "pack", 5, 14.00),  # case-insensitive: tops up again
    ("Sugar", "kg", 20, 9.40),  # new
    ("Flour", "kg", -3, 8.00),  # refused
]:
    products, message = add_product(products, *args)
    print(message)

show("After the updates", products)
show("Search: name contains 'al'", search_by_name(products, "al"))
show("Search: price between 7 and 12", search_by_price(products, 7, 12))
show("Search: name contains 'caviar'", search_by_name(products, "caviar"))

# --- tests -------------------------------------------------------------
test = [{"name": "A", "unit": "pcs", "quantity": 1, "price": 1.0}]
test, _ = add_product(test, "a", "pcs", 4, 1.0)  # case-insensitive top-up
assert test[0]["quantity"] == 5
assert len(test) == 1, "must not create a duplicate for a different case"
test, msg = add_product(test, "B", "pcs", 0, 1.0)
assert msg.startswith("x") and len(test) == 1
assert search_by_name(test, "zzz") == []
print("\nAll tests passed.")
