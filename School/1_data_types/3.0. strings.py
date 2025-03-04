#----------------------------------------   Strings in Python   -------------------------------------------------------#
#                                        -----------------------

"""
In programming, a string is a sequence of characters. It is a data type used
to represent textual data, such as words, sentences, or any other sequence of
characters, including spaces, punctuation marks, and digits.
Strings are typically enclosed in quotes (either single (') or double (") ),
and they can be manipulated in many ways in programming languages.
"""

# Key Points about Strings:
'''
Sequence of Characters: A string is made up of characters 
(letters, digits, symbols, etc.).
Enclosed in Quotes: In most programming languages, strings
are enclosed in either single quotes (') or double quotes ("),
or even triple quotes for multi-line strings
'''
#----------------------------------------------------------------------------------------------------------------------#

# Immutable:
'''
In many programming languages (like Python), strings are immutable,
meaning their content cannot be changed after they are created.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Indexable and Iterable:
'''
Strings can be indexed, meaning individual characters in a string
can be accessed using an index, and they can also be iterated over
in loops.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. String Initialization
string1 = "Hello, World!"
string2 = 'Python Programming'

# Printing the strings
print("String 1:", string1)
print("String 2:", string2)

# 2. String Length
print("\nLength of String 1:", len(string1))
print("Length of String 2:", len(string2))

# 3. String Concatenation
greeting = string1 + " " + string2
print("\nConcatenated String:", greeting)

# 4. String Repetition
repeated_greeting = string1 * 3
print("\nRepeated String 1 (3 times):", repeated_greeting)

# 5. String Slicing
substring = string2[7:18]  # Extracts 'Programming'
print("\nSliced String (from index 7 to 17):", substring)

# 6. String Methods
upper_string = string1.upper()  # Convert to uppercase
lower_string = string2.lower()  # Convert to lowercase
title_string = upper_string.title()  # Convert to title
strip_string = string2.strip()  # Deletes the space character from beginning and end of the string
replaced_string = string1.replace("World", "Python")  # Replace substring

print("\nUppercase String 1:", upper_string)
print("Lowercase String 2:", lower_string)
print("Title String 1:", title_string)
print("Strip String 2:", strip_string)
print("Replaced String 1:", replaced_string)

# 7. String Formatting
name = "John"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print("\nFormatted String:", formatted_string)

# 8. String Checking
is_digit = "12345".isdigit()  # Check if string contains only digits
is_alpha = "Python".isalpha()  # Check if string contains only alphabetic characters

print("\nIs '12345' a digit?", is_digit)
print("Is 'Python' alphabetic?", is_alpha)

# 9. String Splitting
split_string = string2.split()  # Split string into words based on spaces
print("\nSplit String 2:", split_string)

# 10. String Joining
joined_string = " ".join(split_string)  # Join list of words back into a string
print("\nJoined String:", joined_string)

# 11. Escape Characters
escaped_string = "This is a string with a newline\nand a tab\t!"
print("\nString with escape characters:", escaped_string)
#----------------------------------------------------------------------------------------------------------------------#