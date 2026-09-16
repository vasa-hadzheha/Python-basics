# Glossary — every term, one sentence

⬅ [Course home](../README.md)

No jargon explained with more jargon. Where a term is taught in a lesson, the lesson
is linked.

---

## A

**accumulator** — a variable that starts empty and grows on each pass of a loop; start
at `0` for a sum or count, `1` for a product. [L4](meeting-1/04-while-loops.md)

**argument** — a value you pass *into* a function when calling it: the `5` in
`double(5)`. [L8](meeting-2/08-functions.md)

**assert** — a statement that does nothing when true and crashes when false; the
simplest form of test. [L8](meeting-2/08-functions.md)

**attribute** — a value stored on an object, reached with a dot: `rect.a`.
[Appendix](APPENDIX-classes.md)

## B

**BOM (byte order mark)** — invisible characters Excel puts at the start of a CSV;
read with `encoding="utf-8-sig"` to remove them, or your first column name will be
wrong in a way you cannot see. [L11](meeting-3/11-csv-and-excel.md)

**bool** — the type with exactly two values, `True` and `False`.
[L1](meeting-1/01-values-and-types.md)

**break** — leave the enclosing loop immediately. [L4](meeting-1/04-while-loops.md)

**built-in** — a function Python provides without an import: `len`, `sum`, `max`,
`print`, `sorted`. Do not name your own variables after them.

## C

**class** — a definition binding data to the operations that belong to it.
[Appendix](APPENDIX-classes.md)

**comment** — text after `#` that Python ignores and humans read.

**comprehension** — building a list (or dict) in one expression:
`[n*2 for n in items if n > 0]`. [L6](meeting-2/06-lists.md)

**commit** — in SQL, the instruction that makes your changes permanent; without it they
are discarded. [L12](meeting-3/12-sql-from-python.md)

**concatenate** — join two strings end to end with `+`.

**constraint** — a rule declared in a database schema (`NOT NULL`, `CHECK`,
`PRIMARY KEY`) that the database enforces for every program, forever.
[L12](meeting-3/12-sql-from-python.md)

**continue** — skip the rest of this pass and go back to the loop's condition.
[L4](meeting-1/04-while-loops.md)

**CSV** — comma-separated values; a text table. Often semicolon-separated in Europe.
[L11](meeting-3/11-csv-and-excel.md)

**cursor** — the object that runs SQL statements on a database connection.
[L12](meeting-3/12-sql-from-python.md)

## D

**delimiter** — the character separating fields in a text table: `,`, `;`, tab or `|`.
[L11](meeting-3/11-csv-and-excel.md)

**dict (dictionary)** — a collection mapping keys to values, looked up by name:
`row["price"]`. [L9](meeting-2/09-dicts-and-records.md)

**docstring** — the `"""text"""` directly under a `def`, stating what the function
promises. [L8](meeting-2/08-functions.md)

**dunder** — a method with double underscores, like `__init__` or `__eq__`, that hooks
into Python syntax. [Appendix](APPENDIX-classes.md)

## E

**edge case** — an input at the boundary of what your code expects: zero rows, an empty
string, a negative number. The place bugs live.

**encoding** — the agreement about which bytes mean which characters; `utf-8` is the
modern default and you should always state it. [L10](meeting-3/10-files.md)

**enumerate** — wraps a loop so you get the position as well as the item:
`for i, x in enumerate(items, start=1)`. [L5](meeting-1/05-for-loops.md)

**epsilon** — a small tolerance used to compare floats, because `==` on floats is
unreliable: `fabs(a - b) < 1e-9`. [L1](meeting-1/01-values-and-types.md)

**ETL** — Extract, Transform, Load; the shape of a data pipeline.
[L13](meeting-3/13-mini-etl-project.md)

**exception** — Python's way of reporting a failure, e.g. `ValueError`.
[L14](meeting-3/14-how-to-read-code.md)

## F

**f-string** — a string prefixed with `f` where `{expressions}` are substituted:
`f"total {x:.2f}"`. [L2](meeting-1/02-input-and-output.md)

**falsy** — a value Python treats as false without a comparison: `0`, `""`, `[]`, `{}`,
`None`. [L3](meeting-1/03-conditions.md)

