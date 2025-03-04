# Appending to Files in Python
# -----------------------------

# To append data to an existing file, open the file in 'append' ('a') mode.
# This will allow you to add new content to the end of the file without overwriting the existing content.

# Example: Appending to a file
file = open('example_append.txt', 'a')  # Open the file in append mode
file.write("New content added to the file.\n")  # Append to the file
file.close()

# Best Practices
# --------------
# 1. Use the 'a' mode to add content to a file without removing existing data.
# 2. Consider using context managers to automatically handle file opening and closing.

# Exercises
# ---------
# 1. Open a file in append mode and add a few new lines.
# 2. Create a program that appends user input into a file until the user decides to stop.