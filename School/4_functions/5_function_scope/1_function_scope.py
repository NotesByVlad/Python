#----------------------------------------   Function Scope in Python   ------------------------------------------------#
#                                        ------------------------------------

"""
In Python, scope refers to the visibility and lifetime of variables. The scope of a variable is determined by where
it is declared in the code.
There are different types of scopes that determine how and where a variable can be accessed:

1. **Local Scope**: A variable that is defined inside a function is said to have a local scope. It can only be
   accessed within that function.
2. **Global Scope**: A variable that is defined outside of all functions is said to have a global scope. It can be
   accessed from anywhere in the program.
3. **Enclosing Scope**: This refers to the scope of functions that are nested inside other functions. A variable in
   an enclosing scope can be accessed by inner functions.
4. **Built-in Scope**: This refers to the scope of Python's built-in functions and exceptions.

The scope determines how Python resolves variable names when there are multiple variables with the same name in
different scopes.

Key Concepts:
- **LEGB Rule**: Python uses the LEGB rule to determine the order of scope lookup: Local, Enclosing, Global, and
  Built-in.
- **Local Variables**: Variables defined inside a function or block of code.
- **Global Variables**: Variables defined outside any function, usually at the top level of the program.
- **Global Keyword**: Allows a function to modify a global variable.
"""

# 1. **Local Scope**:
# A variable defined inside a function is in the local scope and can only be accessed within that function.
def local_scope_example():
    x = 10  # Local variable
    print(f"Inside the function, x = {x}")

# Calling the function
local_scope_example()

# Uncommenting the next line will cause an error because x is not accessible outside the function
# print(x)  # NameError: name 'x' is not defined

# 2. **Global Scope**:
# A variable defined outside of any function is in the global scope and can be accessed anywhere in the program.
x = 20  # Global variable

def global_scope_example():
    print(f"Inside the function, global x = {x}")

# Calling the function
global_scope_example()

# Accessing the global variable outside the function
print(f"Outside the function, global x = {x}")

# 3. **Enclosing Scope**:
# A variable from an enclosing function can be accessed by nested (inner) functions.
def outer_function():
    x = 30  # Enclosing variable

    def inner_function():
        print(f"Inside the inner function, x from enclosing scope = {x}")

    inner_function()

# Calling the outer function
outer_function()

# 4. **Global Keyword**:
# In Python, if you want to modify a global variable inside a function, you must use the `global` keyword.
def modify_global_variable():
    global x  # Declare that we are using the global variable x
    x = 100  # Modify the global variable

# Calling the function to modify the global variable
modify_global_variable()

# Print the modified global variable
print(f"Modified global x = {x}")

# 5. **Built-in Scope**:
# Python has a built-in scope that contains all the built-in functions and exceptions, like `print()`, `len()`, etc.
# These built-in names are always accessible in your program.
print(f"Built-in function print(): {len('Hello, world!')}")  # Using built-in len() function

# 6. **Global vs Local Variables**:
# If a variable has the same name in both local and global scopes, the local variable will take precedence inside
# the function.
x = 50  # Global variable

def local_scope_priority():
    x = 10  # Local variable with the same name
    print(f"Inside the function, local x = {x}")

# Calling the function
local_scope_priority()

# Accessing the global variable outside the function
print(f"Outside the function, global x = {x}")

# 7. **Nonlocal Keyword**:
# In nested functions, if you want to modify a variable from the enclosing scope (but not the global scope),
# you can use the `nonlocal` keyword.
def enclosing_scope_example():
    x = 40  # Enclosing variable

    def inner_function():
        nonlocal x  # Declare that we are modifying the enclosing variable
        x = 50  # Modify the enclosing variable

    inner_function()
    print(f"After inner function, x from enclosing scope = {x}")

# Calling the enclosing function
enclosing_scope_example()

# Summary:
'''
- **Local Scope**: Variables defined inside a function.
- **Global Scope**: Variables defined outside any function, accessible from anywhere in the program.
- **Enclosing Scope**: Variables from enclosing functions accessible by nested functions.
- **Built-in Scope**: Python’s built-in functions and exceptions are available everywhere.
- **Global Keyword**: Use `global` to modify global variables inside functions.
- **Local Variable Precedence**: Local variables take precedence over global variables in their scope.
- **Nonlocal Keyword**: Used to modify variables from the enclosing (but not global) scope.
'''

#----------------------------------------------------------------------------------------------------------------------#
