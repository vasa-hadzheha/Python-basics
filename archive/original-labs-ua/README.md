# Original lab archive (Ukrainian)

⬅ [Course home](../../README.md) · [Translation map](../../exercise-bank/README.md#translation-map--original--english)

This is the **original, unmodified** Python lab work this course was built from,
written in Ukrainian. It is kept here so that:

1. nothing is lost,
2. you can compare any English exercise with what it came from,
3. the bugs documented in the course can be verified against the real source.

**Nothing here has been edited.** Only `.idea/` folders and Office `~$` lock files were
removed, and the files were moved from the repository root into this folder.

---

## Contents

| Folder | Lab | Topic | Translated to |
|--------|-----|-------|---------------|
| `Math exercises (input, float)` | 4 | input, float, `if`, `math` | [Meeting 1](../../course/meeting-1/exercises.md) |
| `Cycles (while, for, import math)` | 5 | `while`, `for`, series | [Meeting 1](../../course/meeting-1/exercises.md) |
| `Arr` | 6 | arrays / lists | [Meeting 2](../../course/meeting-2/exercises.md) |
| `Random, Matrix` | 7 | matrices, `random` | [Meeting 2](../../course/meeting-2/exercises.md) |
| `Functions (def)` | 8 | functions | [Meeting 2](../../course/meeting-2/exercises.md) |
| `Lists, func` | 9 | dicts as records | [Meeting 2](../../course/meeting-2/exercises.md) |
| `Classes` | 10 | classes | [Appendix](../../course/APPENDIX-classes.md) |
| `Work-With-Files` | 11 | file I/O | [Meeting 3](../../course/meeting-3/exercises.md) |
| `Classes (Matrix, Angel)` | 12 | dunder methods | [Appendix](../../course/APPENDIX-classes.md) |
| `Class-Rectangle` | 12 | operator overloading | [Appendix](../../course/APPENDIX-classes.md) |
| `Class-Rectangle (properties)` | 12 | `@property`, inheritance | [Appendix](../../course/APPENDIX-classes.md) |
| `Class-Prism` | 12 | *(unfinished — `SyntaxError`)* | [Ex A.9](../../course/APPENDIX-classes.md) |
| `Module work` | — | `TCircle`, `Cone` | [Ex A.8](../../course/APPENDIX-classes.md) |
| `Checker` | — | coordinate pairing | [Ex 3.4](../../course/meeting-3/exercises.md) |
| `Aditional exercises` | — | extra loop practice | [Meeting 1](../../course/meeting-1/exercises.md) |

The `.docx` files are the original lab write-ups. They contain the **task statements**,
which is where the English exercise wording came from. Their text was extracted and
translated; the screenshots they contain were not needed.

---

## A note on the code

This is student work, and it was good student work — it solved the problems set and it
passed. Several files carry the author's own honest comments where something did not
behave as expected:

- `# Error--не працює` ("Error — does not work")
- `# ЗАЦИКЛЮЄ ПОВІДОМЛЕННЯ` ("IT LOOPS THE MESSAGE")
- `# НЕ РАХУЄ ПЛОЩУ ТА ПЕРИМЕТР!!!` ("DOES NOT CALCULATE AREA OR PERIMETER!!!")
- `# Недороблено` ("unfinished")
- `# не розумію умову задачі` ("I do not understand the task condition")

Those comments are **more valuable than clean code would have been.** Each marks a
real confusion, and each one is now a worked explanation in the course — see the
[27 documented bugs](../../exercise-bank/README.md#the-bugs-found-in-the-original-archive).

The course is built on the premise that reading code critically is the skill worth
teaching. These files are where the examples came from, and they earn their place.

---

## Running these files

Most of them work, if you are patient with the prompts:

```bash
cd "archive/original-labs-ua/Math exercises (input, float)"
python3 "Варіант 2  Завд.1.py"
```

Two caveats:

- `Class-Prism/Завдання.1 Варіант 2.py` raises `SyntaxError` — the file ends in the
  middle of a `def`.
- `Work-With-Files` and `Checker` scripts expect their data files in the current
  directory, so `cd` into the folder first.

The English versions in [`exercise-bank/`](../../exercise-bank/) all run from the
repository root and are the ones to use for learning.
