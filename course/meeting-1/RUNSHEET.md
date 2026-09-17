# Meeting 1 — Presenter runsheet

⬅ [Meeting 1](README.md) · [Presenter notes](../HOW-TO-TEACH.md) · [Course home](../../README.md)

**Print this.** It is the only page you need in your hand. Every keystroke is written
out, every output shown, every deliberate mistake marked.

> **The rule for the whole session:** your screen shows a **terminal**, nothing else.
> No lesson files, no cheatsheet, no slides. They read the lessons before and after;
> in the room they watch you type and then type themselves.

---

## Pre-flight — the evening before

- [ ] `git clone` the repo fresh and run `bash tools/run-all-scripts.sh` — expect `passed: 80`
- [ ] Terminal font at **18pt or bigger**. Test it from the back of the room
- [ ] Terminal colours: light background is easier to project than dark
- [ ] `python3 --version` works, and `cd` into the repo root
- [ ] A **second** terminal tab already open at the repo root (for the demos)
- [ ] Spare laptop, charged, with Python on it
- [ ] Have `SETUP.md` sent a week ago; expect a third not to have done it

**One week before, send:**

> Before Thursday, please follow `SETUP.md` in the repo and reply with the output of
> `python3 --version`. It takes 15 minutes. If it does not work, tell me now rather
> than on the day.

---

## 0:00 — Welcome (5 min) · no typing

Say roughly this, in your own words:

> "An AI can write you a function in four seconds. What it cannot do is tell you whether
> that function is right. Today is about reading Python — so that when something hands
> you fifty lines, you can say what it does and spot what is wrong with it.
>
> You will type everything yourselves. I will make mistakes on purpose. By the end you
> will read a short script out loud and say what it does."

Then: **"Everyone run `python3 --version` now."** Fix stragglers while the rest skim
[SETUP.md](../../SETUP.md). Hard stop at 0:15 — carry on and help the stuck ones during
the first exercise block.

---

## 0:15 — BLOCK 1 · Values and types (30 min)

### Live-code (8 min) — open a bare `python3`

| Type this | Say this |
|-----------|----------|
| `10 + 10` | "Numbers. No surprise." |
| `"10" + "10"` | **Pause before Enter.** "What comes out?" Wait for an answer. |
| | Now Enter → `'1010'`. "Same characters. Completely different answer." |
| `type("10")` | "`<class 'str'>` — it was never a number. Quotes make text." |
| `type(10)` | "`<class 'int'>`. `+` means *add* for numbers and *join* for text." |

**This is your hook.** Let the surprise sit for a second before moving on.

| Type this | Output | Say this |
|-----------|--------|----------|
| `7 / 2` | `3.5` | "Division always gives a decimal…" |
| `7 // 2` | `3` | "…unless you use two slashes. That is the whole part." |
| `7 % 2` | `1` | "And percent is the remainder. Seven divided by two is three, remainder one." |
| `407 % 10` | `7` | "The last digit." |
| `407 // 10` | `40` | "Everything except the last digit. Remember these two — we use them after the break." |
| `10 % 2 == 0` | `True` | "This is how you ask 'is it even'." |
| `7 % 2 == 0` | `False` | |
| `int(3.99)` | `3` | "Careful — `int` **chops**, it does not round." |
| `round(3.99)` | `4` | "That rounds." |

### The float moment (3 min)

| Type this | Output |
|-----------|--------|
| `0.1 + 0.2` | `0.30000000000000004` |
| `0.1 + 0.2 == 0.3` | `False` |

> "Not a bug. Computers store decimals in binary, and 0.1 has no exact binary form —
> same reason you cannot write one third exactly on paper. So **never compare two
> decimals with `==`**. There is a full explanation in the repo if you want it."

If someone asks *why* and you have the time, second tab:
`python3 examples/meeting-1/01_float_precision.py`

### 🔍 Predict (3 min) — on the whiteboard, not the screen

```
x = 5
x = x + x
x = x * 2
print(x)
```

Hands up for the answer. Someone will say 10. Walk the three lines one at a time:
5 → 10 → 20. **"`=` means *gets*, not *equals*."**

### They type (12 min)

> "Exercise 1.1 in `course/meeting-1/exercises.md`. Predict each line, write it down,
> then check in the shell. Ten lines. Go."

Walk the room. Do not sit down.

---

## 0:45 — BLOCK 2 · Input and output (20 min)

### Live-code (7 min) — **the planned mistake**

Create `demo.py` in front of them and type **exactly this**:

```python
age = input("How old are you? ")
print(age + 10)
```

Run it, type `30`:

```
TypeError: can only concatenate str (not "int") to str
```

> "Read the last line first. *That* is what went wrong. Now the line above says where."

Now change it to the **worse** version — and this is the important one:

```python
age = input("How old are you? ")
print(age * 3)
```

