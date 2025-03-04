#----------------------------------------   Iterating Over a List   --------------------------------------------#
#                                               ----------------------------

"""
Iterating over a list allows you to access each element one by one. Python provides several ways to iterate over a list.

Key Points:
1. Use a for loop to iterate through the elements.
2. Use list comprehension for a more compact iteration.
3. Use `enumerate()` to get both index and value during iteration.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [10, 20, 30, 40]

# 1. Using a For Loop to Iterate Through the List
"""
A simple for loop is the most common way to iterate through all elements.
"""
for item in my_list:
    print(item)

# 2. Using List Comprehension for Iteration
"""
List comprehension allows you to iterate and transform elements concisely.
"""
squared_list = [x**2 for x in my_list]
print("Squared values:", squared_list)

# 3. Using enumerate() to Iterate with Index
"""
The enumerate() function gives both the index and value during iteration.
"""
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

#----------------------------------------------------------------------------------------------------------------------#
