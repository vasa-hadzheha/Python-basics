# Lesson 10 — Files

⬅ [Meeting 3](README.md) · ➡ [Next: CSV and Excel](11-csv-and-excel.md)

---

## Why you care

`input()` needs a human at a keyboard. A file does not. The moment your script reads a
file instead of asking questions, it can run at 3am on a schedule — and that is the
difference between a toy and a tool.

---

## The idea

```mermaid
flowchart LR
    O["<b>open</b> the file<br/>say read or write"] --> U["<b>use</b> it<br/>loop over lines,<br/>or write text"]
    U --> C["<b>close</b> it<br/><i>with does this for you</i>"]
```

---

## The syntax: always use `with`

```python
with open("data/numbers.txt") as f:
    contents = f.read()
print(contents)
```

The `with` block **closes the file automatically** — even if the code inside crashes.
Compare the manual version, which the original archive uses:

```python
f = open("data/numbers.txt")     # ✗ don't
contents = f.read()
f.close()                        # skipped entirely if the line above raises
```

An unclosed file on Windows stays locked, so the next program cannot open it —
a genuinely annoying bug to chase. **Always `with`.** There is no case where the
manual form is better.

### The three modes you need

| Mode | Meaning | If the file exists | If it does not |
|------|---------|-------------------|----------------|
| `"r"` | read (the default) | reads it | `FileNotFoundError` |
| `"w"` | write | ⚠️ **erases it completely** | creates it |
| `"a"` | append | adds to the end | creates it |

> **⚠️ `"w"` destroys the existing file the instant you open it** — before you write
> anything. There is no undo and no warning. Double-check the filename in any `open(...,
> "w")` you write or review. This is the single most destructive one-character typo in
> Python.

---

## Reading, four ways

```python
# 1. the whole file as one string — fine for small files
with open("data/numbers.txt") as f:
    text = f.read()

# 2. a list of lines — each one still has its "\n" on the end
with open("data/numbers.txt") as f:
    lines = f.readlines()

# 3. line by line — THE ONE TO USE
with open("data/numbers.txt") as f:
    for line in f:
        print(line.strip())

# 4. with line numbers, for error messages
with open("data/numbers.txt") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}: {line.strip()}")
```

**Form 3 is the default choice**, because it reads one line at a time and therefore works
on a 10 GB file as happily as on a 10-line one. `f.read()` on a 10 GB file tries to put
10 GB in memory.

Form 4 is what you use in real pipelines: when row 4,517 is malformed, your error
message should say *4,517*.

### `.strip()` is not optional

Every line you read ends with a newline character, `\n`:

```python
with open("data/numbers.txt") as f:
    for line in f:
        print(repr(line))          # repr() shows you the invisible characters
```

```
'313 4 52 -7 18\n'
'-91 6 -3 44 0\n'
'12 -55 8 23 -1\n'
```

That trailing `\n` breaks comparisons in ways that are maddening to debug, because
the two strings *look* identical when printed:

```python
line = "DE\n"
print(line == "DE")              # False!  😱
print(line.strip() == "DE")      # True
```

| Method | Removes |
|--------|---------|
| `.strip()` | whitespace from **both** ends |
| `.rstrip()` | from the right only |
| `.lstrip()` | from the left only |
| `.strip("\n")` | only newlines, keeping spaces |

**Rule: `.strip()` every value you read from a file, always.** It costs nothing and
prevents a whole class of invisible bug. A stray space in a product code from a
supplier's export is a real, weekly occurrence.

---

## Worked example 1 — largest of the negative numbers

Task 1 from the original Lab 11.

```python
values = []

with open("data/numbers.txt") as f:
    for line_number, line in enumerate(f, start=1):
        for token in line.split():            # split() on whitespace
            try:
                values.append(float(token))
            except ValueError:
                print(f"  line {line_number}: skipping {token!r} — not a number")

print(f"Read {len(values)} numbers")

negatives = [v for v in values if v < 0]

if negatives:                                 # guard: max([]) raises ValueError
    print(f"Negative numbers   : {negatives}")
    print(f"Largest negative   : {max(negatives)}")
else:
    print("There are no negative numbers in the file.")
```

