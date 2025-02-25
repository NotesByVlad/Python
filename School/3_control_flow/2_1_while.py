#---------------------------------------- While Loops in Python -------------------------------------------------------#
#                                        -----------------------

"""
A `while` loop in Python repeatedly executes a block of code as long as a specified condition is `True`.
It is primarily used when the number of iterations is not known beforehand and depends on a condition.
"""

# Key Points about While Loops:
'''
1. Conditional: Executes based on a condition that is evaluated before each iteration.
2. Potentially Infinite: Must ensure the condition eventually becomes `False` to avoid infinite loops.
3. Flexible: Suitable for situations where the termination depends on a dynamic condition.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic While Loop
'''
The syntax of a `while` loop is:
while condition:
    # Code block
'''

# Example:
print("Basic While Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1  # Increment count to avoid an infinite loop

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using break in While Loops
'''
The `break` statement is used to exit the loop prematurely, even if the condition is still `True`.
'''

# Example:
print("\nUsing break in While Loop:")
num = 1
while num <= 10:
    if num == 6:
        break  # Exit the loop when num is 6
    print(num)
    num += 1

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using continue in While Loops
'''
The `continue` statement skips the rest of the code in the current iteration and proceeds to the next iteration.
'''

# Example:
print("\nUsing continue in While Loop:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

#----------------------------------------------------------------------------------------------------------------------#

# 4. Infinite Loops
'''
A `while` loop without a condition that becomes `False` will result in an infinite loop.
Use caution and always include a way to terminate the loop.
'''

# Example:
# Uncomment the code below to observe an infinite loop (use Ctrl+C to stop it):
# while True:
#     print("This is an infinite loop!")

#----------------------------------------------------------------------------------------------------------------------#

# 5. While Loop with Else
'''
The `else` block in a `while` loop executes only if the loop condition becomes `False` naturally (not via `break`).
'''

# Example:
print("\nWhile Loop with Else:")
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed naturally")

#----------------------------------------------------------------------------------------------------------------------#

# 6. Nested While Loops
'''
A `while` loop can be nested within another `while` loop to work with multiple levels of conditions.
'''

# Example:
print("\nNested While Loops:")
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"Outer loop {i}, Inner loop {j}")
        j += 1
    i += 1

#----------------------------------------------------------------------------------------------------------------------#

# 7. Using Conditions Dynamically
'''
The condition of a `while` loop can be updated dynamically inside the loop, making it flexible.
'''

# Example:
print("\nDynamic Condition Update:")
total = 0
while total < 50:
    total += 10
    print("Current total:", total)

#----------------------------------------------------------------------------------------------------------------------#

# 8. Using Input in While Loops
'''
The `while` loop can be used to repeatedly prompt the user until a valid input is received.
'''

# Example:
print("\nUsing Input in While Loop:")
password = ""
while password != "12345":
    password = input("Enter the password: ")
print("Access granted!")

#----------------------------------------------------------------------------------------------------------------------#

# 9. Simulating Do-While Behavior
'''
Python does not have a built-in `do-while` loop, but the same behavior can be simulated by using a `while` loop with 
an initial condition that always evaluates to `True` and breaking inside the loop.
'''

# Example:
print("\nSimulating Do-While Loop:")
while True:
    guess = int(input("Guess a number (0 to exit): "))
    if guess == 0:
        break
    print("You guessed:", guess)

#----------------------------------------------------------------------------------------------------------------------#

# 10. Common Pitfalls
'''
1. Infinite Loops: Always ensure the loop has a way to terminate.
2. Off-by-One Errors: Carefully initialize and update loop variables to avoid running the loop too many or too few times.
3. Condition Logic: Incorrect or overly complex conditions can make the loop unpredictable.
'''

# Example of Infinite Loop (Uncomment to Test):
# x = 10
# while x > 0:  # This condition is always true because x is not decremented
#     print("Infinite loop!")

# Corrected Version:
# x = 10
# while x > 0:
#     print("Count:", x)
#     x -= 1  # Decrement x to terminate the loop

#----------------------------------------------------------------------------------------------------------------------#
