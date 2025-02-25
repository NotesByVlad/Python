#---------------------------------------- Logical Operator: NOT in Python ---------------------------------------------#
#                                        ---------------------------------

"""
The `not` operator is a logical operator that inverts the truth value of a condition.
If the condition is True, it becomes False, and if it is False, it becomes True.
"""

# Key Points about `not` Operator:
'''
1. The `not` operator is used to invert the boolean value of an expression.
2. If the expression evaluates to True, `not` will make it False.
3. If the expression evaluates to False, `not` will make it True.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `not`
# Example: Inverting a boolean condition.
print("Basic NOT Example:")
x = 10
if not x < 5:
    print("x is not less than 5!")
else:
    print("x is less than 5.")

# Output: x is not less than 5!
# The condition x < 5 is False, so `not` makes it True.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using `not` with Other Logical Operators
# Example: Using `not` to negate a condition combined with `and` or `or`.
print("\nUsing NOT with AND and OR:")
x = 10
y = 5
if not (x > 5 and y < 3):
    print("The condition is False!")
else:
    print("The condition is True!")

# Output: The condition is False!
# The condition (x > 5 and y < 3) is True, so `not` inverts it to False.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Short-circuit Behavior of `not`
# Example: Demonstrating the effect of `not` on conditions.
print("\nShort-circuit Behavior of NOT:")
x = 0
y = 10
if not x > 0 or y < 20:  # Since `not x > 0` is True, the second part is not evaluated
    print("At least one condition is True!")
else:
    print("Both conditions are False!")

# Output: At least one condition is True!
# `not x > 0` is True, so the second condition is not evaluated.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `not` with Equality
# Example: Negating equality conditions.
print("\nUsing NOT with Equality:")
x = 5
if not x == 10:
    print("x is not equal to 10!")
else:
    print("x is equal to 10.")

# Output: x is not equal to 10!
# The condition x == 10 is False, so `not` makes it True.

#----------------------------------------------------------------------------------------------------------------------#
