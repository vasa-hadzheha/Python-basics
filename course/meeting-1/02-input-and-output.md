# Lesson 2 — Input and output

⬅ [Previous: Values and types](01-values-and-types.md) · [Meeting 1](README.md) · ➡ [Next: Conditions](03-conditions.md)

---

## Why you care

A program that cannot take data in and cannot report results out is a program nobody
can use. And there is one specific fact about `input()` that causes more beginner bugs
than anything else in Python. Let us deal with it immediately.

---

## `input()` always gives you text. Always.

```mermaid
flowchart LR
    U["You type<br/>42"] --> I["input()"]
    I --> S["the string '42'<br/><i>always a str,<br/>never a number</i>"]
    S --> C["int() or float()"]
    C --> N["the number 42<br/><i>now you can do maths</i>"]
```

```python
age = input("How old are you? ")
print(type(age))            # <class 'str'>  ← even if you typed 30
print(age + 10)             # 💥 TypeError
```

The fix is to convert at the moment you read:

```python
age = int(input("How old are you? "))       # int() wraps input()
print(age + 10)                             # ✓ works
```

Read that nesting from the **inside out**, which is how all nested calls are read:

1. `input("How old are you? ")` — print the prompt, wait, hand back what was typed as text
2. `int(...)` — turn that text into a whole number
3. `age = ...` — label the result `age`

| You need | Write |
|----------|-------|
| a whole number | `n = int(input("n = "))` |
| a decimal number | `x = float(input("x = "))` |
| text | `name = input("name: ")` — no conversion needed |

> **Rule of thumb:** counts and indexes → `int()`. Measurements, prices, coordinates → `float()`.
> The original lab archive follows exactly this: `float(input(...))` for side lengths and
> coordinates, `int(input(...))` for "how many elements".

---

## `print()` — four ways, one recommendation

```python
name = "Bread"
qty = 6
price = 13.5
```

### 1. Commas — quick and fine for debugging

```python
print("Product:", name, "Qty:", qty)
# Product: Bread Qty: 6
```

`print` inserts a space between comma-separated items automatically.

### 2. f-strings — **use this one**

Put an `f` before the quote, then write `{variable}` inside the text:

```python
print(f"Product: {name}, quantity: {qty}, price: {price}")
# Product: Bread, quantity: 6, price: 13.5
```

f-strings can hold any expression, and they can format numbers:

```python
print(f"Total: {qty * price:.2f} EUR")     # Total: 81.00 EUR
print(f"{qty} x {name} @ {price:.2f}")     # 6 x Bread @ 13.50
```

`:.2f` means *"show as a decimal with exactly 2 places"*. For money this is not optional —
`81.0` in a report looks like an error, `81.00` looks like a number.

### 3. `.format()` — you will see it in older code

```python
print("Product: {0}, qty: {1}".format(name, qty))
```

This is what the whole original lab archive uses, and what most pre-2017 Python code and
plenty of AI-generated code uses. **You must be able to read it** — `{0}` is the first
argument, `{1}` the second — but write f-strings in new code.

### 4. `%` — very old, read-only

```python
print("Product: %s, qty: %d" % (name, qty))
```

You do not need to write this. Recognise it and move on.

---

## Formatting numbers — the bits that matter for reports

```python
value = 1234.5678

print(f"{value:.2f}")       # 1234.57      2 decimal places
print(f"{value:.0f}")       # 1235         no decimals, rounded
print(f"{value:10.2f}")     #    1234.57   width 10, right-aligned
print(f"{value:,.2f}")      # 1,234.57     thousands separator
```

Width control is how you produce a readable table in a terminal — we build a full one in
[Lesson 7](../meeting-2/07-nested-lists-and-matrices.md):

```python
print(f"{'Product':<12}{'Qty':>5}{'Price':>10}")
print(f"{'Bread':<12}{6:>5}{13.5:>10.2f}")
```

```
Product       Qty     Price
Bread           6     13.50
```

