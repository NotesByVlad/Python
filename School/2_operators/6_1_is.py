#---------------------------------------- Identity Operator: IS in Python ---------------------------------------------#
#                                        ---------------------------------

"""
The `is` operator is used to check if two variables refer to the same object in memory.
It does not check if the values of the objects are equal, but rather if they are the same object.
"""

# Key Points about `is` Operator:
'''
1. The `is` operator compares the memory addresses of two objects.
2. It returns `True` if both variables point to the same object in memory.
3. It is typically used to check for identity rather than equality.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `is`
# Example: Comparing two variables using `is`.
print("Basic IS Example:")
x = [1, 2, 3]
y = x  # y points to the same object as x
if x is y:
    print("x and y refer to the same object in memory!")
else:
    print("x and y refer to different objects.")

# Output: x and y refer to the same object in memory!
# x and y refer to the same list object in memory.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Comparing Different Objects with `is`
# Example: Comparing variables that do not refer to the same object.
print("\nComparing Different Objects with IS:")
a = [1, 2, 3]
b = [1, 2, 3]  # b has the same value as 'a' but they are different objects
if a is b:
    print("a and b refer to the same object in memory!")
else:
    print("a and b refer to different objects.")

# Output: a and b refer to different objects.
# The two lists have the same value, but they are stored in different memory locations.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using `is` to Compare with `None`
# Example: Checking if a variable is `None` using `is`.
print("\nUsing IS with None:")
var = None
if var is None:
    print("The variable is None!")
else:
    print("The variable is not None.")

# Output: The variable is None!
# We use `is` to check if the variable refers to the None object.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Identity Comparison with `is` and Mutable Objects
# Example: Comparing mutable objects with `is`.
print("\nIdentity Comparison with Mutable Objects:")
x = {"name": "Alice", "age": 30}
y = {"name": "Alice", "age": 30}
if x is y:
    print("x and y refer to the same object in memory!")
else:
    print("x and y refer to different objects.")

# Output: x and y refer to different objects.
# The two dictionaries have the same values but are different objects in memory.

#----------------------------------------------------------------------------------------------------------------------#
