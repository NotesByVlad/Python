# Opening and Closing Files in Python
# -----------------------------------

# To work with a file in Python, you first need to open it using the `open()` function.
# The `open()` function returns a file object that allows you to read or write to the file.
# After you're done working with the file, always close it using the `close()` method to release system resources.

# Example: Opening and closing a file
file = open('example.txt', 'w')  # Open a file for writing
file.write("Hello, world!\n")    # Write to the file
file.close()                     # Close the file

# Best Practices
# --------------
# 1. Always close the file after you're done working with it to free up resources.
# 2. Use exception handling (try-except-finally) to ensure the file is closed even if an error occurs.

# Exercises
# ---------
# 1. Write a program that opens a file and writes a series of numbers into it.
# 2. Open a file and use the `read()` method to read its contents, then close it.