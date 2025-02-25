#---------------------------------------- For Loops in Python ---------------------------------------------------------#
#                                        ---------------------

"""
In programming, a for loop is used to iterate over a sequence (e.g., a list, tuple, string, or range).
It allows you to execute a block of code repeatedly for each item in the sequence.
Python's `for` loop is simple and flexible, making it ideal for iterating over elements of collections.
"""

# Key Points about For Loops:
'''
1. Iteration: Executes a block of code for each item in a sequence.
2. Sequence: Can iterate over various sequences like lists, tuples, strings, dictionaries, and ranges.
3. Automatic: Python handles the iteration automatically without requiring an index or counter.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic For Loop
'''
The basic syntax of a `for` loop in Python is:
for variable in sequence:
    # Code block
'''

# Example:
print("Basic For Loop Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using range() in For Loops
'''
The `range()` function generates a sequence of numbers, which is useful for iterating a specific number of times.
Syntax: range(start, stop, step)
- start: Starting value (default is 0)
- stop: End value (exclusive)
- step: Increment (default is 1)
'''

# Example:
print("\nUsing range in For Loops:")
for i in range(1, 6):  # Iterates from 1 to 5
    print(i)

#----------------------------------------------------------------------------------------------------------------------#

# 3. Iterating Over Strings
'''
You can use a `for` loop to iterate over the characters in a string.
'''

# Example:
print("\nIterating Over a String:")
word = "Python"
for char in word:
    print(char)

#----------------------------------------------------------------------------------------------------------------------#

# 4. Nested For Loops
'''
A `for` loop can be nested inside another `for` loop, which is useful for working with multi-dimensional data.
'''

# Example:
print("\nNested For Loops Example:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

#----------------------------------------------------------------------------------------------------------------------#

# 5. Using break and continue
'''
- `break`: Exits the loop prematurely.
- `continue`: Skips the current iteration and proceeds to the next one.
'''

# Example:
print("\nUsing break and continue:")
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop when num is 5
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

#----------------------------------------------------------------------------------------------------------------------#

# 6. Using else with For Loops
'''
An optional `else` block can be added to a `for` loop. It executes only if the loop is not terminated by a `break`.
'''

# Example:
print("\nFor Loop with Else:")
for number in range(1, 6):
    if number == 4:
        break
else:
    print("Completed without break")

#----------------------------------------------------------------------------------------------------------------------#

# 7. Iterating Over Dictionaries
'''
To iterate over key-value pairs in a dictionary, use the `items()` method.
'''

# Example:
print("\nIterating Over a Dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

#----------------------------------------------------------------------------------------------------------------------#

# 8. Enumerate in For Loops
'''
The `enumerate()` function adds a counter to the iteration, providing the index and the value of each item.
'''

# Example:
print("\nUsing Enumerate in For Loops:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

#----------------------------------------------------------------------------------------------------------------------#

# 9. Zip in For Loops
'''
The `zip()` function allows you to iterate over multiple sequences simultaneously.
'''

# Example:
print("\nUsing Zip in For Loops:")
names = ["John", "Jane", "Doe"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

#----------------------------------------------------------------------------------------------------------------------#

# 10. List Comprehensions (Shortcut for Loops)
'''
List comprehensions provide a concise way to create lists using a `for` loop in a single line.
Syntax: [expression for item in sequence if condition]
'''

# Example:
print("\nUsing List Comprehensions:")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

#----------------------------------------------------------------------------------------------------------------------#

# 11. Common Pitfalls
'''
1. Modifying the sequence during iteration (can lead to unexpected behavior).
2. Forgetting the colon `:` after `for` or `else`.
3. Using `break` when `else` is needed for completion.
'''

# Example:
# Incorrect: for i in range(5) (Missing colon)
# Correct: for i in range(5):

#----------------------------------------------------------------------------------------------------------------------#
