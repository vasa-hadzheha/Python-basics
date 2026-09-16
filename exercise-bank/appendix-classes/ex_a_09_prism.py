"""Exercise A.9 - Prism: finish the unfinished class.
Original: "Class-Prism/Завдання.1 Варіант 2.py"

THE ORIGINAL IS A STUB. It ends mid-file:

    def sides_len(self):
        sides = [random.randint(3, 20) for i in range(self.count_sides)]
        return sides

    def S(self):
        <nothing - the file just stops>

which is a SyntaxError: a def with no body will not even import.

There is also a design problem worth naming. sides_len() GENERATES RANDOM
sides every time it is called, so two calls give two different prisms.
Area and volume computed from separate calls would not agree with each
other. Random data belongs in a constructor or a factory, never in a
getter.

This version takes the side lengths as data, and offers a separate
classmethod for the random case.
"""

import math
import random


class RegularPrism:
    """A prism whose base is a regular polygon with n equal sides."""

    def __init__(self, side_count, side_length, height):
        if side_count < 3:
            raise ValueError("a polygon needs at least 3 sides")
        if side_length <= 0 or height <= 0:
            raise ValueError("side length and height must be positive")
        self.side_count = int(side_count)
        self.side_length = float(side_length)
        self.height = float(height)

    @classmethod
    def random(cls, side_count, height, seed=None):
        """A prism with a random side length - generated ONCE, at creation.

        This is where randomness belongs. The original generated new
        random sides on every call to sides_len(), so no two computations
        described the same solid.
        """
        if seed is not None:
            random.seed(seed)
        return cls(side_count, random.randint(3, 20), height)

    # --- geometry ------------------------------------------------------
    def base_perimeter(self):
        return self.side_count * self.side_length

    def base_area(self):
        """Area of a regular n-gon: (n * s^2) / (4 * tan(pi/n))."""
        return (self.side_count * self.side_length**2) / (
            4 * math.tan(math.pi / self.side_count)
        )

    def lateral_area(self):
        """The sides: perimeter x height."""
        return self.base_perimeter() * self.height

    def total_area(self):
        """Both bases plus the sides."""
        return 2 * self.base_area() + self.lateral_area()

    def volume(self):
        return self.base_area() * self.height

    def summary(self):
        """A dict, so the caller chooses what to do with it."""
        return {
            "sides": self.side_count,
            "side_length": self.side_length,
            "height": self.height,
            "base_perimeter": round(self.base_perimeter(), 4),
            "base_area": round(self.base_area(), 4),
            "lateral_area": round(self.lateral_area(), 4),
            "total_area": round(self.total_area(), 4),
            "volume": round(self.volume(), 4),
        }

    def __str__(self):
        return (
            f"RegularPrism({self.side_count} sides, "
            f"s={self.side_length:g}, h={self.height:g})"
        )


if __name__ == "__main__":
    prism = RegularPrism(side_count=6, side_length=4, height=10)
    print(prism)
    for key, value in prism.summary().items():
        print(f"  {key:<16}{value}")

    print("\nA random prism (seeded, so this run is reproducible):")
    random_prism = RegularPrism.random(side_count=5, height=8, seed=42)
    print(f"  {random_prism}")
    print(f"  volume {random_prism.volume():.4f}")
    print(f"  volume {random_prism.volume():.4f}   <- called twice, SAME answer")
    print("  The original would have given two different answers here,")
    print("  because it regenerated the sides on every call.")

    print("\nA square prism is a cuboid, which we can check by hand:")
    square = RegularPrism(4, 3, 10)
    print(f"  4 sides of 3, height 10 -> volume {square.volume():.4f}")
    print(f"  a 3x3x10 box            -> volume {3 * 3 * 10}")

    # --- tests: check against shapes we can compute by hand -----------
    # A square prism with side 3 and height 10 is a 3x3x10 box.
    square = RegularPrism(4, 3, 10)
    assert abs(square.base_area() - 9.0) < 1e-9
    assert abs(square.volume() - 90.0) < 1e-9
    assert abs(square.lateral_area() - 4 * 3 * 10) < 1e-9
    assert abs(square.total_area() - (2 * 9 + 120)) < 1e-9

    # An equilateral triangle of side 2 has area sqrt(3).
    triangle = RegularPrism(3, 2, 1)
    assert abs(triangle.base_area() - math.sqrt(3)) < 1e-9

    # A regular hexagon of side s has area 3*sqrt(3)/2 * s^2.
    hexagon = RegularPrism(6, 4, 1)
    assert abs(hexagon.base_area() - (3 * math.sqrt(3) / 2) * 16) < 1e-9

    # Randomness happens once, at construction.
    r = RegularPrism.random(5, 8, seed=1)
    assert r.volume() == r.volume(), "repeated calls must agree"

    for bad in ((2, 1, 1), (3, 0, 1), (3, 1, 0), (3, -1, 1)):
        try:
            RegularPrism(*bad)
            raise AssertionError(f"{bad} should have raised")
        except ValueError:
            pass
    print("\nAll tests passed.")
