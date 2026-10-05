# Session 1 — Lists — likes, prices and followers

⬅ [Practice home](README.md) · [Course home](../../README.md)

You already know what a list is. This session is a warm-up with **real marketing numbers**: likes, followers, prices and customers of a pretend online shop called **Pixel Shop** (it sells hoodies, caps, mugs and stickers).

Every exercise is short. Most solutions are 2 to 6 lines.

### A list is a row of numbered boxes

```text
followers = [1200, 1230, 1215, 1290]

counting from the start:   0     1     2     3
counting from the end:    -4    -3    -2    -1
```

Computers start counting at **0**, not 1. The last box can always be reached with **-1**.

### The tools for this session

| Tool | What it does | Example | Result |
|------|--------------|---------|--------|
| `len(x)` | how many items | `len([5, 8, 2])` | `3` |
| `sum(x)` | add them all up | `sum([5, 8, 2])` | `15` |
| `max(x)` / `min(x)` | biggest / smallest | `max([5, 8, 2])` | `8` |
| `sorted(x)` | a new, sorted list | `sorted([5, 8, 2])` | `[2, 5, 8]` |
| `x.append(v)` | add at the end | | |
| `x.remove(v)` | delete an item | | |
| `x.count(v)` | how many times `v` appears | `[1, 2, 1].count(1)` | `2` |
| `x.index(v)` | at which position is `v` | `[5, 8, 2].index(8)` | `1` |
| `[a for a in x if ...]` | keep only some items | | |

## The exercises at a glance

| # | Exercise | Level | Time |
|---|----------|-------|------|
| 1.1 | First and last day | ⭐ easy | 2 min |
| 1.2 | Total and average likes | ⭐ easy | 2 min |
| 1.3 | Best post | ⭐ easy | 3 min |
| 1.4 | Viral posts | ⭐⭐ medium | 3 min |
| 1.5 | Black Friday prices | ⭐⭐ medium | 3 min |
| 1.6 | Newsletter list | ⭐ easy | 3 min |
| 1.7 | Budgets, biggest first | ⭐ easy | 3 min |
| 1.8 | The podium | ⭐⭐ medium | 3 min |
| 1.9 | Where did customers hear about us? | ⭐⭐ medium | 4 min |
| 1.10 | Daily growth | ⭐⭐⭐ stretch | 5 min |
| 1.11 | Your own data | ⭐⭐⭐ stretch | 6 min |

About **37 minutes** in total. Work top to bottom: each exercise leans on the one before it.

> **How to work:** read the task, type the data yourself, try it, open the **hint** only if you are stuck, and open the **solution** only after you have something that runs. Then compare — a different working answer is fine.

---

## Exercise 1.1 — First and last day

Level: ⭐ easy · about 2 min

**Your task.** Pixel Shop's Instagram account has a list with the number of followers at the end of each day this week. Print the **first** day, the **last** day, and **how many days** are in the list.

Start with this data:

```python
followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
```

You should see:

```text
First day: 1200
Last day: 1475
Days counted: 7
```

<details>
<summary>Hint (try without it first)</summary>

The first item has number **0**. The last item can always be reached with **-1**. And `len(followers)` counts the items.

</details>

<details>
<summary>Full solution</summary>

```python
followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
print("First day:", followers[0])
print("Last day:", followers[-1])
print("Days counted:", len(followers))
```

**How it works**

- `followers[0]` — position 0 is the first item (computers start counting at 0).
- `followers[-1]` — a minus number counts from the end, so -1 is the last item. You do not need to know how long the list is.
- `len(followers)` — "length": how many items are in the list.

</details>

---

## Exercise 1.2 — Total and average likes

Level: ⭐ easy · about 2 min

**Your task.** Here are the likes of the last five posts. Print the **total** likes and the **average** likes per post, with one decimal.

Start with this data:

```python
likes = [120, 85, 300, 45, 210]
```

You should see:

```text
Total likes: 760
Average likes: 152.0
```

<details>
<summary>Hint (try without it first)</summary>

`sum(likes)` adds everything up. The average is the total divided by *how many* posts there are. Inside an f-string, `:.1f` shows one decimal.

</details>

<details>
<summary>Full solution</summary>

```python
likes = [120, 85, 300, 45, 210]
total = sum(likes)
average = total / len(likes)
print("Total likes:", total)
print(f"Average likes: {average:.1f}")
```

**How it works**

- `sum(likes)` adds all five numbers: 120 + 85 + 300 + 45 + 210.
- `total / len(likes)` divides by the number of posts (5).
- `{average:.1f}` means "show this number with 1 digit after the point".

</details>

---

## Exercise 1.3 — Best post

Level: ⭐ easy · about 3 min

**Your task.** Which post got the most likes? Print its **number** (counting from 1, like a human) and how many likes it got.

Start with this data:

```python
likes = [120, 85, 300, 45, 210]
```

You should see:

```text
Best post: #3 with 300 likes
```

<details>
<summary>Hint (try without it first)</summary>

