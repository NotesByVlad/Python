#----------------------------------------   Functions in Python   -----------------------------------------------------#
#                                        -------------------------

"""
In Python, a **function** is a block of code that only runs when it is called. Functions allow you to break down
your program into smaller, reusable, and logically organized sections.

### Key Concepts:
- **Function Definition**: Functions are defined using the `def` keyword, followed by the function name and
  optional parameters.
- **Parameters and Arguments**: Functions can take parameters (variables defined in the function definition)
  and arguments (values passed to the function).
- **Return Statement**: Functions can return values using the `return` statement. If no return statement
  is provided, the function returns `None` by default.
- **Function Scope**: Variables defined inside a function are local to that function and are not accessible outside.
- **Function Overloading**: Python does not support function overloading (multiple functions with the same name but
  different parameters). Instead, default arguments, variable-length arguments, or keyword arguments are used.
- **Lambda Functions**: These are small, anonymous functions defined using the `lambda` keyword.

"""

# 1. **Basic Function**:
# A simple function that takes no arguments and returns nothing.

def greet():
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!

# 2. **Function with Parameters**:
# A function that takes parameters and performs an operation using them.

def add(a, b):
    return a + b

# Calling the function with arguments
result = add(3, 4)
print(result)  # Output: 7

# Explanation:
# add(3, 4) returns 3 + 4 = 7.

# 3. **Function with Default Parameters**:
# Functions can have default values for parameters. If no argument is provided, the default value is used.

def greet_person(name="Stranger"):
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet_person()         # Output: Hello, Stranger!
greet_person("Alice")  # Output: Hello, Alice!

# Explanation:
# The parameter `name` has a default value of "Stranger", which is used when no argument is provided.

# 4. **Function with Variable-Length Arguments (Args)**:
# You can define a function that accepts a variable number of positional arguments using `*args`.

def sum_of_numbers(*args):
    return sum(args)

# Calling the function with different numbers of arguments
print(sum_of_numbers(1, 2, 3))        # Output: 6
print(sum_of_numbers(4, 5, 6, 7, 8))  # Output: 30

# Explanation:
# The `*args` allows you to pass any number of positional arguments to the function.

# 5. **Function with Keyword Arguments (Kwargs)**:
# A function can accept an arbitrary number of keyword arguments using `**kwargs`, which are passed as a dictionary.

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
display_info(name="Alice", age=30, city="New York")

# Output:
# name: Alice
# age: 30
# city: New York

# Explanation:
# The `**kwargs` allows you to pass any number of keyword arguments to the function.

# 6. **Lambda Functions**:
# Lambda functions are small anonymous functions defined using the `lambda` keyword.
# Lambda functions can take any number of arguments but can only have a single expression.

# Example of a lambda function that adds two numbers:
add_lambda = lambda a, b: a + b
print(add_lambda(3, 4))  # Output: 7

# Explanation:
# The lambda function `lambda a, b: a + b` is equivalent to the function `def add(a, b): return a + b`.

# 7. **Returning Multiple Values from a Function**:
# A function can return multiple values by separating them with commas. This will return a tuple.

def get_student_info():
    name = "John"
    age = 21
    major = "Computer Science"
    return name, age, major

# Calling the function and unpacking the returned values
name, age, major = get_student_info()
print(f"Name: {name}, Age: {age}, Major: {major}")

# Output:
# Name: John, Age: 21, Major: Computer Science

# Explanation:
# The function returns a tuple `(name, age, major)`, which is unpacked into individual variables.

# 8. **Recursion in Functions**:
# A function can call itself (recursion) to solve problems that can be broken down into smaller subproblems.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
print(factorial(5))  # Output: 120

# Explanation:
# The function `factorial` calls itself with a smaller value of `n` until `n` reaches 0 (base case).

# 9. **Function Scope and Lifetime**:
# Variables inside a function are local to that function and cannot be accessed outside it.
# However, global variables can be accessed within a function (unless they are shadowed by local variables).

x = 10  # Global variable

def modify_variable():
    global x  # Declare x as a global variable to modify it
    x = 20  # Modify the global variable

modify_variable()
print(x)  # Output: 20

# Explanation:
# The `global` keyword allows the function to modify the global variable `x`.

# 10. **Functions as First-Class Citizens**:
# In Python, functions are first-class objects. This means functions can be passed as arguments,
# returned from other functions, and assigned to variables.

# Example of a function that accepts another function as an argument:

def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

# Calling the function with another function as an argument
result = apply_function(square, 5)
print(result)  # Output: 25

# Explanation:
# The function `apply_function` accepts a function (`square`) as an argument and applies it to `value`.

# 11. **Nested Functions**:
# Functions can be defined inside other functions. The inner function can access variables from the outer
# function's scope.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Calling the function and using the nested function
add_five = outer_function(5)
print(add_five(10))  # Output: 15

# Explanation:
# The function `inner_function` is nested inside `outer_function`. The `add_five` function holds the reference to
# the inner function with `x = 5`.

# 12. **Function Annotations**:
# Python allows optional function annotations to provide hints about the types of parameters and the return type.

def multiply(a: int, b: int) -> int:
    return a * b

# Calling the function
print(multiply(3, 4))  # Output: 12

# Explanation:
# The function annotations `a: int`, `b: int`, and `-> int` provide type hints, though they are not enforced at runtime.

# 13. **Summary**:
'''
- **Function Definition**: Use `def` to define a function with optional parameters.
- **Parameters and Arguments**: Functions can accept parameters, and arguments are passed to them.
- **Return Statement**: Functions return values using `return`.
- **Variable-Length Arguments**: `*args` and `**kwargs` allow functions to accept a variable number of arguments.
- **Lambda Functions**: Small anonymous functions created using the `lambda` keyword.
- **Recursion**: A function calling itself to solve a problem recursively.
- **Function Scope**: Variables in functions are local to that function.
- **Functions as First-Class Citizens**: Functions can be passed as arguments, returned from other functions, 
  and assigned to variables.
- **Nested Functions**: Functions defined inside other functions.
- **Function Annotations**: Optional hints about the types of parameters and return values.
'''

#----------------------------------------------------------------------------------------------------------------------#
