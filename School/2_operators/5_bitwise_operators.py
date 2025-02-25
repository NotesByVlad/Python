#----------------------------------------   Bitwise Operators in Python   ---------------------------------------------#
#                                        ---------------------------------

"""
Bitwise operators are used to perform operations on binary numbers.
"""

# Key Bitwise Operators:
'''
- & (AND): Performs a bitwise AND operation.
- | (OR): Performs a bitwise OR operation.
- ^ (XOR): Performs a bitwise XOR operation.
- ~ (NOT): Performs a bitwise NOT operation (inverts all bits).
- << (Left Shift): Shifts the bits to the left by the specified number of positions.
- >> (Right Shift): Shifts the bits to the right by the specified number of positions.
'''

# Examples:
a = 5  # In binary: 0101
b = 3  # In binary: 0011

print(f"a & b: {a & b}")  # Bitwise AND
print(f"a | b: {a | b}")  # Bitwise OR
print(f"a ^ b: {a ^ b}")  # Bitwise XOR
print(f"~a: {~a}")  # Bitwise NOT
print(f"a << 1: {a << 1}")  # Left Shift
print(f"a >> 1: {a >> 1}")  # Right Shift
#----------------------------------------------------------------------------------------------------------------------#
