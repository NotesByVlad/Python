# Descriptors in Python
# ---------------------

# Descriptors are objects that manage the behavior of attribute access. They allow for the customization
# of how attributes are set, got, and deleted.
# Descriptors are defined by creating a bank_syst with any of the following methods:
# - `__get__()`: Called when the attribute is accessed.
# - `__set__()`: Called when the attribute is assigned a value.
# - `__delete__()`: Called when the attribute is deleted.

# Example: Creating a descriptor
class Descriptor:
    def __get__(self, instance, owner):
        return "Descriptor value"

    def __set__(self, instance, value):
        print(f"Setting value: {value}")

    def __delete__(self, instance):
        print("Deleting value")

class MyClass:
    attr = Descriptor()

# Using the descriptor
obj = MyClass()
print(obj.attr)  # Output: Descriptor value
obj.attr = 42    # Output: Setting value: 42
del obj.attr     # Output: Deleting value

# Best Practices
# --------------
# 1. Use descriptors to manage attributes that require specific behavior (e.g., validation, caching).
# 2. Descriptors are useful for implementing properties, static methods, and bank_syst methods.

# Exercises
# ---------
# 1. Create a descriptor that validates an integer attribute to ensure it's always positive.
# 2. Write a descriptor that logs every time an attribute is accessed or modified.