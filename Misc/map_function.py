"""
The map function takes in a function and a iterable as arguments,
    and gives out result of each element in the iterable using the function.
"""


def get_square(n):
    return n * n


iterable_1 = [1, 2, 3, 4, 5]
result = map(get_square, iterable_1)
print(list(result))
