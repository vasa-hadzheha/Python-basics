"""Exercise 2.14 - Column statistics and a group-by.  [work-flavoured]

Practises: pulling a column out of a list of dicts, aggregating it, and
writing a GROUP BY by hand.

In Lesson 12 you write the same thing as one line of SQL. Seeing both is
the point - it is the same operation, expressed at two altitudes.
"""

sales = [
    {"region": "North", "product": "Bread", "units": 120, "revenue": 1620.00},
    {"region": "South", "product": "Bread", "units": 80, "revenue": 1080.00},
    {"region": "North", "product": "Milk", "units": 200, "revenue": 2800.00},
    {"region": "South", "product": "Milk", "units": 150, "revenue": 2100.00},
    {"region": "North", "product": "Cola", "units": 90, "revenue": 1079.10},
]


def column(rows, field):
    """Pull one field out of every row, as a plain list."""
    return [row[field] for row in rows]


def column_stats(rows, field):
    """Return count/sum/min/max/mean for one numeric field.

    Guards the empty case: sum([]) / len([]) is ZeroDivisionError.
    """
    values = column(rows, field)
    if not values:
        return {"count": 0, "sum": 0.0, "min": None, "max": None, "mean": None}
    return {
        "count": len(values),
        "sum": sum(values),
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
    }


def group_sum(rows, key_field, value_field):
    """Total value_field per distinct key_field. This is a GROUP BY."""
    totals = {}
    for row in rows:
        key = row[key_field]
        # The counting pattern from Lesson 9, summing instead of counting.
        totals[key] = totals.get(key, 0) + row[value_field]
    return totals


# --- the column report --------------------------------------------------
print(f"{'Column':<12}{'Count':>6}{'Sum':>11}{'Min':>11}{'Max':>11}{'Mean':>11}")
for field in ("units", "revenue"):
    s = column_stats(sales, field)
    print(
        f"{field:<12}{s['count']:>6}{s['sum']:>11.2f}"
        f"{s['min']:>11.2f}{s['max']:>11.2f}{s['mean']:>11.2f}"
    )

# --- the group-by report ------------------------------------------------
print("\nRevenue by region")
by_region = group_sum(sales, "region", "revenue")
# Sort the (key, value) pairs by value, highest first.
for region, total in sorted(by_region.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{region:<52}{total:>11.2f}")

print("\nUnits by product")
by_product = group_sum(sales, "product", "units")
for product, total in sorted(by_product.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{product:<52}{total:>11}")

# --- tests -------------------------------------------------------------
assert column_stats([], "units")["count"] == 0, "empty input must not crash"
assert column_stats(sales, "units")["sum"] == 640
assert column_stats(sales, "units")["mean"] == 128.0
assert group_sum(sales, "region", "units") == {"North": 410, "South": 230}
print("\nAll tests passed.")
