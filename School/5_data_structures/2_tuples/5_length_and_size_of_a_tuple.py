#----------------------------------------   Length and Size of a Tuple   -----------------------------------------#
#                                            ------------------------

"""
You can find the length of a tuple using len() and measure the memory usage using sys.getsizeof().

Key Points:
1. len() returns the number of elements in the tuple.
2. sys.getsizeof() returns the memory size of the tuple in bytes.
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Length of a Tuple
"""
Find the number of elements in a tuple using len().
"""
print("Original tuple:", my_tuple)
print("Length of the tuple:", len(my_tuple))

# 2. Size of a Tuple
"""
Measure the memory size of a tuple using sys.getsizeof().
"""
import sys
print("Size of the tuple in bytes:", sys.getsizeof(my_tuple))

#----------------------------------------------------------------------------------------------------------------------#
