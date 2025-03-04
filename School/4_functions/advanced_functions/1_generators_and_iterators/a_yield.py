#----------------------------------------   'yield' in Python   -------------------------------------------------------#
#                                        -----------------------

"""
In Python, the `yield` keyword is used in a function to make it a generator function.
When the function is called, it does not execute immediately but returns a generator object.

The `yield` keyword pauses the function, saving its state, and resumes from where it left off on subsequent calls.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about `yield`:
'''
- Used in Generator Functions: Functions with `yield` are generator functions.
- State Preservation: The function's local state is preserved across `yield` calls.
- Produces Values: Each `yield` produces a value for the calling code.
- Lazy Evaluation: Values are generated on demand, saving memory.
- Can Be Used Multiple Times: `yield` can be used in loops or conditionals for multiple outputs.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Basic Example of `yield`

def simple_generator():
    """A simple generator using yield."""
    yield 1
    yield 2
    yield 3

# Using the Generator
for value in simple_generator():
    print(value)

# Output:
# 1
# 2
# 3

#----------------------------------------------------------------------------------------------------------------------#

# `yield` with Stateful Generators

def countdown(start):
    """Generator that counts down from a start value."""
    while start > 0:
        yield start
        start -= 1

# Using the Countdown Generator
for number in countdown(5):
    print(number)

# Output:
# 5
# 4
# 3
# 2
# 1

#----------------------------------------------------------------------------------------------------------------------#

# Generator Functions vs. Normal Functions
'''
- Normal functions use `return` to output a value and terminate the function.
- Generator functions use `yield` to produce a value and pause execution, allowing resumption later.

Example:

def normal_function():
    return "Finished"

def generator_function():
    yield "Paused"
    yield "Resumed"

print(normal_function())            # Output: Finished
for state in generator_function():  # Output: Paused, Resumed
    print(state)
'''
#----------------------------------------------------------------------------------------------------------------------#

# Sending Values to a Generator

def echo():
    """A generator that echoes the value sent to it."""
    while True:
        value = yield
        print(f"Received: {value}")

# Using the Generator

echo_gen = echo()
next(echo_gen)  # Prime the generator

echo_gen.send("Hello")  # Output: Received: Hello
echo_gen.send("World")  # Output: Received: World

#----------------------------------------------------------------------------------------------------------------------#

# Using `yield` for Infinite Sequences

def infinite_numbers():
    """An infinite generator that produces consecutive numbers."""
    num = 0
    while True:
        yield num
        num += 1

# Using the Infinite Generator
infinite_gen = infinite_numbers()
for _ in range(5):
    print(next(infinite_gen))

# Output:
# 0
# 1
# 2
# 3
# 4

#----------------------------------------------------------------------------------------------------------------------#

# Benefits of Using `yield`
'''
1. Memory Efficiency: Generates values on demand instead of storing them in memory.
2. Simplicity: Provides a clean way to write stateful iterators without manually managing state.
3. Infinite Sequences: Can generate values indefinitely, making it suitable for tasks like data streams.
4. Enhanced Control: Allows sending data back into the generator using `.send()`.
'''
#----------------------------------------------------------------------------------------------------------------------#
