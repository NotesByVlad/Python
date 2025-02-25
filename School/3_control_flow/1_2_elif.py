#---------------------------------------- Elif Statements in Python ---------------------------------------------------#
#                                        ---------------------------

"""
The `elif` statement in Python allows you to check multiple conditions. It is short for "else if" and is used
when you have more than two possible conditions to evaluate. It follows an initial `if` statement and can be
followed by one or more additional `elif` statements, ending with an optional `else`.
"""

# Key Points about Elif Statements:
'''
1. Multiple Conditions: Allows checking of multiple conditions.
2. Following an If: `elif` must come after an `if` statement.
3. Optional Else: The `else` statement is optional after `elif` statements.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Elif Statement
'''
An `elif` statement is used to check additional conditions after the first `if`.
'''

# Example:
print("Basic Elif Statement Example:")
x = 5
if x > 10:
    print("x is greater than 10")
elif x > 0:
    print("x is greater than 0 but less than or equal to 10")
else:
    print("x is less than or equal to 0")

#----------------------------------------------------------------------------------------------------------------------#

# 2. Multiple Elif Conditions
'''
You can have multiple `elif` statements to check for several conditions in sequence.
'''

# Example:
print("\nMultiple Elif Conditions:")
y = 18
if y > 20:
    print("y is greater than 20")
elif y > 10:
    print("y is greater than 10 but less than or equal to 20")
elif y > 5:
    print("y is greater than 5 but less than or equal to 10")
else:
    print("y is 5 or less")

#----------------------------------------------------------------------------------------------------------------------#

# 3. Elif with Logical Operators
'''
You can also use logical operators (`and`, `or`, `not`) with `elif` statements to combine multiple conditions.
'''

# Example:
print("\nElif with Logical Operators:")
age = 16
has_permission = False
if age >= 18:
    print("You are an adult.")
elif age >= 13 and has_permission:
    print("You are a teenager with permission.")
else:
    print("You are underage.")

#----------------------------------------------------------------------------------------------------------------------#

# 4. Elif Without Else
'''
You do not need to include an `else` block if there is no "default" condition required.
'''

# Example:
print("\nElif Without Else:")
z = 20
if z < 10:
    print("z is less than 10")
elif z == 20:
    print("z is 20")

#----------------------------------------------------------------------------------------------------------------------#

# 5. Common Pitfalls
'''
1. Forgetting to use `elif` after the first `if` statement.
2. Improperly ordering `if`, `elif`, and `else` (remember: `elif` comes after `if`).
3. Using `elif` with no preceding `if` statement.
'''

# Example of Common Pitfall:
# if x == 10:
#     print("x is 10")
# elif x == 10:  # Redundant, same condition as the first `if`
#     print("x is still 10")

#----------------------------------------------------------------------------------------------------------------------#
