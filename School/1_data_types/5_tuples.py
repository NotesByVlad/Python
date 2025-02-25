#----------------------------------------   Tuples in Python   --------------------------------------------------------#
#                                        -----------------------

"""
A tuple is a collection of ordered elements, similar to a list, but with a key difference:
tuples are **immutable**, meaning their content cannot be changed after they are created.

Tuples are typically used to group related data together and are defined using parentheses `()`.
They can contain elements of different data types.
"""

# Key Points about Tuples:
'''
Ordered: Tuples maintain the order of elements, just like lists.
Immutable: Once created, the elements of a tuple cannot be changed, added, or removed.
Heterogeneous: A tuple can contain elements of different data types.
Indexable and Iterable: Tuples allow access to individual elements using their index and support iteration.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Tuple Initialization
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('Python', 'is', 'fun')
tuple3 = (1, 'Python', 3.14, (10, 20))

# Printing the tuples
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

# 2. Tuple Length
print("\nLength of Tuple 1:", len(tuple1))
print("Length of Tuple 2:", len(tuple2))

# 3. Accessing Elements
print("\nFirst Element of Tuple 1:", tuple1[0])  # Access by index
print("Last Element of Tuple 2:", tuple2[-1])   # Access by negative index

# 4. Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested_tuple)
print("Accessing Element (Row 2, Column 1):", nested_tuple[1][0])

# 5. Tuple Concatenation
combined_tuple = tuple1 + tuple2
print("\nConcatenated Tuple:", combined_tuple)

# 6. Tuple Repetition
repeated_tuple = tuple2 * 2
print("\nRepeated Tuple 2 (2 times):", repeated_tuple)

# 7. Tuple Slicing
sub_tuple = tuple1[1:4]  # Extract a sub-tuple (elements from index 1 to 3)
print("\nSliced Tuple 1 (from index 1 to 3):", sub_tuple)

# 8. Iterating Over a Tuple
print("\nIterating over Tuple 1:")
for element in tuple1:
    print(element, end=" ")

# 9. Tuple Unpacking
a, b, c = (1, 2, 3)  # Unpacking values into variables
print("\n\nTuple Unpacking:")
print(f"a = {a}, b = {b}, c = {c}")

# 10. Using `enumerate`
print("\nEnumerating Tuple 2:")
for index, value in enumerate(tuple2):
    print(f"Index {index}: {value}")

# 11. Checking Membership
print("\nIs 'Python' in Tuple 2?", 'Python' in tuple2)
print("Is 10 in Tuple 1?", 10 in tuple1)

# 12. Immutability
'''
Tuples are immutable, so operations like adding, removing, or changing elements 
are not allowed. However, you can create a new tuple if you need to modify it.
'''
try:
    tuple1[1] = 10  # Attempt to modify
except TypeError as e:
    print("\nError Demonstrating Immutability:", e)

# 13. Tuple Methods
'''
Since tuples are immutable, they have fewer methods compared to lists.
Common methods include:
'''
count_example = (1, 2, 2, 3, 4, 2).count(2)  # Count occurrences of an element
index_example = tuple2.index('fun')  # Find the index of an element

print("\nCount of '2' in (1, 2, 2, 3, 4, 2):", count_example)
print("Index of 'fun' in Tuple 2:", index_example)

# 14. Tuples vs Lists
'''
Tuples are preferred when immutability is desired, ensuring the data remains constant.
They are slightly faster than lists for certain operations due to their immutability.
'''

# 15. Single-Element Tuples
'''
A single-element tuple must include a trailing comma. Without the comma, 
it is interpreted as the value inside parentheses, not a tuple.
'''
single_tuple = (42,)  # Single-element tuple
not_a_tuple = (42)    # Just an integer
print("\nSingle-Element Tuple:", single_tuple)
print("Not a Tuple (just an int):", not_a_tuple)

#----------------------------------------------------------------------------------------------------------------------#
