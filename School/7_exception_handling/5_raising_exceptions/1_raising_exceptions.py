# Raising Exceptions in Python
# -----------------------------

# You can raise exceptions manually using the `raise` keyword.

# Example: Raising an Exception
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    print("You are eligible.")

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")

# Best Practices
# --------------
# 1. Raise exceptions when the program encounters an invalid state.
# 2. Use `raise` to pass exceptions up the call stack for higher-level handling.

# Exercises
# ---------
# 1. Write a function that raises a `TypeError` if an input is not a string.
# 2. Create a function that raises a custom exception if the input value is negative.