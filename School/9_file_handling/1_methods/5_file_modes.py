# File Modes in Python
# --------------------

# File modes define the behavior when opening a file. The common modes are:
# - 'r' - Read (default). Opens the file for reading.
# - 'w' - Write. Opens the file for writing (creates a new file or overwrites an existing one).
# - 'a' - Append. Opens the file for appending (creates a new file if it doesn't exist).
# - 'b' - Binary mode. Used when working with binary files (e.g., images, videos).
# - 'x' - Exclusive creation. Creates a new file but raises an error if the file already exists.

# Example: Using different file modes
file = open('example.txt', 'r')  # Open for reading
content = file.read()
file.close()

file = open('example_new.txt', 'w')  # Open for writing (overwrite)
file.write("New content.")
file.close()

file = open('example_bin.bin', 'wb')  # Open for binary writing
file.write(b"Some binary data")  # Notice the 'b' prefix for binary data
file.close()

# Best Practices
# --------------
# 1. Always choose the right file mode based on the operation you're performing (reading, writing, appending).
# 2. Consider binary mode when working with non-text files.

# Exercises
# ---------
# 1. Write a program that reads a text file and then writes its content to a new file in binary mode.
# 2. Create a program that opens a file in exclusive mode and handles the error if the file already exists.