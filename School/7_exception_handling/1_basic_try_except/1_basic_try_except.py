# Basic Try/Except in Python
# --------------------------

# The basic structure for handling exceptions in Python involves the `try` and `except` blocks.

# Example: Basic Try/Except
try:
    num = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Output: Error: Division by zero is not allowed.

# Best Practices
# --------------
# 1. Always catch specific exceptions rather than using a generic `except` block.
# 2. Handle exceptions gracefully to ensure program continuity.

# Exercises
# ---------
# 1. Write a program that catches `FileNotFoundError` when trying to open a non-existent file.
# 2. Handle a `ValueError` when converting a string to an integer.