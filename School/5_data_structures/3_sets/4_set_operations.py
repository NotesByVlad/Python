#----------------------------------------   Set Operations   --------------------------------------------------#
#                                            ------------------------

"""
Python sets support several operations such as union, intersection, difference, and symmetric difference.

Key Points:
1. Union combines elements from two sets.
2. Intersection returns elements common to both sets.
3. Difference returns elements only in the first set.
4. Symmetric difference returns elements in either set, but not both.
"""

# Example Sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# 1. Union of Sets
"""
Combine all elements from two sets using union().
"""
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of sets:", set1.union(set2))

# 2. Intersection of Sets
"""
Get the common elements between two sets using intersection().
"""
print("Intersection of sets:", set1.intersection(set2))

# 3. Difference of Sets
"""
Get the elements that are in set1 but not in set2 using difference().
"""
print("Difference of sets (set1 - set2):", set1.difference(set2))

# 4. Symmetric Difference of Sets
"""
Get elements that are in either set, but not in both, using symmetric_difference().
"""
print("Symmetric difference of sets:", set1.symmetric_difference(set2))

#----------------------------------------------------------------------------------------------------------------------#