**float** — a decimal number. Approximate, so never compare two with `==`.
[L1](meeting-1/01-values-and-types.md)

**for loop** — repeats once per item in a collection; cannot run forever.
[L5](meeting-1/05-for-loops.md)

**function** — a named block of code taking inputs and returning an output; the unit of
code review. [L8](meeting-2/08-functions.md)

## G

**global** — a variable defined outside any function. Read them sparingly; write them
essentially never. [L8](meeting-2/08-functions.md)

**GROUP BY** — the SQL clause that buckets rows so you can aggregate each bucket.
[L12](meeting-3/12-sql-from-python.md)

## H

**HAVING** — filters *groups* after `GROUP BY`; `WHERE` filters *rows* before it.
[L12](meeting-3/12-sql-from-python.md)

## I

**idempotent** — safe to run more than once with the same result; essential for any
scheduled job. [Ex 3.10](meeting-3/exercises.md#exercise-310--incremental-load-)

**immutable** — cannot be changed after creation: numbers, strings, tuples. The opposite
is **mutable**: lists, dicts.

**import** — loads a module so you can use it: `import math`.

**indentation** — the leading spaces that define a block in Python; part of the
language, not a style choice. Use 4 spaces. [L3](meeting-1/03-conditions.md)

**index** — an item's position in a list, counting from **0**.
[L6](meeting-2/06-lists.md)

**inheritance** — defining a class as a specialisation of another.
[Appendix](APPENDIX-classes.md)

**in place** — modifying an object directly rather than returning a new one;
`x.sort()` sorts in place, `sorted(x)` does not. [L6](meeting-2/06-lists.md)

**instance** — one particular object of a class. [Appendix](APPENDIX-classes.md)

**int** — a whole number. [L1](meeting-1/01-values-and-types.md)

## J

**JOIN** — combining two tables on a shared key. In Python, key one side by that field
first. [Ex 2.16](meeting-2/exercises.md#exercise-216--reconcile-two-price-lists-)

## K

**key** — the name you look a value up by in a dict, or the column that identifies a
row in a table. [L9](meeting-2/09-dicts-and-records.md)

**keyword argument** — passing an argument by name: `sorted(x, reverse=True)`.
[L8](meeting-2/08-functions.md)

## L

**lambda** — a one-line unnamed function, used mainly as `key=lambda r: r["price"]`.
Read it; rarely write it. [L9](meeting-2/09-dicts-and-records.md)

**lazy** — an operation that describes work without doing it until you ask for the
result, e.g. `pl.scan_csv`. [L10](meeting-3/10-files.md)

**list** — an ordered collection, indexed from 0. [L6](meeting-2/06-lists.md)

**list of dicts** — the standard Python shape for a table: one dict per row, keyed by
column name. [L9](meeting-2/09-dicts-and-records.md)

## M

**method** — a function belonging to an object: `"abc".upper()`, `my_list.append(1)`.

**modulo (`%`)** — the remainder of a division; `x % 2 == 0` tests even.
[L1](meeting-1/01-values-and-types.md)

**module** — a file of Python you can import.

**mutable default** — a `[]` or `{}` used as a default argument; created once and shared
between calls. Always a bug. [L8](meeting-2/08-functions.md)

## N

**None** — the value meaning "no value". A function with no `return` returns it.

## O

**off-by-one** — the error of being one position out; the commonest list bug.

**operator precedence** — which operation happens first. `**` beats `/`, so
`x ** 1/2` is `(x**1)/2`, not a square root. [L8](meeting-2/08-functions.md)

## P

**parameter** — the name in a function's definition; the **argument** is the value
passed in. [L8](meeting-2/08-functions.md)

**parameterised query** — SQL where values are passed separately as `?`, never
formatted into the text. The defence against SQL injection.
[L12](meeting-3/12-sql-from-python.md)

**Parquet** — a compressed columnar file format, much faster than CSV at scale.

**pipeline** — a script that moves data from source to destination, validating it on the
way. [L13](meeting-3/13-mini-etl-project.md)

**PRIMARY KEY** — the column whose value uniquely identifies a row; the database
enforces it. [L12](meeting-3/12-sql-from-python.md)

**property** — a method accessed *without* brackets, via `@property`.
[Appendix](APPENDIX-classes.md)

## R

**range** — generates whole numbers; `range(5)` gives 0–4, **excluding** 5.
[L5](meeting-1/05-for-loops.md)

**reconcile** — confirm the numbers add up: rows in = rows out + rows rejected.
[L13](meeting-3/13-mini-etl-project.md)

**reference** — two names pointing at the same object, which is why `b = a` does not
copy a list. [L6](meeting-2/06-lists.md)

**reject** — an input row that cannot be processed; it must be written somewhere with a
reason, never silently dropped. [L13](meeting-3/13-mini-etl-project.md)

**REPL** — the interactive `>>>` shell. The fastest way to check what something does.
[SETUP](../SETUP.md)

**return** — hands a value back to the caller. Not the same as `print`.
[L8](meeting-2/08-functions.md)

**rollback** — undo an uncommitted set of database changes.
[L12](meeting-3/12-sql-from-python.md)

## S

**schema** — the definition of a table's columns, types and constraints.
[L12](meeting-3/12-sql-from-python.md)

**scope** — where a name is visible; variables made inside a function die with it.
[L8](meeting-2/08-functions.md)

**seed** — a fixed starting value making "random" numbers repeatable, so a bug you found
is a bug you can find again. [L7](meeting-2/07-nested-lists-and-matrices.md)

**self** — the first parameter of a method; the instance it was called on.
[Appendix](APPENDIX-classes.md)

**sentinel** — a magic value standing in for "none" or "used", e.g. `10000000`. A bug
whenever real data could reach it.
[Ex 2.11](meeting-2/exercises.md#exercise-211--rows-by-even-positive-sum)

**set** — an unordered collection with no duplicates; `set(x)` de-duplicates anything.
[Ex 2.15](meeting-2/exercises.md#exercise-215--find-the-duplicates-)

**shadowing** — naming your variable after a built-in (`list`, `sum`, `max`) so the
original stops working. [L8](meeting-2/08-functions.md)

**short-circuit** — stopping evaluation once the answer is settled; `and` stops at the
first false, `any()` at the first true.

**slice** — a piece of a list: `x[1:4]`, with the end **excluded**.
[L6](meeting-2/06-lists.md)

**SQL injection** — an attack where input is treated as SQL code; prevented by
parameterised queries. [L12](meeting-3/12-sql-from-python.md)

**str** — text. [L1](meeting-1/01-values-and-types.md)

**strip** — remove whitespace from the ends of a string. Do it to every value you read
from a file. [L10](meeting-3/10-files.md)

## T

**traceback** — the report Python prints when it fails. Read it bottom-up.
[L14](meeting-3/14-how-to-read-code.md)

**transaction** — a group of database changes applied all together or not at all.
[L12](meeting-3/12-sql-from-python.md)

**transpose** — swap rows and columns: `zip(*table)`.
[L7](meeting-2/07-nested-lists-and-matrices.md)

**truthy** — any value Python treats as true in a condition; everything not **falsy**.
[L3](meeting-1/03-conditions.md)

**tuple** — like a list but immutable, written with `( )`. Returning several values
gives you one.

## U

**upsert** — insert a row, or update it if the key already exists; how you make a load
idempotent. [Ex 3.10](meeting-3/exercises.md#exercise-310--incremental-load-)

## V

**validate** — check data is usable before using it. The most valuable habit in this
course. [L13](meeting-3/13-mini-etl-project.md)

**variable** — a label pointing at a value. `=` means "gets", not "equals".
[L1](meeting-1/01-values-and-types.md)

**vectorised** — an operation applied to a whole column at once in compiled code, rather
than row by row in Python. Why `polars` is fast.
[L11](meeting-3/11-csv-and-excel.md)

**virtual environment (venv)** — a private folder of libraries for one project.
[SETUP](../SETUP.md)

## W

**WHERE** — filters *rows* in SQL, before grouping. Compare **HAVING**.
[L12](meeting-3/12-sql-from-python.md)

**while loop** — repeats while a condition holds; can run forever if you forget the
update. [L4](meeting-1/04-while-loops.md)

**whitespace** — spaces, tabs and newlines. Significant in Python indentation, and the
invisible cause of many comparison bugs.

**with** — opens a resource and guarantees it is closed, even on error.
[L10](meeting-3/10-files.md)
