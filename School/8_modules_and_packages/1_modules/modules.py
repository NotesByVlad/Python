#---------------------------------------- Working with Modules in Python ----------------------------------------------#
#                                        --------------------------------

"""
A module is a file containing Python definitions and statements.
It can define functions, classes, and variables. Modules are used
to organize code into reusable pieces and to avoid name conflicts
by grouping related code together.

Key Points about Modules:

- What is a Module?: A module is a file that defines functions, classes, and variables, 
  and can be imported into other scripts.

- Importing Modules: Modules can be imported using import, from ... import, and import ... as.

- Standard Library Modules: Python provides a vast set of built-in modules for various 
  tasks like data manipulation, web development, file handling, etc.
"""
#----------------------------------------------------------------------------------------------------------------------#

#  1. Importing a Module
''' You can import an entire module using the import keyword. '''

#  Example:
import math

#  Using a function from the math module
result = math.sqrt(16)
print("Square root of 16:", result)

#----------------------------------------------------------------------------------------------------------------------#

#  2. Importing Specific Functions or Classes
''' You can import specific functions or classes from a module using from module import function. '''

#  Example:
from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time)
#----------------------------------------------------------------------------------------------------------------------#

#  3. Using Aliases with Modules
''' You can create aliases for modules to make them easier to reference. '''

# Example:
import numpy as np

array = np.array([1, 2, 3])
print("Numpy array:", array)

#----------------------------------------------------------------------------------------------------------------------#

#  4. Standard Library Modules
''' 
Python provides a rich set of built-in modules in its standard library for various purposes, such as:

- os for file operations
- sys for system-related operations
- json for JSON data manipulation
- random for generating random numbers
- re for regular expressions 
'''

#  Example:
import os

print("Current working directory:", os.getcwd())
#----------------------------------------------------------------------------------------------------------------------#

#  5. Creating Your Own Module
''' 
You can create your own Python module by saving a Python file 
(e.g., mymodule.py) containing functions, classes, or variables. 
'''

#  Example of creating and using a custom module:
#    ______________________________
#   | -- in mymodule.py file --    |
#   |                              |
#   | def greet(name):             |
#   | 	 return f"Hello, {name}!"  |
#   | PI = 3.14159                 |
#   |______________________________|
#
#  Using the custom module:
# import mymodule
#
# print(mymodule.greet("Alice"))
# print("Value of PI:", mymodule.PI)
#----------------------------------------------------------------------------------------------------------------------#

#  6. Benefits of Using Modules
'''
Code Reusability: Modules allow you to reuse code across different scripts.
Avoiding Conflicts: Namespaces reduce the risk of name conflicts.
Readability and Maintenance: Modular code is easier to read, maintain, and update.
'''
#----------------------------------------------------------------------------------------------------------------------#

#  7. Built-in Modules and Packages
''' 
Python provides a vast collection of built-in modules for various tasks. 
These modules are organized into packages, which are collections of modules. 
'''

#  Example:
import math
import statistics

numbers = [1, 2, 3, 4, 5]
mean = statistics.mean(numbers)
print("Mean of numbers:", mean)
#----------------------------------------------------------------------------------------------------------------------#

#  8. Using the __name__ attribute
''' 
The __name__ attribute can be used to determine if a module is being run 
directly or imported into another module. 
'''

#  Example:
def main(): print("This is the main function.")

if __name__ == "main":
	main()
#----------------------------------------------------------------------------------------------------------------------#

#  Conclusion:
''' 
Modules play a fundamental role in organizing and structuring Python code,
promoting code reuse, and reducing potential namespace conflicts. 
'''
#----------------------------------------------------------------------------------------------------------------------#