"""Exercise A.5 - Angle: increase and decrease by an amount in radians.
Original: Lab 12, Task 2.

The original stores DEGREES and adds math.degrees(radians), which is
correct - but it prints inside its methods, calls input() inside them, and
never normalises, so an angle can drift to 7000 degrees.

THE REAL LESSON HERE IS UNITS. Mixing degrees and radians is one of the
most expensive classes of bug in engineering software. The defence is to
name every value for its unit and convert at exactly one boundary.
"""

import math


class Angle:
    """An angle, stored internally in degrees and normalised to [0, 360)."""

    def __init__(self, degrees=0.0):
        self._degrees = self._normalise(float(degrees))

    @staticmethod
    def _normalise(degrees):
        """Fold any value into [0, 360). -30 becomes 330; 400 becomes 40."""
        return degrees % 360

    # --- two ways to read it, each named for its unit ------------------
    @property
    def degrees(self):
        return self._degrees

    @property
    def radians(self):
        return math.radians(self._degrees)

    # --- changes return a NEW Angle; the original is untouched ---------
    def increased_by_radians(self, radians):
        return Angle(self._degrees + math.degrees(radians))

    def decreased_by_radians(self, radians):
        return Angle(self._degrees - math.degrees(radians))

    def increased_by_degrees(self, degrees):
        return Angle(self._degrees + degrees)

    def __eq__(self, other):
        if not isinstance(other, Angle):
            return NotImplemented
        # Floats, so compare with a tolerance (Lesson 1).
        return math.fabs(self._degrees - other._degrees) < 1e-9

    def __str__(self):
        return f"{self._degrees:.4f}deg ({self.radians:.4f}rad)"

    def __repr__(self):
        return f"Angle({self._degrees!r})"


if __name__ == "__main__":
    angle = Angle(60)
    print(f"start           : {angle}")

    bigger = angle.increased_by_radians(math.pi / 6)  # +30 degrees
    print(f"+ pi/6 rad      : {bigger}")

    smaller = bigger.decreased_by_radians(math.pi / 2)  # -90 degrees
    print(f"then - pi/2 rad : {smaller}")

    print(f"original intact : {angle}")

    print("\nNormalisation keeps values sane:")
    for start in (-30, 370, 720, 45):
        print(f"  Angle({start:>4}) -> {Angle(start).degrees:>8.2f}deg")

    print("\nWhy the unit is in every name:")
    print("  increased_by_radians(1) and increased_by_degrees(1) differ by 56x.")
    print(f"  by radians: {Angle(0).increased_by_radians(1).degrees:.4f}deg")
    print(f"  by degrees: {Angle(0).increased_by_degrees(1).degrees:.4f}deg")
    print("  A parameter called just 'amount' would make this a coin toss.")

    # --- tests -------------------------------------------------------
    assert Angle(60).degrees == 60
    assert Angle(-30).degrees == 330, "negatives must fold into [0, 360)"
    assert Angle(400).degrees == 40
    assert Angle(720) == Angle(0)
    assert abs(Angle(180).radians - math.pi) < 1e-12
    assert Angle(60).increased_by_degrees(30) == Angle(90)
    assert abs(Angle(0).increased_by_radians(math.pi).degrees - 180) < 1e-9
    a = Angle(60)
    a.increased_by_degrees(10)
    assert a == Angle(60), "changes must return a new Angle, not mutate"
    print("\nAll tests passed.")
