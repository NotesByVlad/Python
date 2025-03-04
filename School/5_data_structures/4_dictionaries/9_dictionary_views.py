#----------------------------------------   Dictionary Views   ------------------------------------------------#
#                                            --------------------------

"""
In Python, dictionary views provide dynamic views on the dictionary’s entries (keys, values, and items).
They allow you to interact with and iterate over the contents of a dictionary in real-time, reflecting changes made to the dictionary.
"""

# Key Points about Dictionary Views:
'''
1. Methods like `keys()`, `values()`, and `items()` return view objects.
2. Views reflect real-time changes to the dictionary.
3. Views are iterable and can be converted to lists if needed.
4. They provide a memory-efficient way to work with dictionary data.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland"
}

# 1. Viewing Keys Using `keys()`
"""
The `keys()` method returns a view of the dictionary's keys.
"""
keys_view = my_dict.keys()
print("Keys View:", keys_view)

# Iterating Over Keys
for key in keys_view:
    print("Key:", key)

# 2. Viewing Values Using `values()`
"""
The `values()` method returns a view of the dictionary's values.
"""
values_view = my_dict.values()
print("Values View:", values_view)

# Iterating Over Values
for value in values_view:
    print("Value:", value)

# 3. Viewing Key-Value Pairs Using `items()`
"""
The `items()` method returns a view of the dictionary's key-value pairs as tuples.
"""
items_view = my_dict.items()
print("Items View:", items_view)

# Iterating Over Key-Value Pairs
for key, value in items_view:
    print(f"{key}: {value}")

# 4. Real-Time Updates in Views
"""
Modifying the dictionary reflects immediately in the views.
"""
my_dict["profession"] = "Explorer"
print("Keys View After Update:", keys_view)
print("Values View After Update:", values_view)
print("Items View After Update:", items_view)

#----------------------------------------------------------------------------------------------------------------------#
