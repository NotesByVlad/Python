#----------------------------------------   Slicing a Tuple   -------------------------------------------------#
#                                            ------------------------

"""
Tuples can be sliced to extract a subset of elements. Slicing creates a new tuple.
You can slice using the start, stop, and step arguments.

Key Points:
1. You can slice a tuple to get a subtuple.
2. You can include a step argument to skip elements.
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Slicing a Tuple (start:stop)
"""
Extract a subset of elements from the tuple using slicing.
"""
print("Original tuple:", my_tuple)
print("Sliced tuple (from index 1 to 3):", my_tuple[1:4])

# 2. Slicing with Step (start:stop:step)
"""
Extract elements with a step, which skips elements at regular intervals.
"""
print("Sliced tuple with step (1:5:2):", my_tuple[1:5:2])

#----------------------------------------------------------------------------------------------------------------------#
