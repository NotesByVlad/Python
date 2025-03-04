#----------------------------------------   Integers in Python   -----------------------------------------------#
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
#---------------------------------------------------------------------------------------------------------------#

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
floor division, modulus and exponentiation.
'''
addition_result       = int1 + int2 # Addition
subtraction_result    = int1 - int2 # Subtraction
multiplication_result = int1 * 2    # Multiplication
division_result       = int1 / 2    # Division
floor_division_result = int1 // 5   # Floor Division (quotient only)
modulus_result        = int1 % 5    # Modulus (remainder)
exponentiation_result = int1 ** 2   # Exponentiation

print("\nAddition:",      addition_result)
print("Subtraction:",     subtraction_result)
print("Multiplication:",  multiplication_result)
print("Division:",        division_result)
print("Floor Division:",  floor_division_result)
print("Modulus:",         modulus_result)
print("Exponentiation:",  exponentiation_result)

# 3. Comparisons with Integers
'''
Integers can be compared using comparison operators like ==, !=, >, <, >=, and <=.
'''
is_equal            = (int1 == 42)   # True   == equal
not_equal           = (int1 != int2) # True   != not equal
is_greater          = (int1 > int2)  # True   >  greater
is_greater_or_equal = (int1 >= int2) # True   >= greater or equal
is_less             = (int3 < int1)  # True   <  less
is_less_or_equal    = (int1 <= int2) # False  <= less or equal

print("\nIs Integer 1 equal to 42?",                is_equal)
print("Is Integer 1 not equal to Integer 2?",       not_equal)
print("Is Integer 1 greater than Integer 2?",       is_greater)
print("Is Integer 1 greater or equal to Integer 2", is_greater_or_equal)
print("Is Integer 3 less than Integer 1?",          is_less)
print("Is Integer 1 less or equal to Integer 2?",   is_less_or_equal)

# 4. Bitwise Operations
'''
Integers support bitwise operations, which operate at the binary level:
- AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Left Shift (`<<`), Right Shift (`>>`).
'''

# AND (&) → bitwise_and = int1 & 15
# compares each bit of int1 with 15 (which is 1111 in binary)
# it only keeps the bits that are 1 in both numbers
# example: 10 & 15 → 1010 & 1111 → 1010 (which is 10 in decimal)
bitwise_and = int1 & 15   # Binary AND

# OR (|) → bitwise_or = int1 | 15
# compares each bit and keeps a 1 if either number has a 1
# example: 10 | 15 → 1010 | 1111 → 1111 (which is 15)
bitwise_or = int1 | 15    # Binary OR

# XOR (^) → bitwise_xor = int1 ^ 15
# this keeps a 1 if the bits are different, and a 0 if they’re the same
# example: 10 ^ 15 → 1010 ^ 1111 → 0101 (which is 5)
bitwise_xor = int1 ^ 15   # Binary XOR

# NOT (~) → bitwise_not = ~int1
# this flips all the bits (turns 1s to 0s and vice versa)
# in Python, it also changes the sign because of how negative numbers are stored (two’s complement)
# example: ~10 → ~1010 → -11 (yes, negative!)
bitwise_not = ~int1       # Binary NOT

# Left Shift (<<) → left_shift = int1 << 2
# this shifts all bits to the left by 2 places, adding 0s at the end
# it's like multiplying by 2^2 (or 4)
# example: 10 << 2 → 1010 becomes 101000 (which is 40)
left_shift = int1 << 2    # Shift left by 2 bits

# Right Shift (>>) → right_shift = int1 >> 2
# this shifts bits to the right by 2 places, removing the last two bits
# it's like dividing by 2^2 (or 4)
# example: 10 >> 2 → 1010 becomes 0010 (which is 2)
right_shift = int1 >> 2   # Shift right by 2 bits

print("\nBitwise AND:", bitwise_and)
print("Bitwise OR:",    bitwise_or)
print("Bitwise XOR:",   bitwise_xor)
print("Bitwise NOT:",   bitwise_not)
print("Left Shift:",    left_shift)
print("Right Shift:",   right_shift)

# 5. Converting to Integers
'''
Integers can be created by casting from strings, floats, or other data types.
'''
float_to_int = int(3.14)  # From a float (truncates decimal part)
str_to_int   = int("123") # From a string (must be a valid number)

print("\nFloat to Integer:", float_to_int)
print("String to Integer:",  str_to_int)

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

absolute_value = abs(int2)     # Absolute value
power_value    = pow(2, 10)    # 2 raised to the power of 10
divmod_result  = divmod(42, 5) # Quotient and remainder as a tuple

print("\nAbsolute Value of Integer 2:", absolute_value)
print("Power (2^10):",                  power_value)
print("Divmod (42 / 5):",               divmod_result)

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

#---------------------------------------------------------------------------------------------------------------#
