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

## Arithmetic — with the English name of each operation

| Write | Name of the operation | Say it aloud | `7` and `2` give | The result is called |
|-------|----------------------|--------------|------------------|----------------------|
| `a + b` | **addition** | "seven plus two" | `9` | the **sum** |
| `a - b` | **subtraction** | "seven minus two" | `5` | the **difference** |
| `a * b` | **multiplication** | "seven times two" | `14` | the **product** |
| `a / b` | **division** (true division) | "seven divided by two" | `3.5` | the **quotient** |
| `a // b` | **floor division** (integer division) | "seven floor-divided by two" | `3` | the **quotient**, remainder thrown away |
| `a % b` | **modulo** (modulus) | "seven modulo two", "seven mod two" | `1` | the **remainder** |
| `a ** b` | **exponentiation** | "seven to the power of two" | `49` | the **power** |
| `-a` | **negation** | "minus seven", "negative seven" | `-7` | |
| `abs(a)` | **absolute value** | "the absolute value of minus five" | `5` | |

### `/` vs `//` vs `%` — one sentence covers all three

Remember school division: **"7 divided by 2 is 3, remainder 1."**

```
        7 / 2   =  3.5        ← the exact answer, as a decimal
        7 // 2  =  3          ← the "3"         (how many whole times)
        7 % 2   =  1          ← the "remainder 1"
```

So `//` and `%` are the two halves of one school division, and `/` is the exact answer.
They fit back together:

```python
(7 // 2) * 2 + (7 % 2)  ==  7        # always true
```

```python
7 + 2   9        7 / 2   3.5   ← always a float, even 4 / 2 → 2.0
7 - 2   5        7 // 2  3     ← floor: remainder discarded
7 * 2   14       7 % 2   1     ← remainder only
2 ** 8  256      abs(-5) 5

x % 2 == 0       # is x even?   (remainder of 0 when divided by 2)
n % 10           # last digit      n // 10  # drop the last digit
x += 1  x -= 1  x *= 2  total += price
```

---

## Symbol names in English

What to call each character when you search for help, read code aloud, or ask a
colleague. Where British and American English differ, both are given.

### Brackets — three kinds, three jobs

| Symbol | English name | What it does in Python |
|--------|--------------|------------------------|
| `( )` | **parentheses** (one is a *parenthesis*) · UK also **round brackets** | calling a function `print(x)`; grouping `(a + b) * 2`; a tuple `(1, 2)` |
| `[ ]` | **square brackets** · US often just **brackets** | a list `[1, 2]`; indexing `items[0]`; slicing `items[1:3]` |
| `{ }` | **curly braces** · also **braces**, **curly brackets** | a dict `{"a": 1}`; a set `{1, 2}`; a placeholder in an f-string `f"{name}"` |
| `< >` | **angle brackets** · as operators, **less than** / **greater than** | comparison `a < b`. Not used for grouping in Python |

> Say **"open"** and **"close"** for the two halves: `(` is an opening parenthesis,
> `)` a closing parenthesis.

### Operator and punctuation symbols

| Symbol | English name | In Python |
|--------|--------------|-----------|
| `+` | **plus** (plus sign) | add; join strings and lists |
| `-` | **minus** · as punctuation, **hyphen** or **dash** | subtract; negate |
| `*` | **asterisk** · spoken **"star"** | multiply; `*args`; unpack `zip(*rows)`; `"-" * 40` |
| `/` | **(forward) slash** | divide; separates folders in a path |
| `\` | **backslash** | escape character: `\n` newline, `\t` tab, `\\` a literal backslash |
| `%` | **percent** (percent sign) | modulo; old-style formatting `"%s" % x` |
| `=` | **equals sign** | assignment — read it as "gets", not "equals" |
| `==` | **double equals** · "is equal to" | comparison |
| `!=` | **not equal to** · "bang equals" | comparison |
| `!` | **exclamation mark** (UK) · **exclamation point** (US) · spoken **"bang"** | only in `!=` and `{x!r}` — Python has no standalone `!` |
| `&` | **ampersand** | bitwise AND; set and dict-key intersection `a.keys() & b.keys()` |
| `\|` | **pipe** · **vertical bar** | bitwise OR; set union; type union `int \| None` |
| `^` | **caret** · also **hat**, **circumflex** | bitwise XOR. ⚠️ **not** a power — use `**` |
| `~` | **tilde** | bitwise NOT; in pandas and Polars, "not" |
| `@` | **at sign** · spoken **"at"** | decorator `@property`; matrix multiplication |
| `:` | **colon** | ends `if` / `for` / `while` / `def` / `class`; slices; dict `key: value` |
| `;` | **semicolon** | separates two statements on one line. Rare — avoid it |
| `,` | **comma** | separates items and arguments |
| `.` | **dot** · UK **full stop** · US **period** | attribute or method access `text.strip()`; decimal point |
| `_` | **underscore** | word separator in `snake_case`; "I do not need this value" |
| `#` | **hash** (UK) · **pound sign**, **number sign**, **octothorpe** (US) | starts a comment |
| `?` | **question mark** | not used in Python. It is the parameter placeholder in SQL |
| `$` | **dollar sign** | not used in Python. Common in shells and regular expressions |