| Code | Meaning |
|------|---------|
| `:<12` | left-align in 12 characters |
| `:>5` | right-align in 5 characters |
| `:^9` | centre in 9 characters |
| `:>10.2f` | right-align in 10, 2 decimals — **numbers always right-align** |

> **⚠️ The number before the dot is width; after the dot is decimals.**
> `f"{0.1:20f}"` asks for 20 *characters* and gives you the default 6 decimals —
> `'            0.100000'`. To see 20 decimals you need the dot: `f"{0.1:.20f}"`.
> This trips people up the moment they try to inspect a float, and it is why the
> rounding error in [Lesson 1's float box](01-values-and-types.md#the-float-box--read-this-once-remember-it-forever)
> stays invisible.

---

## Worked example — a piecewise function

Task 4 from the original Lab 4: compute

```
y = ln|x| − n    if x ≤ n
y = cos(x·n)     if x > n
```

```python
import math

x = float(input("Enter x: "))          # float: could be 2.5
n = float(input("Enter n: "))

if x <= n:
    y = math.log(math.fabs(x)) - n     # math.fabs = absolute value
else:                                  # log of a negative number is an error,
    y = math.cos(x * n)                # so fabs protects us

print(f"y = {y:.6f}")
```

```
Enter x: 2
Enter n: 5
y = -4.306853
```

Note **why** `math.fabs` is there: `math.log(-3)` raises `ValueError`. Wrapping the
argument in `fabs` makes the domain safe. That is defensive programming, and spotting it
is the kind of thing a code review should catch.

▶ Run it: `python3 examples/meeting-1/02_piecewise.py`

---

## 🔍 Read this code

**(a)** The user types `5`. What is printed?
```python
n = input("n = ")
print(n * 3)
```

**(b)** The user types `5`. What is printed?
```python
n = int(input("n = "))
print(n * 3)
```

**(c)**
```python
total = 7
count = 2
print(f"Average: {total / count}")
print(f"Average: {total / count:.1f}")
```

<details>
<summary><b>Answers</b></summary>

**(a)** `555`. No `int()`, so `n` is the string `"5"`, and `"5" * 3` repeats the text.
This is the single most common beginner bug in Python, and it never raises an error —
it just silently gives you nonsense. That is what makes it dangerous.

**(b)** `15`. With `int()` you get real multiplication.

**(c)**
```
Average: 3.5
Average: 3.5
```
Both print `3.5` — but for a different reason. The first prints the full float; the second
formats it to one decimal. Change `total` to `22` and the difference shows:
`11.0` vs `11.0`… change `count` to `3` and you get `7.333333333333333` vs `7.3`.
**In any report, always pin the decimals.**

</details>

---

## Traps

| Trap | Symptom | Fix |
|------|---------|-----|
| forgot `int()`/`float()` | `"5" * 3 == "555"`, or `TypeError` on `+` | convert at read time |
| `int(input())` but user typed `3.5` | `ValueError: invalid literal for int()` | use `float()` when decimals are possible |
| forgot the `f` prefix | prints the literal text `{name}` | `f"...{name}..."` |
| prompt with no trailing space | `Enter x:5` — ugly | `input("Enter x: ")` — note the space |
| using `input()` in a script run by a scheduler | it hangs forever waiting | read from a file or arguments instead |

That last one is worth dwelling on. `input()` is excellent for *learning* and for small
tools a human runs by hand. It is the **wrong** way to feed a real pipeline, because an
automated job has no human to type. In Meeting 3 we replace `input()` with
[reading files](../meeting-3/10-files.md), which is how production code gets its data.

---

## Recap

- `input()` returns a **string**, always. Wrap it: `int(input(...))` / `float(input(...))`.
- Read nested calls inside-out.
- Write f-strings: `f"text {value}"`. Read `.format()` — the old labs are full of it.
- `:.2f` for money, `:<12` / `:>8` for aligned columns.
- `input()` is for humans at a keyboard, not for automated jobs.

➡ [Next: Conditions](03-conditions.md)
