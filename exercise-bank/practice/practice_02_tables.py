"""Practice session 2 - Tables — a list of lists: every solution.

Run all of them:
    python3 exercise-bank/practice/practice_02_tables.py
Run just one:
    python3 exercise-bank/practice/practice_02_tables.py 2.1

Each exercise is wrapped in its own function so that one exercise cannot change the data of another.
"""

import sys


def exercise_2_1():
    print("=" * 60)
    print('Exercise 2.1 - Find the cell')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    print("Cap row:", sales[1])
    print("Mug in Feb:", sales[2][2])
    print("Rows:", len(sales))
    print("Columns:", len(sales[0]))


def exercise_2_2():
    print("=" * 60)
    print('Exercise 2.2 - Print the table')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    for row in sales:
        for cell in row:
            print(cell, end=" ")
        print()


def exercise_2_3():
    print("=" * 60)
    print('Exercise 2.3 - A nice-looking table')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    print(f"{'Product':<10}{'Jan':>6}{'Feb':>6}{'Mar':>6}")
    for row in sales:
        print(f"{row[0]:<10}{row[1]:>6}{row[2]:>6}{row[3]:>6}")


def exercise_2_4():
    print("=" * 60)
    print('Exercise 2.4 - Total per product')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    for row in sales:
        name = row[0]
        total = sum(row[1:])
        print(f"{name} sold {total} units")


def exercise_2_5():
    print("=" * 60)
    print('Exercise 2.5 - Best seller')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    best_name = ""
    best_total = 0
    for row in sales:
        total = sum(row[1:])
        if total > best_total:
            best_total = total
            best_name = row[0]
    print(f"Best seller: {best_name} ({best_total} units)")


def exercise_2_6():
    print("=" * 60)
    print('Exercise 2.6 - Total per month')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    months = ["Jan", "Feb", "Mar"]
    for j, month in enumerate(months, start=1):
        month_total = 0
        for row in sales:
            month_total += row[j]
        print(f"{month}: {month_total}")


def exercise_2_7():
    print("=" * 60)
    print('Exercise 2.7 - Did we hit the target?')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    months = ["Jan", "Feb", "Mar"]
    TARGET = 200
    for j, month in enumerate(months, start=1):
        month_total = sum([row[j] for row in sales])
        if month_total >= TARGET:
            print(f"{month}: {month_total} - target reached")
        else:
            print(f"{month}: {month_total} - missed by {TARGET - month_total}")


def exercise_2_8():
    print("=" * 60)
    print('Exercise 2.8 - Add a product (a new row)')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    sales.append(["Poster", 15, 25, 30])
    print("Products now:", len(sales))
    print("Last row:", sales[-1])


def exercise_2_9():
    print("=" * 60)
    print('Exercise 2.9 - Add a Total column')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    for row in sales:
        row.append(sum(row[1:]))

    for row in sales:
        print(row)


def exercise_2_10():
    print("=" * 60)
    print('Exercise 2.10 - Share of the total')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    grand_total = 0
    for row in sales:
        grand_total += sum(row[1:])

    for row in sales:
        share = sum(row[1:]) / grand_total * 100
        print(f"{row[0]}: {share:.1f}%")


def exercise_2_11():
    print("=" * 60)
    print('Exercise 2.11 - A blank tracking grid')
    print("=" * 60)
    tracker = [[0 for _ in range(3)] for _ in range(4)]
    tracker[0][0] = 5
    for row in tracker:
        print(row)
    print()
    print('[extra] The trap: [[0] * 3] * 4')
    wrong = [[0] * 3] * 4
    wrong[0][0] = 5
    for row in wrong:
        print(row)


def exercise_2_12():
    print("=" * 60)
    print('Exercise 2.12 - Bonus: flip the table')
    print("=" * 60)
    sales = [
        ["Hoodie",   30,  45, 50],
        ["Cap",      20,  15, 25],
        ["Mug",      40,  35, 60],
        ["Sticker", 100, 120, 90],
    ]
    months = ["Jan", "Feb", "Mar"]
    numbers = [row[1:] for row in sales]      # drop the names
    flipped = list(zip(*numbers))
    for month, column in zip(months, flipped):
        print(month, list(column))


EXERCISES = {
    "2.1": exercise_2_1,
    "2.2": exercise_2_2,
    "2.3": exercise_2_3,
    "2.4": exercise_2_4,
    "2.5": exercise_2_5,
    "2.6": exercise_2_6,
    "2.7": exercise_2_7,
    "2.8": exercise_2_8,
    "2.9": exercise_2_9,
    "2.10": exercise_2_10,
    "2.11": exercise_2_11,
    "2.12": exercise_2_12,
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
