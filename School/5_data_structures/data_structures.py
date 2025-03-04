#----------------------------------------   Data Structures in Python   ----------------------------------------#
#                                        ------------------------------------

"""
Data structures are essential for organizing, managing, and storing data in an efficient way for
various tasks and algorithms. Python provides a rich set of built-in data structures that are
highly optimized and flexible.

### Key Concepts:
- **Lists**: Ordered collections that are mutable (can be changed).
- **Tuples**: Ordered collections that are immutable.
- **Dictionaries**: Unordered collections of key-value pairs.
- **Sets**: Unordered collections of unique elements.
- **Strings**: Sequences of characters that are immutable.

"""

# 1. **Lists**:
# Lists are ordered collections of items that are mutable (can be changed). They are defined using square brackets `[]`.

# Basic list:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing elements:
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry (last element)

# Modifying elements:
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Adding elements:
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']

# Removing elements:
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Slicing lists:
print(fruits[1:3])  # Output: ['orange', 'grape']

# Iterating over a list:
for fruit in fruits:
    print(fruit)

# Explanation:
# Lists are ordered and mutable, and elements can be accessed using indices. They support methods like `append()`, `remove()`, and slicing.

# 2. **Tuples**:
# Tuples are ordered collections, but they are immutable, meaning their elements cannot be changed after creation. They are defined using parentheses `()`.

# Basic tuple:
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Accessing elements:
print(coordinates[0])  # Output: 10
print(coordinates[-1])  # Output: 20

# Concatenating tuples:
coordinates = coordinates + (30, 40)
print(coordinates)  # Output: (10, 20, 30, 40)

# Iterating over a tuple:
for coord in coordinates:
    print(coord)

# Explanation:
# Tuples are similar to lists but immutable, meaning they cannot be modified after they are created. Useful when you want to ensure data integrity.

# 3. **Dictionaries**:
# Dictionaries are unordered collections of key-value pairs. They are defined using curly braces `{}` and are mutable.

# Basic dictionary:
person = {"name": "John", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values by key:
print(person["name"])  # Output: John

# Modifying values:
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding key-value pairs:
person["job"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing key-value pairs:
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

# Iterating over a dictionary:
for key, value in person.items():
    print(f"{key}: {value}")

# Explanation:
# Dictionaries store data in key-value pairs. Keys must be unique, and values can be accessed, modified, added, and deleted using keys.

# 4. **Sets**:
# Sets are unordered collections of unique elements. They are defined using curly braces `{}` or the `set()` constructor.

# Basic set:
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'banana', 'cherry', 'apple'}

# Adding elements:
fruits_set.add("grape")
print(fruits_set)  # Output: {'banana', 'cherry', 'apple', 'grape'}

# Removing elements:
fruits_set.remove("banana")
print(fruits_set)  # Output: {'cherry', 'apple', 'grape'}

# Set operations (union, intersection, difference):
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))        # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Output: {3}
print(set1.difference(set2))   # Output: {1, 2}

# Iterating over a set:
for fruit in fruits_set:
    print(fruit)

# Explanation:
# Sets are unordered and contain unique elements. They support various set operations like union, intersection, and difference.

# 5. **Strings**:
# Strings are sequences of characters, and they are immutable in Python. They are defined using single or double quotes.

# Basic string:
greeting = "Hello, World!"
print(greeting)  # Output: Hello, World!

# Accessing characters:
print(greeting[0])  # Output: H
print(greeting[-1]) # Output: !

# String slicing:
print(greeting[7:12])  # Output: World

# String methods:
print(greeting.lower())  # Output: hello, world!
print(greeting.upper())  # Output: HELLO, WORLD!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!

# Iterating over a string:
for char in greeting:
    print(char)

# Explanation:
# Strings are immutable sequences of characters and offer a wide range of methods for manipulation (like `lower()`, `upper()`, `replace()`).

# 6. **List Comprehensions**:
# List comprehensions provide a concise way to create lists based on some condition or transformation.

# Basic list comprehension:
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With a condition:
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Explanation:
# List comprehensions allow you to create lists in a single line, optionally including conditions for filtering.

# 7. **Dictionaries Comprehensions**:
# Similar to list comprehensions but used for creating dictionaries.

# Basic dictionary comprehension:
squared_dict = {x: x ** 2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Explanation:
# Dictionary comprehensions allow you to create dictionaries in a single line.

# 8. **Summary**:
'''
- **Lists**: Ordered, mutable collections. They support indexing, slicing, and methods like `append()`, `remove()`.
- **Tuples**: Ordered, immutable collections. They cannot be modified after creation.
- **Dictionaries**: Unordered collections of key-value pairs. They allow fast lookups by key.
- **Sets**: Unordered collections of unique elements. They support set operations like `union()`, `intersection()`, and `difference()`.
- **Strings**: Immutable sequences of characters with many built-in methods for manipulation.
- **List Comprehensions**: A concise way to create lists, with optional conditions.
- **Dictionary Comprehensions**: A concise way to create dictionaries.

'''

#----------------------------------------------------------------------------------------------------------------------#
