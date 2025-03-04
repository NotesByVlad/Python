#----------------------------------------   Converting Tuple to Other Data Structures   -------------------------#
#                                            ------------------------

"""
You can convert a tuple into other data structures like lists, sets, or dictionaries.

Key Points:
1. Convert a tuple to a list using list().
2. Convert a tuple to a set to remove duplicates using set().
3. Convert a tuple to dictionary keys using dict.fromkeys().
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Converting Tuple to List
"""
Convert the tuple to a list.
"""
my_list = list(my_tuple)
print("Converted to list:", my_list)

# 2. Converting Tuple to Set
"""
Convert the tuple to a set (removes duplicates).
"""
my_set = set(my_tuple)
print("Converted to set:", my_set)

# 3. Converting Tuple to Dictionary Keys
"""
Convert the tuple to dictionary keys using dict.fromkeys() (values are None).
"""
my_dict = dict.fromkeys(my_tuple)
print("Converted to dictionary keys:", my_dict)

#----------------------------------------------------------------------------------------------------------------------#