### Quotes

| Symbol | English name | In Python |
|--------|--------------|-----------|
| `'` | **single quote** · **apostrophe** | a string: `'text'` |
| `"` | **double quote** | a string: `"text"` — identical in meaning to single |
| `'''` or 3 × `"` | **triple quote** | a multi-line string; a docstring |
| `` ` `` | **backtick** · **grave accent** | not used in Python. Markdown and shells use it |

### Multi-character operators — how to say them

| Symbol | Say it | Means |
|--------|--------|-------|
| `**` | "double star" / "to the power of" | exponent; `**kwargs` |
| `//` | "double slash" / "floor division" | integer division |
| `==` | "double equals" | is equal to |
| `!=` | "not equals" / "bang equals" | is not equal to |
| `<=` `>=` | "less than or equal to" | comparison |
| `+=` | "plus equals" | `x += 1` is short for `x = x + 1` |
| `->` | "arrow" | return type: `def f() -> int:` |
| `:=` | the **walrus** operator | assign inside an expression |
| `__init__` | "**dunder** init" | *d*ouble *under*score — a special method |
| `...` | "ellipsis" · in the shell, the **continuation prompt** | the `Ellipsis` object; also a `pass` placeholder |

### The three that catch people out

| | |
|---|---|
| `^` is **not** a power | `2 ^ 8` is `10`, not `256`. Use `2 ** 8` |
| `=` is **not** equality | `=` assigns, `==` compares |
| `\` is **not** division | `\` escapes, `/` divides |

---

## Abbreviations decoded

Python inherited a lot of short names from C. Here is what they stand for — and, first,
how to look up any name yourself without leaving the terminal.

### Find out yourself — three commands

```bash
>>> import math
>>> help(math.sqrt)          # a sentence explaining it. Press q to leave
Return the square root of x.

>>> math.sqrt.__doc__        # the same sentence, no pager
'Return the square root of x.'

