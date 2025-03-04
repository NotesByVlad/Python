#----------------------------------------   Iterating Over Dictionaries   ------------------------------------------------#
#                                            --------------------------

"""
Dictionaries in Python allow iteration over their keys, values, or key-value pairs.
These iterations are efficient and make it easy to access and manipulate dictionary contents.
"""

# Key Points about Iterating Over Dictionaries:
'''
1. Iterating over a dictionary by default yields its keys.
2. Use `values()` to iterate over values only.
3. Use `items()` to iterate over key-value pairs.
4. Iteration order reflects the insertion order (Python 3.7+).
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland"
}

# 1. Iterating Over Keys
"""
By default, iterating over a dictionary yields its keys.
"""
print("Keys:")
for key in my_dict:
    print(key)

# 2. Iterating Over Values
"""
Use the `values()` method to iterate over the dictionary's values.
"""
print("Values:")
for value in my_dict.values():
    print(value)

# 3. Iterating Over Key-Value Pairs
"""
Use the `items()` method to iterate over key-value pairs as tuples.
"""
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 4. Enumerating Keys (Optional Use Case)
"""
If you need the index along with the keys, use `enumerate`.
"""
print("Enumerated Keys:")
for index, key in enumerate(my_dict):
    print(f"{index}: {key}")

#----------------------------------------------------------------------------------------------------------------------#
