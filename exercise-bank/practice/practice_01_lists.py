"""Practice session 1 - Lists — likes, prices and followers: every solution.

Run all of them:
    python3 exercise-bank/practice/practice_01_lists.py
Run just one:
    python3 exercise-bank/practice/practice_01_lists.py 1.1

Exercise 1.11 asks you to TYPE answers, so running everything will pause for them.

Each exercise is wrapped in its own function so that one exercise cannot change the data of another.
"""

import sys


def exercise_1_1():
    print("=" * 60)
    print('Exercise 1.1 - First and last day')
    print("=" * 60)
    followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
    print("First day:", followers[0])
    print("Last day:", followers[-1])
    print("Days counted:", len(followers))


def exercise_1_2():
    print("=" * 60)
    print('Exercise 1.2 - Total and average likes')
    print("=" * 60)
    likes = [120, 85, 300, 45, 210]
    total = sum(likes)
    average = total / len(likes)
    print("Total likes:", total)
    print(f"Average likes: {average:.1f}")


def exercise_1_3():
    print("=" * 60)
    print('Exercise 1.3 - Best post')
    print("=" * 60)
    likes = [120, 85, 300, 45, 210]
    best = max(likes)
    position = likes.index(best)
    print(f"Best post: #{position + 1} with {best} likes")


def exercise_1_4():
    print("=" * 60)
    print('Exercise 1.4 - Viral posts')
    print("=" * 60)
    likes = [120, 85, 300, 45, 210]
    viral = [x for x in likes if x > 100]
    print("Viral posts:", viral)
    print("How many:", len(viral))


def exercise_1_5():
    print("=" * 60)
    print('Exercise 1.5 - Black Friday prices')
    print("=" * 60)
    prices = [40.0, 15.0, 8.5, 4.0]   # hoodie, cap, mug, sticker
    sale_prices = [round(p * 0.8, 2) for p in prices]
    print("Sale prices:", sale_prices)
    print()
    print('[extra] What you get without round')
    prices = [40.0, 15.0, 8.5, 4.0]
    print([p * 0.8 for p in prices])


def exercise_1_6():
    print("=" * 60)
    print('Exercise 1.6 - Newsletter list')
    print("=" * 60)
    subscribers = ["Anna", "Ben", "Cleo", "Dan"]
    subscribers.append("Eva")
    subscribers.remove("Ben")
    print("Subscribers:", subscribers)
    print("Total:", len(subscribers))


def exercise_1_7():
    print("=" * 60)
    print('Exercise 1.7 - Budgets, biggest first')
    print("=" * 60)
    budgets = [500, 1200, 300, 800]
    biggest_first = sorted(budgets, reverse=True)
    print("Biggest first:", biggest_first)
    print("Original:", budgets)


def exercise_1_8():
    print("=" * 60)
    print('Exercise 1.8 - The podium')
    print("=" * 60)
    likes = [120, 85, 300, 45, 210]
    top3 = sorted(likes, reverse=True)[:3]
    print("Top 3 posts:", top3)


def exercise_1_9():
    print("=" * 60)
    print('Exercise 1.9 - Where did customers hear about us?')
    print("=" * 60)
    heard_from = ["Instagram", "TikTok", "Instagram", "Email", "Instagram", "TikTok"]
    for source in ["Instagram", "TikTok", "Email"]:
        print(f"{source}: {heard_from.count(source)}")


def exercise_1_10():
    print("=" * 60)
    print('Exercise 1.10 - Daily growth')
    print("=" * 60)
    followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
    changes = [followers[i] - followers[i - 1] for i in range(1, len(followers))]
    lost = [c for c in changes if c < 0]
    print("Daily changes:", changes)
    print("Days we lost followers:", len(lost))


def exercise_1_11():
    print("=" * 60)
    print('Exercise 1.11 - Your own data')
    print("=" * 60)
    n = int(input("How many posts? "))
    likes = [float(input(f"Likes of post {i + 1}: ")) for i in range(n)]
    print("Total:", sum(likes))
    print("Average:", sum(likes) / len(likes))
    print("Best:", max(likes))


EXERCISES = {
    "1.1": exercise_1_1,
    "1.2": exercise_1_2,
    "1.3": exercise_1_3,
    "1.4": exercise_1_4,
    "1.5": exercise_1_5,
    "1.6": exercise_1_6,
    "1.7": exercise_1_7,
    "1.8": exercise_1_8,
    "1.9": exercise_1_9,
    "1.10": exercise_1_10,
    "1.11": exercise_1_11,
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
