#---------------------------------------- Else Statements in Python ---------------------------------------------------#
#                                        ---------------------------

"""
The `else` statement in Python provides a block of code that runs when all preceding `if` and `elif`
conditions are false.
It is used as a fallback when none of the conditions are met.
"""

# Key Points about Else Statements:
'''
1. Default Action: The `else` block is executed if all prior conditions are `False`.
2. Optional: The `else` statement is not required, but it helps handle cases when no conditions are met.
3. Must Follow if/elif: The `else` statement must come after all `if` and `elif` statements.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Else Statement
'''
The `else` block runs only when all preceding `if` and `elif` conditions evaluate to `False`.
'''

# Example:
print("Basic Else Statement Example:")
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using Else After If and Elif
'''
The `else` statement can be used after `if` and `elif` statements to handle the default case.
'''

# Example:
print("\nElse After If and Elif:")
y = 12
if y > 20:
    print("y is greater than 20")
elif y > 10:
    print("y is greater than 10 but less than or equal to 20")
else:
    print("y is 10 or less")

#----------------------------------------------------------------------------------------------------------------------#

# 3. Else Without Any Condition
'''
The `else` statement does not have a condition and executes when no other conditions are met.
'''

# Example:
print("\nElse Without Any Condition:")
number = 0
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

#----------------------------------------------------------------------------------------------------------------------#

# 4. Common Pitfalls
'''
1. Using `else` without a preceding `if` or `elif` statement (invalid syntax).
2. Misplacing the `else` block (it must come after all `if`/`elif` statements).
3. Forgetting to handle all possible conditions when using `else` (if not handled, unexpected results can occur).
'''

# Example of Common Pitfall:
# x = 10
# else:  # This will raise a SyntaxError because `else` must follow `if` or `elif`
#     print("Invalid")

#----------------------------------------------------------------------------------------------------------------------#
