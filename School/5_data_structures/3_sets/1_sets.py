#----------------------------------------   Sets in Python   ----------------------------------------------------------#
#                                        -----------------------

'''
A set is an unordered collection of unique elements. It is used to store
multiple items in a single variable, ensuring that duplicates are not allowed.

Sets are mutable, meaning elements can be added or removed. Sets are defined
using curly braces `{}` or the `set()` constructor. Since sets are unordered,
they do not support indexing or slicing.
'''

# Key Points about Sets:
'''
Unordered: The elements in a set are not stored in any particular order.
Unique Elements: Duplicate elements are automatically removed.
Mutable: Sets can be modified by adding or removing elements.
Unindexed: Sets do not support indexing or slicing.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Set Initialization
set1 = {1, 2, 3, 4, 5}
set2 = {'Python', 'is', 'fun'}
set3 = set([1, 2, 2, 3, 4])  # Using the `set()` constructor

# Printing the sets
print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3 (duplicates removed):", set3)

# 2. Adding Elements
set1.add(6)  # Add a single element
set2.update(['and', 'useful'])  # Add multiple elements
print("\nSet 1 after Add:", set1)
print("Set 2 after Update:", set2)

# 3. Removing Elements
set1.remove(3)  # Remove a specific element (raises KeyError if not found)
set2.discard('fun')  # Remove a specific element (does not raise error if not found)
print("\nSet 1 after Remove:", set1)
print("Set 2 after Discard:", set2)

# 4. Checking Membership
print("\nIs 4 in Set 1?", 4 in set1)
print("Is 'fun' in Set 2?", 'fun' in set2)

# 5. Set Operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

union_set = setA | setB  # Union: Combine all unique elements from both sets
intersection_set = setA & setB  # Intersection: Elements common to both sets
difference_set = setA - setB  # Difference: Elements in setA but not in setB
symmetric_difference_set = setA ^ setB  # Symmetric Difference: Elements in either setA or setB but not both

print("\nSet A:", setA)
print("Set B:", setB)
print("Union of A and B:", union_set)
print("Intersection of A and B:", intersection_set)
print("Difference (A - B):", difference_set)
print("Symmetric Difference (A ^ B):", symmetric_difference_set)

# 6. Iterating Over a Set
print("\nIterating over Set 1:")
for element in set1:
    print(element, end=" ")

# 7. Frozen Sets
'''
A `frozenset` is an immutable version of a set. Once created, it cannot be modified.
Useful when you need an immutable collection of unique elements.
'''
frozen_set = frozenset([1, 2, 3, 4])
print("\n\nFrozen Set:", frozen_set)

# 8. Set Methods
'''
Common methods for sets include:
- `add()`: Add an element.
- `remove()`: Remove an element (raises an error if not found).
- `discard()`: Remove an element (does not raise an error if not found).
- `union()`: Combine elements from two sets.
- `intersection()`: Find common elements.
- `difference()`: Find elements in one set but not the other.
- `symmetric_difference()`: Find elements in either set but not both.
'''

# Example: Using `union` and `intersection` as methods
union_example = setA.union(setB)
intersection_example = setA.intersection(setB)

print("\nUnion (using method):", union_example)
print("Intersection (using method):", intersection_example)

# 9. Clearing a Set
set1.clear()  # Remove all elements
print("\nCleared Set 1:", set1)

# 10. Set Comprehension
squared_set = {x**2 for x in range(5)}  # Create a set of squares
print("\nSet Comprehension (Squares):", squared_set)

#----------------------------------------------------------------------------------------------------------------------#
