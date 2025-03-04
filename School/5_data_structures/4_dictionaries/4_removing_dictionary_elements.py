#----------------------------------------   Removing Dictionary Elements   ------------------------------------------------#
#                                            --------------------------

"""
In Python, dictionaries are mutable, and elements can be removed using various methods.
These operations allow you to delete specific key-value pairs, remove arbitrary pairs,
or clear the dictionary entirely.
"""

# Key Points about Removing Dictionary Elements:
'''
1. Use `pop` to remove a key and return its value. It raises a KeyError if the key doesn’t exist (unless a default is provided).
2. The `popitem` method removes and returns an arbitrary key-value pair (useful for Python 3.7+ where insertion order is maintained).
3. The `del` statement can be used to delete specific keys or the entire dictionary.
4. The `clear` method removes all elements from the dictionary.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland",
    "profession": "Explorer"
}

# 1. Removing a Specific Key-Value Pair Using `pop`
"""
The `pop` method removes a key-value pair and returns the value associated with the key.
If the key is not found, it raises a KeyError unless a default is specified.
"""
age = my_dict.pop("age")
print("Removed 'age':", age)
print("After pop:", my_dict)

# 2. Removing an Arbitrary Key-Value Pair Using `popitem`
"""
The `popitem` method removes and returns the last inserted key-value pair as a tuple.
Useful for efficiently managing dictionary entries in order.
"""
last_item = my_dict.popitem()
print("Removed arbitrary key-value pair:", last_item)
print("After popitem:", my_dict)

# 3. Deleting a Key or the Entire Dictionary Using `del`
"""
The `del` statement can delete a specific key or the entire dictionary.
"""
del my_dict["location"]
print("After deleting 'location':", my_dict)

# Uncomment the line below to delete the entire dictionary:
# del my_dict

# 4. Removing All Key-Value Pairs Using `clear`
"""
The `clear` method removes all elements, leaving an empty dictionary.
"""
my_dict.clear()
print("After clear:", my_dict)

#----------------------------------------------------------------------------------------------------------------------#
