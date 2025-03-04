#----------------------------------------   Basic Functions in Python   -----------------------------------------------#
#                                        -------------------------------

"""
In Python, a function is a block of reusable code that is used to perform a specific task.
Functions allow us to break down our program into smaller, manageable pieces.
Functions can accept input through parameters and can return output as a result.

Functions are not a data type themselves, but they are defined using the `def` keyword and can be used to encapsulate
code that performs operations.
"""

# Key Points about Functions:
'''
1. **Function Definition**: A function is defined using the `def` keyword followed by the function name and parentheses.
2. **Parameters**: Functions can take parameters (input values) inside the parentheses.
3. **Return Statement**: Functions can return a value using the `return` statement.
4. **Function Call**: A function is called by using its name followed by parentheses.
5. **Docstrings**: Functions can have a documentation string (docstring) that explains what the function does.
'''

# 1. **Function Definition and Calling**:
# A simple function that takes no parameters and prints a message.
def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

# 2. **Function with Parameters**:
# A function that takes parameters and performs an operation.
def add(a, b):
    return a + b

# Calling the function with arguments
result = add(5, 3)
print(f"Sum of 5 and 3 is: {result}")

# 3. **Function with Return Value**:
# A function that returns a value, which can then be used in expressions.
def multiply(a, b):
    return a * b

product = multiply(4, 6)
print(f"Product of 4 and 6 is: {product}")

# 4. **Function with Default Parameters**:
# Parameters can have default values in case no argument is passed when calling the function.
def greet_user(name="User"):
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet_user("Alice")
greet_user()

# 5. **Function with Multiple Return Values**:
# A function can return multiple values as a tuple.
def division(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = division(10, 3)
print(f"Quotient: {q}, Remainder: {r}")

# 6. **Lambda Functions**:
# Python also supports anonymous functions, called lambda functions. These are small, unnamed functions.
# They are often used for short, throwaway functions.
square = lambda x: x ** 2
print(f"Square of 5 is: {square(5)}")

#----------------------------------------------------------------------------------------------------------------------#

# Variables and Functions
'''
While functions are not a data type, they can be used to store and process data, similar to how variables hold data.
Variables can be passed as arguments to functions, and functions can return values to be stored in variables.

For example, the result of a function can be assigned to a variable:
'''
a = add(3, 7)  # The result of add(3, 7) is assigned to variable 'a'
print(f"The result of add(3, 7) is stored in a: {a}")

#----------------------------------------------------------------------------------------------------------------------#

# Summary:
'''
- A **function** is a block of code that performs a specific task and can take input (parameters) and return output 
  (using `return`).
- Functions are defined with the `def` keyword and called by their name.
- Functions can have parameters with default values, return multiple values, and use lambda functions for simple 
  operations.
- While functions are not a data type themselves, they can process and manipulate variables and data.
'''
#----------------------------------------------------------------------------------------------------------------------#
