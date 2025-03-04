#----------------------------------------   Adding Elements to a List   -----------------------------------------------#
#                                            -------------------------

"""
Adding elements to a list in Python can be done using various methods. Python provides multiple built-in functions
and operations to append, insert, or extend lists.

Key Points:
1. Use `append()` to add a single element to the end of the list.
2. Use `extend()` to add multiple elements to the end of the list.
3. Use `insert()` to add an element at a specific index.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30]

# 1. Adding a Single Element with append()
"""
The append() method adds a single element to the end of the list.
"""
my_list.append(40)  # Add 40 to the end of the list
print("List after appending 40:", my_list)

# 2. Adding Multiple Elements with extend()
"""
The extend() method adds all elements from an iterable (e.g., list, tuple) to the end of the list.
"""
my_list.extend([50, 60])  # Add multiple elements to the end
print("List after extending with [50, 60]:", my_list)

# 3. Adding an Element at a Specific Position with insert()
"""
The insert() method adds an element at a specified index, shifting existing elements to the right.
"""
my_list.insert(1, 15)  # Add 15 at index 1
print("List after inserting 15 at index 1:", my_list)

# 4. Using Concatenation to Add Elements
"""
Lists can be combined using the `+` operator, creating a new list with the combined elements.
"""
new_list = my_list + [70, 80]
print("New list after concatenation:", new_list)

# 5. Repeating Elements with Multiplication
"""
Use the `*` operator to repeat the elements of a list.
"""
repeated_list = my_list * 2
print("Repeated list:", repeated_list)

#----------------------------------------------------------------------------------------------------------------------#
