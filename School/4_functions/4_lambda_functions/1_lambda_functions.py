#----------------------------------------   Lambda Functions in Python   ----------------------------------------------#
#                                        ------------------------------------

"""
In Python, a lambda function is a small anonymous function defined using the `lambda` keyword.
Lambda functions are also known as anonymous functions because they do not require a name. They can have any number
of arguments,
but they can only have a single expression. Lambda functions are commonly used for short, throwaway functions or when
passing a
function as an argument to higher-order functions (functions that take other functions as arguments).

While lambda functions provide a more concise way to write small functions, traditional functions
(using the `def` keyword)
can be more readable for complex logic.

Key Points:
1. **Lambda Function Syntax**: A lambda function is defined using the `lambda` keyword, followed by parameters
   and a single expression.
2. **Anonymous Functions**: Lambda functions do not require a name.
3. **Traditional Function**: The `def` keyword is used to define traditional functions with a name, and they can
   contain multiple expressions.
4. **Use Cases**: Lambda functions are often used in conjunction with functions like `map()`, `filter()`, and
   `sorted()`.
"""

# 1. **Traditional Function**:
# First, let's define a regular function using the `def` keyword. This is a named function.
def add(a, b):
    return a + b

# Calling the traditional function
result = add(5, 3)
print(f"Traditional Function result: {result}")

# 2. **Lambda Function**:
# Now, let's define the same function as a lambda function. A lambda function is an anonymous function and is
# defined in one line.
add_lambda = lambda a, b: a + b

# Calling the lambda function
lambda_result = add_lambda(5, 3)
print(f"Lambda Function result: {lambda_result}")

# 3. **Using Lambda Functions in Built-in Functions**:
# Lambda functions are often used in functions like `map()`, `filter()`, and `sorted()`.
# They allow you to write compact code for small tasks.
numbers = [1, 2, 3, 4, 5]

# Using lambda with `map()` to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers using map and lambda: {squared_numbers}")

# Using lambda with `filter()` to get even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using filter and lambda: {even_numbers}")

# Using lambda with `sorted()` to sort the list based on the second character of each string
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda x: x[1])
print(f"Words sorted by second character using lambda: {sorted_words}")

# 4. **Lambda with Multiple Arguments**:
# A lambda function can take multiple arguments, just like a normal function.
multiply = lambda x, y, z: x * y * z

# Calling the lambda function
multiplication_result = multiply(2, 3, 4)
print(f"Multiplication result using lambda: {multiplication_result}")

# 5. **Returning Lambda Functions from Other Functions**:
# Lambda functions can also be returned from other functions.
def make_multiplier(factor):
    return lambda x: x * factor

# Creating a lambda function that multiplies a number by 3
multiply_by_3 = make_multiplier(3)
print(f"Result of multiplying 5 by 3 using lambda: {multiply_by_3(5)}")

# 6. **Lambda Functions vs Regular Functions**:
# Lambda functions are more concise, but they are limited to a single expression.
# Traditional functions (using `def`) are better suited for more complex logic.

# Traditional function with multiple expressions
def complex_add(a, b):
    sum_result = a + b
    return sum_result * 2  # Additional logic after returning

# Lambda function with single expression
complex_add_lambda = lambda a, b: (a + b) * 2

# Both functions give the same result
print(f"Traditional function result: {complex_add(5, 3)}")
print(f"Lambda function result: {complex_add_lambda(5, 3)}")

# Summary:
'''
- **Lambda functions**: Anonymous functions defined using `lambda`, with a single expression.
- **Traditional functions**: Defined using `def` and can have multiple expressions, making them more versatile.
- **Use cases**: Lambda functions are useful for small, short-lived tasks, and are often used with higher-order 
  functions like `map()`, `filter()`, and `sorted()`.
- **Lambda vs Regular Function**: Regular functions are more suitable for complex tasks with multiple expressions, 
  while lambda functions are concise for simple tasks.
'''
#----------------------------------------------------------------------------------------------------------------------#
