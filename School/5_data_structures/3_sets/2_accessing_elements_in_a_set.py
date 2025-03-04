#----------------------------------------   Accessing Elements in a Set   ----------------------------------------#
#                                            ------------------------

"""
Sets in Python are unordered collections of unique elements. You cannot access individual elements using indices,
but you can iterate through a set or use membership tests.

Key Points:
1. Elements in a set cannot be accessed via indexing.
2. Membership test (in) can be used to check if an element is in the set.
"""

# Example Set
my_set = {10, 20, 30, 40, 50}

# 1. Checking if an Element Exists in the Set
"""
You can check if an element is present in the set using the 'in' operator.
"""
print("Original set:", my_set)
print("Is 20 in the set?", 20 in my_set)
print("Is 60 in the set?", 60 in my_set)

# 2. Iterating Over a Set
"""
Since sets are unordered, you can loop through the elements without any guaranteed order.
"""
print("Iterating through the set:")
for element in my_set:
    print(element)

#----------------------------------------------------------------------------------------------------------------------#
