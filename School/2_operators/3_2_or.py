#---------------------------------------- Logical Operator: OR in Python ----------------------------------------------#
#                                        --------------------------------

"""
The `or` operator is a logical operator that returns True if at least one of the conditions is true.
It is used to check if at least one of the multiple conditions is true.
"""

# Key Points about `or` Operator:
'''
1. The `or` operator returns True if at least one of the conditions is True.
2. If both conditions are False, the result of the expression will be False.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `or`
# Example: Checking if at least one condition is true.
print("Basic OR Example:")
x = 10
y = 5
if x > 5 or y > 10:
    print("At least one condition is True!")
else:
    print("Both conditions are False!")

# Output: At least one condition is True!
# x > 5 is True, so the overall condition is True even though y > 10 is False.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Combining Multiple Conditions with `or`
# Example: Checking if at least one condition out of many is true.
print("\nCombining Multiple Conditions with OR:")
x = 5
y = 3
z = 10
if x > y or z > y or x < 0:
    print("At least one condition is True!")
else:
    print("All conditions are False!")

# Output: At least one condition is True!
# x > y is True, so the overall condition is True.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Short-circuit Behavior of `or`
# Example: If the first condition is True, the second condition is not evaluated.
print("\nShort-circuit Behavior of OR:")
x = 10
y = 20
if x < 5 or y > 10:  # Since x < 5 is False, y > 10 is evaluated and it is True
    print("At least one condition is True!")
else:
    print("Both conditions are False!")

# Output: At least one condition is True!
# The second condition y > 10 is True, so the overall condition is True.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `or` with Other Logical Operators
# Example: Combining `or` with `and` to create more complex conditions.
print("\nUsing OR with AND:")
x = 10
y = 5
z = 3
if (x > 5 and y < 10) or z < 0:
    print("The complex condition is True!")
else:
    print("The complex condition is False!")

# Output: The complex condition is True!
# (x > 5 and y < 10) is True, so the overall condition is True, even though z < 0 is False.

#----------------------------------------------------------------------------------------------------------------------#