`max(likes)` finds the biggest number. `likes.index(number)` tells you *where* in the list it sits. But positions start at 0, and people count from 1.

</details>

<details>
<summary>Full solution</summary>

```python
likes = [120, 85, 300, 45, 210]
best = max(likes)
position = likes.index(best)
print(f"Best post: #{position + 1} with {best} likes")
```

**How it works**

- `max(likes)` is `300`.
- `likes.index(300)` is `2`, because 300 is in the third box and boxes are numbered 0, 1, **2**.
- So we print `position + 1`, which is `3`: "post number 3".

</details>

---

## Exercise 1.4 — Viral posts

Level: ⭐⭐ medium · about 3 min

**Your task.** A post is **viral** if it got more than 100 likes. Make a new list with only the viral posts and print how many there are.

Start with this data:

```python
likes = [120, 85, 300, 45, 210]
```

You should see:

```text
Viral posts: [120, 300, 210]
How many: 3
```

<details>
<summary>Hint (try without it first)</summary>

Read the one-line pattern like a sentence: *"for every `x` in `likes`, keep `x` if `x > 100`"*. That is `[x for x in likes if x > 100]`. If you prefer, start with an empty list and use a normal `for` loop with `.append(x)`.

</details>

<details>
<summary>Full solution</summary>

```python
likes = [120, 85, 300, 45, 210]
viral = [x for x in likes if x > 100]
print("Viral posts:", viral)
print("How many:", len(viral))
```

**How it works**

The one-liner is a short way of writing this loop:

```python
viral = []
for x in likes:
    if x > 100:
        viral.append(x)
```

Both give the same result. The one-liner is what you will see in most Python code, so get used to reading it.

</details>

---

## Exercise 1.5 — Black Friday prices

Level: ⭐⭐ medium · about 3 min

**Your task.** It is Black Friday: everything is **20% cheaper**. Make a new list with the reduced prices, rounded to 2 decimals.

Start with this data:

```python
prices = [40.0, 15.0, 8.5, 4.0]   # hoodie, cap, mug, sticker
```

You should see:

```text
Sale prices: [32.0, 12.0, 6.8, 3.2]
```

<details>
<summary>Hint (try without it first)</summary>

20% cheaper means you pay 80% of the price, so multiply by `0.8`. Wrap the result in `round(number, 2)`.

</details>

<details>
<summary>Full solution</summary>

```python
prices = [40.0, 15.0, 8.5, 4.0]   # hoodie, cap, mug, sticker
sale_prices = [round(p * 0.8, 2) for p in prices]
print("Sale prices:", sale_prices)
```

**How it works**

- `p * 0.8` is "80% of the price".
- `round(..., 2)` keeps 2 decimals.

Why the `round`? Try it without: the mug would show up as `6.800000000000001`. Computers store decimals in binary, so tiny errors appear. Rounding hides them (Lesson 1 explains why).

**What you get without round**

```python
prices = [40.0, 15.0, 8.5, 4.0]
print([p * 0.8 for p in prices])
```

which prints:

```text
[32.0, 12.0, 6.800000000000001, 3.2]
```

</details>

---

## Exercise 1.6 — Newsletter list

Level: ⭐ easy · about 3 min

**Your task.** Eva joined the newsletter and Ben left it. Update the list, then print it with the new total.

Start with this data:

```python
subscribers = ["Anna", "Ben", "Cleo", "Dan"]
```

You should see:

```text
Subscribers: ['Anna', 'Cleo', 'Dan', 'Eva']
Total: 4
```

<details>
<summary>Hint (try without it first)</summary>

`.append(x)` adds `x` at the end of the list. `.remove(x)` deletes the first item that equals `x`.

</details>

<details>
<summary>Full solution</summary>

```python
subscribers = ["Anna", "Ben", "Cleo", "Dan"]
subscribers.append("Eva")
subscribers.remove("Ben")
print("Subscribers:", subscribers)
print("Total:", len(subscribers))
```

**How it works**

Both change the list itself, so there is no need to write `subscribers = ...`.

Careful: `.remove("Zoe")` when Zoe is not in the list stops the program with a `ValueError`. Try it, and read the message.

</details>

---

## Exercise 1.7 — Budgets, biggest first

Level: ⭐ easy · about 3 min

**Your task.** Show the campaign budgets from the **biggest to the smallest**, but keep the original list unchanged.

Start with this data:

```python
budgets = [500, 1200, 300, 800]
```

You should see:

```text
Biggest first: [1200, 800, 500, 300]
Original: [500, 1200, 300, 800]
```

<details>
<summary>Hint (try without it first)</summary>

`sorted(x)` gives you a **new** sorted list and leaves the old one alone. Add `reverse=True` to put the biggest first. (`x.sort()` would change the original list — not what we want here.)

</details>

<details>
<summary>Full solution</summary>

```python
budgets = [500, 1200, 300, 800]
biggest_first = sorted(budgets, reverse=True)
print("Biggest first:", biggest_first)
print("Original:", budgets)
```

**How it works**

`sorted()` makes a sorted *copy*. The original list `budgets` is still in its old order, which is why the second print shows `[500, 1200, 300, 800]`.

