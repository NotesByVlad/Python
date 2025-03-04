#----------------------------------------   Miscellaneous List Operations   --------------------------------------------#
#                                               ----------------------------

"""
Miscellaneous operations on lists include tasks like checking if an element exists, finding indices, and removing duplicates.

Key Points:
1. Use `in` to check if an element exists in a list.
2. Use `index()` to find the index of an element.
3. Use `set()` to remove duplicates from a list.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 40, 20, 50, 30]

# 1. Checking if an Element Exists
"""
The `in` keyword checks if an element exists in a list.
"""
print(20 in my_list)  # True
print(100 in my_list)  # False

# 2. Finding the Index of an Element
"""
The `index()` method returns the first index of the given element.
"""
index_of_20 = my_list.index(20)
print("Index of 20:", index_of_20)

# 3. Removing Duplicates with `set()`
"""
Using `set()` removes duplicate values but does not maintain the original order.
"""
unique_elements = list(set(my_list))
print("List without duplicates:", unique_elements)

#----------------------------------------------------------------------------------------------------------------------#
