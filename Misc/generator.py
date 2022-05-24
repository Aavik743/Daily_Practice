"""

It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in
a defined function.

Generators are implemented using a function. Just as iterators, generators also follow lazy evaluation.

Here, the yield function returns the data without affecting or exiting the function. It will return a
sequence of data in an iterable format where we need to iterate over the sequence to use the data as they won’t store
the entire sequence in the memory.

"""


def get_squares(n):
    for num in range(1, n + 1):
        yield num * num


sqr = get_squares(3)

print("Squares: ")
print(next(sqr))
print(next(sqr))
print(next(sqr))