Type `30` → `303030`

> "**No error at all.** It just silently gave nonsense. That is the dangerous kind of
> bug, and it is the whole reason this course exists."

Then fix it:

```python
age = int(input("How old are you? "))
print(age * 3)          # 90
```

> "`input()` always hands you text. Always. You convert it yourself."

### f-strings (5 min)

| Type this | Output |
|-----------|--------|
| `name = "Bread"` | |
| `qty = 6` | |
| `price = 13.5` | |
| `f"{qty} x {name}"` | `'6 x Bread'` |
| `f"total {qty * price}"` | `'total 81.0'` |
| `f"total {qty * price:.2f}"` | `'total 81.00'` |

> "`:.2f` — two decimals. For money that is not optional. `81.0` in a report looks like
> a defect; `81.00` looks like a number."

### They type (8 min)

> "Exercise 1.2 — ask for two sides of a rectangle, print the area and perimeter to two
> decimals. The hint is there if you need it."

---

## 1:05 — BLOCK 3 · Conditions (30 min)

### Live-code (8 min) — **the indentation mistake**

```python
temperature = 15

if temperature > 20:
    print("Warm")
else:
    print("Cold")
```

Run it → `Cold`. Then **delete the colon** after `> 20` and re-run:

```
SyntaxError: expected ':'
```

> "It tells you exactly what it wants. Put it back."

Now the one that matters — add a second line inside the `if`, then **move it four spaces
left** while they watch:

```python
if temperature > 20:
    print("Warm")
    print("still inside")     # ← move this to column 0 and re-run
```

> "Indented, it only runs when it is warm. Not indented, it runs always. **In Python the
> spaces are the language**, not decoration."

Then chaining:

| Type this | Output |
|-----------|--------|
| `1 <= 1.5 <= 2` | `True` |
| `5 > 3 and 2 > 1` | `True` |
| `5 > 3 or 2 > 9` | `True` |
| `bool(0)`, `bool("")`, `bool([])` | `False` each time |

> "`and` is strict — one false ruins it. `or` is generous — one true saves it. And zero,
> empty text and an empty list all count as false, which is why you can write
> `if my_list:` to mean 'if it is not empty'."

### 🔍 Predict (4 min) — the highest-value slide of the meeting

Write **both** on the board, side by side:

```
x = 10                  x = 10
if x > 5:               if x > 5:
    print("A")              print("A")
if x > 8:               elif x > 8:
    print("B")              print("B")
else:                   else:
    print("C")              print("C")
```

Ask for both answers. **Left prints `A` then `B`. Right prints only `A`.**

> "Two separate `if`s both get tested. One `if`/`elif` chain stops at the first match.
> Identical-looking code, different behaviour. Spotting this is exactly the reading skill
> we are here for."

### They type (15 min)

> "Exercises 1.3 and 1.4 — the triangle area, and the interval check. 1.3 needs
> `import math`. Guard the bad input *before* you compute."

---

## 1:35 — ☕ BREAK (10 min) · a real break, leave the room

---

## 1:45 — BLOCK 4 · while loops (25 min)

### Live-code (4 min) — **the infinite loop**

Type it from scratch, deliberately leaving out the update:

```python
i = 1
while i <= 5:
    print(i)
```

Run it. Let `1` flood for two or three seconds. Then:

> **"Ctrl-C."**
>
> "Every programmer does this several times a week. It is not a failure — it is the fire
> extinguisher."

Then add the missing line and re-run:

```python
    i += 1
```

**Optional, if they are enjoying it** (second tab):

```bash
python3 examples/meeting-1/04_infinite_loops.py 4 slow
```

That is the float one — it counts *past* 1.0 and never stops. Ctrl-C and it prints its
own explanation.

### The trace table (8 min) — 🌟 **the most valuable thing you will do today**

Put this on screen and leave it there:

```python
n = 1020
zero_count = 0

while n > 0:
    last_digit = n % 10
    if last_digit == 0:
        zero_count += 1
    n = n // 10
```

Now go to the **whiteboard** and draw only the header:

```
 pass │   n   │ n % 10 │ zero? │ count │ n // 10
```

**Fill it by asking, never telling.** *"n is 1020. What is 1020 % 10?"* … *"So count
becomes?"* … *"And 1020 // 10?"*

The finished table:

| pass | `n` | `n % 10` | zero? | `count` | `n // 10` |
|------|-----|----------|-------|---------|-----------|
| 1 | 1020 | 0 | ✅ | 1 | 102 |
| 2 | 102 | 2 | — | 1 | 10 |
| 3 | 10 | 0 | ✅ | 2 | 1 |
| 4 | 1 | 1 | — | 2 | 0 |
| exit | 0 | `0 > 0` is **False** → stop | | **2** | |

**Two things to do explicitly:**

