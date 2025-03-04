#----------------------------------------   Accessing List Elements   ------------------------------------------------#
#                                            --------------------------

"""
Lists in Python are ordered collections of items (elements) and can store a variety of data types.
To access elements in a list, we use indexing. Python lists support both positive and negative
indexing.

Positive Indexing: Starts from 0 for the first element, 1 for the second, and so on.
Negative Indexing: Starts from -1 for the last element, -2 for the second last, and so on.
"""

# Key Points about Accessing List Elements:
'''
1. Lists are indexed starting from 0 (positive indexing).
2. Negative indexing starts from -1 (the last element).
3. Indexing allows us to retrieve a specific element in a list.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 40, 50]

# 1. Accessing Elements with Positive Indexing
"""
Positive indexing starts from 0 and increases as we move right.
"""
print("Element at index 0 (first element):", my_list[0])  # First element
print("Element at index 2 (third element):", my_list[2])  # Third element
print("Element at index 4 (fifth element):", my_list[4])  # Fifth element

# 2. Accessing Elements with Negative Indexing
"""
Negative indexing starts from -1 and decreases as we move left.
"""
print("Element at index -1 (last element):", my_list[-1])  # Last element
print("Element at index -3 (third last element):", my_list[-3])  # Third last element
print("Element at index -5 (first element using negative indexing):", my_list[-5])  # First element

#----------------------------------------------------------------------------------------------------------------------#
