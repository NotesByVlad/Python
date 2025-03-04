# Working with File Paths in Python
# -------------------------------

# Python provides the `os` and `pathlib` modules for working with file paths.
# These modules allow you to create, modify, and navigate file system paths.

# Example: Using `os.path` to get the current working directory
import os

current_directory = os.getcwd()  # Get the current working directory
print(f"Current directory: {current_directory}")

# Example: Joining paths with `os.path.join()`
file_path = os.path.join(current_directory, 'example.txt')
print(f"Full file path: {file_path}")

# Example: Using `pathlib.Path`
from pathlib import Path

file_path = Path('example.txt')
if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

# Best Practices
# --------------
# 1. Use `os.path.join()` or `pathlib.Path` to build file paths instead of hardcoding them.
# 2. Use `pathlib` for more modern and readable code when dealing with paths.

# Exercises
# ---------
# 1. Write a program that checks if a file exists and prints its full path.
# 2. Use `os` or `pathlib` to create a new directory and write to a file inside it.