#---------------------------------------- Conditional Statements in Python --------------------------------------------#
#                                        ----------------------------------

"""
Conditional statements in programming allow you to execute certain parts of code based on specific conditions.
They help in decision-making by executing different code blocks depending on whether a given condition is true or false.
Python provides several ways to write conditional statements.
"""

# Key Points about Conditional Statements:
'''
Decision-Making: They control the flow of a program based on conditions.
Boolean Expressions: Conditional statements use Boolean expressions 
(conditions that evaluate to True or False).
Indentation: Python uses indentation to define the code blocks 
that belong to the condition.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic if Statement
'''
The `if` statement is used to execute a block of code if a given condition is True.
'''

# Example:
x = 10
if x > 5:
    print("x is greater than 5")

#----------------------------------------------------------------------------------------------------------------------#

# 2. if-else Statement
'''
The `if-else` statement executes one block of code if the condition is True and another block if the condition is False.
'''

# Example:
y = 7
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

#----------------------------------------------------------------------------------------------------------------------#

# 3. if-elif-else Statement
'''
The `if-elif-else` statement allows multiple conditions to be checked in sequence. 
As soon as one condition evaluates to True, the corresponding block is executed, and the rest are skipped.
'''

# Example:
z = -1
if z > 0:
    print("z is positive")
elif z == 0:
    print("z is zero")
else:
    print("z is negative")

#----------------------------------------------------------------------------------------------------------------------#

# 4. Nested if Statements
'''
You can use nested `if` statements to check conditions within conditions. 
While powerful, excessive nesting can make the code harder to read.
'''

# Example:
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")

#----------------------------------------------------------------------------------------------------------------------#

# 5. Ternary Conditional Operator
'''
Python supports a shorthand for the `if-else` statement called the ternary operator.
Syntax: `value_if_true if condition else value_if_false`
'''

# Example:
age = 18
status = "Adult" if age >= 18 else "Minor"
print("\nTernary Result:", status)

#----------------------------------------------------------------------------------------------------------------------#

# 6. Logical Operators in Conditions
'''
Logical operators `and`, `or`, and `not` are often used to combine or modify conditions.
'''

# Example:
num = 8
if num > 0 and num % 2 == 0:
    print("num is a positive even number")

if not (num < 0):
    print("num is not negative")

#----------------------------------------------------------------------------------------------------------------------#

# 7. Membership and Identity Operators in Conditions
'''
Membership (`in`, `not in`) and identity (`is`, `is not`) operators can also be used in conditional statements.
'''

# Example:
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("\nApple is in the list")

if fruits is not None:
    print("The fruits list exists")

#----------------------------------------------------------------------------------------------------------------------#

# 8. Checking with isinstance
'''
Use `isinstance` to check the data type of a variable.
'''

# Example:
value = 42
if isinstance(value, int):
    print("\nValue is an integer")

#----------------------------------------------------------------------------------------------------------------------#

# 9. Combining Multiple Conditions
'''
Combine multiple conditions to make more complex decisions.
'''

# Example:
temp = 25
weather = "sunny"

if temp > 20 and weather == "sunny":
    print("\nIt's a nice day for a walk")

#----------------------------------------------------------------------------------------------------------------------#

# 10. Guard Clauses
'''
Guard clauses are a way to handle edge cases early and improve code readability.
'''

# Example:
def check_number(n):
    if n < 0:
        return "Number is negative"
    if n == 0:
        return "Number is zero"
    return "Number is positive"

print("\nGuard Clause Result:", check_number(5))

#----------------------------------------------------------------------------------------------------------------------#

# 11. Common Pitfalls
'''
1. Forgetting to use proper indentation.
2. Using `=` instead of `==` in conditions.
3. Not handling all possible cases (e.g., missing an `else` block).
'''

# Example:
# Incorrect: if x = 5: (This will cause a syntax error)
# Correct: if x == 5:

#----------------------------------------------------------------------------------------------------------------------#
