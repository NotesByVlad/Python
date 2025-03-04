#----------------------------------------   Performance Considerations in Dictionaries   ------------------------------------------------#
#                                            -------------------------------------------

"""
Dictionaries in Python are highly optimized for performance. This section explores the time complexities of common
dictionary operations and when dictionaries should be used over other data structures.
"""

# Key Points about Dictionary Performance:
'''
1. Dictionary operations like lookup, insertion, and deletion are generally O(1), which makes them very efficient.
2. However, dictionaries use more memory than other data structures like lists or sets.
3. Understanding when to use dictionaries can significantly improve the performance of your program.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Time Complexity of Common Dictionary Operations
"""
Dictionaries provide O(1) average time complexity for the following operations:
- Lookup (key access)
- Insertion of a new key-value pair
- Deletion of a key-value pair
This means that these operations take constant time, regardless of the size of the dictionary.
"""

# Example of O(1) Lookup
my_dict = {"name": "Alice", "age": 30, "location": "Wonderland"}
print("Name:", my_dict["name"])  # O(1) lookup
print("Age:", my_dict["age"])    # O(1) lookup

# 2. Insertion Performance
"""
Inserting a new key-value pair into a dictionary is an O(1) operation on average.
"""
my_dict["profession"] = "Engineer"  # O(1) insertion
print("After Insertion:", my_dict)

# 3. Deletion Performance
"""
Deleting a key-value pair using `del` or `pop()` is also an O(1) operation on average.
"""
del my_dict["location"]  # O(1) deletion
print("After Deletion:", my_dict)

# 4. Memory Considerations
"""
Dictionaries in Python use hash tables, which allows them to have O(1) time complexity for most operations.
However, hash tables use more memory than other data structures like lists.
"""

import sys
print("Memory Usage of Dictionary:", sys.getsizeof(my_dict))  # Check memory size

# 5. When to Use Dictionaries vs Other Data Structures
"""
Dictionaries are preferred over lists when you need fast lookups, insertions, or deletions by key.
However, if you only need sequential access or don't need fast key-based access, lists or sets may be more memory efficient.
"""

#----------------------------------------------------------------------------------------------------------------------#
