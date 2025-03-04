#----------------------------------------   Querying a Set   -------------------------------------------------#
#                                            ------------------------

"""
You can query sets to check membership, get the length, or check if one set is a subset or superset of another.

Key Points:
1. Check if an element exists using 'in'.
2. Check if one set is a subset or superset of another using issubset() and issuperset().
3. Check if two sets are disjoint using isdisjoint().
"""

# Example Sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {10, 20}

# 1. Membership Test
"""
Check if an element exists in a set using 'in'.
"""
print("Is 20 in set1?", 20 in set1)
print("Is 60 in set1?", 60 in set1)

# 2. Checking Subset and Superset
"""
Check if one set is a subset or superset of another.
"""
print("Is set3 a subset of set1?", set3.issubset(set1))
print("Is set1 a superset of set3?", set1.issuperset(set3))

# 3. Checking if Sets are Disjoint
"""
Check if two sets have no common elements using isdisjoint().
"""
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))

# 4. Length of Set
"""
Get the number of elements in the set using len().
"""
print("Length of set1:", len(set1))

#----------------------------------------------------------------------------------------------------------------------#
