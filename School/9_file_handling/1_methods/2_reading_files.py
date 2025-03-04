# Reading Files in Python
# ------------------------

# Python provides various methods to read from a file. The common methods are:
# - `read()` to read the entire file at once.
# - `readline()` to read a single line at a time.
# - `readlines()` to read all lines and return them as a list of strings.

# Example: Reading an entire file
file = open('example.txt', 'r')  # Open the file in read mode
content = file.read()            # Read the entire content
file.close()

print(content)  # Output: Hello, world!

# Example: Reading a file line by line
file = open('example.txt', 'r')
for line in file:
    print(line.strip())  # Strip removes newline characters

file.close()

# Best Practices
# --------------
# 1. Always handle file reading operations within a context manager or close the file after reading.
# 2. Use `readlines()` for reading lines into a list when you want to work with multiple lines at once.

# Exercises
# ---------
# 1. Write a program that opens a file, reads its contents, and prints each line.
# 2. Open a text file, read it into a list, and count the number of lines in the file.