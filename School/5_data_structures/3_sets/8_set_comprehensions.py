#----------------------------------------   Set Comprehensions   ------------------------------------------------------#
#                                        ------------------------

"""
Set comprehensions allow you to create new sets by applying a condition or operation to elements of an existing set.

Key Points:
1. Use set comprehensions to create new sets based on an existing iterable.
"""

# Example Set
my_set = {10, 20, 30, 40, 50}

# 1. Creating a Set Using Set Comprehension
"""
Create a new set by adding 5 to each element of the original set.
"""
new_set = {x + 5 for x in my_set}
print("New set after adding 5 to each element:", new_set)

# 2. Creating a Set with a Condition
"""
Create a new set that includes only even numbers from the original set.
"""
even_set = {x for x in my_set if x % 2 == 0}
print("New set with even numbers:", even_set)

#----------------------------------------------------------------------------------------------------------------------#

# Set Comprehensions in Data Structures

# Basic Set Comprehension
numbers = [1, 2, 3, 3, 4]
unique_numbers = {num for num in numbers}
print("Unique numbers:", unique_numbers)  # Output: {1, 2, 3, 4}

# Set Comprehension with Conditions
even_numbers = {num for num in numbers if num % 2 == 0}
print("Even numbers:", even_numbers)  # Output: {2, 4}

# Union of Two Sets Using Comprehension
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = {num for num in set1}.union(set2)
print("Union of sets:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of Two Sets Using Comprehension
intersection_set = {num for num in set1 if num in set2}
print("Intersection of sets:", intersection_set)  # Output: {3}

# Set Difference Using Comprehension
difference_set = {num for num in set1 if num not in set2}
print("Difference of sets:", difference_set)  # Output: {1, 2}
#----------------------------------------------------------------------------------------------------------------------#