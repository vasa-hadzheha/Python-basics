"""Exercise A.1 - Vector: length and normalisation.
Original: Lab 10, Task 1.

See examples/appendix-classes/vector.py for the fully annotated version,
including a demonstration of the archive's shared-class-attribute bug.

WHAT THE ORIGINAL DID WRONG
  * n = [] in the class body, so every Vector shared one list
  * normalise() mutated self and printed, instead of returning a Vector
  * inp() called input() inside the class, making it untestable
"""

import math


class Vector:
    """A vector in n-dimensional space."""

    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("a vector needs at least one coordinate")
        self.coordinates = list(coordinates)  # copy the caller's list

    @property
    def dimension(self):
        return len(self.coordinates)

    def length(self):
        return math.sqrt(sum(v**2 for v in self.coordinates))

    def normalised(self):
        """A NEW unit vector in the same direction."""
        magnitude = self.length()
        if magnitude == 0:
            raise ValueError("the zero vector cannot be normalised")
        return Vector([v / magnitude for v in self.coordinates])

    def dot(self, other):
        if self.dimension != other.dimension:
            raise ValueError("vectors must have the same dimension")
        return sum(p * q for p, q in zip(self.coordinates, other.coordinates))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.dimension == other.dimension and all(
            math.fabs(p - q) < 1e-9 for p, q in zip(self.coordinates, other.coordinates)
        )

    def __str__(self):
        return f"({', '.join(f'{v:g}' for v in self.coordinates)})"

    def __repr__(self):
        return f"Vector({self.coordinates!r})"


if __name__ == "__main__":
    # Input is gathered OUTSIDE the class, so the class stays testable.
    n = int(input("Vector dimension: "))
    coordinates = [float(input(f"x{i + 1} = ")) for i in range(n)]

    v = Vector(coordinates)
    print(f"\nVector      : {v}")
    print(f"Dimension   : {v.dimension}")
    print(f"Length      : {v.length():.6f}")
    try:
        print(f"Normalised  : {v.normalised()}")
        print(f"Unit length : {v.normalised().length():.10f}")
    except ValueError as error:
        print(f"Normalised  : {error}")

    assert Vector([3, 4]).length() == 5.0
    assert Vector([3, 4]).dot(Vector([1, 0])) == 3
    assert (Vector([1, 2]) == Vector([1, 2])) == (Vector([1, 2]) == Vector([1, 2]))
    print("\nAll tests passed.")
