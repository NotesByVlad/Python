#----------------------------------------   Modifying Dictionary Elements   ------------------------------------------------#
#                                            --------------------------

"""
Dictionaries in Python are mutable, meaning you can modify their contents after creation. Modifying a dictionary
involves adding, updating, or removing key-value pairs. Python provides intuitive ways to handle these operations.
"""

# Key Points about Modifying Dictionary Elements:
'''
1. Adding new key-value pairs can be done by assigning a value to a new key.
2. Updating the value of an existing key overwrites the previous value.
3. The `update` method allows bulk updates from another dictionary or iterable of key-value pairs.
4. The `setdefault` method sets a default value for a key if it does not already exist.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland"
}

# 1. Adding a New Key-Value Pair
"""
Simply assign a value to a new key to add it to the dictionary.
"""
my_dict["profession"] = "Explorer"
print("After adding profession:", my_dict)

# 2. Updating an Existing Key's Value
"""
Assigning a new value to an existing key will overwrite its current value.
"""
my_dict["age"] = 26  # Update age
print("After updating age:", my_dict)

# 3. Using the `update` Method
"""
The `update` method can update multiple key-value pairs simultaneously, either from
another dictionary or an iterable of key-value pairs.
"""
my_dict.update({"location": "Neverland", "hobby": "Adventuring"})
print("After updating with update method:", my_dict)

# 4. Using the `setdefault` Method
"""
The `setdefault` method sets a value for a key if the key is not already in the dictionary.
If the key exists, it returns its current value without changing it.
"""
my_dict.setdefault("nickname", "Ali")  # Add new key with default value
my_dict.setdefault("age", 30)          # Existing key, no change to value
print("After using setdefault:", my_dict)

#----------------------------------------------------------------------------------------------------------------------#
