"""Exercise A.3 - Rectangle with arithmetic and a CORRECT __eq__.
Original: Lab 12, Task 1.

THE BUG IN THE ORIGINAL:

    def __eq__(self, other):
        return self.S() < other.S()        # this is LESS THAN, not equal

== must be symmetric: if a == b then b == a. This version gives
    rect1 == rect2 -> False   (21 < 6)
    rect2 == rect1 -> True    (6 < 21)
which also breaks "in", .count(), .index(), set() and dict keys -
everything that uses == internally.

The original's __add__ also takes a NUMBER rather than a Rectangle, which
is a defensible choice but the opposite of what its sibling file does.
We support both, explicitly.
"""

import math
from functools import total_ordering


@total_ordering  # given __eq__ and __lt__, fills in <=, >, >=
class Rectangle:
    """A rectangle with sides a and b."""

    def __init__(self, a=0.0, b=None):
        """Rectangle() -> 0x0;  Rectangle(3) -> a square;  Rectangle(3, 7)."""
        if b is None:
            b = a  # one argument means a square
        if a < 0 or b < 0:
            raise ValueError("a side cannot be negative")
        self.a = float(a)
        self.b = float(b)

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    # --- comparison: keeps the promise the name makes -------------------
    def __eq__(self, other):
        """Two rectangles are equal when their sides match (in either order)."""
        if not isinstance(other, Rectangle):
            return NotImplemented  # NOT False - let Python try the other side
        eps = 1e-9
        return (
            math.fabs(self.a - other.a) < eps and math.fabs(self.b - other.b) < eps
        ) or (math.fabs(self.a - other.b) < eps and math.fabs(self.b - other.a) < eps)

    def __lt__(self, other):
        """Ordering is by AREA - a separate question from equality."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __hash__(self):
        # Defining __eq__ removes the default __hash__, so a Rectangle
        # could not go in a set. Restore it, consistently with __eq__.
        return hash(frozenset((self.a, self.b)))

    # --- arithmetic ----------------------------------------------------
    def __add__(self, other):
        """Rect + Rect adds the sides; Rect + number grows both sides."""
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b + other.b)
        if isinstance(other, (int, float)):
            return Rectangle(self.a + other, self.b + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(math.fabs(self.a - other.a), math.fabs(self.b - other.b))
        if isinstance(other, (int, float)):
            return Rectangle(math.fabs(self.a - other), math.fabs(self.b - other))
        return NotImplemented

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Rectangle(self.a * math.fabs(factor), self.b * math.fabs(factor))

    __rmul__ = __mul__  # so 2 * rect works as well as rect * 2

    def __str__(self):
        return f"Rectangle({self.a:g} x {self.b:g})"

    def __repr__(self):
        return f"Rectangle({self.a!r}, {self.b!r})"


if __name__ == "__main__":
    r1 = Rectangle(3, 7)
    r2 = Rectangle(2, 3)
    r3 = Rectangle(4)  # a square

    for r in (r1, r2, r3):
        print(f"{str(r):<24}area {r.area():>7.2f}   perimeter {r.perimeter():>7.2f}")

    print(f"\nr1 + r2  = {r1 + r2}")
    print(f"r1 + 6   = {r1 + 6}")
    print(f"r1 - r2  = {r1 - r2}")
    print(f"r1 * 2   = {r1 * 2}")
    print(f"2 * r1   = {2 * r1}")

    print("\n" + "=" * 58)
    print("  WHY THE ORIGINAL __eq__ WAS BROKEN")
    print("=" * 58)

    class BrokenRectangle(Rectangle):
        def __eq__(self, other):
            return self.area() < other.area()  # the archive's version

    b1, b2 = BrokenRectangle(3, 7), BrokenRectangle(2, 3)
    print(f"  b1 == b2 -> {b1 == b2}")
    print(f"  b2 == b1 -> {b2 == b1}   <- not symmetric, so it is not equality")

    print(f"\n  Correct version: r1 == r2 -> {r1 == r2}, r2 == r1 -> {r2 == r1}")
    print(f"  Rectangle(3, 7) == Rectangle(7, 3) -> {Rectangle(3, 7) == Rectangle(7, 3)}")
    print(f"  r1 > r2 (by area, via total_ordering) -> {r1 > r2}")

    # --- tests -------------------------------------------------------
    assert (r1 == r2) == (r2 == r1), "__eq__ must be symmetric"
    assert Rectangle(3, 7) == Rectangle(7, 3)
    assert Rectangle(3, 7) != Rectangle(3, 8)
    assert (Rectangle(1, 1) == "not a rectangle") is False
    assert r1 > r2 and r2 < r1
    assert sorted([r1, r2, r3], key=Rectangle.area)[0] == r2
    assert len({Rectangle(3, 7), Rectangle(7, 3)}) == 1, "equal objects hash alike"
    assert (r1 + 6) == Rectangle(9, 13)
    assert (r1 * -2) == Rectangle(6, 14), "a negative factor uses its absolute value"
    try:
        Rectangle(-1, 2)
        raise AssertionError("a negative side should have raised")
    except ValueError:
        pass
    print("\nAll tests passed.")
