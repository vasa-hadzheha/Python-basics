"""Exercise A.6 - Matrix: display, min, max, indexing.
Original: Lab 12, Task 3.

WHAT THE ORIGINAL DID WRONG - and the first one is a great example of a
bug that reads as correct:

    if el in self.matrix[i] == True:

Python CHAINS this as  (el in self.matrix[i]) and (self.matrix[i] == True),
and a list is never equal to True, so the condition is ALWAYS False. The
author's comment says "Error -- does not work", and this is why.

Also:
  * __setitem__(self, row, col, value) cannot work - Python passes exactly
    one key, so a 2-D subscript needs m[row, col] and a tuple key
  * "in list(self.count_row)" calls list() on an int -> TypeError
  * show_matrix() returns print(...), i.e. returns None
"""


class Matrix:
    """A 2-D matrix wrapping a list of rows."""

    def __init__(self, rows):
        if not rows or not rows[0]:
            raise ValueError("a matrix needs at least one row and one column")
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            # Ragged input is the most common real matrix bug. Refuse it.
            raise ValueError("every row must have the same number of columns")
        self.rows = [list(row) for row in rows]  # copy each row

    @property
    def row_count(self):
        return len(self.rows)

    @property
    def column_count(self):
        return len(self.rows[0])

    # --- a 2-D subscript takes a TUPLE key ----------------------------
    def __getitem__(self, key):
        """m[i, j] is one cell; m[i] is a whole row."""
        if isinstance(key, tuple):
            i, j = key
            self._check(i, j)
            return self.rows[i][j]
        self._check(key, 0)
        return list(self.rows[key])  # a copy, so callers cannot mutate us

    def __setitem__(self, key, value):
        """m[i, j] = value"""
        if not isinstance(key, tuple):
            raise TypeError("assign a single cell: m[row, column] = value")
        i, j = key
        self._check(i, j)
        self.rows[i][j] = value

    def _check(self, i, j):
        if not (0 <= i < self.row_count):
            raise IndexError(f"row {i} is outside 0..{self.row_count - 1}")
        if not (0 <= j < self.column_count):
            raise IndexError(f"column {j} is outside 0..{self.column_count - 1}")

    # --- aggregates RETURN values; they do not print ------------------
    def flat(self):
        return [cell for row in self.rows for cell in row]

    def minimum(self):
        return min(self.flat())

    def maximum(self):
        return max(self.flat())

    def total(self):
        return sum(self.flat())

    def transposed(self):
        return Matrix([list(column) for column in zip(*self.rows)])

    def __contains__(self, value):
        """Enables "value in matrix" - what the original was reaching for."""
        return value in self.flat()

    def __str__(self):
        """An aligned grid. The original returned print(...), i.e. None."""
        width = max(len(f"{cell:g}") for cell in self.flat()) + 2
        return "\n".join(
            "".join(f"{cell:>{width}g}" for cell in row) for row in self.rows
        )


if __name__ == "__main__":
    m = Matrix([[3, -1, 400], [5, 22, 7], [-8, 9, 1]])

    print("Matrix:")
    print(m)
    print(f"\nshape   : {m.row_count} x {m.column_count}")
    print(f"min     : {m.minimum()}")
    print(f"max     : {m.maximum()}")
    print(f"total   : {m.total()}")
    print(f"m[1, 2] : {m[1, 2]}")
    print(f"m[1]    : {m[1]}")
    print(f"22 in m : {22 in m}")
    print(f"99 in m : {99 in m}")

    m[0, 0] = 999
    print(f"\nafter m[0, 0] = 999:\n{m}")

    print("\nTransposed:")
    print(m.transposed())

    print("\nThe errors the original could not raise:")
    for key in ((9, 0), (0, 9), (-1, 0)):
        try:
            m[key]
        except IndexError as error:
            print(f"  m{key} -> IndexError: {error}")

    print("\n" + "=" * 62)
    print("  THE ORIGINAL'S ALWAYS-FALSE CONDITION")
    print("=" * 62)
    row = [3, -1, 400]
    print(f"  row = {row}")
    print(f"  (3 in row)            -> {3 in row}")
    print(f"  (3 in row) == True    -> {(3 in row) == True}")
    print(f"  3 in row == True      -> {3 in row == True}   <- CHAINED, always False")
    print("  Python reads it as: (3 in row) and (row == True).")
    print("  A list is never equal to True, so the whole thing is always False.")

    # --- tests -------------------------------------------------------
    t = Matrix([[1, 2], [3, 4]])
    assert t.minimum() == 1 and t.maximum() == 4 and t.total() == 10
    assert t[0, 1] == 2 and t[1] == [3, 4]
    assert 3 in t and 99 not in t
    assert t.transposed()[0, 1] == 3
    t[0, 0] = 9
    assert t[0, 0] == 9
    # A returned row must be a copy, or callers could corrupt the matrix.
    borrowed = t[0]
    borrowed[0] = -1
    assert t[0, 0] == 9, "__getitem__ must return a copy of the row"
    try:
        Matrix([[1, 2], [3]])
        raise AssertionError("ragged rows should have raised")
    except ValueError:
        pass
    try:
        t[5, 5]
        raise AssertionError("an out-of-range index should have raised")
    except IndexError:
        pass
    print("\nAll tests passed.")
