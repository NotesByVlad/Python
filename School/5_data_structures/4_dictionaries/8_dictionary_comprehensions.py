#----------------------------------------   Dictionary Comprehensions   ------------------------------------------------#
#                                            --------------------------

"""
Dictionary comprehensions in Python provide a concise way to create dictionaries.
They use a single line of code to construct dictionaries from iterables or other dictionaries.
"""

# Key Points about Dictionary Comprehensions:
'''
1. Syntax: `{key_expr: value_expr for item in iterable}`.
2. They can include conditions to filter items.
3. Useful for transforming data, swapping keys and values, and more.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Creating a Dictionary from a List
"""
Example: Create a dictionary where keys are numbers, and values are their squares.
"""
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print("Squares:", squares)

# 2. Filtering Items in a Dictionary Comprehension
"""
Example: Create a dictionary with even numbers only.
"""
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print("Even Squares:", even_squares)

# 3. Transforming an Existing Dictionary
"""
Example: Increase all values in a dictionary by 10.
"""
original_dict = {"a": 1, "b": 2, "c": 3}
transformed_dict = {key: value + 10 for key, value in original_dict.items()}
print("Transformed Dictionary:", transformed_dict)

# 4. Swapping Keys and Values
"""
Example: Create a new dictionary by swapping keys and values.
"""
swapped_dict = {value: key for key, value in original_dict.items()}
print("Swapped Dictionary:", swapped_dict)

# 5. Nested Dictionary Comprehensions
"""
Example: Create a dictionary of dictionaries.
"""
nested_dict = {num: {"square": num**2, "cube": num**3} for num in numbers}
print("Nested Dictionary:", nested_dict)

#----------------------------------------------------------------------------------------------------------------------#
# --------------------------------Dictionary Comprehensions in Data Structures--------------------------------------

# Basic Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
square_dict = {num: num ** 2 for num in numbers}
print("Square dictionary:", square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary Comprehension with Filtering
even_square_dict = {num: num ** 2 for num in numbers if num % 2 == 0}
print("Even square dictionary:", even_square_dict)  # Output: {2: 4, 4: 16}

# Merging Two Dictionaries Using Comprehension
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {key: value for d in [dict1, dict2] for key, value in d.items()}
print("Merged dictionary:", merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Creating a Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print("Combined dictionary:", combined_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Inverting a Dictionary (Swapping Keys and Values)
inverted_dict = {value: key for key, value in square_dict.items()}
print("Inverted dictionary:", inverted_dict)  # Output: {1: 1, 4: 2, 9: 3, 16: 4, 25: 5}