```
Read 15 numbers
Negative numbers   : [-7.0, -91.0, -3.0, -55.0, -1.0]
Largest negative   : -1.0
```

Three details that matter:

1. **`line.split()` with no argument splits on any whitespace** and discards empty
   pieces. `line.split(" ")` splits on single spaces only, so two spaces in a row give
   you an empty string, and `float("")` raises `ValueError`. The archive uses
   `row.split(' ')` and gets away with it because its test file is tidy. Real files
   are not. **Use bare `.split()` for whitespace.**
2. **The `try`/`except` keeps one bad token from killing the run** — and it says which
   line and which token, so you can go and look.
3. **`if negatives:` before `max()`.** `max([])` raises `ValueError: max() arg is an
   empty sequence`. The archive calls `max(s)` unguarded, so the same script crashes on
   a file with no negative numbers. Empty input is not an edge case; it is Tuesday.

▶ Run it: `python3 examples/meeting-3/10_largest_negative.py`

---

## Writing files

```python
results = [3.5, -2.0, 18.25]

with open("out/results.txt", "w") as f:
    f.write("value\n")                        # you supply the \n yourself
    for value in results:
        f.write(f"{value:.2f}\n")
```

`f.write()` does **not** add a newline — unlike `print()`. Forget the `\n` and your
whole file is one enormous line.

You can also point `print()` at a file, which is often tidier:

```python
with open("out/results.txt", "w") as f:
    print("value", file=f)
    for value in results:
        print(f"{value:.2f}", file=f)
```

### Creating the folder first

`open("out/results.txt", "w")` fails with `FileNotFoundError` if `out/` does not exist —
writing a file does not create its directory.

```python
from pathlib import Path

Path("out").mkdir(exist_ok=True)          # exist_ok: fine if it is already there
```

`pathlib` is the modern way to handle paths, and worth knowing:

```python
from pathlib import Path

source = Path("data") / "numbers.txt"     # the / operator joins paths
print(source.exists())                    # True
print(source.name)                        # numbers.txt
print(source.suffix)                      # .txt
print(source.stat().st_size)              # size in bytes
```

The `/` operator produces the right separator on every OS, which is why you should use
it instead of gluing strings with `"data/" + filename`.

---

## Worked example 2 — replace zeros, write the result

Task 2 from the original Lab 11: read numbers, replace every zero with the maximum
value in the file, write the result out.

```python
from pathlib import Path

values = []
with open("data/numbers_with_zeros.txt") as f:
    for line in f:
        values.extend(float(token) for token in line.split())

if not values:
    print("The file is empty — nothing to do.")
else:
    largest = max(values)
    replaced = [largest if v == 0 else v for v in values]

    Path("out").mkdir(exist_ok=True)
    with open("out/replaced.txt", "w") as f:
        for value in replaced:
            f.write(f"{value:g}\n")          # one number per line

    print(f"Largest value  : {largest:g}")
    print(f"Zeros replaced : {values.count(0)}")
    print(f"Wrote {len(replaced)} values to out/replaced.txt")
```

```
Largest value  : 22
Zeros replaced : 5
Wrote 15 values to out/replaced.txt
```

**Compare with the archive**, which ends with:

```python
with open("new_data.txt", 'w') as f:
    f.write(str(new_list))                   # ✗
```

`str(a_list)` produces `[5.0, 22.0, 12.0, ...]` — brackets, commas and all — as a
single line. It is *a* file, but nothing can read it back except Python's own `eval`,
which you should never point at a data file. **One value per line** (or proper CSV,
which is [Lesson 11](11-csv-and-excel.md)) is readable by every tool ever written,
including Excel.

> **The test for any output format: can you read it back in?** Write the reader before
> you commit to the writer. If reading it back is awkward, the format is wrong.

▶ Run it: `python3 examples/meeting-3/10_replace_zeros.py`

---

## Worked example 3 — search a catalogue

