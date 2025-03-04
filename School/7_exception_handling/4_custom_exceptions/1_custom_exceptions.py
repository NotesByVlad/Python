# Custom Exceptions in Python
# ---------------------------

# You can define your own exception classes by subclassing the built-in `Exception` bank_syst.

# Example: Creating and Raising Custom Exception
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return num

try:
    check_number(-5)
except NegativeNumberError as e:
    print(f"Custom Error: {e}")

# Best Practices
# --------------
# 1. Create custom exceptions for application-specific errors.
# 2. Use custom exceptions for better clarity and handling of specific errors.

# Exercises
# ---------
# 1. Write a custom exception `NotEnoughFundsError` and raise it when a bank account balance is insufficient.
# 2. Create a `FileFormatError` for invalid file formats.