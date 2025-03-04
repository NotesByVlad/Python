#----------------------------------------   Function Parameters in Python   -------------------------------------------#
#                                        -----------------------------------

"""
In Python, parameters are the values passed into a function when it is called.
A function can have one or more parameters, which allow the function to perform different tasks based on the
values passed to it.

Function parameters can be classified into various types, and understanding them is key to writing flexible
and efficient functions.

Key Points:
1. **Positional Parameters**: These are the parameters that must be passed in the correct order.
2. **Default Parameters**: These parameters have default values if no argument is provided when calling the function.
3. **Keyword Parameters**: These parameters are passed by explicitly specifying the parameter name during the
   function call.
4. **Arbitrary Arguments (*args)**: These allow a function to accept a variable number of positional arguments.
5. **Arbitrary Keyword Arguments (**kwargs)**: These allow a function to accept a variable number of keyword arguments
   (arguments passed by name).
"""

# 1. **Positional Parameters**:
# Positional parameters are the most common type of parameters. They must be passed in the correct order when calling
# the function.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with positional arguments
greet("Alice", 30)

# 2. **Default Parameters**:
# Default parameters are parameters that have a default value. If no value is provided for the parameter,
# the default value is used.
def greet(name="User", age=18):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with and without passing arguments
greet("Bob", 25)
greet()  # Will use default values

# 3. **Keyword Parameters**:
# Keyword arguments are passed by explicitly specifying the parameter names in the function call.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function using keyword arguments
greet(age=40, name="Charlie")

# 4. **Arbitrary Positional Arguments (*args)**:
# *args allows a function to accept a variable number of positional arguments. These arguments are stored in a tuple.
def sum_numbers(*args):
    total = sum(args)
    print(f"The sum of the numbers is: {total}")

# Calling the function with different numbers of arguments
sum_numbers(1, 2, 3)
sum_numbers(5, 10, 15, 20)

# 5. **Arbitrary Keyword Arguments (**kwargs)**:
# **kwargs allows a function to accept a variable number of keyword arguments. These arguments are stored in a
# dictionary.
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
describe_person(name="Dave", age=28, profession="Engineer")

# 6. **Combining Positional, Default, Arbitrary Arguments, and Keyword Arguments**:
# A function can accept a combination of different types of parameters. However, the order matters:
# positional parameters first, followed by default parameters, then *args, and finally **kwargs.

def mixed_function(a, b=5, *args, c, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# Calling the function with positional arguments, keyword arguments, and *args/**kwargs
mixed_function(10, 3, 7, 8, c=15, name="Eve", city="Paris")

# Summary:
'''
- **Positional Parameters**: Must be passed in the correct order when calling the function.
- **Default Parameters**: Have default values that are used if no argument is passed.
- **Keyword Parameters**: Are explicitly passed by specifying the parameter name.
- **Arbitrary Arguments (*args)**: Allow the function to accept any number of positional arguments.
- **Arbitrary Keyword Arguments (**kwargs)**: Allow the function to accept any number of keyword arguments.
'''
#----------------------------------------------------------------------------------------------------------------------#