1. After each row, **draw an arrow** from the `n // 10` cell down to the `n` cell of the
   next row. *"The loop's output becomes its next input."* That arrow is the insight.
2. **Write the exit row out.** *"When does this stop?"* — `n` reaches 0, `0 > 0` is
   False. The question that kills infinite loops.

Close with:

> "This is not a teaching toy. When a loop misbehaves at work, four rows on a scrap of
> paper finds the bug faster than staring at the screen. I do this constantly."

### They type (13 min)

> "Exercise 1.11 — count the zeros in a number. Then test it with `0`, and with `-500`.
> Both will surprise you."

---

## 2:10 — BLOCK 5 · for loops (20 min)

### Live-code (5 min)

| Type this | Output | Say this |
|-----------|--------|----------|
| `list(range(5))` | `[0, 1, 2, 3, 4]` | "**Five numbers, and none of them is 5.** Settle it here." |
| `list(range(1, 6))` | `[1, 2, 3, 4, 5]` | "Give it a start and it shifts." |
| `list(range(0, 10, 2))` | `[0, 2, 4, 6, 8]` | "Third number is the step — the even ones." |
| `list(range(1, 10, 2))` | `[1, 3, 5, 7, 9]` | "Start at 1 and you get the odd ones." |

> "Whenever a `range` confuses you, wrap it in `list()` and look. Two seconds, no doubt."

Then the comparison that matters:

```python
for item in ["Bread", "Milk", "Salt"]:
    print(item)

for i, item in enumerate(["Bread", "Milk", "Salt"], start=1):
    print(i, item)
```

> "Loop over the items unless you actually need the position. And `for` cannot forget to
> advance — which is why it can never hang. **Default to `for`.**"

### They type (12 min)

> "Exercise 1.8 — the sum of the first 17 even numbers, once with `while` and once with
> `for`. Then tell me which you preferred and why."

---

## 2:30 — Close (5 min)

1. **The four verbs.** *"Store, decide, repeat, output. Everything you will ever read is
   those four, nested. That is genuinely all there is."*
2. **Show the cheatsheet — now, not earlier.** Open `course/CHEATSHEET.md`, scroll to the
   **traps table** at the bottom. *"You are not expected to memorise anything. This is
   the page. The traps at the end are what will bite you in the homework."*
3. **Homework:** exercises 1.9 to 1.15. *"1.15 is an invoice line with real validation —
   it is the one that looks like our actual work."*
4. **Set the expectation for next time:** *"Meeting 2 is collections — one variable
   holding a whole table. Read lessons 6 and 7 beforehand if you can."*

---

## If you fall behind

Cut in this order. **Never cut the bold ones.**

| Cut first | |
|-----------|---|
| 1 | Block 5's `enumerate` comparison |
| 2 | Block 3's truthiness (`bool(0)` etc.) |
| 3 | Block 1's `int()` vs `round()` |
| 4 | The optional `04_infinite_loops.py` demo |
| 5 | Shorten the last "they type" to 6 minutes and move it to homework |

| **Never cut** | Why |
|---|---|
| **`"10" + "10"`** | the hook for the whole course |
| **`age * 3` → `303030`** | the silent-wrong-answer moment |
| **moving a line 4 spaces** | indentation is the language |
| **Ctrl-C on the infinite loop** | errors are information, not failure |
| **the trace table** | the loop model everything else rests on |
| **`list(range(5))`** | settles the off-by-one forever |

---

## Questions you will get — short answers

| Question | Answer |
|----------|--------|
| "Why does counting start at 0?" | "An index is a distance from the start. The first item is 0 steps in. It also makes `range(len(x))` line up exactly." Show `list(range(3))` and move on. |
| "Why do I need `int()` around `input()`?" | "A keyboard produces characters. Python cannot know whether `5` is a number, a house number or a password — so it hands you the text and you decide." |
| "`while` or `for`?" | "`for` unless you genuinely cannot know how many passes. Fewer `while` loops means fewer hangs." |
| "Do I have to memorise this?" | "No. You have to *recognise* it. That is what the cheatsheet is for." |
| "My answer looks different from the solution." | "Good — that is normal. Which one handles empty input better?" |
| "Why not just let AI write it?" | "It can, and it will be wrong about your data in ways you cannot see. Meeting 3 has an example that returns an empty result after printing one error nobody reads." |
| "What is `:.2f` again?" | Cheatsheet, *Formatting* section. Do not explain it twice — point. |

---

## After the meeting — same day

Send one short message:

> Files from today: `examples/meeting-1/` has everything I typed.
> Homework: exercises 1.9–1.15 in `course/meeting-1/exercises.md` — **open the hint
> before the solution.**
> Stuck for more than 15 minutes? Message me, that is what I am for.

**Success test:** can they take a 10-line script they have never seen and say what it
does, line by line, without running it? If yes, Meeting 1 worked.
