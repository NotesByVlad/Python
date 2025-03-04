#----------------------------------------   Copying a Set   --------------------------------------------------#
#                                            ------------------------

"""
You can copy a set in Python to create a new set that is independent of the original.

Key Points:
1. Use copy() to create a shallow copy of a set.
2. Use the set constructor to create a copy as well.
"""

# Example Set
my_set = {10, 20, 30, 40, 50}

# 1. Shallow Copy Using copy()
"""
Create a copy of a set using the copy() method.
"""
set_copy = my_set.copy()
print("Original set:", my_set)
print("Shallow copy of the set:", set_copy)

# 2. Creating a Set Copy Using the set() Constructor
"""
Alternatively, you can create a copy of the set using the set() constructor.
"""
set_copy2 = set(my_set)
print("Another copy of the set:", set_copy2)

#----------------------------------------------------------------------------------------------------------------------#
