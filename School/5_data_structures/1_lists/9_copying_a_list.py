#----------------------------------------   Copying a List   --------------------------------------------#
#                                               ----------------------------

"""
Copying a list refers to creating a new list that contains the same elements as the original list.
This is essential to avoid modifying the original list when working with it.

Key Points:
1. Use `copy()` for a shallow copy of the list.
2. Use slicing to copy a list.
3. Use `deepcopy()` from the `copy` module for a deep copy when working with nested lists.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
original_list = [10, 20, 30, 40]

# 1. Using copy() to Create a Shallow Copy
"""
The copy() method creates a shallow copy of the list.
"""
copied_list = original_list.copy()
print("Shallow copied list:", copied_list)

# 2. Using Slicing to Copy the List
"""
Slicing the list from the beginning to the end creates a new list with the same elements.
"""
sliced_copy = original_list[:]
print("Sliced copied list:", sliced_copy)

# 3. Using deepcopy() for Nested Lists
"""
To create a deep copy of a nested list, use the deepcopy() function from the copy module.
"""
import copy
nested_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(nested_list)
print("Deep copied nested list:", deep_copied_list)

#----------------------------------------------------------------------------------------------------------------------#
