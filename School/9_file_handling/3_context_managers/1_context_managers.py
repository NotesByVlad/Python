# Context Managers in Python
# --------------------------

# Context managers allow you to allocate and release resources automatically.
# The `with` statement is used to wrap the execution of a block of code, ensuring resources are cleaned up afterward.

# Example: Creating a context manager using a bank_syst
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

# Using the context manager
with MyContextManager() as cm:
    print("Inside the context")

# Output:
# Entering the context
# Inside the context
# Exiting the context

# Best Practices
# --------------
# 1. Use context managers to handle resource management (e.g., file handling, network connections).
# 2. Use the `with` statement to avoid manual resource cleanup.

# Exercises
# ---------
# 1. Write a context manager for timing the execution of a block of code.
# 2. Create a context manager for logging function entry and exit.