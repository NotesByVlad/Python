#----------------------------------------   Accessing Elements in a Tuple   ----------------------------------------#
#                                            ------------------------

"""
Tuples in Python are immutable sequences, and you can access elements using indexing and slicing.
Accessing elements from a tuple works similarly to lists.

Key Points:
1. Individual elements can be accessed using indexing.
2. Negative indexing allows access from the end of the tuple.
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Accessing a Single Element
"""
Access a specific element using its index.
"""
print("Original tuple:", my_tuple)
print("Element at index 1:", my_tuple[1])  # Access the second element (index 1)

# 2. Accessing an Element Using Negative Indexing
"""
Use negative indexing to access elements from the end of the tuple.
"""
print("Element at index -1 (last element):", my_tuple[-1])
print("Element at index -2 (second last element):", my_tuple[-2])

#----------------------------------------------------------------------------------------------------------------------#
