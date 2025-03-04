# The `__init__.py` File in Python
# -------------------------------

# The `__init__.py` file is used to mark a directory as a Python package and can be used to initialize package-level code.

# Example: `mypackage/__init__.py`
# You can import specific modules when the package is imported.
from .module1 import function1
from .module2 import function2

# Now, you can directly access the functions at the package level:
import mypackage

print(mypackage.function1())  # Output: Function 1 from module 1
print(mypackage.function2())  # Output: Function 2 from module 2

# Best Practices
# --------------
# 1. Use `__init__.py` to expose package-level functionality or perform setup tasks.
# 2. Keep `__init__.py` files minimal; they should only contain initialization code for the package.

# Exercises
# ---------
# 1. Modify a package's `__init__.py` file to import selected functions from each module.
# 2. Write a package for handling user authentication and expose login and logout functions through `__init__.py`.