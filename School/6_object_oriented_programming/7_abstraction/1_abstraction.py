#----------------------------------------   Abstraction in Python Classes   -------------------------------------------#
#                                        -----------------------------------

"""
Abstraction is a core concept in object-oriented programming (OOP) that allows
hiding the complex implementation details and exposing only the necessary parts
of an object. It simplifies the process of understanding and managing classes
and objects by focusing only on the essential features.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Abstraction:
'''
1. In Python, abstraction is typically achieved through abstract classes and interfaces.
2. It helps manage complexity by providing a simplified interface to users.
3. Abstract classes cannot be instantiated directly; they act as a blueprint for other classes.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. Abstract Class Example

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

    def habitat(self):
        return "Domestic"

class Lion(Animal):
    def sound(self):
        return "Roar"

    def habitat(self):
        return "Wild"

# Creating instances
dog = Dog()
lion = Lion()

# Demonstrating abstraction
print("Dog Sound:", dog.sound())        # Output: Dog Sound: Bark
print("Dog Habitat:", dog.habitat())    # Output: Dog Habitat: Domestic

print("Lion Sound:", lion.sound())      # Output: Lion Sound: Roar
print("Lion Habitat:", lion.habitat())  # Output: Lion Habitat: Wild

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using Abstraction with Interfaces

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing a Circle"

class Rectangle(Drawable):
    def draw(self):
        return "Drawing a Rectangle"

# Creating objects
circle = Circle()
rectangle = Rectangle()

# Abstraction in action
print(circle.draw())       # Output: Drawing a Circle
print(rectangle.draw())    # Output: Drawing a Rectangle

#----------------------------------------------------------------------------------------------------------------------#

