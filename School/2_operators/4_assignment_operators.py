#----------------------------------------   Assignment Operators in Python   ------------------------------------------#
#                                        -----------------------------------

"""
Assignment operators are used to assign values to variables.
"""

# Key Assignment Operators:
'''
- =: Assigns the right operand to the left operand.
- +=: Adds the right operand to the left operand and assigns the result to the left operand.
- -=: Subtracts the right operand from the left operand and assigns the result to the left operand.
- *=: Multiplies the left operand by the right operand and assigns the result to the left operand.
- /=: Divides the left operand by the right operand and assigns the result to the left operand.
- //=: Performs floor division and assigns the result to the left operand.
- %=: Performs modulus and assigns the result to the left operand.
- **=: Performs exponentiation and assigns the result to the left operand.
'''

# Examples:
a = 5
b = 3

a += b  # Equivalent to a = a + b
print(f"a += b:  {a}")

a -= b  # Equivalent to a = a - b
print(f"a -= b:  {a}")

a *= b  # Equivalent to a = a * b
print(f"a *= b:  {a}")

a /= b  # Equivalent to a = a / b
print(f"a /= b:  {a}")

a %= 2           # Modulus and assign
print(f"a %= b:  {a}")

# Exponent and Floor Division Assignments
a = 5
a **= 2          # Exponent and assign
print(f"a **= b: {a}")

a //= 3          # Floor Division and assign
print(f"a //= b: {a}")
#----------------------------------------------------------------------------------------------------------------------#

