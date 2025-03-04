# Using Context Manager for File Handling
# ---------------------------------------

# A context manager automatically handles the opening and closing of files, ensuring proper resource management.

# Example: Using `with` statement for file handling
with open('example_with.txt', 'w') as file:  # No need to call file.close()
    file.write("This is written using context manager.")

# The file is automatically closed when the block inside the `with` statement is executed.

# Best Practices
# --------------
# 1. Always use `with` to handle file operations to automatically close the file, even in case of errors.
# 2. Avoid manually opening and closing files without `with` as it may lead to resource leaks.

# Exercises
# ---------
# 1. Use a `with` statement to write a series of numbers into a file.
# 2. Create a program that reads a file using the `with` statement and prints each line.