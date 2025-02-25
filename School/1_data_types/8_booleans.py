#----------------------------------------   Booleans in Python   ------------------------------------------------------#
#                                        -----------------------

"""
In Python, a boolean is a data type with two possible values: `True` and `False`.
Booleans are often used in conditional statements and expressions to represent
truth values or to control the flow of a program.

Boolean values are derived from expressions and can also be explicitly set.
They are instances of the `bool` class.
"""

# Key Points about Booleans:
'''
Two Possible Values: `True` and `False`.
Conditional Control: Booleans are commonly used in if-else conditions.
Logical Operations: Booleans can be combined using logical operators like `and`, `or`, and `not`.
Derived from Expressions: Many expressions evaluate to a boolean value (e.g., comparisons).
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Boolean Values
bool_true = True
bool_false = False
print("Boolean True:", bool_true)
print("Boolean False:", bool_false)

# 2. Booleans from Expressions
is_equal = (5 == 5)  # True
is_not_equal = (5 != 3)  # True
is_greater = (10 > 5)  # True
is_less_or_equal = (5 <= 5)  # True

print("\nIs 5 equal to 5?", is_equal)
print("Is 5 not equal to 3?", is_not_equal)
print("Is 10 greater than 5?", is_greater)
print("Is 5 less than or equal to 5?", is_less_or_equal)

# 3. Boolean and Non-Boolean Values
'''
In Python, many non-boolean values can be evaluated in a boolean context:
- `0`, `None`, empty collections (`[]`, `{}`, `''`) are considered `False`.
- Non-zero numbers and non-empty collections are considered `True`.
'''

print("\nBoolean value of 0:", bool(0))
print("Boolean value of 1:", bool(1))
print("Boolean value of an empty string:", bool(''))
print("Boolean value of a non-empty string:", bool('Python'))

# 4. Logical Operators
bool_and = True and False  # False
bool_or = True or False  # True
bool_not = not True  # False

print("\nLogical AND (True and False):", bool_and)
print("Logical OR (True or False):", bool_or)
print("Logical NOT (not True):", bool_not)

# 5. Using Booleans in Conditional Statements
age = 18
if age >= 18:
    print("\nEligible to vote!")
else:
    print("\nNot eligible to vote.")

# 6. Combining Conditions
has_id = True
is_adult = age >= 18
if has_id and is_adult:
    print("Access granted.")
else:
    print("Access denied.")

# 7. Boolean Methods
'''
Some Python data types have methods that return boolean values.
Examples include:
- `str.isdigit()`: Check if a string contains only digits.
- `str.isalpha()`: Check if a string contains only letters.
- `list.isEmpty()`: Check if a list is empty (via boolean casting).
'''

example_string = "12345"
print("\nIs '12345' all digits?", example_string.isdigit())
print("Is 'Python123' all alphabetic?", "Python123".isalpha())

# 8. Short-Circuit Evaluation
'''
Logical operators `and` and `or` perform short-circuit evaluation:
- `and` stops evaluating as soon as it encounters `False`.
- `or` stops evaluating as soon as it encounters `True`.
'''

x = 10
result = (x > 5) and (x < 20)  # True
print("\nShort-Circuit AND Evaluation:", result)

# 9. Boolean in Data Structures
'''
Booleans can be used in data structures such as lists, tuples, and dictionaries.
'''
bool_list = [True, False, True]
print("\nBoolean List:", bool_list)

# 10. Casting to Boolean
'''
You can explicitly cast values to boolean using the `bool()` function.
'''
print("\nCasting 0 to Boolean:", bool(0))  # False
print("Casting 100 to Boolean:", bool(100))  # True
print("Casting an empty list to Boolean:", bool([]))  # False

#----------------------------------------------------------------------------------------------------------------------#
