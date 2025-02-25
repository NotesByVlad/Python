#---------------------------------------- If Statements in Python -----------------------------------------------------#
#                                        -------------------------

"""
An `if` statement is used to evaluate a condition. If the condition is `True`, a block of code will be executed.
It is the simplest form of conditional statement and is essential for decision-making in programming.
"""

# Key Points about If Statements:
'''
1. Conditional: Executes a block of code if a specified condition is true.
2. Simple Decision: Best used when you only need to check a single condition.
3. Single Block: Can be used independently without `elif` or `else`.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic If Statement
'''
The basic syntax of an `if` statement is:
if condition:
    # Code block
'''

# Example:
print("Basic If Statement Example:")
x = 10
if x > 5:
    print("x is greater than 5")

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using If with Comparison Operators
'''
Comparison operators like `>`, `<`, `>=`, `<=`, `==`, and `!=` are commonly used in `if` statements.
'''

# Example:
print("\nIf with Comparison Operators:")
y = 15
if y == 15:
    print("y is equal to 15")

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using If with Logical Operators
'''
Logical operators `and`, `or`, and `not` can be used to combine multiple conditions in an `if` statement.
'''

# Example:
print("\nIf with Logical Operators:")
age = 20
has_permission = True
if age >= 18 and has_permission:
    print("You can access this content.")

#----------------------------------------------------------------------------------------------------------------------#

# 4. Nested If Statements
'''
`if` statements can be nested inside other `if` statements for more complex decision-making.
'''

# Example:
print("\nNested If Statements:")
a = 10
b = 5
if a > 0:
    if b > 0:
        print("Both a and b are positive.")
    else:
        print("b is non-positive.")

#----------------------------------------------------------------------------------------------------------------------#

# 5. Common Pitfalls
'''
1. Incorrect indentation: Python uses indentation to define code blocks. Improper indentation can result in errors.
2. Not using comparison operators correctly (e.g., using `=` instead of `==`).
'''

# Example of Common Pitfall (Incorrect Comparison):
# x = 10
# if x = 10:  # Incorrect, should be `==` for comparison
#     print("x is 10")

#----------------------------------------------------------------------------------------------------------------------#
