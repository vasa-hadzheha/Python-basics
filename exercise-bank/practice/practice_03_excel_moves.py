"""Practice session 3 - Excel moves in Python: every solution.

Run all of them:
    python3 exercise-bank/practice/practice_03_excel_moves.py
Run just one:
    python3 exercise-bank/practice/practice_03_excel_moves.py 3.1

Each exercise is wrapped in its own function so that one exercise cannot change the data of another.
"""

import sys


def exercise_3_1():
    print("=" * 60)
    print('Exercise 3.1 - SUM a column')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    total_spend = 0
    for row in campaigns:
        total_spend += row[1]
    print("Total spend:", total_spend, "EUR")


def exercise_3_2():
    print("=" * 60)
    print('Exercise 3.2 - AVERAGE a column')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    clicks = [row[2] for row in campaigns]
    print("Average clicks:", sum(clicks) / len(clicks))


def exercise_3_3():
    print("=" * 60)
    print('Exercise 3.3 - Biggest and smallest')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    spends = [row[1] for row in campaigns]
    biggest = campaigns[spends.index(max(spends))]
    smallest = campaigns[spends.index(min(spends))]
    print(f"Biggest budget: {biggest[0]} ({biggest[1]} EUR)")
    print(f"Smallest budget: {smallest[0]} ({smallest[1]} EUR)")


def exercise_3_4():
    print("=" * 60)
    print('Exercise 3.4 - COUNTIF')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    count = 0
    for row in campaigns:
        if row[2] > 3000:
            count += 1
    print("Channels with more than 3000 clicks:", count)


def exercise_3_5():
    print("=" * 60)
    print('Exercise 3.5 - SUMIF')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    orders_from_big = 0
    for row in campaigns:
        if row[1] > 250:
            orders_from_big += row[3]
    print("Orders from big-budget channels:", orders_from_big)


def exercise_3_6():
    print("=" * 60)
    print('Exercise 3.6 - IF')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    for row in campaigns:
        channel = row[0]
        conversion = row[3] / row[2] * 100
        if conversion >= 2:
            verdict = "worth it"
        else:
            verdict = "check again"
        print(f"{channel:<10}{conversion:>5.1f}%  {verdict}")


def exercise_3_7():
    print("=" * 60)
    print('Exercise 3.7 - A formula column, dragged down')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    for row in campaigns:
        row.append(round(row[1] / row[3], 2))

    for row in campaigns:
        print(row)


def exercise_3_8():
    print("=" * 60)
    print('Exercise 3.8 - VLOOKUP')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    for wanted in ["Email", "Radio"]:
        found = False
        for row in campaigns:
            if row[0] == wanted:
                print(f"{wanted} got {row[3]} orders")
                found = True
                break
        if not found:
            print(f"{wanted}: not found")


def exercise_3_9():
    print("=" * 60)
    print('Exercise 3.9 - Sort largest to smallest')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    def get_orders(row):
        return row[3]

    ranked = sorted(campaigns, key=get_orders, reverse=True)
    for row in ranked:
        print(f"{row[0]:<10}{row[3]:>5}")


def exercise_3_10():
    print("=" * 60)
    print('Exercise 3.10 - Filter')
    print("=" * 60)
    campaigns = [
        ["Instagram", 500, 5000, 100],
        ["TikTok",    300, 6000,  60],
        ["Email",     100, 2000, 100],
        ["Google",    800, 4000, 120],
        ["Flyers",    200,  500,   5],
    ]
    cheap = [row for row in campaigns if row[1] <= 300]
    for row in cheap:
        print(row[0], row[1])


def exercise_3_11():
    print("=" * 60)
    print('Exercise 3.11 - Bonus: a pivot table')
    print("=" * 60)
    orders = [
        ["Hoodie", 2], ["Cap", 1], ["Hoodie", 1],
        ["Mug", 3], ["Cap", 2], ["Hoodie", 1],
    ]
    totals = {}
    for product, quantity in orders:
        totals[product] = totals.get(product, 0) + quantity

    for product, quantity in totals.items():
        print(product, quantity)


EXERCISES = {
    "3.1": exercise_3_1,
    "3.2": exercise_3_2,
    "3.3": exercise_3_3,
    "3.4": exercise_3_4,
    "3.5": exercise_3_5,
    "3.6": exercise_3_6,
    "3.7": exercise_3_7,
    "3.8": exercise_3_8,
    "3.9": exercise_3_9,
    "3.10": exercise_3_10,
    "3.11": exercise_3_11,
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
