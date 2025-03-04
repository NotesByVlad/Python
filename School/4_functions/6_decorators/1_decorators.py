#----------------------------------------   Decorators in Python   ----------------------------------------------------#
#                                        ------------------------------------

"""
In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods.
A decorator is a function that takes another function as input and returns a new function that typically extends
or modifies the original function.

### Key Concepts:
- **Function as First-Class Objects**: In Python, functions are first-class objects, meaning they can be passed
  as arguments to other functions, returned from functions, and assigned to variables.
- **Decorator Function**: A function that takes another function and returns a new function that adds some kind
  of functionality to the original one.
- **Syntax**: The syntax for decorators uses the `@decorator_name` syntax, placed above the function definition.
- **Wrapper Function**: The function inside the decorator that wraps the original function and typically modifies
  its behavior.

### Types of Decorators:
1. **Function Decorators**: These are the most common type and are used to modify the behavior of functions.
2. **Class Decorators**: These are used to modify classes.
3. **Method Decorators**: These are used to modify methods within a class.
4. **Chaining Decorators**: Multiple decorators can be applied to a single function by stacking them.

### Decorator Structure:
A decorator is typically implemented as a function that accepts another function, and inside it, another function
(the wrapper) is defined to modify or extend the original function's behavior.

Key Example:
- A decorator can be used to log the execution of a function or check for some condition before executing it.

"""

# 1. **Simple Function Decorator**:
# A basic decorator that adds some behavior before or after the execution of a function.

def simple_decorator(func):
    def wrapper():
        print("Before the function call.")
        func()  # Call the original function
        print("After the function call.")
    return wrapper

# Applying the decorator using the "@" symbol
@simple_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()

# Output:
# Before the function call.
# Hello, World!
# After the function call.

# 2. **Function Decorators with Arguments**:
# A decorator can also accept arguments, allowing the function it decorates to accept parameters.

def greet_decorator(func):
    def wrapper(name):
        print(f"Hello, {name}!")
        func(name)
    return wrapper

# Applying the decorator to a function with arguments
@greet_decorator
def say_hello_to(name):
    print(f"How are you, {name}?")

# Calling the decorated function with an argument
say_hello_to("Alice")

# Output:
# Hello, Alice!
# How are you, Alice?

# 3. **Returning a Value from a Decorator**:
# A decorator can modify or even replace the return value of the original function.

def double_return_value(func):
    def wrapper():
        result = func()  # Call the original function
        return result * 2  # Modify the return value
    return wrapper

@double_return_value
def get_number():
    return 5

# Calling the decorated function
print(get_number())  # Output will be doubled

# Output:
# 10

# 4. **Decorators with Arguments**:
# Sometimes you may want to pass arguments to the decorator itself. To do this, the decorator must return a
# function that takes a function as an argument.

def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(times=3)
def greet():
    print("Hello!")

# Calling the decorated function
greet()  # This will print "Hello!" three times

# Output:
# Hello!
# Hello!
# Hello!

# 5. **Class Method Decorators**:
# Decorators can also be used for modifying methods in classes.

class MyClass:
    def __init__(self):
        self.value = 10

    # Decorator to modify the behavior of a method
    @staticmethod
    def decorator_method(func):
        def wrapper(self, *args, **kwargs):
            print("Before calling the method")
            result = func(self, *args, **kwargs)
            print("After calling the method")
            return result
        return wrapper

    @decorator_method
    def show_value(self):
        print(f"The value is {self.value}")

# Calling the decorated method
obj = MyClass()
obj.show_value()

# Output:
# Before calling the method
# The value is 10
# After calling the method

# 6. **Chaining Multiple Decorators**:
# You can apply more than one decorator to a function. The decorators are applied from bottom to top.

def decorator_one(func):
    def wrapper():
        print("Decorator One: Before function call.")
        func()
        print("Decorator One: After function call.")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two: Before function call.")
        func()
        print("Decorator Two: After function call.")
    return wrapper

@decorator_one
@decorator_two
def say_goodbye():
    print("Goodbye!")

# Calling the decorated function
say_goodbye()

# Output:
# Decorator One: Before function call.
# Decorator Two: Before function call.
# Goodbye!
# Decorator Two: After function call.
# Decorator One: After function call.

# 7. **Decorators with Arguments and Return Values**:
# Sometimes a decorator needs to handle more complex cases where arguments and return values are important.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Calling the decorated function
result = add(3, 4)

# Output:
# Calling function add with arguments (3, 4) and keyword arguments {}
# Function add returned 7

# 8. **Using functools.wraps with Decorators**:
# It's a good practice to use `functools.wraps` to ensure that the decorated function retains its original
# function name, docstring, etc.

from functools import wraps

def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_wraps
def example_function():
    """This is an example function."""
    print("Inside example function.")

# Calling the decorated function
example_function()

# Checking the function's docstring and name after decoration
print(example_function.__name__)  # example_function
print(example_function.__doc__)  # This is an example function.

# 9. **Summary**:
'''
- **Decorators**: Functions that modify or extend the behavior of other functions or methods.
- **Function Decorators**: The most common use case, adding behavior around a function.
- **Arguments in Decorators**: Decorators can take arguments and be applied with additional functionality.
- **Chaining Decorators**: Multiple decorators can be applied to a single function, with the outermost 
  decorator being applied last.
- **Class Method Decorators**: Decorators can be used to modify methods inside classes.
- **`functools.wraps`**: Used to preserve the original function's name, docstring, and other attributes when 
  it is decorated.
'''

#----------------------------------------------------------------------------------------------------------------------#
