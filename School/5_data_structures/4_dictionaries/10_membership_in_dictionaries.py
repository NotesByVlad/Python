#----------------------------------------   Checking Membership in Dictionaries   ------------------------------------------------#
#                                            --------------------------

"""
In Python, membership operators (`in` and `not in`) can be used to check for the presence of keys in a dictionary.
Membership testing is efficient and is primarily focused on the dictionary's keys.
"""

# Key Points about Checking Membership in Dictionaries:
'''
1. The `in` operator checks if a key exists in the dictionary.
2. The `not in` operator checks if a key does not exist in the dictionary.
3. Membership testing is case-sensitive and works only on keys, not values.
4. To check membership in values, use the `values()` method.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland"
}

# 1. Checking Key Membership Using `in`
"""
Use `in` to check if a key exists in the dictionary.
"""
print("Is 'name' a key in the dictionary?", 'name' in my_dict)
print("Is 'profession' a key in the dictionary?", 'profession' in my_dict)

# 2. Checking Key Membership Using `not in`
"""
Use `not in` to check if a key does not exist in the dictionary.
"""
print("Is 'age' not a key in the dictionary?", 'age' not in my_dict)
print("Is 'hobby' not a key in the dictionary?", 'hobby' not in my_dict)

# 3. Checking Membership in Values
"""
To check if a value exists in the dictionary, use the `values()` method.
"""
print("Is 'Alice' a value in the dictionary?", 'Alice' in my_dict.values())
print("Is 'Explorer' a value in the dictionary?", 'Explorer' in my_dict.values())

# 4. Checking Membership in Key-Value Pairs (Advanced)
"""
To check for specific key-value pairs, use the `items()` method.
"""
print("Is ('name', 'Alice') a key-value pair in the dictionary?", ('name', 'Alice') in my_dict.items())
print("Is ('age', 30) a key-value pair in the dictionary?", ('age', 30) in my_dict.items())

#----------------------------------------------------------------------------------------------------------------------#
