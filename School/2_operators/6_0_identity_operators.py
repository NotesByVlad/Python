#----------------------------------------   Identity Operators in Python   --------------------------------------------#
#                                        ----------------------------------

"""
Identity operators are used to compare the memory locations of two objects.
"""

# Key Identity Operators:
'''
- is: Returns True if both operands refer to the same object in memory.
- is not: Returns True if both operands do not refer to the same object in memory.
'''

# Examples:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b: {a is b}")  # True, both refer to the same object
print(f"a is c: {a is c}")  # False, different objects even though the content is the same
print(f"a is not c: {a is not c}")  # True
#----------------------------------------------------------------------------------------------------------------------#


# ------------------------------- Using IS and IS NOT for Identity Comparison in Python -------------------------------#
#                                 ------------------------------------------------------

'''
The `is` and `is not` operators are used to check if two variables point to the same object in memory 
(identity comparison).
These operators do not compare the values of objects, but their identity.
'''

# Key Points about `is` and `is not`:
'''
1. `is`: Returns `True` if two variables point to the same object in memory.
2. `is not`: Returns `True` if two variables point to different objects in memory.
'''

# ---------------------------------------------------------------------------------------------------------------------#

# 1. Identity Comparison with `is` and `is not`
# Example: Checking identity of variables.
print("Identity Comparison using IS and IS NOT:")
x = 1000
y = 1000
z = x
if x is y:
	print("x and y refer to the same object.")
else:
	print("x and y refer to different objects.")

if x is z:
	print("x and z refer to the same object.")
else:
	print("x and z refer to different objects.")

# Output:
# x and y refer to different objects.
# x and z refer to the same object.
# Even though x and y have the same value, they are different objects, while x and z are the same object.

# ---------------------------------------------------------------------------------------------------------------------#

# 2. Using `is` and `is not` with None
# Example: Checking if variables are `None` using `is` and `is not`.
print("\nUsing IS and IS NOT with None:")
a = None
b = 5
if a is None:
	print("a is None.")
else:
	print("a is not None.")

if b is not None:
	print("b is not None.")

# Output:
# a is None.
# b is not None.
# We use `is` to check for identity with None.

# ---------------------------------------------------------------------------------------------------------------------#

# 3. Identity Comparison with Lists (Mutable Objects)
# Example: Using `is` and `is not` with mutable objects like lists.
print("\nIdentity Comparison with Lists:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
if list1 is list2:
	print("list1 and list2 refer to the same object.")
else:
	print("list1 and list2 refer to different objects.")

if list1 is list3:
	print("list1 and list3 refer to the same object.")
else:
	print("list1 and list3 refer to different objects.")

# Output:
# list1 and list2 refer to different objects.
# list1 and list3 refer to the same object.
# list1 and list2 have the same value, but they are different objects, while list1 and list3 refer to the same object.

# ---------------------------------------------------------------------------------------------------------------------#
