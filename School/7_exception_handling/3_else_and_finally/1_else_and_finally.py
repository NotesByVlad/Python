# Else and Finally in Python
# --------------------------

# The `else` block runs if no exceptions occur in the `try` block, while `finally` always runs,
# regardless of whether an exception was raised or not.

# Example: Using Else and Finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("This block always executes.")

# Best Practices
# --------------
# 1. Use `else` to handle code that runs when no exception occurs.
# 2. Use `finally` to clean up resources, like closing files or network connections.

# Exercises
# ---------
# 1. Write a program that reads from a file. Use `finally` to close the file after reading.
# 2. Add an `else` block to a program that calculates factorial without raising errors.