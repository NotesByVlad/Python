#----------------------------------------   Floats in Python   --------------------------------------------------------#
#                                        -----------------------

"""
In Python, a float (short for "floating point number") is a data type used to represent
real numbers with decimal points. Floats can also be used to represent scientific notation
and are commonly used in mathematical computations.

Floating-point numbers are stored as binary approximations, which may lead to precision issues.
"""

# Key Points about Floats:
'''
- Real Numbers: Floats represent numbers with a decimal point (e.g., 3.14, -0.001).
- Precision: Floats are approximations, not exact representations.
- Scientific Notation: Floats can represent large or small numbers using `e` or `E`.
- Operations: Floats support arithmetic, comparisons, and built-in methods.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Float Initialization
float1 = 3.14159  # Standard float
float2 = -123.456  # Negative float
float3 = 1.23e4  # Scientific notation (1.23 × 10^4 = 12300.0)
float4 = float("3.14")  # From a string

print("Float 1:", float1)
print("Float 2:", float2)
print("Float 3 (scientific notation):", float3)
print("Float 4 (from string):", float4)

# 2. Arithmetic with Floats
'''
Floats support standard arithmetic operations like addition, subtraction, 
multiplication, and division.
'''
add_result = float1 + float2
sub_result = float1 - float2
mul_result = float1 * float2
div_result = float1 / 2

print("\nAddition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)

# 3. Comparisons with Floats
'''
Floats can be compared using standard comparison operators.
'''
is_equal = (3.14 == float4)  # True
is_greater = (float1 > float2)  # True
is_less = (float3 < 1.5e4)  # True

print("\nIs 3.14 equal to Float 4?", is_equal)
print("Is Float 1 greater than Float 2?", is_greater)
print("Is Float 3 less than 1.5e4?", is_less)

# 4. Float Precision
'''
Floats may lose precision due to their binary representation.
'''
imprecise_sum = 0.1 + 0.2  # This may not exactly equal 0.3
print("\n0.1 + 0.2 =", imprecise_sum)

# 5. Rounding Floats
'''
The `round()` function can be used to round floats to a specified number of decimal places.
'''
rounded_value = round(float1, 2)  # Round to 2 decimal places
print("\nRounded Float 1 (to 2 decimal places):", rounded_value)

# 6. Float Methods
'''
Floats support useful methods through the `math` module, such as:
- `math.floor()`: Rounds down to the nearest integer.
- `math.ceil()`: Rounds up to the nearest integer.
- `math.sqrt()`: Computes the square root.
- `math.isclose()`: Checks if two floats are close within a tolerance.
'''

import math

floor_value = math.floor(float1)  # Round down
ceil_value = math.ceil(float1)  # Round up
sqrt_value = math.sqrt(16.0)  # Square root

print("\nFloor of Float 1:", floor_value)
print("Ceiling of Float 1:", ceil_value)
print("Square Root of 16.0:", sqrt_value)

# 7. Casting to Floats
'''
Floats can be created by casting integers, strings, or other data types.
'''
int_to_float = float(42)  # From an integer
str_to_float = float("2.71828")  # From a string

print("\nInteger to Float:", int_to_float)
print("String to Float:", str_to_float)

# 8. Floats in Scientific Notation
'''
Floats can be expressed in scientific notation, making it easy to represent very large or very small numbers.
'''
large_float = 1.2e6  # 1.2 × 10^6 = 1200000.0
small_float = 5.67e-4  # 5.67 × 10^-4 = 0.000567

print("\nLarge Float (1.2e6):", large_float)
print("Small Float (5.67e-4):", small_float)

# 9. Float Infinity and NaN
'''
Special float values include:
- `math.inf`: Represents infinity.
- `math.nan`: Represents "Not a Number."
'''
infinity = math.inf
negative_infinity = -math.inf
nan_value = math.nan

print("\nPositive Infinity:", infinity)
print("Negative Infinity:", negative_infinity)
print("NaN Value:", nan_value)

# Checking special float values
is_infinite = math.isinf(infinity)  # True
is_nan = math.isnan(nan_value)  # True

print("Is Infinity infinite?", is_infinite)
print("Is NaN a number?", is_nan)

# 10. Using Floats in Lists
'''
Floats can be used in lists or other data structures.
'''
float_list = [3.14, 2.718, 1.618]
sum_of_floats = sum(float_list)  # Sum of elements
average = sum_of_floats / len(float_list)  # Average

print("\nList of Floats:", float_list)
print("Sum of Floats:", sum_of_floats)
print("Average of Floats:", average)

#----------------------------------------------------------------------------------------------------------------------#
