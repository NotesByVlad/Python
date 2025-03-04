# Creating Your Own Modules
# -------------------------

# You can create your own modules by saving Python code in a `.py` file. Any Python file can be used as a module.

# Example: Create a module "calculator.py" with addition, subtraction, and multiplication functions.
# Save this code as calculator.py.

# calculator.py (module)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Now, in another Python file, import and use the functions from this module.
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.multiply(4, 2)

print(result1)  # Output: 15
print(result2)  # Output: 8

# Best Practices
# --------------
# 1. Organize reusable code into modules to improve maintainability.
# 2. Use clear, descriptive names for functions and variables in your module.

# Exercises
# ---------
# 1. Create a module that checks if a number is prime.
# 2. Write a module for string manipulations like reversing, trimming, etc.