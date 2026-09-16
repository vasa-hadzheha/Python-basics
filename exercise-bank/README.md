# Exercise bank — and the translation map

⬅ [Course home](../README.md)

Every exercise in the course, with a reference solution. And, below, a complete map
from each original Ukrainian lab file to where it now lives in English — so you can
confirm nothing was lost.

**Run everything from the repository root:**
```bash
python3 exercise-bank/meeting-1/ex_1_03_triangle_area.py
```

---

## Contents

| Folder | Exercises | Covers |
|--------|-----------|--------|
| [`meeting-1/`](meeting-1/) | 14 solutions for [15 tasks](../course/meeting-1/exercises.md) | types, input, conditions, loops |
| [`meeting-2/`](meeting-2/) | 15 solutions for [16 tasks](../course/meeting-2/exercises.md) | lists, tables, functions, dicts |
| [`meeting-3/`](meeting-3/) | 12 solutions for [12 tasks](../course/meeting-3/exercises.md) | files, CSV, SQL, ETL, code review |
| [`appendix-classes/`](appendix-classes/) | 9 solutions for [9 tasks](../course/APPENDIX-classes.md) | classes (optional) |

**50 reference solutions.** Every one runs, and most end with an `assert` suite that
passes.

### How to use them

Open the **hint** in the exercise first. Only open the solution once you have something
working — then compare and ask *why* it differs from yours. The comparison is where the
learning is; two working answers to the same problem is normal.

Each solution's docstring says what the original archive version did, what was wrong
with it, and why the fix is a fix.

---

## Translation map — original → English

The original lab work is preserved under
[`archive/original-labs-ua/`](../archive/original-labs-ua/). Nothing was deleted.