</details>

---

## Exercise 1.8 — The podium

Level: ⭐⭐ medium · about 3 min

**Your task.** Print the **top 3 posts** by likes.

Start with this data:

```python
likes = [120, 85, 300, 45, 210]
```

You should see:

```text
Top 3 posts: [300, 210, 120]
```

<details>
<summary>Hint (try without it first)</summary>

First sort so the biggest comes first. Then take a **slice**. `[:3]` means "from the start, up to (but not including) position 3", which is the first three items.

</details>

<details>
<summary>Full solution</summary>

```python
likes = [120, 85, 300, 45, 210]
top3 = sorted(likes, reverse=True)[:3]
print("Top 3 posts:", top3)
```

**How it works**

1. `sorted(likes, reverse=True)` gives `[300, 210, 120, 85, 45]`.
2. `[:3]` keeps positions 0, 1 and 2.

Change `3` to `5` to get a top 5.

</details>

---

## Exercise 1.9 — Where did customers hear about us?

Level: ⭐⭐ medium · about 4 min

**Your task.** Every new customer was asked where they heard about Pixel Shop. Count how many came from each of the three sources: Instagram, TikTok and Email.

Start with this data:

```python
heard_from = ["Instagram", "TikTok", "Instagram", "Email", "Instagram", "TikTok"]
```

You should see:

```text
Instagram: 3
TikTok: 2
Email: 1
```

<details>
<summary>Hint (try without it first)</summary>

`my_list.count("Instagram")` tells you how many times that item appears in the list. Put the three names in a list of their own and loop over it.

</details>

<details>
<summary>Full solution</summary>

```python
heard_from = ["Instagram", "TikTok", "Instagram", "Email", "Instagram", "TikTok"]
for source in ["Instagram", "TikTok", "Email"]:
    print(f"{source}: {heard_from.count(source)}")
```

**How it works**

The loop runs three times. Each time, `source` is the next name, and `heard_from.count(source)` counts how often it appears.

This is a tiny version of a **survey result**. In Session 3 you will do the same for bigger tables.

</details>

---

## Exercise 1.10 — Daily growth

Level: ⭐⭐⭐ stretch · about 5 min

**Your task.** Make a list with the **change per day** (today minus yesterday). Then print on how many days the shop **lost** followers.

Start with this data:

```python
followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
```

You should see:

```text
Daily changes: [30, -15, 75, 60, 60, 65]
Days we lost followers: 1
```

<details>
<summary>Hint (try without it first)</summary>

The first day has no "yesterday", so start at position 1: `range(1, len(followers))`. The change on day `i` is `followers[i] - followers[i - 1]`. A day with a loss has a **negative** change.

</details>

<details>
<summary>Full solution</summary>

```python
followers = [1200, 1230, 1215, 1290, 1350, 1410, 1475]
changes = [followers[i] - followers[i - 1] for i in range(1, len(followers))]
lost = [c for c in changes if c < 0]
print("Daily changes:", changes)
print("Days we lost followers:", len(lost))
```

**How it works**

- `range(1, len(followers))` gives 1, 2, 3, 4, 5, 6.
- For `i = 1`: `1230 - 1200 = 30`. For `i = 2`: `1215 - 1230 = -15` (a loss!).
- The second list keeps only the negative changes, and we count them.

</details>

---

## Exercise 1.11 — Your own data

Level: ⭐⭐⭐ stretch · about 6 min

**Your task.** Ask the user how many posts there are, then ask for the likes of each post. Print the **total**, the **average** and the **best** post.

You should see something like this (the values after each question are what the user typed):

```text
How many posts? 3
Likes of post 1: 100
Likes of post 2: 250
Likes of post 3: 40
Total: 390.0
Average: 130.0
Best: 250.0
```

<details>
<summary>Hint (try without it first)</summary>

Use the pattern from the cheatsheet: `n = int(input(...))`, then the one-line pattern `[float(input(...)) for i in range(n)]`. `input()` always gives you **text**, so wrap it in `int()` or `float()`.

</details>

<details>
<summary>Full solution</summary>

```python
n = int(input("How many posts? "))
likes = [float(input(f"Likes of post {i + 1}: ")) for i in range(n)]
print("Total:", sum(likes))
print("Average:", sum(likes) / len(likes))
print("Best:", max(likes))
```

**How it works**

- `range(n)` makes the loop run once per post.
- `f"Likes of post {i + 1}: "` asks for "post 1", "post 2"... (`i` starts at 0, so we add 1).
- Then it is the same `sum`, `len` and `max` as before.

**Try it:** run it and type `0` for the number of posts. It crashes with `ZeroDivisionError`, because you cannot divide by zero posts. Fix it by wrapping the last three lines in `if n > 0:`. Real data is empty more often than you think.

</details>

---

All the solutions of this session in one runnable file: [`exercise-bank/practice/practice_01_lists.py`](../../exercise-bank/practice/practice_01_lists.py)

➡ [Session 2: Tables](02-tables.md)
