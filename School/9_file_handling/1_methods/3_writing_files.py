# Writing Files in Python
# ------------------------

# To write to a file, you open the file in 'write' ('w') or 'append' ('a') mode.
# - `write()` writes a string to the file.
# - `writelines()` writes a list of strings to the file.

# Example: Writing to a file (overwrite mode)
file = open('example_write.txt', 'w')  # Open the file in write mode (creates a new file)
file.write("Hello, world!\n")          # Write to the file
file.write("Welcome to Python file handling.\n")
file.close()

# Example: Writing multiple lines to a file
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open('example_lines.txt', 'w')
file.writelines(lines)  # Write the list of strings to the file
file.close()

# Best Practices
# --------------
# 1. Use the 'w' mode to overwrite a file and 'a' mode to append.
# 2. Always close the file after writing to ensure the data is saved.

# Exercises
# ---------
# 1. Create a program that writes a series of strings to a new text file.
# 2. Write a function that takes a list of strings and writes them to a file.