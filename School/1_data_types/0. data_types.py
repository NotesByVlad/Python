#----------------------------------------   Data Types in Python   ---------------------------------------------#
#                                        --------------------------

"""
In Python, data types define the kind of value a variable can hold. Each data type specifies the type of
data it represents, such as numbers, strings, lists, etc.
Python has several built-in data types, which are divided into categories like numeric types,
sequence types, mapping types, etc.

It is important to note that variables are not considered a data type,
but they are used to store data of specific types.


Key Points about Data Types:

  **Data Types**: These define the type of value that a variable can hold.
    - Integer (int): Whole numbers like 1, -10, 200.
    - Floating-point numbers (float): Numbers with decimal points, like 3.14, -2.71.
    - String (str): A sequence of characters, such as "hello", "world".
    - List: An ordered collection of items, such as [1, 2, 3], ["apple", "banana"].
    - Tuple: An immutable, ordered collection of items, like (1, 2, 3).
    - Dictionary (dict): A collection of key-value pairs, such as {"name": "Alice", "age": 30}.
    - Set: A collection of unique, unordered items, like {1, 2, 3}.
    - Boolean (bool): True or False values.
    - Bytes: An immutable sequence of bytes.
    - Bytearray: A mutable sequence of bytes.
    - NoneType: A special type representing the absence of value (None).
"""

#---------------------------------------------------------------------------------------------------------------#

# 1. **Integers (int)**: Whole numbers without decimals.
x = 10
y = -25
print(f"Integer x: {x}, Integer y: {y}")

# 2. **Floating-point numbers (float)**: Numbers with decimal points.
pi = 3.14159
height = 5.9
print(f"Float pi: {pi}, Float height: {height}")

# 3. **Strings (str)**: A sequence of characters enclosed in quotes.
name = "Alice"
message = "Welcome to Python"
print(f"String name: {name}, String message: {message}")

# 4. **Lists**: Ordered, changeable, and allows duplicates.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Modifying the list
print(f"List fruits: {fruits}")

# 5. **Tuples**: Ordered, immutable collection of items.
coordinates = (10, 20)
print(f"Tuple coordinates: {coordinates}")

# 6. **Dictionaries (dict)**: Collection of key-value pairs.
person = {"name": "John", "age": 25}
person["city"] = "New York"  # Adding a key-value pair
print(f"Dictionary person: {person}")

# 7. **Sets**: Unordered collection of unique items.
numbers = {1, 2, 3, 4}
numbers.add(5)  # Adding a number to the set
print(f"Set numbers: {numbers}")

# 8. **Booleans (bool)**: Values representing True or False.
is_active = True
is_admin = False
print(f"Boolean is_active: {is_active}, Boolean is_admin: {is_admin}")

# 9. **Bytes**: Immutable sequence of bytes, typically used for binary data.
byte_data = bytes([0, 1, 2, 3, 4])
print(f"Bytes byte_data: {byte_data}")

# 10. **Bytearray**: Mutable sequence of bytes; can be modified after creation.
mutable_byte_data = bytearray([5, 6, 7, 8, 9])
mutable_byte_data[0] = 10  # Modify the first byte
print(f"Bytearray mutable_byte_data: {mutable_byte_data}")

# 11. **NoneType**: A special type representing a null or absent value.
nothing = None
print(f"NoneType nothing: {nothing}")








#---------------------------------------------------------------------------------------------------------------#

# Variables and Data Types
'''
In Python, **variables** are not data types themselves. Instead, they are used to store data of specific types. 

A variable can hold any of the data types discussed above, and the type of data a variable stores is determined 
by the value assigned to it. 

For example:
'''
a = 42  # a is an integer variable
b = "Hello"  # b is a string variable
c = [1, 2, 3]  # c is a list variable

# Python is dynamically typed, meaning the type of the variable is determined at runtime based on the value 
# it holds.
print(f"Variable a holds an integer: {a}")
print(f"Variable b holds a string: {b}")
print(f"Variable c holds a list: {c}")

# You can also change the type of data a variable holds:
a = "Now I'm a string!"  # Reassigning a string to variable a
print(f"Now, variable a holds a string: {a}")

# So, to clarify:
# - Variables store data, and the type of data is determined by the value assigned to them.
# - Variables themselves do not have a data type.
# - The data type refers to the kind of value stored in the variable (e.g., integer, string, list, etc.).

#---------------------------------------------------------------------------------------------------------------#

# Summary:
'''
- **Data Types** define the type of data that a variable can store, such as integers, strings, lists, etc.
- **Variables** are labels used to store and reference data of various types.
- In Python, variables are dynamically typed, which means their type is determined by the value they hold at 
  runtime.
- Variables themselves are not data types; they are used to store data that belongs to specific data types.
- New data types covered: **Bytes (immutable)** and **Bytearray (mutable)**, used for handling binary data.
'''
#---------------------------------------------------------------------------------------------------------------#