>>> math.<Tab>               # lists every name in the module
>>> dir(math)                # the same, as a list
```

**`math.` then Tab is the fastest discovery tool in Python.** It shows what exists;
`help()` then says what each one does. No internet needed. `dir("")` lists every string
method; `dir([])` every list method.

### `math` — the maths module

| Name | Stands for | Does |
|------|-----------|------|
| `sqrt` | **sq**uare **r**oo**t** | `sqrt(9)` → `3.0` |
| `isqrt` | **i**nteger **sq**uare **r**oo**t** | `isqrt(10)` → `3` — whole part only |
| `cbrt` | **c**u**b**e **r**oo**t** | `cbrt(8)` → `2.0` |
| `fabs` | **f**loat **abs**olute value | always returns a float |
| `ceil` | **ceil**ing | rounds **up**: `ceil(2.1)` → `3` |
| `floor` | floor | rounds **down**: `floor(2.9)` → `2` |
| `trunc` | **trunc**ate | chops toward zero — same as `int()` |
| `exp` | **exp**onential | `e` to the power of x |
| `log` | **log**arithm | natural log; `log(x, base)` for another base |
| `log2` `log10` | **log**arithm base 2 / 10 | |
| `log1p` | **log** of **1** **p**lus x | accurate for tiny x |
| `expm1` | **exp** **m**inus **1** | accurate for tiny x |
| `fmod` | **f**loat **mod**ulo | like `%`, but C semantics for negatives |
| `modf` | **mod**ulus and **f**raction | `modf(3.5)` → `(0.5, 3.0)` |
| `hypot` | **hypot**enuse | `hypot(3, 4)` → `5.0` |
| `dist` | **dist**ance | Euclidean distance between two points |
| `gcd` | **g**reatest **c**ommon **d**ivisor | |
| `lcm` | **l**owest **c**ommon **m**ultiple | |
| `comb` | **comb**inations | choose k from n, order ignored |
| `perm` | **perm**utations | choose k from n, order matters |
| `prod` | **prod**uct | multiplies an iterable |
| `fsum` | **f**loat **sum** | accurate sum; avoids float drift |
| `isnan` | **is** **n**ot **a** **n**umber | `nan` is the "missing/invalid" float |
| `isinf` | **is** **inf**inite | |
| `isclose` | **is close** | float comparison with a tolerance built in |
| `copysign` | **copy** the **sign** | magnitude of x, sign of y |
| `degrees` `radians` | — | convert between angle units |
| `factorial` | — | `factorial(5)` → `120` (that is `5!`) |
| `pi` `e` `tau` `inf` `nan` | — | constants, not functions — no brackets |

### Built-in functions

| Name | Stands for | Does |
|------|-----------|------|
| `len` | **len**gth | number of items |
| `abs` | **abs**olute value | keeps the type: `abs(-5)` → `5` |
| `str` | **str**ing | text |
| `int` | **int**eger | whole number |
| `float` | **float**ing-point | decimal — "floating" point, it can move |
| `bool` | **bool**ean | after George Boole. `True` / `False` |
| `repr` | **repr**esentation | the developer view; `{x!r}` in an f-string |
| `dir` | **dir**ectory (of names) | what does this object have? |
| `vars` | **var**iable**s** | an object's attributes as a dict |
| `id` | **id**entity | the object's unique number |
| `ord` `chr` | **ord**inal / **char**acter | `ord("A")` → `65`, `chr(65)` → `"A"` |
| `bin` `hex` `oct` | **bin**ary / **hex**adecimal / **oct**al | base 2 / 16 / 8 as text |
| `pow` | **pow**er | same as `**` |
| `divmod` | **div**ide and **mod**ulo | `divmod(7, 2)` → `(3, 1)` — both at once |
| `iter` `next` | **iter**ator | step through something manually |
| `enumerate` | **enumerate** | pairs each item with its position |
| `eval` `exec` | **eval**uate / **exec**ute | run text as code. ⚠️ never on untrusted input |
| `isinstance` | **is** an **instance** of | type check |
| `getattr` `setattr` `hasattr` | get / set / has **attr**ibute | access an attribute by name |

> **`divmod` is underused.** `divmod(n, 10)` gives you the last digit *and* the rest in
> one call — exactly the digit-peeling loop from [Lesson 4](meeting-1/04-while-loops.md).

### `str` methods whose names mislead

| Name | Stands for | Watch out |
|------|-----------|-----------|
| `strip` | strip whitespace from **both** ends | not "delete all spaces" — inner spaces stay |
| `lstrip` `rstrip` | **l**eft / **r**ight strip | one end only |
| `ljust` `rjust` | **l**eft / **r**ight **just**ify | pads to a width |
| `zfill` | **z**ero **fill** | `"7".zfill(3)` → `"007"` — keeps leading zeros! |
| `casefold` | — | a more aggressive `.lower()`, for comparing |
| `partition` | — | splits into exactly **three** parts, once |
| `rsplit` | **r**ight **split** | splits from the end |
| `removeprefix` | — | 3.9+. Safer than slicing |
| `title` | — | `"Title Case"` |
| `expandtabs` | — | turns tabs into spaces |

### `isdigit` vs `isdecimal` vs `isnumeric` — they are not the same

This matters whenever you check text before converting it to a number:

| text | what it is | `isdecimal()` | `isdigit()` | `isnumeric()` | `float()` |
|------|-----------|---------------|-------------|---------------|-----------|
| `"5"` | ASCII five | True | True | True | `5.0` |
| `"٥"` | Arabic-Indic five | True | True | True | `5.0` |
| `"²"` | superscript two | **False** | **True** | True | **ValueError** |
| `"½"` | one half | False | False | **True** | **ValueError** |
| `"Ⅴ"` | Roman numeral five | False | False | **True** | **ValueError** |
| `"-5"` | minus five | False | False | False | `-5.0` |
| `"5.5"` | a decimal | False | False | False | `5.5` |
| `""` | empty | False | False | False | **ValueError** |

Read the `"²"` row carefully: **`isdigit()` says yes and `float()` refuses.** A check
built on `isdigit()` would pass and the conversion on the next line would crash. The last
three rows matter too — no `is*` method accepts a minus sign or a decimal point.

> **So do not pre-test text you are about to convert.** Try the conversion and catch the
> failure — `float()` is the only authority on what `float()` accepts:
> ```python
> try:
>     value = float(raw)
> except ValueError:
>     ...            # not a number
> ```
> `isdigit()` is fine for text that **stays** text — a 13-digit product code you never do
> arithmetic on. `isdecimal()` is the strictest of the three.

### `statistics`, `os.path`, `random`

| Name | Stands for |
|------|-----------|
| `mean` `median` `mode` | average / middle value / most common |
| `stdev` `pstdev` | **st**andard **dev**iation — **s**ample / **p**opulation |
| `variance` `pvariance` | sample / **p**opulation variance |
| `fmean` | **f**loat **mean** — faster |
| `abspath` | **abs**olute **path** |
| `basename` `dirname` | the filename / the folder part |
| `splitext` | **split** the **ext**ension: `("report", ".csv")` |
| `expanduser` | turns `~` into your home folder |
| `normpath` `realpath` | tidy the path / resolve every link |
| `randint` | **rand**om **int**eger — **both** ends included |
| `randrange` | like `range` — the end is **excluded** |
| `choice` `choices` `sample` | one item / k **with** repeats / k **without** repeats |
| `uniform` | a random float, **uniform**ly distributed |
| `gauss` | **Gauss**ian (normal) distribution |
| `shuffle` | reorders **in place**, returns `None` |

### Jargon you will meet in code

| Name | Stands for |
|------|-----------|
| `args` | **arg**ument**s** — `*args` collects extra positional ones |
| `kwargs` | **k**ey**w**ord **arg**ument**s** — `**kwargs` collects named ones |
| `__init__` | **init**ialise — the constructor. Say "**dunder** init" |
| `self` | this instance. Not a keyword — just the convention |
| `cls` | **cl**a**ss** — the convention in a `@classmethod` |
| `csv` | **c**omma-**s**eparated **v**alues |
| `tsv` | **t**ab-**s**eparated **v**alues |
| `json` | **J**ava**S**cript **O**bject **N**otation |
| `sql` | **S**tructured **Q**uery **L**anguage |
| `db` | **d**ata**b**ase |
| `env` / `venv` | **env**ironment / **v**irtual **env**ironment |
| `pip` | the package installer — "**p**ip **i**nstalls **p**ackages" |
| `regex` | **reg**ular **ex**pression — a pattern language |
| `utf-8` | **U**nicode **T**ransformation **F**ormat, 8-bit |
| `bom` | **b**yte **o**rder **m**ark — Excel's invisible CSV prefix |
| `ean` | **E**uropean **A**rticle **N**umber — the 13-digit barcode |
| `etl` | **E**xtract, **T**ransform, **L**oad |
| `eof` | **e**nd **o**f **f**ile — what Ctrl-D sends |
| `stdin` `stdout` `stderr` | **st**an**d**ard **in**put / **out**put / **err**or |
| `tmp` | **t**e**mp**orary |
| `idx` / `i` | **ind**e**x** |
| `num` / `n` | **num**ber |
| `char` | **char**acter |
| `src` / `dst` | **s**our**c**e / **d**e**st**ination |
| `fn` / `func` | **fun**ction |
| `obj` | **obj**ect |
| `param` | **param**eter |
| `attr` | **attr**ibute |
| `iter` | **iter**ate / **iter**ator |
| `lib` | **lib**rary |
| `impl` | **impl**ementation |
| `init` | **init**ialise |
| `config` / `cfg` | **config**uration |
| `dict` | **dict**ionary |
| `str` | **str**ing |
| `len` | **len**gth |
| `msg` | **mes**sa**g**e |
| `val` | **val**ue |
| `res` | **res**ult |
| `err` / `exc` | **err**or / **exc**eption |
| `repr` | **repr**esentation |
| `del` | **del**ete |
| `elif` | **el**se **if** |
| `def` | **def**ine |
| `lambda` | the Greek letter λ — a nameless function |
| `nan` | **n**ot **a** **n**umber |
| `inf` | **inf**inity |
| `mod` | **mod**ulo, or **mod**ule — context decides |

### Why so short?

Most of the maths names come from **C's standard library** from the 1970s, when short
identifiers were the norm. Python kept them so that anyone arriving from C, Excel or
MATLAB finds the same words: `sqrt`, `fabs`, `fmod`, `hypot` and `atan2` are all
unchanged C names, fifty years on.

That is also why `math.fabs` **and** the built-in `abs` both exist: `fabs` is the C one
and always returns a float; `abs` is Python's own and keeps the type.

```python
math.fabs(-5)   # 5.0   always a float
abs(-5)         # 5     stayed an int
```

> **Modern Python does not abbreviate.** New names are spelled out —
> `removeprefix`, `is_integer`, `total_ordering`. Write full words in your own code;
> read the short ones in everyone else's.

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

### Conditional expression (the "ternary") — one line, chooses a VALUE

```python
label = "even" if value % 2 == 0 else "odd"
print("ok" if height >= 165 else "too small")
text = f"{price:.2f}" if price is not None else "-"
```

|  | Chooses | Fits on one line? |
|---|---|---|
| `if` / `else` **statement** | which **code runs** | no — each clause needs its own line |
| `x if cond else y` **expression** | between two **values** | yes |

```python
height = 168; if height >= 165: print("ok") else: print("small")   # ✗ SyntaxError
height = 168; print("ok" if height >= 165 else "small")             # ✓
if height >= 165: print("ok")                                      # ✓ legal, but no else
```

A `;` joins only **simple** statements (`x = 1`, `print(x)`). `if`, `for`, `while`,
`def`, `class` own a block, so they must start their own line — see
[SETUP](../SETUP.md#one-liners-what-a--can-and-cannot-join).

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
