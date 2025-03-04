#----------------------------------------   List Slicing in Python   --------------------------------------------------#
#                                           -------------------------

"""
List slicing allows us to retrieve a subset of elements from a list by specifying a range of indices.
The syntax for slicing is:
    list[start:stop:step]

- start: The starting index (inclusive). Default is 0.
- stop: The ending index (exclusive). Default is the length of the list.
- step: The step size for selecting elements. Default is 1.

Slicing does not modify the original list; it creates a new list.
"""

# Key Points about List Slicing:
'''
1. Allows extracting a portion of the list using start, stop, and step indices.
2. Negative indices can be used for slicing from the end of the list.
3. Step can be used to skip elements (default is 1).
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 1. Basic Slicing
print("Slicing from index 2 to 5 (exclusive):", my_list[2:5])  # [30, 40, 50]
print("Slicing from the start to index 4 (exclusive):", my_list[:4])  # [10, 20, 30, 40]
print("Slicing from index 3 to the end:", my_list[3:])  # [40, 50, 60, 70, 80, 90]

# 2. Slicing with Negative Indices
print("Slicing the last 3 elements:", my_list[-3:])  # [70, 80, 90]
print("Slicing from index -7 to -4 (exclusive):", my_list[-7:-4])  # [20, 30, 40]

# 3. Slicing with Step
print("Slicing every second element:", my_list[::2])  # [10, 30, 50, 70, 90]
print("Slicing every third element from index 1:", my_list[1::3])  # [20, 50, 80]

# 4. Reversing a List using Slicing
print("Reversed list:", my_list[::-1])  # [90, 80, 70, 60, 50, 40, 30, 20, 10]

#----------------------------------------------------------------------------------------------------------------------#
