#----------------------------------------   Iterators in Python   -----------------------------------------------------#
#                                        -------------------------

"""
Iterators in Python are objects that allow you to traverse through all the elements of a collection
(like lists or tuples),
one element at a time. They provide a uniform interface to access elements without exposing the underlying structure.

An object is an iterator if it implements the `__iter__()` and `__next__()` methods.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Iterators:
'''
- Iterator: An object with a `__next__()` method to get the next item and a `__iter__()` method to return itself.
- Iterable: Any object capable of returning an iterator (e.g., lists, tuples, strings).
- StopIteration: Raised to signal that there are no more items to return.
- Use Cases: Iterators simplify sequential data processing, especially when combined with loops or generators.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Creating and Using an Iterator

# Example with an Iterable (List)
my_list = [1, 2, 3]
iterator = iter(my_list)  # Get an iterator from the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3

# StopIteration is raised when there are no more items
# print(next(iterator))  # Uncomment to see the StopIteration error

#----------------------------------------------------------------------------------------------------------------------#

# Custom Iterator Example

class Counter:
    """Custom iterator that counts up to a maximum value."""
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the Custom Iterator
counter = Counter(3)
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3

#----------------------------------------------------------------------------------------------------------------------#

# Iterators vs. Iterables
'''
- Iterable: Any object that can produce an iterator (e.g., list, tuple, string).
- Iterator: The object produced by `iter()` which provides the `__next__()` method.

Example:
list_obj = [10, 20, 30]  # Iterable
list_iter = iter(list_obj)  # Iterator

# The `for` loop automatically handles calling `iter()` and `next()`.
for item in list_obj:
    print(item)
'''
#----------------------------------------------------------------------------------------------------------------------#

# Infinite Iterators (Using itertools)
from itertools import count

# Infinite counter starting from 1
infinite_counter = count(start=1)
for _ in range(3):
    print(next(infinite_counter))

# Output:
# 1
# 2
# 3
#----------------------------------------------------------------------------------------------------------------------#