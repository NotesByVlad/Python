#----------------------------------------   Accessing Dictionary Elements   ------------------------------------------------#
#                                            --------------------------

"""
Dictionaries in Python are unordered collections of key-value pairs. Each key is unique,
and it is used to access the corresponding value.

Accessing elements in a dictionary involves using the key. Python provides several methods
and techniques to retrieve values or keys efficiently.
"""

# Key Points about Accessing Dictionary Elements:
'''
1. Dictionary keys are used to access their corresponding values.
2. Attempting to access a key that does not exist raises a KeyError.
3. Use the `get` method to access values safely, with an optional default.
4. `keys()`, `values()`, and `items()` provide views of the dictionary.
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "Wonderland"
}

# 1. Accessing Values by Key
"""
Using square brackets, you can access the value associated with a specific key.
"""
print("Name:", my_dict["name"])  # Accessing the value for key 'name'
print("Age:", my_dict["age"])    # Accessing the value for key 'age'

# 2. Using the `get` Method
"""
The `get` method retrieves a value associated with a key but does not raise an error
if the key does not exist. Instead, it returns `None` or a specified default value.
"""
print("Location:", my_dict.get("location"))        # Safe access
print("Country:", my_dict.get("country", "Unknown"))  # Default value if key is missing

# 3. Checking for Key Existence
"""
You can check if a key exists in the dictionary using the `in` operator.
"""
if "age" in my_dict:
    print("Age is available in the dictionary.")
if "country" not in my_dict:
    print("Country is not available in the dictionary.")

# 4. Accessing Keys, Values, and Items
"""
Use `keys()`, `values()`, and `items()` to retrieve dictionary components:
- `keys()` provides a view of all keys.
- `values()` provides a view of all values.
- `items()` provides a view of all key-value pairs.
"""
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

#----------------------------------------------------------------------------------------------------------------------#
