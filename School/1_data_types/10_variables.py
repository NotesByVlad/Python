#----------------------------------------   Variables in Python   -----------------------------------------------------#
#                                        -------------------------

"""
In Python, a variable is a named location in memory used to store data. Variables can hold
different data types, such as integers, strings, lists, and more. Python is dynamically typed,
which means you do not need to declare a variable's type; it is inferred from the value assigned.

Variables are the building blocks of a Python program, used to store, update, and manipulate data.
"""

# Key Points about Variables:
'''
- Dynamic Typing: Python variables do not need explicit type declarations.
- Assignment: Use the assignment operator `=` to assign a value to a variable.
- Naming Rules: Variable names must start with a letter or an underscore, followed by letters, 
  digits, or underscores. Names are case-sensitive.
- Scope: A variable's scope determines where it can be accessed (global vs. local).
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Assigning Variables
'''
Variables are created when you assign a value to them.
'''
x = 10  # Integer
y = "Hello, Python"  # String
z = 3.14  # Float
flag = True  # Boolean

print("x:", x)
print("y:", y)
print("z:", z)
print("flag:", flag)

# 2. Multiple Assignments
'''
You can assign multiple variables in a single line.
'''
a, b, c = 1, 2, 3  # Multiple assignments
print("\na:", a, "b:", b, "c:", c)

# Assign the same value to multiple variables
p = q = r = 100
print("\np:", p, "q:", q, "r:", r)

# 3. Dynamic Typing
'''
Python allows reassignment of variables to values of different types.
'''
variable = 42  # Initially an integer
print("\nVariable (int):", variable)
variable = "Now I'm a string!"  # Reassigned to a string
print("Variable (string):", variable)

# 4. Naming Conventions
'''
Follow these conventions for variable names:
- Use descriptive names (`age`, `total_price`) for readability.
- Start with a letter or underscore (_), but avoid leading underscores unless necessary.
- Avoid Python reserved keywords like `if`, `while`, `class`.
- Use snake_case for variables (`user_name`, `max_value`).
'''

user_name = "Alice"
MAX_VALUE = 100  # Constants are typically written in uppercase
print("\nUser Name:", user_name)
print("Max Value:", MAX_VALUE)

# 5. Global and Local Variables
'''
- Global variables are declared outside of any function and accessible throughout the program.
- Local variables are declared inside a function and only accessible within that function.
'''
global_var = "I am global!"

def example_function():
    local_var = "I am local!"
    print("\nInside Function:")
    print("Global Variable:", global_var)  # Access global variable
    print("Local Variable:", local_var)  # Access local variable

example_function()

# Uncommenting the next line would cause an error, as `local_var` is not accessible outside the function.
# print(local_var)

# 6. Using `global` Keyword
'''
The `global` keyword allows modification of global variables within a function.
'''
counter = 0

def increment_counter():
    global counter  # Declare global to modify it
    counter += 1

increment_counter()
increment_counter()
print("\nCounter after increments:", counter)

# 7. Constants
'''
Python does not have a built-in constant type, but variables meant to be constants are usually 
written in uppercase to indicate they should not be modified.
'''
PI = 3.14159  # Convention for a constant
print("\nConstant PI:", PI)

# 8. Deleting Variables
'''
You can delete a variable using the `del` statement.
'''
temp_var = 99
print("\nTemp Variable before deletion:", temp_var)
del temp_var  # Deletes the variable
# Uncommenting the next line would cause an error because the variable is deleted.
# print(temp_var)

# 9. Variable Scope
'''
The scope of a variable determines where it can be accessed.
- Global Scope: Accessible throughout the program.
- Local Scope: Accessible only within the block where defined.
'''
def scope_example():
    local_scope_var = "Local"
    print("\nAccessing Local Variable:", local_scope_var)

scope_example()

# Uncommenting the next line would cause an error because the variable is local.
# print(local_scope_var)

#----------------------------------------------------------------------------------------------------------------------#

# Summary:
'''
1. Variables are created using the assignment operator `=`.
2. Python is dynamically typed, allowing reassignment of different types.
3. Use meaningful variable names for clarity and follow naming conventions.
4. Understand the scope of variables to avoid errors.
5. Use the `global` keyword to modify global variables inside functions.
'''
#----------------------------------------------------------------------------------------------------------------------#
