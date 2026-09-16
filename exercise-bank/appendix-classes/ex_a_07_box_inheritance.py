"""Exercise A.7 - Box(Rectangle): volume by inheritance.
Original: Lab 12 / Class-Rectangle (properties), the Paralelepiped class.

WHAT THE ORIGINAL DID WRONG:
  * its parent had a @property called "repr" and the code wrote rec3.repr
    inside print(), which printed the tuple - but its siblings wrote
    circle.repr without brackets on a plain METHOD, printing
    "<bound method ...>". The comment "DOES NOT CALCULATE AREA OR
    PERIMETER!!!" next to "rec1.p" is exactly this: p is a method, and
    rec1.p without brackets never calls it.
  * super().s() where the parent's method was named differently

RULE: @property -> no brackets. Plain method -> brackets. If you ever see
"<bound method ...>" in your output, you forgot the brackets.
"""


class Rectangle:
    """A rectangle with sides a and b."""

    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("a side cannot be negative")
        self.a = float(a)
        self.b = float(b)

    def area(self):
        """A METHOD - call it with brackets: rect.area()"""
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def sides(self):
        """A PROPERTY - access it without brackets: rect.sides"""
        return (self.a, self.b)

    def __str__(self):
        return f"Rectangle({self.a:g} x {self.b:g})"


class Box(Rectangle):
    """A rectangular box: a Rectangle plus a height."""

    def __init__(self, a, b, height):
        # super() ALREADY knows the instance. Never pass self.
        #   super().__init__(self, a, b)   <- one argument too many
        super().__init__(a, b)
        if height < 0:
            raise ValueError("height cannot be negative")
        self.height = float(height)

    def volume(self):
        # Reuse the inherited method - by its real name, with brackets.
        return self.area() * self.height

    def surface_area(self):
        return 2 * (self.a * self.b + self.a * self.height + self.b * self.height)

    def __str__(self):
        return f"Box({self.a:g} x {self.b:g} x {self.height:g})"


if __name__ == "__main__":
    rect = Rectangle(3, 4)
    box = Box(3, 4, 5)

    print(f"{rect}")
    print(f"  area        {rect.area():>8.2f}      <- method, WITH brackets")
    print(f"  perimeter   {rect.perimeter():>8.2f}")
    print(f"  sides       {rect.sides}          <- property, NO brackets")

    print(f"\n{box}")
    print(f"  area        {box.area():>8.2f}      <- inherited from Rectangle")
    print(f"  volume      {box.volume():>8.2f}      <- its own")
    print(f"  surface     {box.surface_area():>8.2f}")

    print(f"\nisinstance(box, Rectangle) -> {isinstance(box, Rectangle)}")

    print("\n" + "=" * 62)
    print("  BRACKETS: THE BUG THE ARCHIVE COMMENTED ON")
    print("=" * 62)
    print(f"  rect.area()  -> {rect.area()}       correct")
    print(f"  rect.area    -> {rect.area}")
    print("                  ^ that is the METHOD OBJECT, not the area.")
    print("  The archive's comment 'DOES NOT CALCULATE AREA OR PERIMETER!!!'")
    print("  next to 'rec1.p' is exactly this.")
    print()
    try:
        rect.sides()
    except TypeError as error:
        print(f"  rect.sides() -> TypeError: {error}")
        print("                  ^ a property must NOT have brackets.")

    print("\n" + "=" * 62)
    print("  super().__init__(self, ...) - one argument too many")
    print("=" * 62)

    class BrokenBox(Rectangle):
        def __init__(self, a, b, height):
            super().__init__(self, a)  # the archive's mistake
            self.height = height

    try:
        broken = BrokenBox(3, 4, 5)
        print(f"  It constructed, but self.a is now: {type(broken.a).__name__}")
        print(f"  and area() gives: {broken.area()}")
    except (TypeError, ValueError) as error:
        print(f"  {type(error).__name__}: {error}")
    print("  super() already knows the instance. Never pass self to it.")

    # --- tests -------------------------------------------------------
    assert Rectangle(3, 4).area() == 12
    assert Box(3, 4, 5).volume() == 60
    assert Box(3, 4, 5).area() == 12, "the inherited method must still work"
    assert Box(2, 2, 2).surface_area() == 24
    assert isinstance(Box(1, 1, 1), Rectangle)
    assert Rectangle(3, 4).sides == (3.0, 4.0)
    try:
        Box(1, 1, -1)
        raise AssertionError("a negative height should have raised")
    except ValueError:
        pass
    print("\nAll tests passed.")
