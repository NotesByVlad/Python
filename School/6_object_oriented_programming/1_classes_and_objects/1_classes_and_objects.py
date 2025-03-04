#----------------------------------------   Classes and Objects in Python   ---------------------------------------------------------#
#                                        -----------------------

"""
In Python, classes are used to create objects, which are instances of the class.
An object encapsulates data (attributes) and behavior (methods), and classes define
the blueprint for these objects.

Classes are used to model real-world entities or abstract concepts, and they allow
reusability and encapsulation of data.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Classes and Objects:
'''
- Class Definition: A class is defined using the `class` keyword followed by its name.
- Attributes: Data associated with an object, defined within the class.
- Methods: Functions that operate on the data of the object, defined within the class.
- Object: An instance of a class.
- Encapsulation: Hiding of internal data within the class, exposing only necessary methods.
- Inheritance: The ability to create a new class from an existing class.
- Polymorphism: The ability to perform a single action in different ways.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Defining a Simple Class

class Person:
    # Class attributes
    species = 'Human'

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def greet(self):
        # Instance method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        # Another instance method to increment age
        self.age += 1

# Creating an object of the class
person1 = Person("Alice", 30)

# Accessing object attributes and methods
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
person1.have_birthday()
print(person1.greet())  # Output: Hello, my name is Alice and I am 31 years old.

#----------------------------------------------------------------------------------------------------------------------#
