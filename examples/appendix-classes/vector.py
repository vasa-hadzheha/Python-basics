"""Appendix - the archive's Vector class (Lab 10, Task 1), corrected.

Run me:  python3 examples/appendix-classes/vector.py
No input needed.
"""

import math


class Vector:
    """A vector in n-dimensional space."""

    def __init__(self, coordinates):
        """coordinates: a list of numbers."""
        if not coordinates:
            raise ValueError("a vector needs at least one coordinate")
        # list(): copy, so the caller cannot change this vector afterwards
        # by mutating their own list.
        self.coordinates = list(coordinates)

    @property
    def dimension(self):
        return len(self.coordinates)

    def length(self):
        """The Euclidean length (magnitude)."""
        return math.sqrt(sum(value**2 for value in self.coordinates))

    def normalised(self):
        """A NEW unit vector in the same direction.

        Raises ValueError for the zero vector, which has no direction.
        """
        magnitude = self.length()
        if magnitude == 0:
            raise ValueError("the zero vector cannot be normalised")
        return Vector([value / magnitude for value in self.coordinates])

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        eps = 1e-9
        return self.dimension == other.dimension and all(
            math.fabs(p - q) < eps for p, q in zip(self.coordinates, other.coordinates)
        )

    def __str__(self):
        return f"({', '.join(f'{v:g}' for v in self.coordinates)})"

    def __repr__(self):
        return f"Vector({self.coordinates!r})"


# =======================================================================
#  the fixed version in use
# =======================================================================
a = Vector([3, 4])
print(f"a            = {a}")
print(f"a.dimension  = {a.dimension}")
print(f"a.length()   = {a.length()}")

unit = a.normalised()
print(f"a.normalised() = {unit}")
print(f"its length     = {unit.length():.10f}  (a unit vector, so 1)")
print(f"a is unchanged = {a}")  # normalised() returned a NEW vector

b = Vector([6, 8])
print(f"\nb              = {b}")
print(f"b.normalised() = {b.normalised()}")
print("b's result is NOT contaminated by a's - each instance has its own state.")


# =======================================================================
#  the archive's bug, demonstrated
# =======================================================================
class BrokenVector:
    """The archive's version. n is on the CLASS, so all instances share it."""

    n = []  # <-- THE BUG

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def normalise(self, length):
        for value in self.coordinates:
            self.n.append(value / length)  # appends to the SHARED list
        return self.n


print("\n" + "=" * 62)
print("  THE ARCHIVE'S BUG: a mutable value in the class body")
print("=" * 62)
p = BrokenVector([3, 4])
q = BrokenVector([6, 8])
print(f"  p.normalise(5)  -> {p.normalise(5)}")
print(f"  q.normalise(10) -> {q.normalise(10)}")
print("  q's result contains p's values. One list, shared by every instance.")
print(f"  BrokenVector.n is p.n is q.n : {BrokenVector.n is p.n is q.n}")
print("\n  The fix: create every piece of per-instance state in __init__.")


# =======================================================================
#  tests
# =======================================================================
assert Vector([3, 4]).length() == 5.0
assert abs(Vector([3, 4]).normalised().length() - 1.0) < 1e-12
assert Vector([1, 2]) == Vector([1, 2])
assert Vector([1, 2]) != Vector([1, 3])
assert Vector([1, 2]) != Vector([1, 2, 3]), "different dimensions are not equal"
assert (Vector([1, 2]) == "not a vector") is False

# __eq__ must be SYMMETRIC - the archive's version was not.
x, y = Vector([1, 2]), Vector([1, 2])
assert (x == y) == (y == x)

# Each instance keeps its own state.
v1, v2 = Vector([3, 4]), Vector([6, 8])
assert v1.normalised() == Vector([0.6, 0.8])
assert v2.normalised() == Vector([0.6, 0.8])
assert v1.coordinates == [3, 4], "normalised() must not mutate the original"

try:
    Vector([0, 0]).normalised()
    raise AssertionError("the zero vector should have raised")
except ValueError:
    pass

try:
    Vector([])
    raise AssertionError("an empty vector should have raised")
except ValueError:
    pass

print("\nAll tests passed.")
