"""
An iterator is an object which contains a countable number of values and it is used to iterate over iterable
objects like list, tuples, sets, etc.

Iterators are implemented using a class and a local variable for iterating is
not required here, It follows lazy evaluation where the evaluation of the expression will be on hold and stored in
the memory until the item is called specifically which helps us to avoid repeated evaluation.

As lazy evaluation is implemented, it requires only 1 memory location to process the value and when we are using a
large dataset then, wastage of RAM space will be reduced the need to load the entire dataset at the same time will
not be there.

Using an iterator-

iter() keyword is used to create an iterator containing an iterable object.
next() keyword is used to call the next element in the iterable object.
After the iterable object is completed, to use them again reassign them to the same object.
"""

test_list = iter(['Harry', 'Ron', 'Hermione', 'Potter', 'Wesley', 'Granger'])
print(next(test_list))
print(next(test_list))
print(next(test_list))
