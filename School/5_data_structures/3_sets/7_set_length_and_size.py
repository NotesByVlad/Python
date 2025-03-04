#----------------------------------------   Set Length and Size   --------------------------------------------#
#                                            ------------------------

"""
You can find the length of a set using len() and measure the memory usage using sys.getsizeof().

Key Points:
1. len() returns the number of elements in a set.
2. sys.getsizeof() returns the memory size of a set in bytes.
"""

# Example Set
my_set = {10, 20, 30, 40, 50}

# 1. Length of a Set
"""
Get the number of elements in the set using len().
"""
print("Original set:", my_set)
print("Length of the set:", len(my_set))

# 2. Size of a Set
"""
Measure the memory size of the set using sys.getsizeof().
"""
import sys
print("Size of the set in bytes:", sys.getsizeof(my_set))

#----------------------------------------------------------------------------------------------------------------------#
