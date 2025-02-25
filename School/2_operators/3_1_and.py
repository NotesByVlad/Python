#---------------------------------------- Logical Operator: AND in Python ---------------------------------------------#
#                                        ---------------------------------

"""
The `and` operator is a logical operator that returns True if both conditions are true.
It is commonly used in conditional statements to check if multiple conditions are met simultaneously.
"""

# Key Points about `and` Operator:
'''
1. The `and` operator returns True only if both conditions on either side of it are True.
2. If either condition is False, the result of the expression will be False.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `and`
# Example: Checking if two conditions are true.
print("Basic AND Example:")
x = 10
y = 5
if x > 5 and y < 10:
    print("Both conditions are True!")
else:
    print("At least one condition is False!")

# Output: Both conditions are True!
# x is greater than 5 and y is less than 10, so both conditions are True.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Combining Multiple Conditions with `and`
# Example: Checking multiple conditions in a single if statement.
print("\nCombining Multiple Conditions with AND:")
x = 15
y = 10
z = 5
if x > y and y > z and z > 0:
    print("All conditions are True!")
else:
    print("One or more conditions are False!")

# Output: All conditions are True!
# All the conditions x > y, y > z, and z > 0 are True.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Short-circuit Behavior of `and`
# Example: If the first condition is False, the second condition is not evaluated.
print("\nShort-circuit Behavior of AND:")
x = 0
y = 10
if x > 0 and y < 20:  # Since x > 0 is False, y < 20 is not even checked
    print("Both conditions are True!")
else:
    print("At least one condition is False!")

# Output: At least one condition is False!
# x > 0 is False, so the second condition is not evaluated.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `and` with Other Logical Operators
# Example: Combining `and` with `or` to create more complex conditions.
print("\nUsing AND with OR:")
x = 10
y = 5
z = 3
if (x > 5 or y < 10) and z > 0:
    print("The complex condition is True!")
else:
    print("The complex condition is False!")

# Output: The complex condition is True!
# The condition (x > 5 or y < 10) is True, and z > 0 is also True, so the entire condition is True.

#----------------------------------------------------------------------------------------------------------------------#
