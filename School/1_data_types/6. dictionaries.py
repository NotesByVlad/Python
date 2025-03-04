#----------------------------------------   Dictionaries in Python   --------------------------------------------------#
#                                        -----------------------

"""
A dictionary is a collection of key-value pairs. Each key is unique,
and it is used to access its associated value. Dictionaries are one
of the most versatile and commonly used data structures in Python.

Dictionaries are mutable and enclosed in curly braces `{}`. Keys and
values are separated by a colon `:`, and key-value pairs are separated
by commas.
"""

# Key Points about Dictionaries:
'''
Key-Value Pairs: Data is stored as key-value pairs, where keys are unique.
Unordered: Dictionaries do not maintain order (though Python 3.7+ ensures insertion order).
Mutable: Dictionaries can be modified after creation (adding, removing, or updating key-value pairs).
Keys Must Be Immutable: Keys can be strings, numbers, or tuples but not mutable types like lists.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Dictionary Initialization
dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}
dict3 = {'nested': {'key1': 'value1', 'key2': 'value2'}}

# Printing the dictionaries
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)

# 2. Accessing Values
print("\nName in Dictionary 1:", dict1['name'])  # Access using a key
print("Value of key 2 in Dictionary 2:", dict2[2])
print("Nested Value (key1) in Dictionary 3:", dict3['nested']['key1'])

# 3. Adding and Updating Elements
dict1['email'] = 'alice@example.com'  # Adding a new key-value pair
dict1['age'] = 26  # Updating an existing key
print("\nUpdated Dictionary 1:", dict1)

# 4. Removing Elements
dict1.pop('city')  # Remove a specific key-value pair
del dict2[3]       # Delete a key-value pair using `del`
print("\nDictionary 1 after Pop:", dict1)
print("Dictionary 2 after Deletion:", dict2)

# 5. Checking Keys
print("\nIs 'name' in Dictionary 1?", 'name' in dict1)
print("Is 3 in Dictionary 2?", 3 in dict2)

# 6. Iterating Over Dictionaries
print("\nIterating Over Dictionary 1:")
for key, value in dict1.items():
    print(f"{key}: {value}")

# 7. Dictionary Methods
keys = dict1.keys()  # Get all keys
values = dict1.values()  # Get all values
items = dict1.items()  # Get all key-value pairs
print("\nKeys in Dictionary 1:", keys)
print("Values in Dictionary 1:", values)
print("Items in Dictionary 1:", items)

# 8. Merging Dictionaries
dict4 = {'country': 'USA', 'profession': 'Engineer'}
dict1.update(dict4)  # Merge `dict4` into `dict1`
print("\nMerged Dictionary 1:", dict1)

# 9. Default Values with `get`
age = dict1.get('age', 'Not Available')  # Access with a default value
salary = dict1.get('salary', 'Not Available')
print("\nAge in Dictionary 1:", age)
print("Salary in Dictionary 1:", salary)

# 10. Copying Dictionaries
dict_copy = dict1.copy()  # Create a shallow copy
print("\nCopied Dictionary:", dict_copy)

# 11. Clearing a Dictionary
dict_copy.clear()  # Remove all elements
print("Cleared Dictionary:", dict_copy)

# 12. Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}  # Create a dictionary with keys and squared values
print("\nDictionary Comprehension (Squares):", squared_dict)

# 13. Nested Dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print("\nNested Dictionary:", nested_dict)
print("Accessing Person 1's Age:", nested_dict['person1']['age'])

# 14. Dictionaries vs Lists
'''
Dictionaries provide a way to associate meaningful keys with values, 
which can make your data more readable and organized compared to using lists.
'''

# 15. Dictionary Keys Must Be Immutable
'''
Keys can be strings, numbers, or tuples (immutable types), but not lists or dictionaries.
'''
try:
    invalid_dict = {[1, 2]: 'value'}  # This will raise an error
except TypeError as e:
    print("\nError Demonstrating Invalid Key:", e)

#----------------------------------------------------------------------------------------------------------------------#
