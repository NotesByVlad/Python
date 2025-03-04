# Standard Library Modules
# -------------------------

# Python comes with a large standard library of modules that you can use without installing anything extra.
# Some popular standard library modules include:
# - `math` for mathematical operations
# - `datetime` for date and time operations
# - `os` for interacting with the operating system
# - `sys` for system-specific parameters and functions
# - `json` for working with JSON data

# Example: Using the `datetime` module to get the current date and time
import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)  # Output: (Current date and time)

# Example: Using the `os` module to work with the file system
import os

current_directory = os.getcwd()
print(current_directory)  # Output: (Current working directory)

# Best Practices
# --------------
# 1. Explore Python's standard library to avoid reinventing the wheel.
# 2. Use the `import` statement to access functionality provided by these modules.

# Exercises
# ---------
# 1. Use the `math` module to calculate the factorial of a number.
# 2. Write a program that checks if a file exists using the `os` module.