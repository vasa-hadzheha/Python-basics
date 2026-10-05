"""Practice session 5 - The weekly campaign report (project): the complete script.

Run it from the repository root:
    python3 exercise-bank/practice/practice_05_campaign_report.py

It writes out/campaign_report.csv, which you can open in Excel.
"""

def conversion_rate(clicks, orders):
    if clicks == 0:
        return 0.0
    return round(orders / clicks * 100, 2)


def cost_per_order(spend, orders):
    if orders == 0:
        return 0.0
    return round(spend / orders, 2)


def roi(spend, revenue):
    if spend == 0:
        return 0.0
    return round((revenue - spend) / spend * 100, 2)


def column(table, j):
    return [row[j] for row in table]


def add_column(table, make_value):
    new_table = []
    for row in table:
        new_row = row[:]
        new_row.append(make_value(row))
        new_table.append(new_row)
    return new_table


def format_cell(cell):
    if isinstance(cell, float):
        return f"{cell:>10.2f}"
    return f"{cell:>10}"


def print_table(header, rows):
    line = f"{header[0]:<12}"
    for name in header[1:]:
        line += f"{name:>10}"
    print(line)
    print("-" * len(line))
    for row in rows:
        line = f"{row[0]:<12}"
        for cell in row[1:]:
            line += format_cell(cell)
        print(line)


print()
print("=" * 60)
print('Step 5.1 - The numbers and four new columns')
print("=" * 60)
header = ["Channel", "Spend", "Clicks", "Orders"]
rows = [
    ["Instagram", 500, 5000, 100],
    ["TikTok",    300, 6000,  60],
    ["Email",     100, 2000, 100],
    ["Google",    800, 4000, 120],
    ["Flyers",    200,  500,   5],
]
REVENUE_PER_ORDER = 25


def get_conversion(row):
    return conversion_rate(row[2], row[3])


def get_cost_per_order(row):
    return cost_per_order(row[1], row[3])


def get_revenue(row):
    return row[3] * REVENUE_PER_ORDER


def get_roi(row):
    return roi(row[1], row[6])      # spend and revenue (column 6)


rows = add_column(rows, get_conversion)        # becomes column 4
rows = add_column(rows, get_cost_per_order)    # column 5
rows = add_column(rows, get_revenue)           # column 6
rows = add_column(rows, get_roi)               # column 7
header = header + ["Conv %", "Per order", "Revenue", "ROI %"]

print(header)
print(rows[0])


print()
print("=" * 60)
print('Step 5.2 - Print the report')
print("=" * 60)
print_table(header, rows)


print()
print("=" * 60)
print('Step 5.3 - Best and worst channel')
print("=" * 60)
def get_roi_cell(row):
    return row[7]


ranked = sorted(rows, key=get_roi_cell, reverse=True)
best = ranked[0]
worst = ranked[-1]
print(f"Best:  {best[0]} (ROI {best[7]}%)")
print(f"Worst: {worst[0]} (ROI {worst[7]}%)")


print()
print("=" * 60)
print('Step 5.4 - A TOTAL row')
print("=" * 60)
total_spend = sum(column(rows, 1))
total_clicks = sum(column(rows, 2))
total_orders = sum(column(rows, 3))
total_revenue = sum(column(rows, 6))

total_row = [
    "TOTAL", total_spend, total_clicks, total_orders,
    conversion_rate(total_clicks, total_orders),
    cost_per_order(total_spend, total_orders),
    total_revenue,
    roi(total_spend, total_revenue),
]
print_table(header, rows + [total_row])
print()
print('[extra] The wrong way: averaging the percentages')
simple_average = sum(column(rows, 4)) / len(rows)
print("Average of the five percentages:", simple_average)
print("Real overall conversion rate:   ", conversion_rate(total_clicks, total_orders))


print()
print("=" * 60)
print('Step 5.5 - Advice for the boss')
print("=" * 60)
losers = [row for row in rows if row[7] < 0]

for row in losers:
    print(f"Stop or rethink: {row[0]} (ROI {row[7]}%)")

if len(losers) > 0:
    freed_money = sum([row[1] for row in losers])
    print(f"Idea: move {freed_money} EUR to {best[0]}")
else:
    print("Every channel makes money. No changes needed.")


print()
print("=" * 60)
print('Step 5.6 - Send it to Excel')
print("=" * 60)
import csv
from pathlib import Path

Path("out").mkdir(exist_ok=True)
with open("out/campaign_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(header)
    writer.writerows(rows + [total_row])
print("Saved out/campaign_report.csv - open it in Excel!")

with open("out/campaign_report.csv", encoding="utf-8") as f:
    for line in list(f)[:3]:
        print(line.strip())
