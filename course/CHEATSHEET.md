# Python Cheatsheet — one page

⬅ [Course home](../README.md) · Print this. Keep it next to you.

---

## Types and conversion

```python
42          int          # whole number
3.14        float        # decimal
"text"      str          # text
True/False  bool         # yes/no
None        NoneType     # "no value"

type(x)              # what is this?
int("42")  float("3.14")  str(42)
int(3.99)  # 3  ← CHOPS. round(3.99) → 4
```

## Arithmetic

```python
7 + 2   9        7 / 2   3.5   ← always a float
7 - 2   5        7 // 2  3     ← floor, remainder discarded
7 * 2   14       7 % 2   1     ← remainder only
2 ** 8  256      abs(-5) 5

x % 2 == 0       # is x even?
n % 10           # last digit      n // 10  # drop last digit
x += 1  x -= 1  x *= 2  total += price
```

## Strings

```python
f"{name} is {age}"            # f-string — use this
f"{value:.2f}"                # 2 decimals (money)
f"{value:>10.2f}"             # right-aligned, width 10
f"{name:<12}"                 # left-aligned, width 12
f"{value:,.2f}"               # 1,234.56
f"{value!r}"                  # repr — shows quotes, for debugging

"a,b,c".split(",")            # ['a','b','c']
line.split()                  # split on ANY whitespace ← for text files
",".join(["a","b"])           # 'a,b'
" hi \n".strip()              # 'hi'   ← ALWAYS strip file input
"HI".lower()  "hi".upper()
"abc".replace("a","x")
len(s)   "b" in s   s.startswith("a")
"123".isdigit()   "abc".isalpha()
"-" * 40                      # a separator line
```

## Conditions

```python
if x > 10:
    ...
elif x > 5:          # first match wins; order matters
    ...
else:
    ...

==  !=  <  >  <=  >=
1 <= x <= 2          # chaining works
and  or  not         # words, not && || !
x in [1, 2, 3]
if my_list:          # "if not empty" — 0, "", [], None are falsy
```

## Loops

```python
for i in range(5):            # 0 1 2 3 4  ← 5 EXCLUDED
for i in range(1, 6):         # 1 2 3 4 5
for i in range(0, 10, 2):     # 0 2 4 6 8
for i in range(10, 0, -1):    # 10 down to 1

for item in items:                    # the item
for i, item in enumerate(items, 1):   # position + item
for k, v in my_dict.items():          # key + value
for a, b in zip(list1, list2):        # pairs, stops at the shorter

while condition:              # set up · check · body · UPDATE
    ...
break      # leave now
continue   # next pass
```

## Lists

```python
x = [1, 2, 3]        x[0] first   x[-1] last   x[1:3] slice
len(x) sum(x) min(x) max(x) sorted(x) sorted(x, reverse=True)
x.append(v)  x.insert(0,v)  x.remove(v)  x.pop()  del x[0]
x.sort()             # IN PLACE, returns None
sorted(x)            # returns a NEW list
b = x[:]             # COPY.  b = x shares the same list!
[n*2 for n in x]              # comprehension
[n for n in x if n > 0]       # with a filter
all(...)  any(...)            # every / at least one
```

## Nested lists (tables)

```python
t = [[1,2],[3,4]]
t[1][0]              # 3     ← ROW first, then column
len(t)               # rows        len(t[0])  # columns
[[0]*3 for _ in range(3)]     # ✓ correct
[[0]*3]*3                     # ✗ all rows SHARED
zip(*t)              # transpose
```

## Dictionaries

```python
d = {"name": "Bread", "qty": 6}
d["name"]                # KeyError if missing
d.get("x")               # None if missing
d.get("x", 0)            # your default
d["new"] = 1             # add (no .append)
"x" in d   del d["x"]   d.pop("x")
d.keys()  d.values()  d.items()

counts[k] = counts.get(k, 0) + 1          # THE counting pattern
{p["code"]: p for p in rows}              # key a list of dicts by id
sorted(rows, key=lambda r: r["price"])    # sort records
max(rows, key=lambda r: r["price"])
d1.keys() & d2.keys()    # in both      - & | work on keys as sets
d1.keys() - d2.keys()    # first only
```

## Functions

