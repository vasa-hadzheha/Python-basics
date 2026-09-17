# tools — verification scripts

⬅ [Course home](../README.md)

Two checks to run after editing anything in the course. Both exit non-zero on failure,
so they work in CI.

```bash
bash tools/run-all-scripts.sh      # runs all 77 scripts, feeding stdin where needed
python3 tools/check-links.py       # checks every relative markdown link and #anchor
python3 tools/check-tables.py      # checks every markdown table's column count
```

Run both from the **repository root**.

---

## `run-all-scripts.sh`

Executes every file in `examples/` and `exercise-bank/`, supplying keyboard input to
the ones that ask for it. Most scripts end with an `assert` suite, so a pass means the
logic was checked and not merely that the file parsed.

It deletes `out/` first, so the run starts from a clean slate — which is how you catch
a script that only works because a previous run left a file behind.

Expected output:

```
================================================
  passed: 77    failed: 0
================================================
```

**If you add a script, add a line for it here.** An example that does not run is a
broken promise to whoever is learning from it.

## `check-links.py`

Walks every `.md` file, extracts each relative link, and verifies both that the target
file exists and that any `#anchor` matches a real heading. It reproduces GitHub's
slug algorithm, including the detail that each space becomes its own dash — so
`## Exercise 2.4 — Vector × scalar` is `#exercise-24--vector--scalar`, with the
doubled dashes where the `—` and `×` were removed.

Expected output:

```
checked 449 relative links across 28 files
all relative links and anchors resolve
```

External `http(s)://` links are skipped — checking those needs the network and would
make the script flaky. Fenced and inline code is skipped too, so a link quoted as an
*example* (as [OBSIDIAN.md](../OBSIDIAN.md) does when showing GitHub's anchor format) is
not mistaken for navigation.

## `check-tables.py`

Counts the unescaped `|` characters in every row of every markdown table and reports any
table whose rows disagree. Two mistakes it catches, both of which render as a broken or
phantom column on GitHub while looking fine in a plain editor:

- a row missing its final cell, e.g. three cells under a four-column header
- a raw `|` inside a cell — even inside backticks. Write it as `\|`

Expected output:

```
checked 103 tables
every table has a consistent number of columns
```