Task 3 from the original Lab 11, which searches a song list. This introduces
**encodings**, which is the thing about files that most often ruins an afternoon.

```python
QUERY = "1975"

matches = []
with open("data/songs.txt", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        line = line.strip()
        if not line:                                  # skip blank lines
            continue
        if QUERY.lower() in line.lower():             # case-insensitive
            matches.append((line_number, line))

print(f"{len(matches)} match(es) for {QUERY!r}:")
for line_number, line in matches:
    artist, title, year, duration = line.split("|")
    print(f"  line {line_number}: {artist} — {title} ({year}, {duration})")
```

```
2 match(es) for '1975':
  line 1: Queen — Bohemian Rhapsody (1975, 5:55)
  line 2: Pink Floyd — Wish You Were Here (1975, 5:34)
```

**Collect matches, then report.** The archive prints inside the loop and comments out its
"nothing found" message with the note *"IT LOOPS THE MESSAGE"* — because an `else` inside
the loop fires once per non-matching line. Collecting into a list and checking
`len(matches)` afterwards is the fix, and it is the same "accumulate then decide"
shape as [Lesson 4](../meeting-1/04-while-loops.md).

▶ Run it: `python3 examples/meeting-3/10_search_catalogue.py`

---

## Encodings — the 20 minutes this lesson saves you

A file on disk is bytes. An *encoding* is the agreement about which bytes mean which
characters. Get it wrong and you see `Ð¿Ñ€Ð¸Ð²Ñ–Ñ‚` instead of `привіт`, or you get
`UnicodeDecodeError`.

```python
open("file.txt", encoding="utf-8")        # ✓ the modern default — use this
open("file.txt", encoding="cp1252")       # older Windows/Western Europe
open("file.txt", encoding="latin-1")      # never fails, but may give nonsense
```

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `UnicodeDecodeError: 'utf-8' codec can't decode byte...` | the file is not UTF-8 | try `cp1252`, then `latin-1` |
| Text shows as `Ã¤`, `â€™`, `Ð¿` | UTF-8 read as something else | `encoding="utf-8"` |
| An invisible `﻿` on the first field | a BOM, from Excel | `encoding="utf-8-sig"` |

> **Always pass `encoding=` explicitly.** Without it Python uses the machine's default,
> which is UTF-8 on Linux/macOS and often cp1252 on Windows — so the same script
> behaves differently on your laptop and your colleague's. That is a genuinely
> horrible bug to reproduce.

**`encoding="utf-8-sig"` is the one to remember.** Excel writes a "byte order mark" at
the start of CSV files it exports, and `utf-8-sig` strips it silently. Without it, your
first column name is `"﻿ean"` rather than `"ean"`, and `row["ean"]` raises `KeyError`
while the printed output looks perfectly normal. That one has cost everyone an hour.

The archive's `encoding='latin_1'` for the song file is a reasonable guess that happens
to work — `latin-1` maps every possible byte to *some* character, so it never raises.
But it silently mangles anything non-Western, which means the error surfaces later,
in your output, instead of immediately at the read. **Prefer the encoding that fails
loudly over the one that fails quietly.**

---

## Handling a missing file

```python
from pathlib import Path

source = Path("data/numbers.txt")

if not source.exists():
    print(f"✗ {source} not found. Run this from the repository root.")
else:
    with open(source, encoding="utf-8") as f:
        ...
```

Or catch it:

```python
try:
    with open("data/numbers.txt", encoding="utf-8") as f:
        ...
except FileNotFoundError:
    print("✗ data/numbers.txt not found.")
```

Either is fine. The point is the **message**: `"✗ data/numbers.txt not found. Run this
from the repository root."` tells the reader what to do. A bare traceback does not.

> **Relative paths are relative to where you ran the command, not where the file lives.**
> `python3 examples/meeting-3/10_files.py` from the repo root works; `cd examples/meeting-3
> && python3 10_files.py` fails, because `data/` is not there. This confuses everyone
> once. Run everything from the repository root.

---

## 🔍 Read this code

