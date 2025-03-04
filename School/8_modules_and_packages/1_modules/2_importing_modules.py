# Importing Modules in Python
# ----------------------------

# You can import entire modules or specific functions and classes from them using the `import` statement.

# Example: Importing an entire module
import math  # Importing the math module

print(math.sqrt(16))  # Output: 4.0

# Example: Importing specific functions
from math import sqrt, pi  # Import specific functions

print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793

# Example: Renaming a module during import
import math as m

print(m.sqrt(16))  # Output: 4.0

# Best Practices
# --------------
# 1. Only import the specific functions you need to reduce memory usage.
# 2. Use aliases (e.g., `import numpy as np`) for longer module names.

# Exercises
# ---------
# 1. Import the `random` module and generate a random number between 1 and 100.
# 2. Use `from datetime import datetime` to print the current date and time.