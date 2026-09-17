# Meeting 1 — Exercises

⬅ [Meeting 1](README.md) · [Course home](../../README.md) · [Presenter runsheet](RUNSHEET.md)

**15 tasks.** Most come from the original lab archive, translated; the last few are
work-flavoured. They are ordered easy → hard.

### How to work through these

1. Read the statement. Try to start.
2. Stuck? Open the **Hint**. It nudges; it does not answer.
3. Write your attempt in a file, run it, fix the errors.
4. Open the reference solution and **compare**. Ask *why* it differs from yours.

Reference solutions: [`exercise-bank/meeting-1/`](../../exercise-bank/meeting-1/)

| # | Task | Practises |
|---|------|-----------|
| [1.1](#exercise-11--types-warm-up) | Types warm-up | `type()`, conversion |
| [1.2](#exercise-12--rectangle-report) | Rectangle report | `input`, f-strings |
| [1.3](#exercise-13--triangle-area) | Triangle area | `if`, `math.sqrt` |
| [1.4](#exercise-14--interval-membership) | Interval membership | chained comparisons, `and` |
| [1.5](#exercise-15--is-the-triangle-right-angled) | Right-angled triangle | dot product, epsilon |
| [1.6](#exercise-16--piecewise-function) | Piecewise function | `if`/`else`, `math` |
| [1.7](#exercise-17--largest-of-three) | Largest of three | nested conditions |
| [1.8](#exercise-18--sum-of-the-first-17-even-numbers) | Sum of 17 even numbers | `while`, accumulator |
| [1.9](#exercise-19--keep-adding-until-20) | Keep adding until 20 | `while`, unknown count |
| [1.10](#exercise-110--collect-three-even-numbers) | Collect 3 even numbers | `while`, `%`, counter |
| [1.11](#exercise-111--count-the-zeros) | Count the zeros | `%`, `//`, digit loop |
| [1.12](#exercise-112--sum-of-logarithms) | Sum of logarithms | `for`, `range` countdown |
| [1.13](#exercise-113--series-to-a-given-precision) | Series to a precision | `while`, convergence |
| [1.14](#exercise-114--recurrence-relation) | Recurrence relation | `for`, rolling variables |
| [1.15](#exercise-115--invoice-line-with-validation-) | Invoice line + validation 💼 | everything, realistic |

💼 = based on real work, not a textbook.

---

## Exercise 1.1 — Types warm-up

**No code required.** For each line, write down what it prints. Then check in the
interactive shell (`python3`).

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 8)
print("7" + "2")
print(int("7") + int("2"))
print(type(7 / 2))
print(int(9.99))
print(round(9.99))
print(10 % 3 == 1)
```

<details><summary><b>Hint</b></summary>

Three rules cover all ten lines: `/` always returns a float; `+` joins text but adds
numbers; `int()` chops the decimals off rather than rounding.
</details>

<details><summary><b>Answers</b></summary>

```
3.5
3
1
256
72
9
<class 'float'>
9
10
True
```
</details>

---

## Exercise 1.2 — Rectangle report

Ask for the two sides of a rectangle. Print its area and perimeter, each to two decimal
places, in a tidy aligned block.

**Target output:**
```
Side a:  3.5
Side b:  2
Area      :       7.00
Perimeter :      11.00
```

<details><summary><b>Hint</b></summary>

`float(input(...))` for each side, because sides can be decimals. Area is `a * b`,
perimeter is `2 * (a + b)`. For alignment use `f"{label:<10}: {value:>10.2f}"`.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_02_rectangle_report.py)

---

## Exercise 1.3 — Triangle area

*(Original Lab 4, Task 1)*

A triangle is given by the lengths of its three sides. Compute its area.
If the three lengths cannot form a triangle, say so instead.

**Test with:** `3, 4, 5` → area 6. And `1, 2, 50` → not a triangle.

<details><summary><b>Hint</b></summary>

Heron's formula: with `p = (a+b+c)/2`, the area is `sqrt(p·(p−a)·(p−b)·(p−c))`.

The triangle inequality must hold for all three sides: each side must be shorter than
the sum of the other two, i.e. `a + b > c` **and** `a + c > b` **and** `b + c > a`.
Check the sides are positive first — `0, 0, 0` should not slip through.

You need `import math` for `math.sqrt`.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_03_triangle_area.py)

---

## Exercise 1.4 — Interval membership

*(Original Lab 4, Task 2)*

Read four real numbers `a`, `b`, `c`, `d`. For `a` and for `b`, report whether the number
lies in the intersection **[1; 2] ∩ (c; d)**.

Note the brackets: `[1; 2]` **includes** its ends, `(c; d)` **excludes** its ends.

<details><summary><b>Hint</b></summary>

"Lies in the intersection" means it must be in *both* intervals — so `and`.

Square brackets → `<=`. Round brackets → `<`. Python lets you chain:
`1 <= a <= 2 and c < a < d`.

*Bonus thinking:* can `c` itself ever be inside `(c; d)`? The original solution spotted
that it cannot — `c < c` is never true — and short-circuited the whole check. That is a
nice piece of reasoning worth reproducing.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_04_interval_membership.py)

---

## Exercise 1.5 — Is the triangle right-angled?

*(Original Lab 4, Task 3)*

A triangle is given by the coordinates of its vertices `A(x₁,y₁)`, `B(x₂,y₂)`, `C(x₃,y₃)`.
Determine whether it has a right angle.

**Test with:** `(0,0) (4,0) (0,3)` → right-angled. `(0,0) (4,1) (0,3)` → not.

<details><summary><b>Hint</b></summary>

Two vectors are perpendicular exactly when their **dot product** is zero. For vectors
`u = (ux, uy)` and `v = (vx, vy)`, the dot product is `ux*vx + uy*vy`.

So: build the vectors along the sides meeting at each vertex, and test all three
dot products.

⚠️ Do **not** write `== 0`. Floating-point arithmetic gives you `1.4e-17` instead of a
clean zero. Compare `math.fabs(dot) < eps` with `eps = 1e-9`.

Careful with direction: at vertex B the two vectors are `B→A` and `B→C`, not `A→B` and `B→C`.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_05_right_triangle.py)

---

## Exercise 1.6 — Piecewise function

*(Original Lab 4, Task 4)*

Read `x` and `n` and compute `y`:

```
y = ln|x| − n     if x ≤ n
y = cos(x · n)    if x > n
```

<details><summary><b>Hint</b></summary>

One `if`/`else` is enough — the first two cases of the original statement (`x < n` and
`x = n`) give the same formula, so `x <= n` covers both.

`math.log(v)` is the natural logarithm, `math.fabs(v)` the absolute value. The `fabs`
is what keeps `ln` legal for negative `x` — but what about `x = 0`? Decide what your
program should do and handle it.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_06_piecewise.py)

---

## Exercise 1.7 — Largest of three

*(Original archive, `Aditional exercises/new.py`)*

Read three whole numbers and print the largest.

**Then the real task:** the original archive solution for this has a genuine bug.
Write your own, then read the original and find it.

```python
def max(number_1, number_2, number_3):
    if number_1 > number_2 > number_3:
        return number_1
    elif number_2 > number_1 > number_3:
        return number_2
    else:
        return number_3
```

<details><summary><b>Hint</b></summary>

Try the original with `(1, 5, 3)`.

- Is `1 > 5 > 3`? No.
- Is `5 > 1 > 3`? `5 > 1` yes, `1 > 3` **no** → so no.
- Falls through to `else` → returns `3`. But the answer is 5.

The mistake is that a chained comparison `a > b > c` demands a *total ordering* of all
three, which only covers a fraction of the possible arrangements. Compare each candidate
against **both** others instead: `if a >= b and a >= c`.

Two more things worth noticing about that original: naming the function `max` shadows
Python's own built-in `max()`, and using `>` rather than `>=` means ties are handled by
accident rather than on purpose.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_07_largest_of_three.py)

---

## Exercise 1.8 — Sum of the first 17 even numbers

*(Original archive, `SUM завдання №5.py`)*

Compute `2 + 4 + 6 + … ` for the first 17 even numbers, using a `while` loop.
Then write it again with a `for` loop and compare.

<details><summary><b>Hint</b></summary>

`while`: keep a counter `i` from 1 to 17 and a value `d` starting at 2 that grows by 2
each pass; accumulate `d` into `total`.

`for`: `range(2, 35, 2)` hands you the even numbers directly — no counter at all.
That is the point of the comparison.

Check yourself: the sum of the first *n* even numbers is `n·(n+1)`, so the answer
must be 17·18 = **306**.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_08_sum_even.py)

---

## Exercise 1.9 — Keep adding until 20

*(Original archive, `SUM завдання №8.py`)*

Keep asking the user for a number, adding each to a running total, until the total
reaches 20 or more. Then print the total and how many numbers were entered.

<details><summary><b>Hint</b></summary>

This is the textbook case for `while`: the number of passes depends on what the user
types, so you cannot use `for`.

`while total < 20:` — read a number inside the body, add it to `total`, add 1 to a counter.

Think about the edge case: what if the user enters a negative number every time?
The original version loops forever. Is that acceptable? Decide, and say so in a comment.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_09_sum_until_20.py)

---

## Exercise 1.10 — Collect three even numbers

*(Original archive, `завдання №9.py`)*

Keep asking for numbers until the user has entered three **even** ones. Odd numbers are
ignored (but tell the user). Print how many numbers were entered in total.

<details><summary><b>Hint</b></summary>

Two counters: `even_found` (the loop condition) and `attempts` (for the report).
Only `even_found` increases inside the `if`; `attempts` increases every pass.

`number % 2 == 0` tests even.

⚠️ The original version reads with `float(input(...))` and then tests `number % 2 == 0`.
`4.0 % 2` is `0.0`, which is falsy-equal to 0, so it works — but `4.5 % 2` is `0.5`,
and "is 4.5 even" is not a meaningful question. Read with `int()` instead, and think
about what should happen when the user types `abc`.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_10_three_even.py)

---

## Exercise 1.11 — Count the zeros

*(Original Lab 5, Task 2)*

Given a whole number `n`, count how many zero digits it contains.

**Test with:** `1020` → 2. `7` → 0. `100` → 2. `0` → 1. `-500` → 2.

<details><summary><b>Hint</b></summary>

The digit-peeling loop:

- `n % 10` gives you the last digit,
- `n // 10` gives you the number with that digit removed,
- repeat `while n > 0`.

Three edge cases your code must survive, and this is the real content of the exercise:
- `n = 0` — the loop body never runs, but the answer is 1. Special-case it.
- `n = -500` — use `abs(n)` first, or `while n != 0` fails strangely.
- After the loop `n` is 0, so if you want to print the original number, save it first.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_11_count_zeros.py)

---

## Exercise 1.12 — Sum of logarithms

*(Original Lab 5, Task 1)*

Given a real `a ≠ 0` and a natural `n`, compute
`ln|aⁿ| + ln|aⁿ⁻¹| + … + ln|a¹|`.

<details><summary><b>Hint</b></summary>

`for power in range(n, 0, -1):` counts down from `n` to 1 — the negative step is the
third argument.

Accumulate `math.log(math.fabs(a ** power))` into a total starting at `0.0`.

Guard the input: `a = 0` makes `ln(0)` undefined (`ValueError`), and `n < 1` means
there are no terms to add.

*Check yourself:* `ln|aⁿ| = n·ln|a|`, so the whole sum is `(1+2+…+n)·ln|a|`,
i.e. `n(n+1)/2 · ln|a|`. With `a=2, n=3` that is `6 · 0.6931 = 4.1589`.
Confirming a loop against a closed-form formula is a genuinely useful testing habit.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_12_sum_of_logs.py)

---

## Exercise 1.13 — Series to a given precision

*(Original Lab 5, Task 3)*

Verify, to a precision ε, that

```
ln(1 − x) = −( x + x²/2 + x³/3 + x⁴/4 + … )        for |x| < 1
```

Read `x` and `ε`, sum the series until the next term is smaller than `ε`, then compare
the result to `math.log(1 - x)`.

<details><summary><b>Hint</b></summary>

`while math.fabs(term) > eps:` — add the term, increment `k`, compute the next term as
`(x ** k) / k`.

The sign: the series as written above is *negated*, so either subtract each term from
your total or negate at the end.

⚠️ **The guard is the whole point of this exercise.** For `|x| ≥ 1` the terms do not
shrink, `math.fabs(term) > eps` never becomes false, and your program hangs. The original
archive solution has exactly this bug. Reject `|x| >= 1` before you enter the loop.

Also guard `eps <= 0`, which hangs for the same reason.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_13_series_precision.py)

---

## Exercise 1.14 — Recurrence relation

*(Original Lab 5, Task 4)*

Let `x₀ = x₁ = 1` and `xᵢ = xᵢ₋₁ + 2·xᵢ₋₂` for `i = 2, 3, …`. Find `xₙ`.

Write it **both** ways: keeping only the last two values, and keeping the whole sequence
in a list. Then state which you would use for `n = 1_000_000` and why.

**Test with:** `n = 6` → 43. The sequence is 1, 1, 3, 5, 11, 21, 43.

<details><summary><b>Hint</b></summary>

**Rolling variables:** hold `previous2` and `previous1`, compute `current`, then shuffle:
`previous2 = previous1` **then** `previous1 = current`. Order matters — swap those two
lines and you lose a value.

**List:** start `x = [1, 1]` and `x.append(x[i-1] + 2*x[i-2])` inside the loop.

Both need `if n <= 1: result = 1` — `range(2, n+1)` is empty for `n = 1`, so the loop
never runs and `current` would not exist.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_14_recurrence.py)

---

## Exercise 1.15 — Invoice line with validation 💼

**Not from the archive — this one is from our world.**

Write a small tool that asks for one invoice line and prints a formatted result:

- **product code** — must be exactly 13 characters, all digits (an EAN-13 barcode)
- **quantity** — a whole number, greater than 0
- **unit price** — a decimal, greater than 0
- **VAT rate** — one of 0, 7 or 19 (percent)

Re-ask on every invalid entry, explaining what was wrong. Then print:

```
──────────────────────────────────────────
  INVOICE LINE
──────────────────────────────────────────
  Product code   4006381333931
  Quantity                   12
  Unit price              13.50
  Net amount             162.00
  VAT (19%)               30.78
  Gross amount           192.78
──────────────────────────────────────────
```

<details><summary><b>Hint</b></summary>

**On the product code — this is the important part.** Keep it as a **string**, never
convert it to `int`. `int("0401234567890")` is `401234567890`: the leading zero is gone,
the length is wrong, and it will never again match the same code in another file.
This is a real and expensive bug class in data work — treat identifiers as text, always.

Validating it: `len(code) == 13 and code.isdigit()`.

**The validation shape** is one `while True:` per field, with `break` on success:

```python
while True:
    code = input("Product code (13 digits): ").strip()
    if len(code) == 13 and code.isdigit():
        break
    print("  ✗ Must be exactly 13 digits.")
```

`.strip()` removes stray spaces — pasted values are full of them.

**For the numbers**, `int(input(...))` raises `ValueError` on `"abc"` and crashes.
Either check with `.isdigit()` before converting, or learn `try` / `except`:

```python
try:
    quantity = int(raw)
except ValueError:
    print("  ✗ Not a whole number.")
    continue
```

**For the VAT rate**, `if rate in (0, 7, 19):` tests membership in one go.

**The maths:** net = quantity × price; VAT = net × rate/100; gross = net + VAT.
Format money with `:.2f` — always.

**The separator lines** are `print("─" * 42)`. Remember `"text" * 3` from Lesson 1?
This is where it earns its keep.
</details>

➡ [Solution](../../exercise-bank/meeting-1/ex_1_15_invoice_line.py)

---

## Done?

Check yourself against the Meeting 1 goal: **take a 10-line script you have never seen
and say what it does, line by line, without running it.**

If that feels true, go to [Meeting 2](../meeting-2/README.md), where single values
become collections of values — and the code starts to look like real data work.

If it does not feel true yet, redo Exercises 1.11 and 1.14. They are the two that most
reliably expose a shaky loop model.
