# What is a Module?
# -----------------

# A module in Python is simply a file containing Python definitions, functions, classes, and variables.
# It allows you to organize and reuse code.

# Example: Create a module named "math_operations.py" with functions for addition and multiplication.
# Save this as math_operations.py.

# math_operations.py (module)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Now, you can import this module into another script or program:
import math_operations

result1 = math_operations.add(5, 3)
result2 = math_operations.multiply(4, 2)

print(result1)  # Output: 8
print(result2)  # Output: 8

# Best Practices
# --------------
# 1. Organize related functions and classes into modules.
# 2. Name modules using lowercase letters and underscores for readability.

# Exercises
# ---------
# 1. Create a module with functions for basic string manipulations (e.g., reversing, uppercasing).
# 2. Build a module that calculates the area of different shapes (circle, square, rectangle).