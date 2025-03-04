#----------------------------------------   Merging Dictionaries   ------------------------------------------------#
#                                            --------------------------

"""
Merging dictionaries in Python involves combining key-value pairs from two or more dictionaries.
Python offers multiple techniques for merging dictionaries, ranging from traditional methods
like `update` to newer operators introduced in recent Python versions.
"""

# Key Points about Merging Dictionaries:
'''
1. The `update` method adds key-value pairs from one dictionary to another, overwriting existing keys.
2. The `|` operator (Python 3.9+) creates a new dictionary by merging two dictionaries.
3. The `|=` operator (Python 3.9+) updates an existing dictionary in place.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionaries
dict1 = {
    "name": "Alice",
    "age": 25
}
dict2 = {
    "location": "Wonderland",
    "age": 26  # Overlapping key
}

# 1. Using the `update` Method
"""
The `update` method adds key-value pairs from one dictionary to another. It modifies the
original dictionary in place.
"""
dict1.update(dict2)
print("After update:", dict1)

# 2. Using the `|` Operator (Python 3.9+)
"""
The `|` operator creates a new dictionary that is the result of merging two dictionaries.
It does not modify the original dictionaries.
"""
merged_dict = dict1 | dict2
print("Merged using | operator:", merged_dict)

# 3. Using the `|=` Operator (Python 3.9+)
"""
The `|=` operator updates the dictionary on the left in place, similar to `update`.
"""
dict1 |= {"hobby": "Adventuring"}
print("After |= operator:", dict1)

#----------------------------------------------------------------------------------------------------------------------#
