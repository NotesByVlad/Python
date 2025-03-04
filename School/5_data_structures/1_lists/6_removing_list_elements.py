#----------------------------------------   Removing Elements from a List   --------------------------------------------#
#                                              ---------------------------

"""
Removing elements from a list in Python can be done using several methods. These methods allow for removing
specific elements, removing by index, or clearing the entire list.

Key Points:
1. Use `remove()` to delete the first occurrence of a specific value.
2. Use `pop()` to remove an element by its index and return it.
3. Use `del` to delete elements by index or slices.
4. Use `clear()` to remove all elements from the list.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 40, 50, 60, 70]

# 1. Removing a Specific Element with remove()
"""
The remove() method deletes the first occurrence of the specified value.
If the value is not found, it raises a ValueError.
"""
my_list.remove(30)  # Remove the value 30
print("List after removing 30:", my_list)

# 2. Removing an Element by Index with pop()
"""
The pop() method removes and returns the element at the specified index.
If no index is specified, it removes the last element by default.
"""
popped_element = my_list.pop(2)  # Remove the element at index 2
print("Popped element:", popped_element)
print("List after popping index 2:", my_list)

# 3. Removing Elements by Index or Slices with del
"""
The del statement can be used to delete elements at specific indices or slices of the list.
"""
del my_list[1]  # Delete the element at index 1
print("List after deleting index 1:", my_list)

del my_list[1:3]  # Delete elements from index 1 to 2 (exclusive)
print("List after deleting a slice (index 1:3):", my_list)

# 4. Removing All Elements with clear()
"""
The clear() method removes all elements from the list, leaving it empty.
"""
my_list.clear()  # Clear all elements
print("List after clearing all elements:", my_list)

#----------------------------------------------------------------------------------------------------------------------#
