"""Practice session 4 - Functions on tables — your own formulas: every solution.

Run all of them:
    python3 exercise-bank/practice/practice_04_functions.py
Run just one:
    python3 exercise-bank/practice/practice_04_functions.py 4.1

Each exercise is wrapped in its own function so that one exercise cannot change the data of another.
"""

import sys


def exercise_4_1():
    print("=" * 60)
    print('Exercise 4.1 - Your first formula')
    print("=" * 60)
    def money(amount):
        return f"{amount:.2f} EUR"

    print(money(12.5))
    print(money(0.1))
    print(money(1900))


def exercise_4_2():
    print("=" * 60)
    print('Exercise 4.2 - Conversion rate')
    print("=" * 60)
    def conversion_rate(clicks, orders):
        if clicks == 0:
            return 0.0
        return round(orders / clicks * 100, 2)

    print(conversion_rate(5000, 100))
    print(conversion_rate(2000, 100))
    print(conversion_rate(0, 0))

    assert conversion_rate(5000, 100) == 2.0
    assert conversion_rate(0, 0) == 0.0
    print()
    print('[extra] What happens without the guard')
    try:
        print(0 / 0)
    except ZeroDivisionError as error:
        print("Crash:", error)


def exercise_4_3():
    print("=" * 60)
    print('Exercise 4.3 - Return on investment')
    print("=" * 60)
    def roi(spend, revenue):
        if spend == 0:
            return 0.0
        return round((revenue - spend) / spend * 100, 2)

    print(roi(500, 2500))
    print(roi(200, 125))

    assert roi(100, 300) == 200.0
    assert roi(500, 2500) == 400.0
    assert roi(200, 125) == -37.5


def exercise_4_4():
    print("=" * 60)
    print('Exercise 4.4 - A function that takes a row')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    def row_total(row):
        return sum(row[1:])

    for row in sales:
        print(row[0], row_total(row))

    assert row_total(["Hoodie", 30, 45, 50]) == 125


def exercise_4_5():
    print("=" * 60)
    print('Exercise 4.5 - Get a column')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    def column(table, j):
        return [row[j] for row in table]

    january = column(sales, 1)
    print("January column:", january)
    print("January total:", sum(january))
    print("Best January:", max(january))

    assert column(sales, 1) == [30, 20, 40, 100]


def exercise_4_6():
    print("=" * 60)
    print('Exercise 4.6 - A safe average')
    print("=" * 60)
    def average(numbers):
        if len(numbers) == 0:
            return 0.0
        return sum(numbers) / len(numbers)

    print(average([30, 20, 40, 100]))
    print(average([]))

    assert average([30, 20, 40, 100]) == 47.5
    assert average([]) == 0.0
    print()
    print('[extra] What happens without the guard')
    try:
        print(sum([]) / len([]))
    except ZeroDivisionError as error:
        print("Crash:", error)


def exercise_4_7():
    print("=" * 60)
    print('Exercise 4.7 - The best row')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    def best_row(table, j):
        best = table[0]
        for row in table:
            if row[j] > best[j]:
                best = row
        return best

    winner = best_row(campaigns, 3)
    print("Most orders:", winner[0], winner[3])
    print("Most clicks:", best_row(campaigns, 2)[0])

    assert best_row(campaigns, 3)[0] == "Google"
    assert best_row(campaigns, 2)[0] == "TikTok"


def exercise_4_8():
    print("=" * 60)
    print('Exercise 4.8 - Keep only some rows')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    def filter_rows(table, j, minimum):
        return [row for row in table if row[j] >= minimum]

    busy = filter_rows(campaigns, 2, 4000)
    print([row[0] for row in busy])

    assert len(filter_rows(campaigns, 2, 4000)) == 3
    assert filter_rows(campaigns, 2, 99999) == []


def exercise_4_9():
    print("=" * 60)
    print('Exercise 4.9 - Add a calculated column')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]

    def conversion_rate(clicks, orders):          # from exercise 4.2
        if clicks == 0:
            return 0.0
        return round(orders / clicks * 100, 2)
    def add_column(table, make_value):
        new_table = []
        for row in table:
            new_row = row[:]                   # a copy of the row
            new_row.append(make_value(row))    # the new cell
            new_table.append(new_row)
        return new_table

    def conversion(row):
        return conversion_rate(row[2], row[3])

    with_conversion = add_column(campaigns, conversion)
    for row in with_conversion:
        print(row)
    print("The original still has", len(campaigns[0]), "columns")


def exercise_4_10():
    print("=" * 60)
    print('Exercise 4.10 - A reusable table printer')
    print("=" * 60)
    header = ["Channel", "Spend", "Clicks", "Orders", "Conv %"]
    rows = [
        ["Instagram", 500, 5000, 100, 2.0],
        ["TikTok",    300, 6000,  60, 1.0],
        ["Email",     100, 2000, 100, 5.0],
        ["Google",    800, 4000, 120, 3.0],
        ["Flyers",    200,  500,   5, 1.0],
    ]
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

    print_table(header, rows)


EXERCISES = {
    "4.1": exercise_4_1,
    "4.2": exercise_4_2,
    "4.3": exercise_4_3,
    "4.4": exercise_4_4,
    "4.5": exercise_4_5,
    "4.6": exercise_4_6,
    "4.7": exercise_4_7,
    "4.8": exercise_4_8,
    "4.9": exercise_4_9,
    "4.10": exercise_4_10,
}


def main():
    wanted = sys.argv[1:] or list(EXERCISES)
    for exercise_id in wanted:
        if exercise_id not in EXERCISES:
            raise SystemExit(f"No exercise {exercise_id}. Choose from: {', '.join(EXERCISES)}")
        EXERCISES[exercise_id]()
        print()


if __name__ == "__main__":
    main()
