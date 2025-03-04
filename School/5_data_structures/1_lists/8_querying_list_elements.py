#----------------------------------------   Querying Elements in a List   ---------------------------------------------#
#                                              ---------------------------

"""
Querying elements in a list involves checking for the presence of specific values, counting occurrences,
or finding the index of elements. Python provides several methods for querying list elements efficiently.

Key Points:
1. Use the `in` keyword to check if an element exists in a list.
2. Use the `count()` method to find the number of occurrences of an element.
3. Use the `index()` method to find the first occurrence of an element.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 20, 40, 50, 20]

# 1. Checking for Element Presence with `in`
"""
Use the `in` keyword to verify if an element exists in the list. It returns `True` or `False`.
"""
is_present = 20 in my_list  # Check if 20 exists in the list
print("Is 20 present in the list?:", is_present)

is_absent = 60 in my_list  # Check if 60 exists in the list
print("Is 60 present in the list?:", is_absent)

# 2. Counting Occurrences of an Element with count()
"""
The count() method returns the number of times a specified value appears in the list.
"""
count_20 = my_list.count(20)  # Count occurrences of 20
print("Number of occurrences of 20:", count_20)

count_30 = my_list.count(30)  # Count occurrences of 30
print("Number of occurrences of 30:", count_30)

# 3. Finding the Index of an Element with index()
"""
The index() method returns the index of the first occurrence of a specified value.
If the value is not found, it raises a ValueError.
"""
index_20 = my_list.index(20)  # Find index of the first occurrence of 20
print("Index of the first occurrence of 20:", index_20)

# Handling ValueError with index()
"""
Wrap the index() call in a try-except block to handle cases where the value does not exist.
"""
try:
    index_60 = my_list.index(60)  # Attempt to find index of 60
    print("Index of 60:", index_60)
except ValueError:
    print("60 is not in the list.")

# 4. Using List Comprehension for Advanced Querying
"""
List comprehension can be used to filter or query elements based on a condition.
"""
filtered_list = [x for x in my_list if x > 20]  # Get all elements greater than 20
print("Elements greater than 20:", filtered_list)

#----------------------------------------------------------------------------------------------------------------------#
