#----------------------------------------   Exception Handling in Python   ----------------------------------------#
#                                        ------------------------------------

"""
Exception handling is a mechanism in Python to handle runtime errors, ensuring that the program can recover gracefully instead of crashing.

### Key Concepts:
1. **Basic Try-Except**
2. **Multiple Except Blocks**
3. **Else and Finally**
4. **Custom Exceptions**
5. **Raising Exceptions**
6. **Exception Hierarchy**
"""

# 1. **Basic Try-Except**:
# The `try` block contains code that may raise an exception, while the `except` block handles the exception if it occurs.

try:
    result = 10 / 0  # Division by zero raises an exception
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Explanation:
# When a division by zero occurs, the `ZeroDivisionError` is caught by the `except` block, preventing the program from crashing.

# 2. **Multiple Except Blocks**:
# You can use multiple `except` blocks to handle different types of exceptions separately.

try:
    value = int("abc")  # Trying to convert a string to an integer
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Explanation:
# Multiple `except` blocks allow you to specify different handlers for specific exceptions.

# 3. **Else and Finally**:
# The `else` block executes if no exceptions occur, and the `finally` block executes regardless of whether an exception occurs.

try:
    value = int("123")
except ValueError:
    print("Invalid input!")
else:
    print(f"The input was successfully converted to integer: {value}")
finally:
    print("Execution completed.")

# Explanation:
# - The `else` block runs when the `try` block does not raise an exception.
# - The `finally` block runs regardless of what happens in the `try` or `except` blocks.

# 4. **Custom Exceptions**:
# You can define your own exception classes by inheriting from the `Exception` base class.

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Using the custom exception:
try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print(f"Caught a custom exception: {e}")

# Explanation:
# Custom exceptions allow you to create application-specific error types for better error management.

# 5. **Raising Exceptions**:
# Use the `raise` keyword to explicitly raise an exception when a specific condition occurs.

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Explanation:
# Raising exceptions manually allows you to enforce conditions and signal errors in your code.

# 6. **Exception Hierarchy**:
# Exceptions in Python follow a hierarchy, with `BaseException` being the root class.

try:
    x = int("abc")
except ValueError:
    print("ValueError caught!")
except Exception:
    print("General exception caught!")

# Explanation:
# - `Exception` is the base class for most built-in exceptions.
# - More specific exceptions should appear before more general ones in `except` blocks.

# Visualizing the Exception Hierarchy:
"""
BaseException
|
+-- SystemExit
|
+-- KeyboardInterrupt
|
+-- GeneratorExit
|
+-- Exception
     |
     +-- StopIteration
     +-- ArithmeticError
     |    +-- ZeroDivisionError
     +-- ValueError
     +-- TypeError
     +-- IndexError
"""

# 7. **Summary**:
'''
1. **Basic Try-Except**: Catches exceptions to prevent crashes.
2. **Multiple Except Blocks**: Handles different exceptions differently.
3. **Else and Finally**: `else` runs if no exceptions occur; `finally` always runs.
4. **Custom Exceptions**: Create user-defined exceptions for specific use cases.
5. **Raising Exceptions**: Manually raise exceptions with `raise`.
6. **Exception Hierarchy**: Exceptions follow a class hierarchy, with `BaseException` as the root.
'''

#----------------------------------------------------------------------------------------------------------------------#