### Lab 4 — `Math exercises (input, float)`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Варіант 2  Завд.1.py` | [Ex 1.3](../course/meeting-1/exercises.md#exercise-13--triangle-area) | triangle area (Heron) |
| `Варіант 2 Завд.2.py` | [Ex 1.4](../course/meeting-1/exercises.md#exercise-14--interval-membership) | interval membership |
| `Варіант 2 Зaвдання.3.py` | [Ex 1.5](../course/meeting-1/exercises.md#exercise-15--is-the-triangle-right-angled) | right-angled triangle |
| `Варіант 2 Завд.4.py` | [Ex 1.6](../course/meeting-1/exercises.md#exercise-16--piecewise-function) | piecewise function |

### Lab 5 — `Cycles (while, for, import math)`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Варіант 2 Завд.1.py` | [Ex 1.12](../course/meeting-1/exercises.md#exercise-112--sum-of-logarithms) | sum of logarithms |
| `Варіант 2 Завд.2.py` | [Ex 1.11](../course/meeting-1/exercises.md#exercise-111--count-the-zeros) | count the zeros |
| `Варіант 2 Завд.3.py` | [Ex 1.13](../course/meeting-1/exercises.md#exercise-113--series-to-a-given-precision) | series to a precision |
| `Варіант 2 Завд.4.py` + `4 2-ий спосіб.py` | [Ex 1.14](../course/meeting-1/exercises.md#exercise-114--recurrence-relation) | recurrence (both versions) |

### Lab 6 — `Arr`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Завд.1 Варіант2.py` | [Ex 2.2](../course/meeting-2/exercises.md#exercise-22--geometric-mean) | geometric mean |
| `Завд.2 Варіант2.py` | [Ex 2.3](../course/meeting-2/exercises.md#exercise-23--generate-then-filter) | generate then filter |
| `Завд.3 Варіант2.py` | [Ex 2.4](../course/meeting-2/exercises.md#exercise-24--vector--scalar) | vector × scalar |
| `Завд.4 Варіант2.py` | [Ex 2.5](../course/meeting-2/exercises.md#exercise-25--sort-descending) | sort descending |

### Lab 7 — `Random, Matrix`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Завд.1 Варіант2.py` | [Ex 2.6](../course/meeting-2/exercises.md#exercise-26--selective-matrix-sum) | selective matrix sum |
| `Завд.2 Варіант2.py` | [Ex 2.7](../course/meeting-2/exercises.md#exercise-27--replace-zeros-from-a-second-matrix) | replace zeros from B |
| `Завд.3 Варіант2.py` | [Ex 2.8](../course/meeting-2/exercises.md#exercise-28--matrix--vector) | matrix × vector |
| `Завд.4 Варіант2.py` | [Ex 2.9](../course/meeting-2/exercises.md#exercise-29--sort-alternate-rows) | sort alternate rows |
| `Завд.5 Варіант2.py` + `5 2-ий спосіб.py` | [Ex 2.10](../course/meeting-2/exercises.md#exercise-210--columns-without-a-zero) | columns without a zero |
| `Завд.6 Варіант2.py` | [Ex 2.11](../course/meeting-2/exercises.md#exercise-211--rows-by-even-positive-sum) | rows by even-positive sum |

### Lab 8 — `Functions (def)`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Завд.1 Варіант2.py` | [L8 worked example 1](../course/meeting-2/08-functions.md) | piecewise f(x, y) |
| `Завд.2 Варіант2.py` | [Ex 2.12](../course/meeting-2/exercises.md#exercise-212--left-rectangle-integral) | left-rectangle integral |
| `Завд.3 Варіант2.py` | [L8 worked example 2](../course/meeting-2/08-functions.md) | recurrence in a function |

### Lab 9 — `Lists, func`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Завд.1 Варіант 2.py` | [L9 worked example](../course/meeting-2/09-dicts-and-records.md) | warehouse stock |
| `Завд.2 Варіант 2.py` | [Ex 2.13](../course/meeting-2/exercises.md#exercise-213--the-cooks-directory) | cook's directory |

### Lab 11 — `Work-With-Files`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Завдання.1 Варіант 2.py` | [Ex 3.1](../course/meeting-3/exercises.md#exercise-31--largest-negative-number) | largest negative |
| `Завдання.2 Варіант 2.py` | [Ex 3.2](../course/meeting-3/exercises.md#exercise-32--replace-zeros-and-write-out) | replace zeros, write out |
| `Завдання.3 Варіант 2.py` | [Ex 3.3](../course/meeting-3/exercises.md#exercise-33--search-a-catalogue) | search a catalogue |

### `Checker` and `Aditional exercises`

| Original file | Now | Topic |
|---------------|-----|-------|
| `Checker/Гаджеги Василя.py` | [Ex 3.4](../course/meeting-3/exercises.md#exercise-34--pair-up-coordinates) | pair up coordinates |
| `new.py` | [Ex 1.7](../course/meeting-1/exercises.md#exercise-17--largest-of-three) | largest of three |
| `SUM завдання №5.py` | [Ex 1.8](../course/meeting-1/exercises.md#exercise-18--sum-of-the-first-17-even-numbers) | sum of 17 even numbers |
| `SUM завдання №8.py` | [Ex 1.9](../course/meeting-1/exercises.md#exercise-19--keep-adding-until-20) | keep adding until 20 |
| `завдання №9.py` | [Ex 1.10](../course/meeting-1/exercises.md#exercise-110--collect-three-even-numbers) | collect 3 even numbers |

### Labs 10 and 12, and the module work — classes

All in the [classes appendix](../course/APPENDIX-classes.md).

| Original file | Now | Topic |
|---------------|-----|-------|
| `Classes/Завд.1 Варіант 2 .py` | Ex A.1 | `Vector` |
| `Classes/Завд.2 Варіант 2.py` | Ex A.2 | `PhoneTariff` |
| `Class-Rectangle/Завд.1 Варіант 2.py` | Ex A.3 | `Rectangle` + arithmetic |
| `Classes (Matrix, Angel)/Завдання.1 Варіант 2.py` | Ex A.4 | `Rectangle` indexing |
| `Classes (Matrix, Angel)/Завдання.2 Варіант 2.py` | Ex A.5 | `Angle` |
| `Classes (Matrix, Angel)/Завдання.3 Варіант 2.py` | Ex A.6 | `Matrix` |
| `Class-Rectangle (properties)/Завдання.1 Варіант 2.py` | Ex A.7 | `Box(Rectangle)` |
| `Module work/Гаджеги Василя Завд.1.py` | Ex A.8 | `Circle` and `Cone` |
| `Class-Prism/Завдання.1 Варіант 2.py` | Ex A.9 | `Prism` (was a stub) |

---

## The bugs found in the original archive

Translating the labs meant running them, and running them found real bugs. Each one is
now a teaching example, because **these are the mistakes that recur in production code
and in AI-generated code**. They are the reason this course is reading-first.

| # | Where | The bug | Why it matters | Taught in |
|---|-------|---------|----------------|-----------|
| 1 | `new.py` | `if a > b > c` to find the largest of three | Chained comparison demands a total ordering, so it returns the wrong answer for `(1, 5, 3)`. Silent. | [Ex 1.7](../course/meeting-1/exercises.md#exercise-17--largest-of-three) |
| 2 | Lab 5.3 | No `\|x\| < 1` check on a Taylor series | For `x = 1.5` the terms grow, so the loop **never ends**. | [Ex 1.13](../course/meeting-1/exercises.md#exercise-113--series-to-a-given-precision) |
| 3 | Lab 5.2 | Digit loop with no `n = 0` case | Returns 0 zeros for the number 0. | [Ex 1.11](../course/meeting-1/exercises.md#exercise-111--count-the-zeros) |
| 4 | Lab 8.1 | `(x**2 + y**4) ** 1/2` for a square root | `**` binds tighter than `/`, so it computes `expr / 2`. No error, plausible number, wrong. | [L8](../course/meeting-2/08-functions.md) |
| 5 | Lab 8.2 | The "integral" function | Computes one rectangle spanning the whole interval, not `n` of them. | [Ex 2.12](../course/meeting-2/exercises.md#exercise-212--left-rectangle-integral) |
| 6 | Lab 8.3 | Returns `el`, the loop's last value | `UnboundLocalError` when the loop does not run; stale value otherwise. | [L8](../course/meeting-2/08-functions.md) |
| 7 | Lab 9.1 | `del_good` subtracts with no stock check | Shipping 999 of 6 leaves **−993 units** in stock. Silent. | [L9](../course/meeting-2/09-dicts-and-records.md) |
| 8 | Lab 9.1/9.2 | `input()` called inside the functions | Untestable, and it hangs forever in a scheduled job. | [L9](../course/meeting-2/09-dicts-and-records.md) |
| 9 | Lab 7.5 (2nd) | `[0 if 0 in column else 1 for column in a]` | `for column in a` iterates **rows**. The name says column; the code gives a row. | [L7](../course/meeting-2/07-nested-lists-and-matrices.md) |
| 10 | Lab 7.6 | Marks used rows with the sentinel `10000000` | Any row scoring above that silently breaks the ordering. | [Ex 2.11](../course/meeting-2/exercises.md#exercise-211--rows-by-even-positive-sum) |
| 11 | Lab 6.2 | `B = b` "to save a copy" | Not a copy — one list, two labels. | [L6](../course/meeting-2/06-lists.md) |
| 12 | Lab 11.1 | `max(s)` with no guard | `ValueError` on a file with no negative numbers. | [Ex 3.1](../course/meeting-3/exercises.md#exercise-31--largest-negative-number) |
| 13 | Lab 11.2 | `f.write(str(new_list))` | Writes `[5.0, 22.0, ...]` on one line. Nothing can read it back. | [Ex 3.2](../course/meeting-3/exercises.md#exercise-32--replace-zeros-and-write-out) |
| 14 | Lab 11.3 | `else` inside the search loop | Prints "nothing found" once per non-matching line. Author's comment: *"IT LOOPS THE MESSAGE"*. | [Ex 3.3](../course/meeting-3/exercises.md#exercise-33--search-a-catalogue) |
| 15 | Lab 11.1–2 | `row.split(' ')` | A double space yields `''`, and `float('')` raises. | [L10](../course/meeting-3/10-files.md) |
| 16 | `Checker` | `range(len(x))` indexing `y[i]` | `IndexError` whenever `y` is the shorter list. | [Ex 3.4](../course/meeting-3/exercises.md#exercise-34--pair-up-coordinates) |
| 17 | Lab 10.1 | `n = []` in the class body | Every `Vector` shares one list; results contaminate each other. | [Appendix](../course/APPENDIX-classes.md) |
| 18 | Lab 10.2 | `sum = 0` in the class body | Works by accident, via `+=` creating an instance attribute. | [Ex A.2](../course/APPENDIX-classes.md) |
| 19 | Lab 12.1 | `__eq__` returns `self.S() < other.S()` | Not symmetric, so it breaks `in`, `set`, dict keys and `.index()`. | [Appendix](../course/APPENDIX-classes.md) |
| 20 | Lab 12.1b | Bare `raise Exception` in `__getitem__` | Cannot be caught specifically. Marked *"Error — does not work"* in the original. | [Ex A.4](../course/APPENDIX-classes.md) |
| 21 | Lab 12.3 | `if el in self.matrix[i] == True:` | Python **chains** this, and a list is never `== True`, so it is **always False**. | [Ex A.6](../course/APPENDIX-classes.md) |
| 22 | Lab 12.3 | `__setitem__(self, row, col, value)` | Python passes one key; a 2-D subscript needs a tuple. | [Ex A.6](../course/APPENDIX-classes.md) |
| 23 | Module work | `super().__init__(self, radius)` | Shifts every argument; `self.radius` becomes a `Cone`. | [Ex A.8](../course/APPENDIX-classes.md) |
| 24 | Module work | `super().s()` where the method is `S_circle` | `AttributeError` on the first call. | [Ex A.8](../course/APPENDIX-classes.md) |
| 25 | Lab 12 (props) | `rec1.p` without brackets | Prints `<bound method ...>`. The original's comment says *"DOES NOT CALCULATE AREA OR PERIMETER!!!"* — this is why. | [Ex A.7](../course/APPENDIX-classes.md) |
| 26 | `Class-Prism` | The file ends mid-`def` | `SyntaxError` — it will not even import. | [Ex A.9](../course/APPENDIX-classes.md) |
| 27 | `Class-Prism` | `sides_len()` generates random sides per call | Two calls describe two different solids, so area and volume disagree. | [Ex A.9](../course/APPENDIX-classes.md) |

### What this list is actually for

Look at bugs 1, 4, 7, 9, 10, 11 and 19. **None of them raises an error.** Each one
produces a plausible-looking number that is wrong.

That is the whole argument for this course. A crash tells you there is a problem.
A wrong number does not — and the only defence is a person who can read the code and
notice. No amount of AI assistance replaces that, because the AI generates exactly
these same mistakes.

The original labs were good student work that passed their assessment. Finding these
bugs was not hard; it needed someone to run the code and ask *"what input breaks this?"*
That is a learnable skill, and it is what Lessons 8, 13 and 14 teach.