```python
def name(a, b=10):
    """What it promises. What happens on bad input."""
    return a + b

name(1)  name(1, 2)  name(b=2, a=1)

# return hands the value BACK. print throws it away.
# defaults must be immutable — never def f(x=[])
raise ValueError("why")       # refuse an impossible request
assert condition, "message"   # a test
```

## Files

```python
with open(path, encoding="utf-8") as f:      # ALWAYS with + encoding
    for line in f:                            # streams; any file size
        print(line.strip())

with open(path, encoding="utf-8") as f:
    for n, line in enumerate(f, 1): ...       # line numbers for errors

with open(path, "w", encoding="utf-8") as f:  # "w" ERASES first!
    f.write("text\n")                         # \n is yours to add
    print("text", file=f)                     # tidier

from pathlib import Path
Path("out").mkdir(exist_ok=True)              # before writing into it
Path("data") / "file.csv"                     # joins correctly
p.exists()  p.name  p.suffix
```

## CSV

```python
import csv

# READ — memorise this line
with open(p, newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f, delimiter=";"):
        row["ean"]              # ALWAYS a string
        float(row["price"])     # convert deliberately

# WRITE
with open(p, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["a","b"], delimiter=";")
    w.writeheader()             # easy to forget
    w.writerows(rows)
```
`utf-8-sig` strips Excel's BOM · `newline=""` is required · `;` for EU files

## SQLite

```python
import sqlite3
con = sqlite3.connect("file.db")     # or ":memory:"
con.row_factory = sqlite3.Row        # so you can use row["name"]

con.executescript(SCHEMA)
con.execute("INSERT INTO t VALUES (?, ?)", (a, b))   # params, never f-string!
con.executemany("INSERT INTO t VALUES (?, ?)", rows) # bulk = much faster
con.commit()                         # WITHOUT THIS NOTHING IS SAVED

for row in con.execute("SELECT a, b FROM t WHERE a = ?", (x,)):
    row["a"]
con.close()
```
```sql
SELECT col, SUM(n) AS total FROM t
WHERE  col = 'x'          -- filters ROWS
GROUP  BY col
HAVING SUM(n) > 10        -- filters GROUPS
ORDER  BY total DESC LIMIT 5;

CREATE TABLE t (
  id    INTEGER PRIMARY KEY,                 -- no duplicates
  code  TEXT    NOT NULL,                    -- TEXT for identifiers
  qty   INTEGER NOT NULL CHECK (qty > 0)     -- impossible data, impossible
);
```

## math and random

```python
import math
math.sqrt(x)  math.fabs(x)  math.log(x)  math.sin(x)  math.pi
math.factorial(n)  math.radians(d)  math.degrees(r)
math.floor(x)  math.ceil(x)

import random
random.randint(1, 6)          # 1..6, both ends included
random.random()               # 0.0 .. <1.0
random.choice(items)
random.seed(42)               # reproducible — use it in tests
```

## Reading an error

```
File "x.py", line 28, in compute      ← WHERE  (lowest File line)
KeyError: 'amount'                    ← WHAT   (last line)
```
Read bottom-up. `print(f"{v!r}")` to inspect. `Ctrl-C` kills a runaway loop.

---

## The traps, in one place

| | |
|---|---|
| `input()` returns **text** | `int(input(...))` |
| `range(5)` excludes 5 | `range(n+1)` to include `n` |
| `b = a` shares the list | `b = a[:]` |
| `[[0]*3]*3` shares rows | `[[0]*3 for _ in range(3)]` |
| `x.sort()` returns `None` | `sorted(x)` |
| `int("0401...")` loses the zero | identifiers stay `str` |
| `0.1+0.2 != 0.3` | `fabs(a-b) < eps` |
| `sum(x)/len(x)` on empty | guard `if x:` |
| `max([])` raises | guard `if x:` |
| `def f(x=[])` shares state | `def f(x=None)` |
| `.split(",")` on real CSV | `csv.DictReader` |
| no `commit()` | data silently lost |
| f-string in SQL | parameters `?` |
| `open(...,"w")` | **erases the file immediately** |
| forgot `.strip()` | `"DE\n" != "DE"` |
| `<bound method ...>` printed | you forgot the `()` |

---

## Every pipeline, in five lines

```
EXTRACT   read it in, check the header first
VALIDATE  check every field; reject with a reason to a FILE
TRANSFORM type it, join it, compute it
LOAD      write it out, under constraints
REPORT    rows in = rows out + rejected  ← print this
```
