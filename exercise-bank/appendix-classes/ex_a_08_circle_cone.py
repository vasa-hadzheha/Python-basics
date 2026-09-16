"""Exercise A.8 - Circle and Cone: the module work, fixed.
Original: "Module work/Гаджеги Василя Завд.1.py" (TCircle and Cone).

The original has FOUR bugs, and all four would have been caught by running
the file once:

  1. super().__init__(self, radius)          - one argument too many
  2. super().s()                             - the parent's method is
                                               called S_circle, not s
  3. print(c3.repr())  vs  print(c5.repr)    - inconsistent brackets on a
                                               plain method
  4. __eq__ returns  self.s() < other.s()    - less-than, not equality;
                                               and s() does not exist

It also has a duplicated "elif arguments_count == 1:" branch that can
never be reached, because the first one already matched.
"""

import copy
import math


class Circle:
    """A circle, defined by its radius."""

    def __init__(self, radius=0.0):
        """Circle(), Circle(5), Circle(5.5) or Circle('5.5')."""
        if isinstance(radius, str):
            radius = radius.strip()
            if not radius:
                raise ValueError("radius string is empty")
            radius = float(radius)
        if not isinstance(radius, (int, float)):
            raise TypeError(f"radius must be a number, got {type(radius).__name__}")
        if radius < 0:
            raise ValueError("radius cannot be negative")
        self.radius = float(radius)

    @classmethod
    def from_circle(cls, other):
        """A copy constructor: Circle.from_circle(c)."""
        return cls(copy.deepcopy(other.radius))

    def area(self):
        """The area. The original called this S_circle and printed 'radius'."""
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return math.fabs(self.radius - other.radius) < 1e-9

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __hash__(self):
        return hash(self.radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        if isinstance(other, (int, float)):
            return Circle(self.radius + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(math.fabs(self.radius - other.radius))
        if isinstance(other, (int, float)):
            return Circle(math.fabs(self.radius - other))
        return NotImplemented

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Circle(self.radius * math.fabs(factor))

    def __str__(self):
        return f"Circle(r={self.radius:g})"

    def __repr__(self):
        return f"Circle({self.radius!r})"


class Cone(Circle):
    """A cone: a circular base plus a height."""

    def __init__(self, radius, height):
        super().__init__(radius)  # NOT super().__init__(self, radius)
        if height < 0:
            raise ValueError("height cannot be negative")
        self.height = float(height)

    def volume(self):
        # The parent's method is area(), and it needs brackets.
        return super().area() * self.height / 3

    def slant_height(self):
        return math.sqrt(self.radius**2 + self.height**2)

    def lateral_area(self):
        return math.pi * self.radius * self.slant_height()

    def __str__(self):
        return f"Cone(r={self.radius:g}, h={self.height:g})"


if __name__ == "__main__":
    c1 = Circle(60)
    c2 = Circle(90)

    print(f"{c1}")
    print(f"  area          {c1.area():>14.2f}")
    print(f"  circumference {c1.circumference():>14.2f}")

    print(f"\nc1 + c2  = {c1 + c2}")
    print(f"c2 - c1  = {c2 - c1}")
    print(f"c1 * 3   = {c1 * 3}")

    c3 = Circle.from_circle(c1)
    print(f"\nCircle.from_circle(c1) = {c3}")
    print(f"  equal to c1        : {c3 == c1}")
    print(f"  the same object    : {c3 is c1}")

    print(f"\nc1 == c2 -> {c1 == c2}   (and symmetrically: {c2 == c1})")
    print(f"c1 <  c2 -> {c1 < c2}")

    cone = Cone(30, 6)
    print(f"\n{cone}")
    print(f"  base area     {cone.area():>14.2f}   <- inherited")
    print(f"  volume        {cone.volume():>14.2f}")
    print(f"  slant height  {cone.slant_height():>14.2f}")
    print(f"  lateral area  {cone.lateral_area():>14.2f}")

    print("\n" + "=" * 62)
    print("  THE FOUR BUGS IN THE ORIGINAL")
    print("=" * 62)
    print("  1. super().__init__(self, radius) - self.radius became a Cone,")
    print("     so the next multiplication raised TypeError.")
    print("  2. super().s() - the parent method was named S_circle.")
    print("     AttributeError, on the very first call.")
    print("  3. c3.repr() in one place, c5.repr in another. One printed the")
    print("     value; the other printed '<bound method ...>'.")
    print("  4. __eq__ returned self.s() < other.s(): less-than, not equal,")
    print("     AND called a method that does not exist.")
    print()
    print("  Every one would have been caught by running the file once.")

    # --- tests -------------------------------------------------------
    assert abs(Circle(1).area() - math.pi) < 1e-12
    assert abs(Circle(1).circumference() - 2 * math.pi) < 1e-12
    assert Circle(5) == Circle(5.0) == Circle("5")
    assert (Circle(5) == Circle(6)) == (Circle(6) == Circle(5)), "must be symmetric"
    assert (Circle(1) == "not a circle") is False
    assert Circle(2) + Circle(3) == Circle(5)
    assert Circle(2) - Circle(5) == Circle(3), "subtraction uses absolute value"
    assert Circle(2) * -3 == Circle(6)
    assert Circle.from_circle(Circle(7)) == Circle(7)

    # A cone of radius r and height h has volume pi*r^2*h/3.
    cone = Cone(3, 9)
    assert abs(cone.volume() - (math.pi * 9 * 9 / 3)) < 1e-9
    assert abs(cone.slant_height() - math.sqrt(9 + 81)) < 1e-12
    assert isinstance(cone, Circle)

    for bad in (-1,):
        try:
            Circle(bad)
            raise AssertionError("a negative radius should have raised")
        except ValueError:
            pass
    try:
        Circle([1, 2])
        raise AssertionError("a list radius should have raised")
    except TypeError:
        pass
    print("\nAll tests passed.")
