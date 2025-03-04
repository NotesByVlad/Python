#----------------------------------------   Combining Lists   --------------------------------------------#
#                                               ----------------------------

"""
Combining lists involves joining two or more lists into a single list. Python provides several ways to concatenate lists.

Key Points:
1. Use the `+` operator to concatenate two lists.
2. Use `extend()` to append elements of one list to another.
3. Use `*` (repetition) to repeat a list.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 1. Using + to Combine Lists
"""
The + operator concatenates two lists into a new list.
"""
combined_list = list1 + list2
print("Combined list using +:", combined_list)

# 2. Using extend() to Add Elements from Another List
"""
The extend() method appends all elements of list2 to list1.
"""
list1.extend(list2)
print("List1 after extending with list2:", list1)

# 3. Using * to Repeat a List
"""
The * operator can repeat a list multiple times.
"""
repeated_list = list1 * 2
print("List repeated twice:", repeated_list)

#----------------------------------------------------------------------------------------------------------------------#
