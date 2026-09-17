"""Lesson 4 - five infinite loops, on purpose.

FOR LIVE DEMO. Pick one, watch it run away, press Ctrl-C, read the fix.

    python3 examples/meeting-1/04_infinite_loops.py        # menu
    python3 examples/meeting-1/04_infinite_loops.py 1      # straight to one
    python3 examples/meeting-1/04_infinite_loops.py 1 slow # 0.3s per line

Ctrl-C is how you stop a runaway program. Every programmer does this
several times a week. It is not a failure - it is the fire extinguisher.
"""

import sys
import time

SLOW = 0.3  # seconds per line when "slow" is passed
WIDTH = 68

DEMOS = {
    "1": {
        "title": "The forgotten update",
        "symptom": "floods the screen with the SAME number",
        "code": """i = 1
while i <= 5:
    print(i)
    # <-- nothing changes i, so the condition is true forever""",
        "fix": """i = 1
while i <= 5:
    print(i)
    i += 1        # <-- THE MISSING LINE""",
        "lesson": "Write the update line FIRST, before you forget it.",
    },
    "2": {
        "title": "The update points the wrong way",
        "symptom": "counts UP forever, away from the condition",
        "code": """n = 10
while n > 0:
    print(n)
    n += 1        # the line exists - but it GROWS n""",
        "fix": """n = 10
while n > 0:
    print(n)
    n -= 1        # shrink towards 0, which is what the condition wants""",
        "lesson": "Match the direction of the update to the condition.",
    },
    "3": {
        "title": "continue before the update",
        "symptom": "prints 0, 1 ... then SILENCE. A frozen cursor.",
        "code": """i = 0
while i < 5:
    if i == 2:
        continue      # jumps back with i STILL 2, forever
    print(i)
    i += 1""",
        "fix": """for i in range(5):    # "for" cannot forget to advance
    if i == 2:
        continue
    print(i)""",
        "lesson": "A silent hang is still a runaway loop. Ctrl-C it.",
    },
    "4": {
        "title": "A float never lands exactly on the target",
        "symptom": "counts past 1.0 and keeps going forever",
        "code": """x = 0.0
while x != 1.0:       # it STEPS OVER 1.0 and never comes back
    print(round(x, 2))
    x += 0.1""",
        "fix": """for step in range(10):    # count in INTEGERS
    x = step * 0.1
    print(round(x, 2))

# or, if you must loop on the float, use a tolerance:
#     while abs(x - 1.0) > 1e-9:""",
        "lesson": "Never use == or != on a float in a loop condition.",
    },
    "5": {
        "title": "The body changes the wrong variable",
        "symptom": "counts up forever; the condition's variable never moves",
        "code": """total = 0
count = 0
while total < 20:     # watches "total"
    count += 1        # but changes "count"
    print(count)""",
        "fix": """total = 0
count = 0
while total < 20:
    total += 3        # change the variable the CONDITION reads
    count += 1
    print(f"total={total} after {count} steps")""",
        "lesson": "Check that the body touches the condition's variable.",
    },
}


def frame(text):
    print("=" * WIDTH)
    print(f"  {text}")
    print("=" * WIDTH)


def show_menu():
    frame("FIVE INFINITE LOOPS")
    print("  Each one runs forever. Press Ctrl-C to stop it.\n")
    for key, demo in DEMOS.items():
        print(f"  {key}. {demo['title']}")
        print(f"     {demo['symptom']}\n")
    print("  Add 'slow' to watch it scroll:  ... 1 slow")
    print("=" * WIDTH)


def run(key, slow):
    demo = DEMOS[key]
    frame(f"{key}. {demo['title'].upper()}")
    print(demo["code"])
    print("-" * WIDTH)
    print(f"  Expect: {demo['symptom']}")
    print("  Press Ctrl-C when you have seen enough.")
    print("-" * WIDTH)
    time.sleep(1.5 if not slow else 2.5)

    delay = SLOW if slow else 0

    try:
        # Each branch is the real broken loop, written out exactly as shown.
        if key == "1":
            i = 1
            while i <= 5:
                print(i)
                time.sleep(delay)

        elif key == "2":
            n = 10
            while n > 0:
                print(n)
                n += 1
                time.sleep(delay)

        elif key == "3":
            print("(watch it stop printing after 0 and 1 - that is the hang)")
            i = 0
            while i < 5:
                if i == 2:
                    time.sleep(delay)
                    continue
                print(i)
                i += 1
                time.sleep(delay)

        elif key == "4":
            x = 0.0
            while x != 1.0:
                print(round(x, 2))
                x += 0.1
                time.sleep(delay)

        elif key == "5":
            total = 0
            count = 0
            while total < 20:
                count += 1
                print(count)
                time.sleep(delay)

    except KeyboardInterrupt:
        # Ctrl-C raises KeyboardInterrupt. Catching it lets us end tidily
        # and show the fix, instead of dumping a traceback.
        print("\n")
        frame("Ctrl-C - you stopped it. That is the right reflex.")
        print("  THE FIX")
        print("-" * WIDTH)
        print(demo["fix"])
        print("-" * WIDTH)
        print(f"  Lesson: {demo['lesson']}")

        if key == "4":
            print()
            print("  WHY it steps over 1.0 - add 0.1 ten times and look:")
            x = 0.0
            for step in range(12):
                marker = "  <-- so close, but not 1.0" if step == 10 else ""
                print(f"    after {step:>2} additions: {x!r}{marker}")
                x += 0.1
            print("  0.9999999999999999 != 1.0, so the loop carries on past it.")
            print("  See examples/meeting-1/01_float_precision.py for why.")

        print()
        print("  Ask this of every loop you write:")
        print("      >>> What input makes this never stop? <<<")
        print("=" * WIDTH)


def main():
    args = [a.lower() for a in sys.argv[1:]]
    slow = "slow" in args
    choice = next((a for a in args if a in DEMOS), None)

    if choice is None:
        show_menu()
        choice = input("\nWhich one? (1-5, or Enter to quit) ").strip()
        if choice not in DEMOS:
            print("Nothing selected. Bye.")
            return

    run(choice, slow)


if __name__ == "__main__":
    main()
