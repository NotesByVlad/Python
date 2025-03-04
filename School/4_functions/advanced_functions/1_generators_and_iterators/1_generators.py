#----------------------------------------   Generators in Python   ----------------------------------------------------#
#                                        --------------------------

"""
Generators in Python are a special type of iterable that allow for lazy evaluation.
They generate values on the fly and do not store the entire sequence in memory, making them
memory-efficient for large datasets or infinite sequences.

Generators are created using functions with the `yield` keyword or generator expressions.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Generators:
'''
- Generator Function: A function that uses `yield` to produce values one at a time.
- Lazy Evaluation: Values are generated only when requested.
- Infinite Sequences: Generators can represent sequences that are too large to store in memory.
- Stateful: Generators maintain their state between iterations.
- Memory Efficiency: Use less memory compared to storing large lists in memory.
- Generator Expressions: Compact syntax for creating generators.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Creating a Generator Function

def count_up_to(limit):
    """Generator that counts up to a specified limit."""
    count = 1
    while count <= limit:
        yield count  # Produces the next value
        count += 1

# Using the Generator
for number in count_up_to(5):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5

#----------------------------------------------------------------------------------------------------------------------#

# Generator Expressions

# A compact way to create a generator
squares = (x**2 for x in range(5))

# Iterating over the Generator Expression
for square in squares:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16

#----------------------------------------------------------------------------------------------------------------------#

# Advantages of Generators
'''
1. Memory Efficiency: Since generators produce values on the fly, they are ideal for large datasets.
2. Infinite Sequences: Generators can handle infinite sequences like Fibonacci numbers without memory issues.
3. Stateful Iteration: Generators maintain their state, making them suitable for complex stateful computations.
4. Cleaner Syntax: `yield` allows for clear and concise logic compared to manually managing iterators.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Example: Infinite Generator

def fibonacci():
    """An infinite generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the Generator
fib = fibonacci()
for _ in range(5):
    print(next(fib))

# Output:
# 0
# 1
# 1
# 2
# 3
#----------------------------------------------------------------------------------------------------------------------#