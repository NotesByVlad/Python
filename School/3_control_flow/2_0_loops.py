#---------------------------------------- Loops in Python -------------------------------------------------------------#
#                                        -----------------

"""
Loops are fundamental structures in programming that allow you to repeat a block of code multiple times.
In Python, there are two main types of loops:
1. for loops: Used for iterating over a sequence (e.g., list, string, range).
2. while loops: Used when you want to execute a block of code as long as a condition is `True`.
"""

# Key Points about Loops:
'''
1. Iteration: Loops allow repetitive tasks without writing redundant code.
2. Sequence and Condition: `for` loops iterate over a sequence, while `while` loops use a condition.
3. Control Statements: Both loop types support `break`, `continue`, and `else`.
4. Efficiency: Avoid infinite loops by ensuring proper termination conditions.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. The for Loop
'''
The `for` loop is used to iterate over sequences like lists, tuples, strings, ranges, or even custom iterables.
'''

# Example:
print("Example of a for Loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#----------------------------------------------------------------------------------------------------------------------#

# 2. The while Loop
'''
The `while` loop executes a block of code as long as a given condition is `True`.
'''

# Example:
print("\nExample of a while Loop:")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

#----------------------------------------------------------------------------------------------------------------------#

# 3. break Statement
'''
The `break` statement exits the loop immediately, regardless of the loop condition.
Useful for stopping a loop prematurely when a specific condition is met.
'''

# Example:
print("\nUsing break:")
for num in range(1, 10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

#----------------------------------------------------------------------------------------------------------------------#

# 4. continue Statement
'''
The `continue` statement skips the current iteration and moves to the next one.
Useful for ignoring specific cases within a loop.
'''

# Example:
print("\nUsing continue:")
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

#----------------------------------------------------------------------------------------------------------------------#

# 5. else with Loops
'''
An `else` block in a loop executes only if the loop completes normally (i.e., not terminated by `break`).
'''

# Example:
print("\nUsing else with Loops:")
for num in range(1, 5):
    if num == 3:
        break
    print(num)
else:
    print("Loop completed without break")

#----------------------------------------------------------------------------------------------------------------------#

# 6. Nested Loops
'''
Loops can be nested inside one another to handle multi-dimensional data or complex iterations.
'''

# Example:
print("\nNested Loops Example:")
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

#----------------------------------------------------------------------------------------------------------------------#

# 7. Iterating with range()
'''
The `range()` function is commonly used with loops for numeric iterations.
Syntax: range(start, stop, step)
'''

# Example:
print("\nUsing range in Loops:")
for i in range(1, 6):  # Iterates from 1 to 5
    print(i)

#----------------------------------------------------------------------------------------------------------------------#

# 8. Iterating with Enumerate
'''
The `enumerate()` function adds a counter to a sequence, providing both the index and the value during iteration.
'''

# Example:
print("\nUsing enumerate in Loops:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

#----------------------------------------------------------------------------------------------------------------------#

# 9. Iterating with zip()
'''
The `zip()` function allows you to iterate over multiple sequences simultaneously.
'''

# Example:
print("\nUsing zip in Loops:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

#----------------------------------------------------------------------------------------------------------------------#

# 10. Infinite Loops
'''
Be cautious of infinite loops, which occur when the termination condition is never met.
While loops are especially prone to this.
'''

# Example of Infinite Loop (Commented Out to Avoid Execution):
# while True:
#     print("This will run forever!")

#----------------------------------------------------------------------------------------------------------------------#

# 11. Comparison: for vs while
'''
1. Use a `for` loop when the number of iterations is predetermined (e.g., iterating over a sequence).
2. Use a `while` loop when the number of iterations depends on a condition that may change dynamically.
'''

# Example:
print("\nComparison of for and while:")
# Using for
for i in range(3):
    print(f"for loop: {i}")

# Using while
j = 0
while j < 3:
    print(f"while loop: {j}")
    j += 1

#----------------------------------------------------------------------------------------------------------------------#

# 12. Loop Comprehensions (List, Dict, Set)
'''
List comprehensions and similar constructs provide a concise way to loop and create collections in one line.
'''

# Example:
print("\nUsing List Comprehensions:")
squares = [x**2 for x in range(1, 6)]  # Square of numbers from 1 to 5
print("Squares:", squares)

#----------------------------------------------------------------------------------------------------------------------#

# 13. Common Pitfalls in Loops
'''
1. Infinite Loops: Ensure a termination condition is met.
2. Modifying the Sequence: Avoid changing the sequence while iterating over it.
3. Nested Loops: Be mindful of performance in complex nested loops.
'''

# Example of Common Pitfall:
# Incorrect: Modifying a list while iterating
# nums = [1, 2, 3, 4]
# for num in nums:
#     nums.remove(num)  # Modifying during iteration can cause unexpected behavior
