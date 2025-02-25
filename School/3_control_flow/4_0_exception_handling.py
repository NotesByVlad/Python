#---------------------------------------- Exception Handling in Conditional Statements --------------------------------#
#                                        ----------------------------------------------

"""
Exception handling is used to catch and manage errors or exceptional situations that may arise during the execution
of code.
It allows you to write code that can respond to unexpected conditions without crashing the program.
In Python, the `try`, `except`, `else`, and `finally` blocks are used for exception handling.
"""

# Key Points about Exception Handling:
'''
1. `try`: Defines a block of code in which exceptions may occur.
2. `except`: Catches exceptions that arise within the `try` block and allows you to handle them.
3. `else`: Executes if no exception is raised in the `try` block.
4. `finally`: Executes after the `try` block (and `except`/`else` blocks if present), regardless of whether an 
    exception was raised or not.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Exception Handling with If-Else
'''
You can combine `try` and `except` blocks inside conditional statements (e.g., `if`, `elif`, `else`) to handle 
specific errors or conditions.
'''

# Example:
print("Basic Exception Handling with If-Else Example:")
x = "hello"
if isinstance(x, int):  # Check if x is an integer
    try:
        result = 10 / x  # This will raise a TypeError if x is not a number
    except TypeError:
        print("Error: Cannot divide by a non-integer value.")
else:
    print("x is not an integer, cannot perform division.")

# Output: x is not an integer, cannot perform division.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Handling Multiple Exceptions in Conditional Statements
'''
You can handle multiple types of exceptions within a conditional block by specifying different `except` clauses.
'''

# Example:
print("\nHandling Multiple Exceptions:")
x = "abc"
if isinstance(x, str):  # Check if x is a string
    try:
        num = int(x)  # This will raise a ValueError
    except ValueError:
        print("Error: Cannot convert a string to an integer.")
else:
    print("x is not a string, cannot convert.")

# Output: Error: Cannot convert a string to an integer.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using Else with Try-Except in Conditionals
'''
You can use the `else` block to execute code if no exceptions were raised in the `try` block.
It’s useful when you want to handle normal logic after a successful operation.
'''

# Example:
print("\nUsing Else with Try-Except in Conditionals:")
x = 10
y = 2
if x > y:
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print(f"Result of division: {result}")
else:
    print("x is not greater than y.")

# Output: Result of division: 5.0
# The else block is executed because no exception occurred in the try block.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using Finally with Try-Except in Conditionals
'''
The `finally` block will execute regardless of whether an exception is raised or not. 
It is often used for cleanup actions, such as closing files or releasing resources.
'''

# Example:
print("\nUsing Finally with Try-Except in Conditionals:")
try:
    x = 10 / 2
    print("Division successful!")
except ZeroDivisionError:
    print("Error: Division by zero.")
finally:
    print("This block is always executed, regardless of whether an exception was raised.")

# Output:
# Division successful!
# This block is always executed, regardless of whether an exception was raised.

#----------------------------------------------------------------------------------------------------------------------#

# 5. Exception Handling in Nested Conditionals
'''
You can use exception handling inside nested conditional blocks. This allows you to manage specific exceptions
at different levels.
'''

# Example:
print("\nException Handling in Nested Conditionals:")
x = "10a"
if isinstance(x, str):
    if len(x) > 5:
        try:
            result = int(x)  # This will raise a ValueError
        except ValueError:
            print("Error: Cannot convert string to integer.")
    else:
        print("String is too short to process.")
else:
    print("x is not a string.")

# Output: Error: Cannot convert string to integer.
# The exception handling occurs only if the inner condition is met.

#----------------------------------------------------------------------------------------------------------------------#

# 6. Common Pitfalls in Exception Handling with Conditionals
'''
1. Ignoring exceptions: Failing to handle exceptions may cause the program to crash unexpectedly.
2. Overusing exception handling: Relying too much on exceptions to control logic can make your code 
   less efficient and harder to maintain.
3. Catching general exceptions: Catching general exceptions (like `Exception`) might mask specific 
   issues that you need to address.
'''

# Example of Common Pitfall:
# try:
#     result = 10 / "string"  # This will raise TypeError
# except Exception:  # Catching all exceptions can hide specific problems.
#     print("An error occurred.")

#----------------------------------------------------------------------------------------------------------------------#
