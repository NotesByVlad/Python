#----------------------------------------   Return Statements in Python   ---------------------------------------------#
#                                        ---------------------------------

"""
In Python, a function is typically used to perform some computation or task, and it can return a value using the
`return` statement.
The `return` statement is what sends the result of the function back to the caller. Once the return statement is
executed, the function ends,
and any code after the return statement is not executed.

Key Points:
1. **Basic Return**: A function can return a single value, such as a number, string, list, etc.
2. **Multiple Return Values**: A function can return multiple values as a tuple.
3. **No Return**: A function can have no return statement, in which case it implicitly returns `None`.
4. **Returning from Different Places**: You can use return statements within conditions or loops, allowing
   for more control over when to return a value.
"""

# 1. **Basic Return**:
# A simple function that returns the sum of two numbers.
def add(a, b):
    return a + b

# Calling the function and printing the returned result
result = add(10, 5)
print(f"The sum of 10 and 5 is: {result}")

# 2. **Multiple Return Values**:
# A function can return multiple values, which will be returned as a tuple.
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns multiple values

# Calling the function and unpacking the returned tuple
quot, rem = divide_and_remainder(10, 3)
print(f"Quotient: {quot}, Remainder: {rem}")

# 3. **No Return Statement**:
# If a function does not have a return statement, it implicitly returns `None`.
def greet(name):
    print(f"Hello, {name}!")

# Calling the function and printing the returned value
result = greet("Alice")
print(f"Returned value from greet function: {result}")  # This will print 'None'

# 4. **Returning from Conditional Statements**:
# You can use the return statement inside if-else conditions to return different values based on conditions.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Calling the function with different values
print(check_number(10))  # Positive
print(check_number(-5))  # Negative
print(check_number(0))   # Zero

# 5. **Returning from Loops**:
# A return statement can also be used inside loops to stop the loop early and return a value immediately.
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number  # Returns the first even number and exits the function
    return None  # If no even number is found, return None

# Calling the function with a list of numbers
numbers = [1, 3, 5, 6, 7, 9]
first_even = find_first_even(numbers)
print(f"The first even number in the list is: {first_even}")

# 6. **Returning `None` Explicitly**:
# A function can also return `None` explicitly, which is equivalent to not returning anything at all.
def do_nothing():
    return None

# Calling the function and printing the result
result = do_nothing()
print(f"Returned value from do_nothing: {result}")  # This will print 'None'

# Summary:
'''
- The **return** statement is used to send a result back from a function to the caller.
- A function can return a single value or multiple values as a tuple.
- If no return statement is provided, the function implicitly returns `None`.
- You can use return statements inside conditional statements and loops to control the flow of execution and return 
  values at specific points.
'''
#----------------------------------------------------------------------------------------------------------------------#
