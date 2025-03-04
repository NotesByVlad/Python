# Multiple Except Blocks in Python
# --------------------------------

# You can handle different exceptions using multiple `except` blocks.

# Example: Handling multiple exceptions
try:
    val = int(input("Enter a number: "))
    result = 10 / val
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"Unexpected error: {e}")

# Best Practices
# --------------
# 1. Catch specific exceptions in separate `except` blocks for clarity.
# 2. Use a generic `except` block as a last resort to catch unexpected errors.

# Exercises
# ---------
# 1. Write a program that catches both `FileNotFoundError` and `PermissionError`.
# 2. Modify the above code to handle `TypeError` when adding incompatible types.