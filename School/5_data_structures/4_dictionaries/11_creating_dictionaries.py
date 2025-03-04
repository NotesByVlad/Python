#----------------------------------------   Creating Dictionaries   ------------------------------------------------#
#                                            ----------------------

"""
In Python, dictionaries can be created in several ways. You can use curly braces `{}`, the `dict()` constructor,
or dictionary comprehensions.
"""

# Key Points about Creating Dictionaries:
'''
1. Dictionaries can be created using curly braces `{}` with key-value pairs.
2. The `dict()` constructor allows for creating dictionaries from other mappings or iterables.
3. Dictionary comprehensions provide a concise way to create dictionaries from existing iterables.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Creating a Dictionary using Curly Braces
"""
This is the most common way to create dictionaries. Key-value pairs are separated by a colon.
"""
my_dict1 = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}
print("Dictionary using curly braces:", my_dict1)

# 2. Creating a Dictionary using the `dict()` Constructor
"""
You can use the `dict()` constructor to create a dictionary from a sequence of key-value pairs.
"""
my_dict2 = dict(name="Bob", age=25, city="Dreamland")
print("Dictionary using `dict()` constructor:", my_dict2)

# 3. Creating a Dictionary from a List of Tuples
"""
You can also create dictionaries from a list of key-value pairs (tuples).
"""
my_list = [("name", "Charlie"), ("age", 22), ("city", "Utopia")]
my_dict3 = dict(my_list)
print("Dictionary from list of tuples:", my_dict3)

# 4. Creating a Dictionary using Dictionary Comprehension
"""
Dictionary comprehensions allow creating dictionaries by transforming an existing iterable.
"""
my_dict4 = {x: x**2 for x in range(5)}
print("Dictionary using comprehension:", my_dict4)

#----------------------------------------------------------------------------------------------------------------------#
