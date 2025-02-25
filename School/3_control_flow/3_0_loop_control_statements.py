#---------------------------------------- Loop Control Statements in Python -------------------------------------------#
#                                        ----------------------

"""
Loop control statements in Python are used to modify the flow of execution within loops.
These statements allow you to either exit the loop prematurely, skip an iteration, or do nothing in a loop.
The three main loop control statements are:
1. break: Exits the loop completely.
2. continue: Skips the current iteration and continues with the next one.
3. pass: Does nothing, used as a placeholder.
"""

# Key Points about Loop Control Statements:
'''
1. `break`: Exits the loop entirely, even if the loop's condition is still true.
2. `continue`: Skips the remaining code inside the loop for the current iteration and moves to the next iteration.
3. `pass`: A null statement that does nothing, often used as a placeholder.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. The `break` Statement
'''
The `break` statement is used to terminate the loop prematurely when a specific condition is met. 
It exits the loop entirely and moves to the next line of code after the loop.
'''

# Example:
print("Using the break Statement:")
for num in range(1, 10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

# Output: 1 2 3 4
# The loop breaks when num is 5, so 5 and higher numbers are not printed.

#----------------------------------------------------------------------------------------------------------------------#

# 2. The `continue` Statement
'''
The `continue` statement is used to skip the rest of the current iteration and move to the next iteration of the loop.
It is often used when you want to ignore specific cases within the loop.
'''

# Example:
print("\nUsing the continue Statement:")
for num in range(1, 10):
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)

# Output: 1 3 5 7 9
# The loop skips even numbers and continues with the next iteration.

#----------------------------------------------------------------------------------------------------------------------#

# 3. The `pass` Statement
'''
The `pass` statement is a null operation. It is used when a statement is syntactically required but you don't want 
to execute any code.
Commonly used as a placeholder for future code or when no action is needed in a loop.
'''

# Example:
print("\nUsing the pass Statement:")
for num in range(1, 6):
    if num == 3:
        pass  # Do nothing when num is 3
    else:
        print(num)

# Output: 1 2 4 5
# The `pass` statement does nothing when num is 3, but it allows the loop to continue.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Nested Loops with Control Statements
'''
Control statements like `break`, `continue`, and `pass` can be used inside nested loops to affect the flow of 
execution at different levels.
'''

# Example (using break in a nested loop):
print("\nBreak in Nested Loops:")
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            break  # Break the inner loop when i and j are both 2
        print(f"i={i}, j={j}")

# Output:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1

# Example (using continue in a nested loop):
print("\nContinue in Nested Loops:")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue  # Skip when j is 2
        print(f"i={i}, j={j}")

# Output:
# i=1, j=1
# i=1, j=3
# i=2, j=1
# i=2, j=3
# i=3, j=1
# i=3, j=3

#----------------------------------------------------------------------------------------------------------------------#

# 5. Using Control Statements in While Loops
'''
Control statements can be used in both `for` and `while` loops. 
Here’s an example using `break`, `continue`, and `pass` in a `while` loop.
'''

# Example (using break in a while loop):
print("\nBreak in While Loop:")
x = 0
while x < 10:
    if x == 5:
        break  # Exit the loop when x equals 5
    print(x)
    x += 1

# Output: 0 1 2 3 4
# The loop breaks when x is 5, so 5 and higher numbers are not printed.

# Example (using continue in a while loop):
print("\nContinue in While Loop:")
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # Skip even numbers
    print(x)

# Output: 1 3 5 7 9
# The loop skips even numbers and continues with the next iteration.

# Example (using pass in a while loop):
print("\nPass in While Loop:")
x = 0
while x < 5:
    x += 1
    if x == 3:
        pass  # Do nothing when x is 3
    else:
        print(x)

# Output: 1 2 4 5
# The `pass` statement does nothing when x is 3, but allows the loop to continue.

#----------------------------------------------------------------------------------------------------------------------#

# 6. Common Pitfalls in Loop Control Statements
'''
1. Infinite loops: Using `continue` or `pass` incorrectly can cause infinite loops, especially in `while` loops.
2. Incorrect use of `break`: Ensure that `break` is used to exit the loop based on a condition, or it may exit 
   prematurely.
3. Skipping necessary iterations: Using `continue` improperly might skip critical logic in some iterations.
'''

# Example of Common Pitfall (Infinite loop):
# x = 0
# while True:
#     if x == 5:
#         continue  # This will skip the increment step and the loop will run forever

#----------------------------------------------------------------------------------------------------------------------#