**(a)** What is wrong here?
```python
f = open("report.txt", "w")
f.write("hello")
```

**(b)** What does this print for a file containing `DE`?
```python
with open("country.txt") as f:
    code = f.readline()
print(code == "DE")
```

**(c)** What is the danger?
```python
with open("important_data.csv", "w") as f:
    pass
```

**(d)**
```python
line = "313 4 52"
print(line.split())
print(line.split(" "))
print("a  b".split(" "))
```

<details>
<summary><b>Answers</b></summary>

**(a)** The file is never closed. On Windows it stays locked; the written data may not
even be flushed to disk. Use `with`.

**(b)** `False`. `readline()` returns `"DE\n"` including the newline.
`code.strip() == "DE"` is `True`. This is the bug that makes you doubt your own eyes.

**(c)** It **erases `important_data.csv`**. Opening in `"w"` mode truncates the file
immediately, and `pass` does nothing, so you are left with an empty file. This is a
real way to destroy data with four words of Python.

**(d)** `['313', '4', '52']`, `['313', '4', '52']`, `['a', '', 'b']`.
The third shows the difference: `split(" ")` on a double space produces an empty string
between them, and `float("")` raises `ValueError`. Bare `.split()` collapses runs of
whitespace and never does this.

</details>

---

## Traps

| Trap | Symptom | Fix |
|------|---------|-----|
| `open(..., "w")` on the wrong file | data destroyed, silently | check the filename twice |
| no `with` | file stays locked, data unflushed | always `with` |
| forgot `.strip()` | comparisons fail invisibly | strip everything you read |
| `f.write()` without `\n` | one giant line | add `\n` or use `print(..., file=f)` |
| no `encoding=` | works on your machine, not a colleague's | always pass it |
| Excel CSV, first column `KeyError` | a BOM | `encoding="utf-8-sig"` |
| `f.read()` on a huge file | memory exhausted | `for line in f:` |
| `max()`/`min()` on data with no matches | `ValueError` | guard with `if values:` |
| writing to a folder that does not exist | `FileNotFoundError` | `Path("out").mkdir(exist_ok=True)` |
| running from the wrong directory | `FileNotFoundError` | run from the repo root |

---

## When your data gets bigger

Everything above streams line by line, so it scales further than you would expect —
a plain `for line in f:` loop handles gigabytes happily.

What it does *not* do is the analysis. Once you want grouping, joining and aggregation
over millions of rows, the loop stops being the right tool:

```python
# stdlib: you write the aggregation yourself (Lesson 12 / Exercise 2.14)
# polars: the aggregation is one expression, and it is parallel and vectorised
import polars as pl

result = (
    pl.scan_csv("data/sales_raw.csv", separator=";")   # scan_ = lazy, does not load it all
      .filter(pl.col("quantity") > 0)
      .group_by("country")
      .agg(pl.col("quantity").sum().alias("total_units"))
      .sort("total_units", descending=True)
      .collect()                                        # only NOW does it read anything
)
```

`pl.scan_csv` + `.collect()` is *lazy*: Polars reads the query first, works out that it
only needs two columns, and never loads the rest. That is the idea the loop cannot give
you, and it is why the production answer is a dataframe library rather than a bigger loop.

`pip install polars` when you want it. Learn the loop first — it is what `scan_csv`
is doing for you.

---

## Recap

- `with open(path, encoding="utf-8") as f:` — always `with`, always `encoding`.
- `"r"` reads, `"w"` **erases and** writes, `"a"` appends.
- `for line in f:` is the default: streams, so file size does not matter.
- `enumerate(f, start=1)` for line numbers in error messages.
- `.strip()` everything. The trailing `\n` is invisible and breaks comparisons.
- Bare `.split()` for whitespace; `.split(";")` for a known delimiter.
- `f.write()` needs its own `\n`; `print(..., file=f)` does not.
- `Path("out").mkdir(exist_ok=True)` before writing into a folder.
- `utf-8-sig` for anything Excel exported.
- Write output one value per line, so it can be read back.

➡ [Next: CSV and Excel](11-csv-and-excel.md)
