# Packages in Python
# ------------------

# A package is a collection of modules grouped together under a common directory.
# A package is usually identified by a directory containing an `__init__.py` file.

# Example: Creating a Package

# Directory structure:
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# mypackage/__init__.py (package initialization)
# This file can be empty or contain package-level imports.

# mypackage/module1.py
def function1():
    return "Function 1 from module 1"

# mypackage/module2.py
def function2():
    return "Function 2 from module 2"

# To use the package:
import mypackage.module1
import mypackage.module2

print(mypackage.module1.function1())  # Output: Function 1 from module 1
print(mypackage.module2.function2())  # Output: Function 2 from module 2

# Best Practices
# --------------
# 1. Use packages to organize modules when your project grows in size.
# 2. Use `__init__.py` to define what is exposed at the package level.

# Exercises
# ---------
# 1. Create a package for basic mathematical operations with multiple modules.
# 2. Build a package for data processing with modules for cleaning, transforming, and visualizing data.