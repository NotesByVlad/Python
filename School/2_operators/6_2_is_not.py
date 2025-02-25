#---------------------------------------- Identity Operator: IS NOT in Python -----------------------------------------#
#                                        -------------------------------------

"""
The `is not` operator is used to check if two variables do not refer to the same object in memory.
It is the opposite of the `is` operator.
"""

# Key Points about `is not` Operator:
'''
1. The `is not` operator checks if two variables do not refer to the same object in memory.
2. It returns `True` if the variables refer to different objects, even if their values are the same.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `is not`
# Example: Comparing two variables using `is not`.
print("Basic IS NOT Example:")
x = [1, 2, 3]
y = [1, 2, 3]  # x and y are different objects
if x is not y:
    print("x and y do not refer to the same object in memory!")
else:
    print("x and y refer to the same object.")

# Output: x and y do not refer to the same object in memory!
# Even though both lists have the same value, they are different objects.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using `is not` to Check if a Variable is not `None`
# Example: Checking if a variable is not `None` using `is not`.
print("\nUsing IS NOT with None:")
var = 10
if var is not None:
    print("The variable is not None!")
else:
    print("The variable is None.")

# Output: The variable is not None!
# We use `is not` to check that the variable is not referring to `None`.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Identity Comparison with `is not` on Mutable Objects
# Example: Comparing mutable objects with `is not`.
print("\nIdentity Comparison with Mutable Objects using IS NOT:")
a = {"name": "Alice", "age": 30}
b = {"name": "Alice", "age": 30}
if a is not b:
    print("a and b do not refer to the same object in memory!")
else:
    print("a and b refer to the same object.")

# Output: a and b do not refer to the same object in memory!
# Although the dictionaries have the same values, they are different objects.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `is not` for String Comparisons (Immutable Example)
# Example: Checking for identity with immutable objects like strings.
print("\nUsing IS NOT with Immutable Objects:")
x = "hello"
y = "hello"
if x is not y:
    print("x and y do not refer to the same object!")
else:
    print("x and y refer to the same object!")

# Output: x and y refer to the same object!
# Python may optimize memory for small strings, making them point to the same object.
