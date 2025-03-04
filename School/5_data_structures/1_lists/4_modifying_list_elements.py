#----------------------------------------   Modifying List Elements   -------------------------------------------------#
#                                            ------------------------

"""
Lists in Python are mutable, meaning their elements can be changed after the list is created.
You can modify a list by directly assigning new values to specific indices or by replacing a subset of elements
using slicing.

Key Points:
1. Individual elements can be updated using indexing.
2. Multiple elements can be updated or replaced using slicing.
3. Modifying a list does not require creating a new list; the existing list is updated.
"""

# Example List
my_list = [10, 20, 30, 40, 50]

# 1. Modifying a Single Element
"""
Assign a new value to a specific index.
"""
print("Original list:", my_list)
my_list[1] = 25  # Change the second element (index 1)
print("List after modifying index 1:", my_list)

# 2. Modifying Multiple Elements using Slicing
"""
Replace a subset of elements by assigning a new list to a slice.
"""
my_list[2:4] = [35, 45]  # Replace elements at indices 2 and 3
print("List after slicing modification (indices 2:4):", my_list)

# 3. Replacing All Elements
"""
Assign a completely new list to replace all elements.
"""
my_list[:] = [100, 200, 300]  # Replace the entire list
print("List after replacing all elements:", my_list)

# 4. Using Loops for Bulk Modification
"""
Modify each element based on a specific condition or operation.
"""
my_list = [10, 20, 30, 40, 50]  # Reset list
for i in range(len(my_list)):
    my_list[i] += 5  # Add 5 to each element
print("List after adding 5 to each element:", my_list)

#----------------------------------------------------------------------------------------------------------------------#
