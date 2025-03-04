#----------------------------------------   Metaclasses in Python   ---------------------------------------------------------#
#                                        -----------------------

"""
In Python, metaclasses are the "classes of classes." They define the behavior and structure of classes themselves.
Using metaclasses, you can control the creation and modification of classes, making them a powerful tool for meta-programming.

Metaclasses allow for dynamic class creation, validation, and customization of class attributes and methods at the time of class definition.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Metaclasses:
'''
- What is a Metaclass? A class responsible for defining the behavior and attributes of other classes.
- `type` as a Metaclass: By default, Python uses `type` as the metaclass for all classes.
- Custom Metaclasses: Created by inheriting from `type` and overriding its methods.
- Key Methods:
  - `__new__`: Controls the creation of a new class.
  - `__init__`: Initializes the class after it has been created.
- Use Cases: Enforcing coding standards, dynamically adding methods or attributes, and more.
- Syntax: Specified using the `metaclass` keyword when defining a class.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Defining a Custom Metaclass

class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        # Modify or add class attributes during creation
        print(f"Creating class {name}")
        dct['created_by_metaclass'] = True
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        # Initialization logic for the class
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)

# Using the Custom Metaclass

class MyClass(metaclass=CustomMeta):
    def my_method(self):
        return "Hello from MyClass"

# Checking the Behavior
instance = MyClass()
print(instance.my_method())
print(f"Was this class created by a metaclass? {MyClass.created_by_metaclass}")

# Output:
# Creating class MyClass
# Initializing class MyClass
# Hello from MyClass
# Was this class created by a metaclass? True

#----------------------------------------------------------------------------------------------------------------------#

# Advanced Example: Enforcing Coding Standards with a Metaclass

class EnforceNamingConventionMeta(type):
    def __new__(cls, name, bases, dct):
        # Enforce method names to start with "do_"
        for attr_name in dct:
            if callable(dct[attr_name]) and not attr_name.startswith("do_"):
                raise TypeError(f"Method {attr_name} in {name} must start with 'do_'")
        return super().__new__(cls, name, bases, dct)

# Using the EnforceNamingConventionMeta

class Task(metaclass=EnforceNamingConventionMeta):
    def do_work(self):
        print("Working")

    # Uncommenting the following method will raise a TypeError:
    # def work(self):
    #     pass

# Checking the Behavior

obj = Task()
obj.do_work()  # Output: Working

# Output if uncommented:
# TypeError: Method work in Task must start with 'do_'
