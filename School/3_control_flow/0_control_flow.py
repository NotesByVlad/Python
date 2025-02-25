# ----------------------------------------   Control Flow in Python   -------------------------------------------------#
#                                        -----------------------------

"""
Control flow in Python refers to the order in which individual statements, instructions, or function calls are
executed or evaluated. It allows a program to make decisions, repeat tasks, and change the flow of execution
based on conditions or iterations.

### Key Concepts:
- **Conditional Statements**: These allow you to make decisions based on whether a condition is true or false.
- **Loops**: These are used to repeat a block of code multiple times.
- **Break, Continue, and Pass**: These are special statements that control the flow of loops or conditionals.
- **Exception Handling**: Using `try`, `except`, `else`, and `finally` to handle errors and control program flow
in case of exceptions.
"""

# 1. **If, Elif, and Else Statements**:
# Conditional statements are used to decide which block of code to execute based on a condition.

# Simple if statement:
x = 5
if x > 0:
	print("x is positive")

# If-elif-else statement:
age = 20
if age < 18:
	print("You are a minor.")
elif age >= 18 and age < 65:
	print("You are an adult.")
else:
	print("You are a senior.")

# Explanation:
# The `if` block is executed if the condition is `True`.
# If the `if` condition is `False`, Python checks the `elif` block.
# If none of the conditions are met, the `else` block is executed.

# 2. **Nested If Statements**:
# You can nest `if` statements inside other `if` or `elif` blocks.

x = 10
y = 20
if x > 5:
	if y > 10:
		print("Both conditions are True.")
	else:
		print("Only x > 5 is True.")
else:
	print("x is not greater than 5.")

# Explanation:
# The inner `if` statement is checked only if the outer `if` condition is `True`.

# 3. **Boolean Logic in Conditional Statements**:
# You can combine multiple conditions using logical operators: `and`, `or`, and `not`.

x = 10
y = 20
if x > 5 and y < 30:
	print("Both conditions are True.")

if x < 5 or y > 15:
	print("At least one condition is True.")

if not x == 10:
	print("x is not equal to 10.")
else:
	print("x is equal to 10.")

# Explanation:
# `and` returns `True` only if both conditions are `True`.
# `or` returns `True` if at least one condition is `True`.
# `not` negates the condition, making `True` `False` and vice versa.

# 4. **While Loops**:
# A `while` loop repeats a block of code as long as the given condition is `True`.

count = 0
while count < 5:
	print(f"Count is {count}")
	count += 1  # Increment count

# Explanation:
# The loop runs as long as `count < 5`. After each iteration, the `count` is incremented.

# 5. **For Loops**:
# A `for` loop is used to iterate over a sequence (like a list, tuple, or string).

# Loop through a list:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
	print(num)

# Loop through a string:
for char in "Hello":
	print(char)

# Using `range()` in a for loop to iterate over a sequence of numbers:
for i in range(3):
	print(f"Iteration {i + 1}")

# Explanation:
# The `for` loop iterates through each element in the sequence (list, string, etc.).
# The `range()` function generates a sequence of numbers.

# 6. **Break, Continue, and Pass Statements**:
# These are control flow statements that modify the behavior of loops.

# The `break` statement exits the loop early.
for i in range(10):
	if i == 5:
		print("Breaking the loop at 5")
		break
	print(i)

# The `continue` statement skips the current iteration and moves to the next one.
for i in range(5):
	if i == 2:
		continue  # Skip when i is 2
	print(i)

# The `pass` statement is a placeholder. It does nothing but is syntactically required.
for i in range(3):
	if i == 2:
		pass  # Do nothing
	else:
		print(i)

# Explanation:
# `break` stops the loop as soon as the condition is met.
# `continue` skips the current iteration and continues with the next one.
# `pass` does nothing and is used when a statement is syntactically required but no action is needed.

# 7. **For-Else and While-Else**:
# Both `for` and `while` loops can have an `else` block, which executes when the loop completes normally
# (i.e., without a `break`).

# For loop with else:
for i in range(3):
	print(i)
else:
	print("Loop finished normally.")

# While loop with else:
count = 0
while count < 3:
	print(count)
	count += 1
else:
	print("While loop finished.")

# Explanation:
# The `else` block runs after the loop completes all its iterations unless the loop was terminated by a `break`.

# 8. **Exception Handling**:
# Python provides a mechanism to handle errors during program execution using `try`, `except`, `else`, and `finally`.

# Basic try-except block:
try:
	num = int(input("Enter a number: "))
	print(f"You entered: {num}")
except ValueError:
	print("That's not a valid number!")

# Handling multiple exceptions:
try:
	a = 10 / 0  # Division by zero
except ZeroDivisionError:
	print("Cannot divide by zero.")
except Exception as e:
	print(f"An error occurred: {e}")

# Using else and finally:
try:
	x = 5 / 2
except ZeroDivisionError:
	print("Cannot divide by zero.")
else:
	print("Division was successful.")
finally:
	print("This block always runs, regardless of errors.")

# Explanation:
# The `try` block contains the code that may raise an exception.
# The `except` block catches specific exceptions and handles them.
# The `else` block runs if no exceptions were raised.
# The `finally` block always runs, whether or not an exception occurred.

# 9. **Ternary Conditional Expression**:
# A short form of the `if-else` statement, also known as the conditional expression.

x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)

# Explanation:
# This expression is equivalent to:
# if x > 0:
#     result = "Positive"
# else:
#     result = "Non-positive"

# 10. **Summary**:
'''
- **If, Elif, Else Statements**: Used to control the flow based on conditions.
- **Nested If Statements**: If statements inside other if or elif blocks.
- **Boolean Logic**: Use logical operators (`and`, `or`, `not`) to combine conditions.
- **While Loops**: Repeats a block of code while a condition is true.
- **For Loops**: Iterates over sequences like lists, tuples, or strings.
- **Break, Continue, Pass**: Control the flow inside loops. `break` exits the loop, `continue` skips an iteration, 
  and `pass` does nothing.
- **For-Else, While-Else**: Executes an `else` block after a loop completes normally.
- **Exception Handling**: Use `try`, `except`, `else`, and `finally` to handle errors gracefully.
- **Ternary Conditional Expression**: A shorthand for `if-else` statements.
'''

# ----------------------------------------------------------------------------------------------------------------------#
