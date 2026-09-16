"""Exercise A.4 - Rectangle with __getitem__, __setitem__, __delitem__.
Original: Lab 12, Task 1 (second part).

WHAT THE ORIGINAL DID WRONG: every one of its three methods ends with

    raise Exception("Некоректний елемент!!!")    #Error--does not work

and the author's own comment says it does not work. Two problems:
  1. a bare Exception cannot be caught specifically - a caller wanting to
     handle "bad index" has to catch everything, including real bugs
  2. it was never actually run, which is why the comment is there

The right exception for a bad subscript is IndexError (or KeyError for a
mapping). Then a caller can write "except IndexError:" and mean it.
"""


class Rectangle:
    """A rectangle whose sides can be read and written as rect[1], rect[2]."""

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def area(self):
        return self.a * self.b

    def __getitem__(self, key):
        """rect[1] is side a, rect[2] is side b."""
        if key == 1:
            return self.a
        if key == 2:
            return self.b
        # Early raise instead of an else: it reads better and the happy
        # path stays unindented.
        raise IndexError(f"a Rectangle has sides 1 and 2, not {key!r}")

    def __setitem__(self, key, value):
        if value < 0:
            raise ValueError("a side cannot be negative")
        if key == 1:
            self.a = float(value)
        elif key == 2:
            self.b = float(value)
        else:
            raise IndexError(f"a Rectangle has sides 1 and 2, not {key!r}")

    def __delitem__(self, key):
        """Deleting a side sets it to 0 - a rectangle always has two sides.

        The original used "del self.a", which removes the attribute
        entirely and makes every later method raise AttributeError. That
        leaves the object in a state its own class cannot handle, which is
        worse than refusing.
        """
        if key == 1:
            self.a = 0.0
        elif key == 2:
            self.b = 0.0
        else:
            raise IndexError(f"a Rectangle has sides 1 and 2, not {key!r}")

    def __len__(self):
        return 2  # a rectangle has two sides

    def __str__(self):
        return f"Rectangle({self.a:g} x {self.b:g})"


if __name__ == "__main__":
    rect = Rectangle(3, 7)
    print(f"{rect}   area {rect.area():g}")
    print(f"  rect[1] = {rect[1]:g}")
    print(f"  rect[2] = {rect[2]:g}")

    rect[2] = 10
    print(f"\nafter rect[2] = 10 -> {rect}   area {rect.area():g}")

    del rect[2]
    print(f"after del rect[2]  -> {rect}   area {rect.area():g}")

    print("\nThe errors the original could not raise:")
    for bad_key in (0, 3, "a"):
        try:
            rect[bad_key]
        except IndexError as error:
            print(f"  rect[{bad_key!r}] -> IndexError: {error}")

    try:
        rect[1] = -5
    except ValueError as error:
        print(f"  rect[1] = -5   -> ValueError: {error}")

    print("\nWhy IndexError and not a bare Exception:")
    print("  a caller can write 'except IndexError:' and handle just this,")
    print("  instead of swallowing every bug in the program too.")

    # __getitem__ starting at 1 means iteration would hit rect[0] first,
    # so this class is deliberately NOT iterable by that accident.
    try:
        list(rect)
        print("\n  (iteration worked - unexpected)")
    except IndexError:
        print("\n  Note: because indexing starts at 1, list(rect) raises -")
        print("  __getitem__ makes an object iterable only if it starts at 0.")

    # --- tests -------------------------------------------------------
    r = Rectangle(3, 7)
    assert r[1] == 3.0 and r[2] == 7.0
    assert len(r) == 2
    r[1] = 5
    assert r[1] == 5.0
    del r[1]
    assert r[1] == 0.0
    assert r.area() == 0.0, "the object is still usable after a delete"
    for bad in (0, 3, -1, "x", None):
        try:
            r[bad]
            raise AssertionError(f"{bad!r} should have raised")
        except IndexError:
            pass
    print("\nAll tests passed.")
