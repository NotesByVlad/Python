#---------------------------------------- Membership Operator: NOT IN in Python ---------------------------------------#
#                                        ---------------------------------------

"""
The `not in` operator is used to check if a value does **not** exist within a sequence.
If the value is not found, it returns `True`; otherwise, it returns `False`.
"""

# Key Points about `not in` Operator:
'''
1. The `not in` operator checks if a value does **not** exist within a sequence (like a list, string, tuple).
2. It returns `True` if the value is not found and `False` if the value is found.
3. It is the inverse of the `in` operator.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Usage of `not in` with a List
# Example: Checking if an element is not present in a list.
print("Basic NOT IN Example with List:")
fruits = ["apple", "banana", "cherry", "date"]
if "grapes" not in fruits:
    print("Grapes are not in the list!")
else:
    print("Grapes are in the list.")

# Output: Grapes are not in the list!
# The element "grapes" is not found in the list.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using `not in` with Strings
# Example: Checking if a substring is not present in a string.
print("\nUsing NOT IN with String:")
sentence = "Hello, welcome to Python programming!"
if "Java" not in sentence:
    print("The word 'Java' is not in the sentence!")
else:
    print("The word 'Java' is in the sentence.")

# Output: The word 'Java' is not in the sentence!
# The substring "Java" is not found in the string.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using `not in` with Tuples
# Example: Checking if an element is not present in a tuple.
print("\nUsing NOT IN with Tuple:")
numbers = (1, 2, 3, 4, 5)
if 6 not in numbers:
    print("6 is not in the tuple!")
else:
    print("6 is in the tuple.")

# Output: 6 is not in the tuple!
# The element 6 is not found in the tuple.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `not in` with Dictionaries (Checking keys)
# Example: Checking if a key does not exist in a dictionary.
print("\nUsing NOT IN with Dictionary:")
person = {"name": "John", "age": 25, "city": "New York"}
if "country" not in person:
    print("Key 'country' does not exist in the dictionary!")
else:
    print("Key 'country' exists in the dictionary.")

# Output: Key 'country' does not exist in the dictionary!
# We check for the non-existence of the key "country" in the dictionary.

#----------------------------------------------------------------------------------------------------------------------#
