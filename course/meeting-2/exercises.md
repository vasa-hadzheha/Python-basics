# Meeting 2 — Exercises

⬅ [Meeting 2](README.md) · [Course home](../../README.md)

**16 tasks.** Exercises 2.1–2.13 are the original lab archive, translated.
2.14–2.16 are work-flavoured. Reference solutions:
[`exercise-bank/meeting-2/`](../../exercise-bank/meeting-2/)

| # | Task | Practises | From |
|---|------|-----------|------|
| [2.1](#exercise-21--list-warm-up) | List warm-up | indexing, slicing | — |
| [2.2](#exercise-22--geometric-mean) | Geometric mean | list building, product accumulator | Lab 6.1 |
| [2.3](#exercise-23--generate-then-filter) | Generate then filter | `if` inside a loop, index parity | Lab 6.2 |
| [2.4](#exercise-24--vector-times-scalar) | Vector × scalar | comprehension | Lab 6.3 |
| [2.5](#exercise-25--sort-descending) | Sort descending | `sorted`, `reverse` | Lab 6.4 |
| [2.6](#exercise-26--selective-matrix-sum) | Selective matrix sum | double loop, `range` step | Lab 7.1 |
| [2.7](#exercise-27--replace-zeros-from-a-second-matrix) | Replace zeros from matrix B | two matrices in step | Lab 7.2 |
| [2.8](#exercise-28--matrix--vector) | Matrix × vector | nested loops, `sum` | Lab 7.3 |
| [2.9](#exercise-29--sort-alternate-rows) | Sort alternate rows | in-place `.sort()` | Lab 7.4 |
| [2.10](#exercise-210--columns-without-a-zero) | Columns without a zero | column-wise loop, `break` | Lab 7.5 |
| [2.11](#exercise-211--rows-by-even-positive-sum) | Rows by even-positive sum | sorting rows by a computed key | Lab 7.6 |
| [2.12](#exercise-212--left-rectangle-integral) | Left-rectangle integral | functions as building blocks | Lab 8.2 |
| [2.13](#exercise-213--the-cooks-directory) | The cook's directory | dicts, search | Lab 9.2 |
| [2.14](#exercise-214--column-statistics-) | Column statistics 💼 | list of dicts, aggregation |
| [2.15](#exercise-215--find-the-duplicates-) | Find the duplicates 💼 | counting pattern |
| [2.16](#exercise-216--reconcile-two-price-lists-) | Reconcile two price lists 💼 | the real job |

💼 = from our world, not a textbook.

---

## Exercise 2.1 — List warm-up

**No code required.** `x = [10, 20, 30, 40, 50]`. Write down each result:

```python
x[0]        x[-1]       x[1:3]      x[:2]       x[3:]
len(x)      sum(x)      max(x)      x[::-1]     x[::2]
30 in x     x.index(30) sorted(x, reverse=True)
```

<details><summary><b>Answers</b></summary>

```
10          50          [20, 30]    [10, 20]    [40, 50]
5           150         50          [50,40,30,20,10]   [10, 30, 50]
True        2           [50, 40, 30, 20, 10]
```
</details>

---

## Exercise 2.2 — Geometric mean

*(Original Lab 6, Task 1)*

Read `n` real numbers into a list. Compute their product, then the geometric mean
(the *n*-th root of the product). If the product is not positive, say there is no real
geometric mean.

**Test with:** `2, 4, 8` → product 64, mean 4.

<details><summary><b>Hint</b></summary>

Read the list in one line: `x = [float(input(f"x{i+1}: ")) for i in range(n)]`.

The product accumulator **starts at 1.0**, not 0 — `0 * anything` is 0.

The *n*-th root is `product ** (1 / n)`.

Two guards worth adding, and the reason this exercise is here:
- `n = 0` makes `1 / n` a `ZeroDivisionError`. Reject it before you divide.
- A negative product has no real *n*-th root — but `(-8) ** (1/3)` does **not** raise,
  it returns the complex number `(1+1.73j)`. Without the guard your report silently
  contains a complex number.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_02_geometric_mean.py)

---

## Exercise 2.3 — Generate then filter

*(Original Lab 6, Task 2)*

Build an array `B` of `n` elements, where for `i` from 1 to `n`:

```
b[i] = 1 + 0.5 + 1/i        if i is even
b[i] = i!/2 + 3             if i is odd
```

Then compute the product of the elements at **odd indexes**.

<details><summary><b>Hint</b></summary>

`math.factorial(i)` gives `i!`. `i % 2 == 0` tests even.

To step over odd indexes: `range(1, len(b), 2)` — start at 1, step 2.

The original lab statement says "elements with odd numbers", which is genuinely
ambiguous: odd *index* (0-based) picks b[1], b[3]…; odd *position* (1-based, as a human
counts) picks b[0], b[2], b[4]…. **Pick one and say so in a comment.** Ambiguity that
survives into code is a bug waiting for someone to notice.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_03_generate_and_filter.py)

---

## Exercise 2.4 — Vector × scalar

*(Original Lab 6, Task 3)*

Read a vector of `n` coordinates and a scalar `a`. Print the vector multiplied by `a`.

<details><summary><b>Hint</b></summary>

One line: `result = [value * a for value in x]`.

⚠️ Note what happens if you write `x * a` instead: for a list, `*` **repeats the list**
(`[1,2] * 3` is `[1,2,1,2,1,2]`), it does not multiply the elements. This is the
`"7" * 3` behaviour from [Lesson 1](../meeting-1/01-values-and-types.md) again, and it
is exactly why `numpy`/`polars` exist — they redefine `*` to mean element-wise
multiplication, which is what you wanted.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_04_vector_scalar.py)

---

## Exercise 2.5 — Sort descending

*(Original Lab 6, Task 4)*

Read `n` numbers and print them sorted from largest to smallest. Print the original
list too, unchanged.

<details><summary><b>Hint</b></summary>

`sorted(x, reverse=True)` returns a **new** list and leaves `x` alone — which is what
lets you print both.

`x.sort(reverse=True)` would sort in place and destroy the original. The exercise is
here specifically to make you choose.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_05_sort_descending.py)

---

## Exercise 2.6 — Selective matrix sum

*(Original Lab 7, Task 1)*

Generate a matrix of random integers. Sum the **positive** elements whose **first index
is even and second index is odd**.

<details><summary><b>Hint</b></summary>

Build it with `[[random.randint(-10, 20) for j in range(cols)] for i in range(rows)]`.

The two `range` calls are the whole exercise:
`range(0, rows, 2)` for even indexes, `range(1, cols, 2)` for odd.

Add `random.seed(7)` at the top so your matrix is the same every run — otherwise you
cannot tell a fixed bug from a lucky matrix.

Print each element as you add it. It is the only practical way to check the total.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_06_selective_sum.py)

---

## Exercise 2.7 — Replace zeros from a second matrix

*(Original Lab 7, Task 2)*

Given matrix `A` (typed in) and matrix `B` of the same size (random), replace every zero
in `A` with the element in the same position in `B`.

<details><summary><b>Hint</b></summary>

A double loop over `i` and `j`, with `if a[i][j] == 0: a[i][j] = b[i][j]`.

⚠️ `A` holds floats typed by the user, so `a[i][j] == 0` is a float comparison.
For a value typed as `0` it is exactly `0.0` and the test works — but a value that
*computed* to nearly zero would not match. If you wanted "near zero", you need the
epsilon test from [Lesson 1](../meeting-1/01-values-and-types.md). Decide which you
mean; say so in a comment.

Build B with the same `rows`/`cols`, or the indexes will not line up.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_07_replace_zeros.py)

---

## Exercise 2.8 — Matrix × vector

*(Original Lab 7, Task 3)*

Given an `n × m` matrix `A` and a vector `x` of `m` coordinates, compute `A·x`.
Then, given a vector `b`, check whether `A·x = b`.

<details><summary><b>Hint</b></summary>

Row `i` of the answer is `sum(A[i][j] * x[j] for j in range(m))` — one number per row,
so the result has `n` elements.

The dimensions must agree: `A` has `m` **columns** and `x` has `m` **elements**.
Check that first and refuse if not; a mismatch is `IndexError` otherwise.

For the `A·x = b` comparison, **do not use `==` on a list of floats.** Compare
element by element with an epsilon:
`all(math.fabs(p - q) < eps for p, q in zip(result, b))`.

The original archive author left a comment saying they did not understand this part of
the task. It is the epsilon comparison — and it is a genuinely good question to have
asked.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_08_matrix_vector.py)

---

## Exercise 2.9 — Sort alternate rows

*(Original Lab 7, Task 4)*

Given a square integer matrix, sort the elements of the **odd-numbered rows** into
ascending order, leaving the others alone.

<details><summary><b>Hint</b></summary>

`for i in range(1, n, 2): m[i].sort()` — that is genuinely the whole solution.

`m[i]` **is** a list, so it has `.sort()`, and sorting it in place modifies the matrix
directly. This is the copy-vs-reference idea from [Lesson 6](06-lists.md) working
*for* you rather than against you.

Note the archive's own comment here: "could use `range(0, r, 2)` for a normal user".
Same 0-based vs 1-based ambiguity as 2.3 — decide and document.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_09_sort_odd_rows.py)

---

## Exercise 2.10 — Columns without a zero

*(Original Lab 7, Task 5)*

Given an integer matrix, count the columns that contain **no** zero element.

<details><summary><b>Hint</b></summary>

To go column-wise, put the column loop **outside**:

```python
for j in range(cols):
    for i in range(rows):
        ...table[i][j]...
```

Use a flag (`has_zero = False`), set it when you find a zero, and `break` — once you
have found one zero the column is settled.

Then write it again with `all(table[i][j] != 0 for i in range(rows))` and check you get
the same answer. Reading that version is the goal; writing the explicit one is the practice.

⚠️ The archive's shortcut `[0 if 0 in column else 1 for column in a]` is **wrong**:
`for column in a` iterates over rows. Run both and see the difference.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_10_columns_without_zero.py)

---

## Exercise 2.11 — Rows by even-positive sum

*(Original Lab 7, Task 6)*

For each row, compute the sum of its **positive even** elements. Then output the rows
ordered by that sum, smallest first.

<details><summary><b>Hint</b></summary>

Per row: `sum(v for v in row if v > 0 and v % 2 == 0)`.

Then sort the rows by that computed value. The clean way is the `key=` argument from
[Lesson 9](09-dicts-and-records.md):

```python
ordered = sorted(table, key=lambda row: sum(v for v in row if v > 0 and v % 2 == 0))
```

⚠️ **Look at how the archive does this** — it is the most interesting bug in the whole
repository:

```python
for i in range(r):
    g.append(a[h.index(min(h))])
    h[h.index(min(h))] = 10000000     # "used" marker
```

It finds the smallest sum, copies that row, then overwrites the sum with 10,000,000 so
it will not be picked again. It works — until a row genuinely sums to more than
10,000,000, at which point the order silently breaks. A **magic sentinel value** that
can collide with real data is a real and common bug class. `sorted(key=...)` has no
such problem.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_11_rows_by_even_sum.py)

---

## Exercise 2.12 — Left-rectangle integral

*(Original Lab 8, Task 2)*

Write a function that approximates a definite integral by the **left-rectangle rule**,
then use it to evaluate an expression.

The left-rectangle rule: split `[a, b]` into `n` strips of width `h = (b − a)/n` and
approximate the area as `h × (f(x₀) + f(x₁) + … + f(xₙ₋₁))`, taking the height from the
**left** edge of each strip.

<details><summary><b>Hint</b></summary>

Two functions, not one:

```python
def f(x):
    """The function being integrated."""
    return math.sqrt(4 * x + math.sin(math.sqrt(x**3)))

def integrate_left(func, a, b, n):
    """Approximate the integral of func from a to b with n left rectangles."""
    h = (b - a) / n
    total = 0.0
    for i in range(n):                 # 0 .. n-1  -> LEFT edges
        total += func(a + i * h)
    return total * h
```

Passing `func` **as an argument** means the integrator works for any function — that is
the point of the exercise, and it is your first taste of composing functions.

Test it on something you know: the integral of `x²` from 0 to 1 is exactly 1/3.
With `n = 1000` you should get about 0.3328. It approaches 1/3 as `n` grows, from below,
because left rectangles undershoot a rising curve.

⚠️ The archive's version does not integrate at all — it computes
`(b-a) * sqrt(4a + sin(sqrt(a**3)))`, which is a **single** rectangle spanning the whole
interval. That is the `n = 1` case, and the error is enormous. Worth comparing.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_12_left_integral.py)

---

## Exercise 2.13 — The cook's directory

*(Original Lab 9, Task 2)*

A product database: name, unit of measure, quantity in stock, unit price.
Support adding a product (or topping up an existing one) and searching by any field.

<details><summary><b>Hint</b></summary>

Use a **list of dicts** — one dict per product — rather than the archive's dict of dicts.
It sorts and filters more naturally and it is the shape a CSV file becomes in Meeting 3.

```python
products = [
    {"name": "Milk", "unit": "pack", "quantity": 10, "price": 14.00},
    ...
]
```

Then:
- search by name: `[p for p in products if query.lower() in p["name"].lower()]`
  — `.lower()` on both sides makes it case-insensitive, which users expect
- search by price range: `[p for p in products if lo <= p["price"] <= hi]`
- add or top up: find it first, `+=` the quantity if present, `.append()` if not

**Keep `input()` out of your functions.** Take the values as arguments and return a
result. The archive's version asks for input *inside* `add_product`, which makes it
impossible to test and impossible to run from a scheduled job — see
[Lesson 8](08-functions.md).
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_13_cooks_directory.py)

---

## Exercise 2.14 — Column statistics 💼

Given this sales table as a list of dicts:

```python
sales = [
    {"region": "North", "product": "Bread", "units": 120, "revenue": 1620.00},
    {"region": "South", "product": "Bread", "units": 80,  "revenue": 1080.00},
    {"region": "North", "product": "Milk",  "units": 200, "revenue": 2800.00},
    {"region": "South", "product": "Milk",  "units": 150, "revenue": 2100.00},
    {"region": "North", "product": "Cola",  "units": 90,  "revenue": 1079.10},
]
```

Print a report showing, for the `units` and `revenue` columns: count, sum, min, max and
mean. Then print the total revenue **per region**, sorted highest first.

**Target output:**
```
Column       Count        Sum        Min        Max       Mean
units            5     640.00      80.00     200.00     128.00
revenue          5    8679.10    1079.10    2800.00    1735.82

Revenue by region
North                                                   5499.10
South                                                   3180.00
```

<details><summary><b>Hint</b></summary>

Pull one column out as a list first — that makes everything else trivial:

```python
values = [row["units"] for row in sales]
print(len(values), sum(values), min(values), max(values), sum(values) / len(values))
```

Write a function `column_stats(rows, field)` that returns a dict, and call it for each
field. Then the report loop is the same for every column. **Guard the empty case**:
`sum([]) / len([])` is `ZeroDivisionError`.

For the per-region total, use the grouping form of the counting pattern from
[Lesson 9](09-dicts-and-records.md):

```python
by_region = {}
for row in sales:
    by_region[row["region"]] = by_region.get(row["region"], 0) + row["revenue"]
```

Then sort the items by value, descending:
`sorted(by_region.items(), key=lambda pair: pair[1], reverse=True)`.

This is a `GROUP BY` written by hand. In [Lesson 12](../meeting-3/12-sql-from-python.md)
you write the same thing as one line of SQL — and seeing both is the point.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_14_column_stats.py)

---

## Exercise 2.15 — Find the duplicates 💼

Given a list of product codes, report:
1. which codes appear more than once, and how many times
2. how many unique codes there are
3. the codes that are **invalid** (not exactly 13 digits)

```python
codes = [
    "4006381333931", "4009900484147", "4006381333931",
    "40099004841", "4311501676851", "4006381333931",
    "4311501676851", "400990048414X", "",
]
```

<details><summary><b>Hint</b></summary>

The counting pattern from [Lesson 9](09-dicts-and-records.md):

```python
counts = {}
for code in codes:
    counts[code] = counts.get(code, 0) + 1
```

Then `duplicates = {c: n for c, n in counts.items() if n > 1}` — a dict comprehension
with a filter.

Unique count is `len(counts)`, or `len(set(codes))`. A `set` is a collection with no
duplicates and no order; `set(codes)` is the fastest way to de-duplicate anything.

Reuse `is_valid_ean13` from [Lesson 8](08-functions.md) — that is what writing it as a
function was for.

**Why this matters:** a duplicate key breaks a join. If you join two tables on a code
that appears three times on one side, you get three times as many rows out as you
expected, and every total downstream is inflated. Checking for duplicates *before*
joining is the single highest-value validation in data work.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_15_find_duplicates.py)

---

## Exercise 2.16 — Reconcile two price lists 💼

**This is the real job, in miniature.** Two price lists arrive — one from the supplier,
one from our own system — and you must report the differences.

```python
supplier = [
    {"code": "4006381333931", "name": "Bread 500g", "price": 13.50},
    {"code": "4009900484147", "name": "Milk 1L",    "price": 14.00},
    {"code": "4311501676851", "name": "Salt 1kg",   "price": 7.20},
    {"code": "5000112637922", "name": "Cola 330ml", "price": 11.99},
]

ours = [
    {"code": "4006381333931", "name": "Bread 500g", "price": 13.50},
    {"code": "4009900484147", "name": "Milk 1L",    "price": 13.80},
    {"code": "4311501676851", "name": "Salt 1kg",   "price": 7.20},
    {"code": "9999999999999", "name": "Old item",   "price": 3.00},
]
```

Report four things:
1. codes in **both**, same price → OK
2. codes in **both**, different price → the change, with the delta and a percentage
3. codes only in the **supplier** list → new products
4. codes only in **our** list → discontinued

<details><summary><b>Hint</b></summary>

**The key move — and this is the lesson of the exercise:** turn each list into a dict
keyed by code *before* you compare anything.

```python
supplier_by_code = {p["code"]: p for p in supplier}
ours_by_code = {p["code"]: p for p in ours}
```

Now membership is a one-liner instead of a nested loop:

```python
in_both = supplier_by_code.keys() & ours_by_code.keys()      # set intersection
only_supplier = supplier_by_code.keys() - ours_by_code.keys()  # set difference
only_ours = ours_by_code.keys() - supplier_by_code.keys()
```

Dict keys behave as sets, so `&` (in both), `-` (in the first only) and `|` (in either)
all work directly. This is the whole of a SQL `INNER JOIN` / `LEFT JOIN` in three lines,
and it is worth recognising that shape.

⚠️ **Compare the prices with a tolerance, not `==`.** These are floats, and a price
that arrived as `13.499999999999998` from a CSV would report as a change.
Use `math.fabs(a - b) < 0.005` — i.e. "differs by less than half a cent".

For the percentage, guard against a zero old price: `ZeroDivisionError` on real data
is a matter of when, not if.

**Why the dict-first approach matters:** the nested-loop version is
`for s in supplier: for o in ours:` — that is 4 × 4 = 16 comparisons here, but
40,000 × 40,000 = 1.6 **billion** on a real file. The dict version is 40,000 lookups.
This is the single most valuable performance idea in the whole course.
</details>

➡ [Solution](../../exercise-bank/meeting-2/ex_2_16_reconcile_prices.py)

---

## Done?

The Meeting 2 goal: **hold a table in memory, walk it, filter it, sort it, and split the
logic into functions you would be happy to have reviewed.**

Exercise 2.16 is the one that matters most — it is a genuine work task, and the
dict-keyed comparison in it is a pattern you will use every week.

➡ **[Meeting 3: Real data](../meeting-3/README.md)** — where the data stops being typed
in and starts coming from files and databases.
