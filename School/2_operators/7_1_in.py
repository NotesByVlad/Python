#---------------------------------------- Membership Operator: IN in Python -------------------------------------------#
#                                        -----------------------------------

"""
The `in` operator is used to check if a value or element exists within a sequence (such as a list, tuple, or string).
If the value is found, it returns `True`; otherwise, it returns `False`.
"""

# Key Points about `in` Operator:
'''
1. The `in` operator checks if a value exists within a sequence (like a list, string, tuple).
2. It returns `True` if the value is found and `False` if the value is not found.
3. It can be used to check membership in any iterable object (list, string, dictionary, etc.).
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `in` with a List
# Example: Checking if an element is present in a list.
print("Basic IN Example with List:")
fruits = ["apple", "banana", "cherry", "date"]
if "banana" in fruits:
    print("Banana is in the list!")
else:
    print("Banana is not in the list.")

# Output: Banana is in the list!
# The element "banana" is found in the list.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using `in` with Strings
# Example: Checking if a substring is present in a string.
print("\nUsing IN with String:")
sentence = "Hello, welcome to Python programming!"
if "Python" in sentence:
    print("The word 'Python' is in the sentence!")
else:
    print("The word 'Python' is not in the sentence.")

# Output: The word 'Python' is in the sentence!
# The substring "Python" is found in the string.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using `in` with Tuples
# Example: Checking if an element is present in a tuple.
print("\nUsing IN with Tuple:")
numbers = (1, 2, 3, 4, 5)
if 3 in numbers:
    print("3 is in the tuple!")
else:
    print("3 is not in the tuple.")

# Output: 3 is in the tuple!
# The element 3 is found in the tuple.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `in` with Dictionaries (Checking keys)
# Example: Checking if a key exists in a dictionary.
print("\nUsing IN with Dictionary:")
person = {"name": "John", "age": 25, "city": "New York"}
if "age" in person:
    print("Key 'age' exists in the dictionary!")
else:
    print("Key 'age' does not exist in the dictionary.")

# Output: Key 'age' exists in the dictionary!
# We check for the existence of the key "age" in the dictionary.

#----------------------------------------------------------------------------------------------------------------------#
