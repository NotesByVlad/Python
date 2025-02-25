#----------------------------------------   Membership Operators in Python   ------------------------------------------#
#                                        ------------------------------------

"""
Membership operators are used to test if a value is present in a sequence (like a list, tuple, or string).
"""

# Key Membership Operators:
'''
- in: Returns True if the value is found in the sequence.
- not in: Returns True if the value is not found in the sequence.
'''

# Examples:
fruits = ["apple", "banana", "cherry"]

print(f"apple in fruits: {'apple' in fruits}")
print(f"orange not in fruits: {'orange' not in fruits}")
#----------------------------------------------------------------------------------------------------------------------#

#--------------------------------- Using IN and NOT IN for Membership Test in Python ----------------------------------#
#                                 ---------------------------------------------------

'''
The `in` and `not in` operators are used to check if a value or element exists in a sequence 
(like a list, string, tuple).
'''

# Key Points about `in` and `not in`:
'''
1. `in`: Returns `True` if the value is found in the sequence (membership test).
2. `not in`: Returns `True` if the value is not found in the sequence (membership test).
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Using `in` to Check Membership in a List
# Example: Check if an element is in a list.
print("Membership Test with IN:")
colors = ["red", "green", "blue", "yellow"]
if "green" in colors:
    print("Green is in the list!")
else:
    print("Green is not in the list.")

# Output: Green is in the list!
# We check if "green" exists in the list.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using `not in` to Check Membership in a String
# Example: Check if a substring is not in a string.
print("\nMembership Test with NOT IN and String:")
sentence = "I love programming in Python"
if "Java" not in sentence:
    print("Java is not mentioned in the sentence!")
else:
    print("Java is mentioned in the sentence.")

# Output: Java is not mentioned in the sentence!
# We check if "Java" is not a part of the sentence.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Using `in` and `not in` with Dictionaries
# Example: Check if a key exists or does not exist in a dictionary.
print("\nMembership Test with IN and NOT IN in Dictionary:")
person = {"name": "Alice", "age": 28, "city": "Los Angeles"}

# Check if a key exists
if "age" in person:
    print("Key 'age' exists in the dictionary.")

# Check if a key does not exist
if "country" not in person:
    print("Key 'country' does not exist in the dictionary.")

# Output:
# Key 'age' exists in the dictionary.
# Key 'country' does not exist in the dictionary.

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `in` and `not in` with Tuples
# Example: Check if an element exists or does not exist in a tuple.
print("\nMembership Test with IN and NOT IN in Tuple:")
numbers = (1, 2, 3, 4, 5)

# Check if an element exists
if 3 in numbers:
    print("3 is in the tuple!")

# Check if an element does not exist
if 6 not in numbers:
    print("6 is not in the tuple.")

# Output:
# 3 is in the tuple!
# 6 is not in the tuple.

#----------------------------------------------------------------------------------------------------------------------#
