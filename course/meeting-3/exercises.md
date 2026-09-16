# Meeting 3 — Exercises

⬅ [Meeting 3](README.md) · [Course home](../../README.md)

**12 tasks.** 3.1–3.4 are the original lab archive, translated. 3.5–3.12 are
work-shaped, and the last two are **code reviews** — the skill the whole course
has been building towards.

Reference solutions: [`exercise-bank/meeting-3/`](../../exercise-bank/meeting-3/)

> **Run everything from the repository root**, so that `data/...` resolves:
> ```bash
> python3 exercise-bank/meeting-3/ex_3_05_sales_summary.py
> ```

| # | Task | Practises | From |
|---|------|-----------|------|
| [3.1](#exercise-31--largest-negative-number) | Largest negative number | file reading, guards | Lab 11.1 |
| [3.2](#exercise-32--replace-zeros-and-write-out) | Replace zeros, write out | writing readable output | Lab 11.2 |
| [3.3](#exercise-33--search-a-catalogue) | Search a catalogue | collect-then-report | Lab 11.3 |
| [3.4](#exercise-34--pair-up-coordinates) | Pair up coordinates | line-indexed parsing | Checker |
| [3.5](#exercise-35--sales-summary-from-csv-) | Sales summary from CSV 💼 | `DictReader`, typing, grouping |
| [3.6](#exercise-36--validate-a-product-file-) | Validate a product file 💼 | rejects with reasons |
| [3.7](#exercise-37--csv--sqlite-) | CSV → SQLite 💼 | schema, constraints, `executemany` |
| [3.8](#exercise-38--answer-five-questions-in-sql-) | Five questions in SQL 💼 | `GROUP BY`, `HAVING`, `JOIN` |
| [3.9](#exercise-39--monthly-report-file-) | Monthly report file 💼 | formatted output |
| [3.10](#exercise-310--incremental-load-) | Incremental load 💼 | upsert, idempotency |
| [3.11](#exercise-311--code-review-the-quick-script-) | **Code review: the quick script** 🔍 | reading for bugs |
| [3.12](#exercise-312--code-review-ai-generated-loader-) | **Code review: AI-generated loader** 🔍 | reviewing generated code |

---

## Exercise 3.1 — Largest negative number

*(Original Lab 11, Task 1)*

`data/numbers.txt` holds numbers separated by spaces, several per line. Read them all
and print the largest of the **negative** ones.

<details><summary><b>Hint</b></summary>

```python
with open("data/numbers.txt", encoding="utf-8") as f:
    for line in f:
        for token in line.split():
            ...
```

Use bare `.split()`, not `.split(" ")` — the second one produces an empty string for
each double space, and `float("")` raises `ValueError`.

⚠️ **Guard `max()`.** `max([])` raises `ValueError: max() arg is an empty sequence`.
The archive version calls `max(s)` unguarded, so it crashes on any file with no
negative numbers. Test yours on a file with none.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_01_largest_negative.py)

---

## Exercise 3.2 — Replace zeros and write out

*(Original Lab 11, Task 2)*

Read `data/numbers_with_zeros.txt`. Replace every zero with the largest value in the
file. Write the result to `out/replaced.txt` — then **read your own output back** and
confirm it round-trips.

<details><summary><b>Hint</b></summary>

`Path("out").mkdir(exist_ok=True)` first — writing a file does not create its folder.

Write **one value per line**, not `str(the_list)`. The archive does the latter,
producing `[5.0, 22.0, ...]` on a single line, which nothing can read back except
`eval()` — and you must never point `eval()` at a data file.

The read-back test is the exercise:
```python
with open("out/replaced.txt", encoding="utf-8") as f:
    readback = [float(line) for line in f]
assert readback == replaced
```
**If you cannot read your own output back, the format is wrong.**
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_02_replace_zeros.py)

---

## Exercise 3.3 — Search a catalogue

*(Original Lab 11, Task 3)*

`data/songs.txt` has one song per line as `artist|title|year|duration`.
Ask for a search term, print every matching line (case-insensitive) with its line
number, and write the matches to `out/search_results.txt`.
Print "nothing found" **exactly once** if there are no matches.

<details><summary><b>Hint</b></summary>

Collect into a list inside the loop, then report after it:

```python
matches = []
for line_number, line in enumerate(f, start=1):
    if query.lower() in line.lower():
        matches.append((line_number, line.strip()))
# report AFTER the loop
if not matches:
    print("nothing found")
```

The archive has a commented-out `else` with the note *"IT LOOPS THE MESSAGE"* — because
an `else` inside the loop fires once per non-matching line. Collect-then-report is the fix.

`line.split("|")` gives you the four fields for a nicely formatted output.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_03_search_catalogue.py)

---

## Exercise 3.4 — Pair up coordinates

*(Original archive, `Checker/`)*

`data/points.txt` has two lines of numbers. Take the **negative** values from line 1 as
x-coordinates and the **positive** values from line 2 as y-coordinates, then print them
paired up as points.

<details><summary><b>Hint</b></summary>

`enumerate(f, start=1)` and branch on the line number — that is the archive's approach
and it is the right one here.

The two lists will have different lengths, so pair only as many as you can:
`for i in range(min(len(x), len(y)))`.

Or use `zip(x, y)`, which stops at the shorter one automatically and is cleaner.
The archive writes an `if len(x) > len(y)` with two near-identical branches;
`zip` replaces the whole thing with one line. Worth comparing.

⚠️ The archive's version has a bug in the `else` branch: it loops
`for i in range(len(x))` and indexes `y[i]`, so when `y` is the shorter list it raises
`IndexError`. `zip` cannot have this bug.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_04_pair_points.py)

---

## Exercise 3.5 — Sales summary from CSV 💼

Read `data/sales_raw.csv` with `csv.DictReader` and print:

1. the number of rows
2. total units and total revenue (`quantity × unit_price`) for the rows you *can* process
3. revenue per country, highest first
4. how many rows you had to skip, and why

<details><summary><b>Hint</b></summary>

`open(path, newline="", encoding="utf-8-sig")` and `csv.DictReader(f, delimiter=";")`.

**Every value is a string**, so `row["quantity"] * row["unit_price"]` is string
arithmetic, not multiplication. Convert deliberately.

The file has deliberate problems: an empty `quantity`, a `-2` quantity, `abc` as a
price, `1,40` with a comma decimal. Write small helpers that return `None` on failure:

```python
def parse_int(raw):
    try:
        return int(raw.strip())
    except (ValueError, AttributeError):
        return None
```

`1,40` should be **recovered** (`.replace(",", ".")`), not skipped — it is a formatting
difference, not a data problem. The negative quantity should be **skipped**, because
guessing what it means would be wrong.

Grouping by country is the counting pattern from
[Lesson 9](../meeting-2/09-dicts-and-records.md).
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_05_sales_summary.py)

---

## Exercise 3.6 — Validate a product file 💼

Write a validator for `data/products.csv` that checks:

- `ean` — exactly 13 digits
- `name` — not empty
- `unit_price` — a number greater than 0
- `vat_rate` — one of 0, 7, 19
- `ean` — not duplicated

Write valid rows to `out/products_clean.csv` and invalid rows to `out/products_rejects.csv`
with a `reason` column. Print the counts and confirm they reconcile.

**Then break the file on purpose:** copy it, corrupt a few rows, and check your
validator catches each one.

<details><summary><b>Hint</b></summary>

Check the header first — `required - set(reader.fieldnames)` — and raise if a column is
missing. A missing column is a broken *file*, not a bad *row*.

One `continue` per failure, so each row gets exactly one reason.

`enumerate(reader, start=2)` because line 1 is the header.

Track duplicates with a `set`:
```python
seen = set()
...
if ean in seen:
    reject("duplicate ean")
    continue
seen.add(ean)
```

**The reconciliation print is the point of the exercise:**
```python
print(f"reconciles: {len(good) + len(rejects) == total_rows}")
```
If that is ever `False`, a row disappeared.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_06_validate_products.py)

---

## Exercise 3.7 — CSV → SQLite 💼

Load `data/products.csv` into a SQLite database at `out/shop.db`, with a schema that
makes bad data **impossible**:

- `ean TEXT PRIMARY KEY` — no duplicates, leading zeros preserved
- `unit_price REAL NOT NULL CHECK (unit_price >= 0)`
- `vat_rate INTEGER NOT NULL CHECK (vat_rate IN (0, 7, 19))`

Then prove the constraints work by trying to insert bad rows and catching the errors.

<details><summary><b>Hint</b></summary>

`connection.executescript(SCHEMA)` runs several statements at once.
Start the schema with `DROP TABLE IF EXISTS product;` so the script is re-runnable.

Use `executemany` for the insert, and **do not forget `connection.commit()`** —
without it your script reports success against an empty database.

To demonstrate the constraints:
```python
try:
    connection.execute("INSERT INTO product VALUES (?, ?, ?, ?, ?, ?)",
                       ("4006381333931", "Duplicate", "pcs", "x", 1.0, 7))
except sqlite3.IntegrityError as error:
    print(f"correctly refused: {error}")
```
`sqlite3.IntegrityError` is what a violated `PRIMARY KEY` or `CHECK` raises.

**This is the lesson:** validation in Python protects one script; a constraint protects
the data from every program that ever touches it.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_07_csv_to_sqlite.py)

---

## Exercise 3.8 — Answer five questions in SQL 💼

Using the database the ETL pipeline builds (`python3 examples/meeting-3/13_etl_pipeline.py`
first), answer these in SQL — not in Python:

1. Total gross revenue per country, highest first.
2. The 3 products with the most units sold.
3. Customers who placed more than one order.
4. Average order value per category.
5. Any day whose total gross revenue exceeded 40.00.

<details><summary><b>Hint</b></summary>

All five are the same shape: `SELECT ... FROM sale GROUP BY ... ORDER BY ...`.

- (1) `GROUP BY country ORDER BY SUM(gross_amount) DESC`
- (2) `GROUP BY ean ORDER BY SUM(quantity) DESC LIMIT 3`
- (3) `GROUP BY customer HAVING COUNT(*) > 1` ← **`HAVING`, not `WHERE`**
- (4) `AVG(gross_amount) GROUP BY category`
- (5) `GROUP BY order_date HAVING SUM(gross_amount) > 40`

**`WHERE` filters rows before grouping; `HAVING` filters groups after.** Questions 3
and 5 are impossible with `WHERE` because the condition is about a group total.

Set `connection.row_factory = sqlite3.Row` so you can write `row["country"]`.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_08_five_questions.py)

---

## Exercise 3.9 — Monthly report file 💼

Produce `out/monthly_report.txt` from the pipeline database: a properly formatted
plain-text report with a header, a per-country section, a per-category section,
a grand total, and a generation timestamp.

It must be something you could paste into an email without apologising.

<details><summary><b>Hint</b></summary>

`print(..., file=f)` is tidier than `f.write(... + "\n")` for a report.

Money to 2 decimals, **always**: `f"{value:>12.2f}"`. Numbers right-aligned,
text left-aligned.

Separator lines with `"-" * 60`, section headers with `"=" * 60`.

For the timestamp:
```python
from datetime import datetime
print(f"Generated: {datetime.now():%Y-%m-%d %H:%M}", file=f)
```

Consider writing a helper `def section(f, title)` so every heading looks the same —
consistency is what makes a generated report look deliberate rather than accidental.

Include the row count and the reconciliation line. A report that does not say how much
data it covers cannot be checked by its reader.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_09_monthly_report.py)

---

## Exercise 3.10 — Incremental load 💼

Make the load **idempotent**: running it twice must not double the data.

Write a script that loads `data/products.csv` into `out/shop.db`, and run it three
times. After every run the table must contain exactly 10 rows. Then change one price
in a copy of the CSV and confirm the update is picked up without creating a duplicate.

<details><summary><b>Hint</b></summary>

`INSERT OR REPLACE INTO product VALUES (...)` — with `ean` as the `PRIMARY KEY`,
this inserts a new row or replaces the existing one. That is an **upsert**.

⚠️ `INSERT OR REPLACE` *deletes and re-inserts* the row, so any column you do not
supply reverts to its default. When you only want to change some columns, use:

```sql
INSERT INTO product (ean, name, unit_price) VALUES (?, ?, ?)
ON CONFLICT(ean) DO UPDATE SET
    name = excluded.name,
    unit_price = excluded.unit_price
```

`excluded` refers to the row you tried to insert. This is the modern form and it is
what you want in production.

**Why this matters:** a scheduled job *will* run twice — someone reruns it after a
failure, or a retry fires. A load that is not idempotent turns that into duplicated
revenue in every report. "Can this safely run twice?" is a standing review question.

Report how many rows were inserted versus updated, using `connection.total_changes`
before and after.
</details>

➡ [Solution](../../exercise-bank/meeting-3/ex_3_10_incremental_load.py)

---

## Exercise 3.11 — Code review: the quick script 🔍

A colleague sends you this and asks *"can you just check this quickly before I run it
on the live export?"*

```python
import csv

def process(filename):
    f = open(filename)
    data = csv.reader(f)
    results = {}
    for row in data:
        code = int(row[0])
        qty = row[2]
        price = row[3]
        total = qty * price
        if row[5] in results:
            results[row[5]] = results[row[5]] + total
        else:
            results[row[5]] = total
    avg = sum(results.values()) / len(results)
    print("Average per country: " + str(avg))
    out = open("results.csv", "w")
    for k in results:
        out.write(k + "," + str(results[k]))
    return results

process("sales.csv")
```

**Write your review.** For each problem: the line, what goes wrong, why it matters,
and what you would suggest. Aim for at least ten findings.

Then compare with the written review in the solution file.

<details><summary><b>Hint — where to look</b></summary>

Walk the [Lesson 14 checklist](14-how-to-read-code.md#part-4--the-review-checklist):

- **Files:** is `with` used? Is either file closed? Is `encoding` set? `newline=""`?
- **The header row:** is it skipped?
- **Types:** what type is `row[2]`? What does `qty * price` actually do?
- **Identifiers:** what does `int(row[0])` do to a code with a leading zero?
  And is `code` even used?
- **Indexes:** `row[5]` — what if a column is inserted before it? What if a row is short?
- **The empty case:** what is `sum(...) / len(results)` when the file has no rows?
- **The output:** is there a header? A newline between rows? Does the delimiter match
  the input? Is money formatted?
- **Data integrity:** are any rows skipped? Would you know? Is there a row count?
- **The destructive one:** what does `open("results.csv", "w")` do to an existing
  `results.csv`, and is that path where they think it is?
</details>

➡ [Written review + a fixed version](../../exercise-bank/meeting-3/ex_3_11_code_review.py)

---

## Exercise 3.12 — Code review: AI-generated loader 🔍

You asked an AI: *"Write a Python function that loads my product CSV and returns a
dict mapping product code to price."* It produced this:

```python
import csv

def load_prices(path):
    """Load product prices from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        A dictionary mapping product codes to prices.
    """
    prices = {}
    try:
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prices[int(row['ean'])] = float(row['unit_price'])
    except Exception as e:
        print(f"Error: {e}")
    return prices
```

It looks good — type-aware, documented, uses `with`, has error handling.
**Review it against `data/products.csv`.** Find at least eight problems.

<details><summary><b>Hint — the AI-specific traps</b></summary>

From the [AI checklist](14-how-to-read-code.md#the-ai-specific-checklist):

1. **The delimiter.** `DictReader` defaults to `,`. Our file is `;`-separated.
   What does `row['ean']` do then?
2. **The encoding.** No `encoding=`, so it differs between Windows and Linux.
   And no `utf-8-sig`, so an Excel BOM makes the first column `"﻿ean"`.
3. **`newline=""`** is missing, which the `csv` module requires.
4. **`int(row['ean'])`** — the leading-zero problem, again. This is the single most
   frequent generated mistake in data code.
5. **`except Exception as e: print(...)`** — it swallows *everything*, prints a line
   nobody will see, and then returns a **partially filled dict** as if all were well.
   Is a half-loaded price list better or worse than a crash?
6. **`float(row['unit_price'])`** raises on an empty or non-numeric cell — and because
   of (5), that aborts the loop and silently truncates the result.
7. **Duplicate `ean`s overwrite silently.** Which price wins? Is that intended?
8. **No count returned.** The caller cannot tell whether it loaded 10 rows or 2.
9. **The docstring is confidently wrong** about the failure behaviour — it promises
   "a dictionary mapping product codes to prices" and does not mention that the
   dictionary may be incomplete.

Then ask the bigger question: **is a dict of `code → price` even the right return
value?** It throws away the name, the unit, the VAT rate and the category. Next week
you will need one of those and rewrite the whole thing. What would you have asked for
instead?
</details>

➡ [Written review + a fixed version](../../exercise-bank/meeting-3/ex_3_12_ai_review.py)

---

## Done?

You can now read a CSV safely, validate it, store it under constraints, query it with
SQL, report on it, and review someone else's attempt at the same thing.

**Where to go next:**

| Want to | Read |
|---------|------|
| Keep a reference beside you | [CHEATSHEET.md](../CHEATSHEET.md) |
| Check a term you half-remember | [GLOSSARY.md](../GLOSSARY.md) |
| Teach this to someone else | [HOW-TO-TEACH.md](../HOW-TO-TEACH.md) |
| Handle bigger data | the **"when your data gets bigger"** box at the end of lessons 10–13 |
| Practise more | redo 3.11 and 3.12 in a month, and see how much more you spot |

The two code reviews are the ones worth repeating. Reading skill compounds.
