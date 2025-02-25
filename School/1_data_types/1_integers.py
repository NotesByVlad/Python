#----------------------------------------   Integers in Python   ------------------------------------------------------#
#                                        -----------------------

"""
In Python, an integer (int) is a whole number, positive or negative, without a decimal point.
Integers are one of the most commonly used data types and support various operations,
methods, and features.

Python's integers are of unlimited precision, meaning they can grow as large as the
available memory allows.
"""

# Key Points about Integers:
'''
- Whole Numbers: Integers do not have a fractional or decimal part.
- Arithmetic Operations: Integers support standard arithmetic operations.
- Type Casting: Integers can be converted from strings, floats, or other data types.
- Bitwise Operations: Integers support bitwise manipulations.
- Precision: Python integers have unlimited precision, unlike fixed-size integers in some languages.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Integer Initialization
int1 = 42  # Positive integer
int2 = -17  # Negative integer
int3 = 0  # Zero (neutral integer)

print("Integer 1:", int1)
print("Integer 2:", int2)
print("Integer 3:", int3)

# 2. Arithmetic with Integers
'''
Standard arithmetic operations include addition, subtraction, multiplication, division, 
exponentiation, and more.
'''
add_result = int1 + int2  # Addition
sub_result = int1 - int2  # Subtraction
mul_result = int1 * 2  # Multiplication
div_result = int1 // 5  # Floor Division (quotient only)
mod_result = int1 % 5  # Modulus (remainder)
exp_result = int1 ** 2  # Exponentiation

print("\nAddition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Floor Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)

# 3. Comparisons with Integers
'''
Integers can be compared using comparison operators like ==, !=, >, <, >=, and <=.
'''
is_equal = (int1 == 42)  # True
is_greater = (int1 > int2)  # True
is_less = (int3 < int1)  # True

print("\nIs Integer 1 equal to 42?", is_equal)
print("Is Integer 1 greater than Integer 2?", is_greater)
print("Is Integer 3 less than Integer 1?", is_less)

# 4. Bitwise Operations
'''
Integers support bitwise operations, which operate at the binary level:
- AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Left Shift (`<<`), Right Shift (`>>`).
'''
bitwise_and = int1 & 15  # Binary AND
bitwise_or = int1 | 15  # Binary OR
bitwise_xor = int1 ^ 15  # Binary XOR
left_shift = int1 << 2  # Shift left by 2 bits
right_shift = int1 >> 2  # Shift right by 2 bits

print("\nBitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)

# 5. Converting to Integers
'''
Integers can be created by casting from strings, floats, or other data types.
'''
float_to_int = int(3.14)  # From a float (truncates decimal part)
str_to_int = int("123")  # From a string (must be a valid number)

print("\nFloat to Integer:", float_to_int)
print("String to Integer:", str_to_int)

# 6. Working with Large Integers
'''
Python supports integers of arbitrary size, limited only by available memory.
'''
large_int = 1234567890123456789012345678901234567890
print("\nLarge Integer:", large_int)

# 7. Common Integer Methods
'''
Python provides methods and functions for integers, such as:
- `abs()`: Returns the absolute value.
- `pow()`: Computes power (with or without a modulus).
- `divmod()`: Returns a tuple (quotient, remainder).
'''

absolute_value = abs(int2)  # Absolute value
power_value = pow(2, 10)  # 2 raised to the power of 10
divmod_result = divmod(42, 5)  # Quotient and remainder as a tuple

print("\nAbsolute Value of Integer 2:", absolute_value)
print("Power (2^10):", power_value)
print("Divmod (42 / 5):", divmod_result)

# 8. Checking Integer Type
'''
Use `isinstance()` to check if a value is an integer.
'''
is_int = isinstance(int1, int)
print("\nIs Integer 1 an integer?", is_int)

# 9. Using Integers in Data Structures
'''
Integers are frequently used in data structures like lists and dictionaries.
'''
int_list = [1, 2, 3, 4, 5]
int_dict = {1: "one", 2: "two", 3: "three"}

print("\nList of Integers:", int_list)
print("Dictionary with Integers as Keys:", int_dict)

# 10. Integer Overflow (No Worry in Python)
'''
In many programming languages, integers have fixed sizes and may overflow if they exceed 
the maximum value. Python integers do not have this limitation due to their arbitrary size.
'''
very_large_int = 2 ** 100  # This would overflow in many languages
print("\nVery Large Integer (2^100):", very_large_int)

#----------------------------------------------------------------------------------------------------------------------#
