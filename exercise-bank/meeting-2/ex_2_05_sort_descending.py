"""Exercise 2.5 - Sort an array descending.  (Original Lab 6, Task 4.)

Practises: sorted() vs .sort() - the whole point of the exercise.
"""

n = int(input("How many elements? "))
k = [float(input(f"element {i + 1}: ")) for i in range(n)]

print(f"Your array      : {k}")

# sorted() returns a NEW list and leaves k alone, which is what lets us
# print both. k.sort(reverse=True) would sort in place and destroy the
# original ordering for good.
descending = sorted(k, reverse=True)

print(f"Descending      : {descending}")
print(f"Original, intact: {k}")
print(f"Ascending       : {sorted(k)}")
