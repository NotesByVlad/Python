#----------------------------------------   Copying Dictionaries   ------------------------------------------------#
#                                            --------------------------

"""
Dictionaries in Python are mutable, and copying them correctly is essential to avoid unintended side effects.
Python provides methods to create shallow and deep copies of dictionaries, each suitable for different use cases.
"""

# Key Points about Copying Dictionaries:
'''
1. Assignment (`=`) creates a reference to the same dictionary; changes affect both references.
2. The `copy` method creates a shallow copy of the dictionary.
3. Use the `copy` module for creating deep copies when nested structures are involved.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": {
        "city": "Wonderland",
        "region": "Fantasy"
    }
}

# 1. Copying by Reference
"""
Using the `=` operator does not create a copy; it creates a reference to the original dictionary.
Changes to one will affect the other.
"""
ref_dict = my_dict
ref_dict["age"] = 26
print("Original after reference modification:", my_dict)

# 2. Creating a Shallow Copy with `copy`
"""
The `copy` method creates a shallow copy. Changes to top-level keys in the copied dictionary
do not affect the original. However, changes to nested objects (e.g., other dictionaries or lists)
will affect both due to shared references.
"""
shallow_copy = my_dict.copy()
shallow_copy["name"] = "Bob"  # Change top-level key
shallow_copy["location"]["city"] = "Neverland"  # Change nested key
print("Original after shallow copy modification:", my_dict)
print("Shallow copy:", shallow_copy)

# 3. Creating a Deep Copy with `copy.deepcopy`
"""
To avoid shared references for nested objects, use the `copy.deepcopy` function from the `copy` module.
This creates a completely independent copy.
"""
import copy

deep_copy = copy.deepcopy(my_dict)
deep_copy["location"]["city"] = "Dreamland"  # Change nested key
print("Original after deep copy modification:", my_dict)
print("Deep copy:", deep_copy)

#----------------------------------------------------------------------------------------------------------------------#
