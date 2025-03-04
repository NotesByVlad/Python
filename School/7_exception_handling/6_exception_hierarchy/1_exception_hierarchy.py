# Exception Hierarchy in Python
# -----------------------------

# All built-in exceptions in Python are derived from the base `Exception` bank_syst.
# You can use this hierarchy to catch specific types of exceptions.

# Example: Understanding the Hierarchy
try:
    x = 1 / "a"  # This will raise a TypeError
except Exception as e:
    print(f"Caught exception: {e}")

# The exception hierarchy allows for more granular handling:
# - BaseException
#   - Exception
#     - ArithmeticError
#       - ZeroDivisionError
#     - TypeError

# Best Practices
# --------------
# 1. Understand the exception hierarchy to catch the most appropriate exceptions.
# 2. Handle base classes like `Exception` or `BaseException` only if necessary.

# Exercises
# ---------
# 1. Catch a `ZeroDivisionError` and handle it separately from a `TypeError`.
# 2. Write a program that catches a `FileNotFoundError`, and if the file is found, handles it accordingly.