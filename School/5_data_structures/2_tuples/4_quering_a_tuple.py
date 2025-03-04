#----------------------------------------   Querying a Tuple   -------------------------------------------------#
#                                            ------------------------

"""
You can query a tuple to find the index of an element or count the occurrences of a value.

Key Points:
1. Use index() to find the first occurrence of a value.
2. Use count() to find how many times a value occurs.
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50, 30, 20, 10)

# 1. Finding the Index of an Element
"""
Find the first occurrence of a value using index().
"""
print("Original tuple:", my_tuple)
print("Index of element 30:", my_tuple.index(30))  # Returns index of the first occurrence of 30

# 2. Counting Occurrences of an Element
"""
Count how many times a value appears in the tuple using count().
"""
print("Count of element 10:", my_tuple.count(10))  # Count how many times 10 appears

#----------------------------------------------------------------------------------------------------------------------#
