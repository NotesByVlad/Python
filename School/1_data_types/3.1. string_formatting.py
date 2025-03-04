#----------------------------------------   String Formatting in Python   ---------------------------------------------#
#                                        ---------------------------------

"""
String formatting in Python refers to the process of inserting values or expressions into a string.
This is essential for creating readable, dynamic, and customized strings, especially in user interfaces or reports.
Python provides several ways to format strings, including the `f-string` method, the `str.format()` method,
and the older `%` formatting.

The most modern and preferred method is the `f-string` (formatted string literals), introduced in Python 3.6.

"""

# Key Points about String Formatting:
'''
- f-strings (formatted string literals): Introduced in Python 3.6, they provide an easy and efficient way to embed 
  expressions inside string literals.
- `str.format()`: A method for formatting strings that works by placing placeholders in the string and filling 
  them with values.
- `%` Formatting: An older style, similar to printf-style formatting in languages like C, but is now considered less 
  modern.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. String Formatting using f-strings (Python 3.6+)
'''
f-strings allow you to directly embed expressions inside a string, using curly braces `{}` and prefixing 
the string with the letter `f`.
'''
name = "Alice"
age = 30
height = 5.7

formatted_string = f"Name: {name}, Age: {age}, Height: {height}m"
print("Formatted with f-string:", formatted_string)

# Expressions can be used inside the curly braces
area = 3.14 * (height ** 2)
formatted_with_expression = f"Area of circle (radius = {height}): {area:.2f}"
print("Formatted with f-string (expression inside):", formatted_with_expression)

# 2. String Formatting using `str.format()`
'''
The `str.format()` method allows you to place curly braces `{}` in the string and use the `.format()` method 
to inject values.
'''
formatted_string_format = "Name: {}, Age: {}, Height: {}m".format(name, age, height)
print("\nFormatted with str.format():", formatted_string_format)

# You can also use positional and keyword arguments
formatted_with_positional = "Name: {0}, Age: {1}, Height: {2}m".format(name, age, height)
formatted_with_keyword = "Name: {n}, Age: {a}, Height: {h}m".format(n=name, a=age, h=height)

print("Formatted with positional arguments:", formatted_with_positional)
print("Formatted with keyword arguments:", formatted_with_keyword)

# 3. String Formatting using `%` Operator (Older Style)
'''
The `%` operator allows formatting of strings in a way similar to C programming language's `printf`.
'''
formatted_percent = "Name: %s, Age: %d, Height: %.2f m" % (name, age, height)
print("\nFormatted with % operator:", formatted_percent)

# 4. Alignment and Padding
'''
Strings can be aligned (left, right, center) and padded with spaces or other characters.
'''
left_aligned = f"{name:<10}"  # Left-aligned (default is to pad with spaces)
right_aligned = f"{name:>10}"  # Right-aligned
center_aligned = f"{name:^10}"  # Center-aligned

# Padding with custom characters
padded_string = f"{name:.^10}"  # Pad with dot ('.')

print("\nLeft Aligned:", left_aligned)
print("Right Aligned:", right_aligned)
print("Center Aligned:", center_aligned)
print("Padded with dots:", padded_string)

# 5. Formatting Numbers (Decimal Places, Padding, Thousands Separator)
'''
You can format numbers to have a specific number of decimal places or use thousands separators.
'''
large_number = 1234567.8901
formatted_number = f"{large_number:,.2f}"  # Comma as thousands separator, 2 decimal places
formatted_percentage = f"{0.1234:.2%}"  # Percentage format (multiplies by 100 and adds % sign

print("\nFormatted large number with commas:", formatted_number)
print("Formatted as percentage:", formatted_percentage)

# 6. Formatting Dates
'''
You can format dates using `str.format()` or `f-strings` combined with `strftime()`.
'''
import datetime

today = datetime.datetime.now()
formatted_date = f"Today is {today:%B %d, %Y}"  # Month day, Year (e.g., December 10, 2024)

print("\nFormatted Date:", formatted_date)

# 7. String Interpolation with Expressions in f-strings
'''
You can perform simple expressions directly inside f-strings.
'''
x = 10
y = 20
formatted_expression = f"The sum of {x} and {y} is {x + y}."
print("\nString with expression:", formatted_expression)

# 8. Reusing Format Specifiers
'''
You can reuse format specifiers, especially when the same variable needs to appear multiple times.
'''
formatted_reuse = "Name: {0}, Age: {1}, Name again: {0}".format(name, age)
print("\nReusing format specifiers:", formatted_reuse)

# 9. Customizing String Output with Width and Precision
'''
You can control the width and precision of numbers, which is helpful for creating tables or formatted reports.
'''
pi = 3.14159265358979
formatted_width = f"Pi with width 10: {pi:10}"  # Right-aligned with a total width of 10
formatted_precision = f"Pi with 3 decimal places: {pi:.3f}"  # Only 3 decimal places

print("\nFormatted width:", formatted_width)
print("Formatted precision:", formatted_precision)

# 10. Combining Multiple Formatting Techniques
'''
You can combine different formatting techniques like alignment, width, padding, etc.
'''
combined_format = f"Name: {name:.^10}, Age: {age:>5}, Height: {height:.2f}m"
print("\nCombined formatting:", combined_format)

#----------------------------------------------------------------------------------------------------------------------#

# Summary:
'''
1. f-strings provide the easiest and most efficient way to format strings in Python.
2. `str.format()` allows more flexibility with positional and keyword arguments.
3. The `%` operator is the oldest formatting method, but it's less commonly used now.
4. You can align, pad, and format numbers or dates in many different ways.
5. Use string interpolation (expressions inside f-strings) for dynamic string generation.
'''
#----------------------------------------------------------------------------------------------------------------------#
