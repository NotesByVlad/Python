#----------------------------------------   Polymorphism in Python Classes   ------------------------------------------#
#                                        ------------------------------------

"""
Polymorphism, in the context of object-oriented programming, allows objects of different types
to be treated as objects of a common superclass. This enables a single interface to handle
different types of objects seamlessly.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Polymorphism:
'''
1. In Python, polymorphism can be achieved through method overriding and the use of interfaces or abstract classes.
2. It allows a single method name to operate differently based on the object it is working with.
3. The ability to call the same method with different objects and get different results.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Method Overriding - Example of Polymorphism

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
print("Dog:", dog.sound())  # Output: Dog: Bark
print("Cat:", cat.sound())  # Output: Cat: Meow

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using Polymorphism with a Function

def make_sound(animal):
    print(animal.sound())

# Passing different objects
make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow

#----------------------------------------------------------------------------------------------------------------------#

# 3. Polymorphism with Abstract Base Class (ABC)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Creating instances
circle = Circle(5)
square = Square(4)

# Polymorphism with area method
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Square Area:", square.area())  # Output: Square Area: 16

#----------------------------------------------------------------------------------------------------------------------#

# 4. Operator Overloading for Polymorphism

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Creating two vectors
v1 = Vector(2, 3)
v2 = Vector(4, 1)

# Using overloaded + operator
result = v1 + v2
print(result)  # Output: Vector(6, 4)

#----------------------------------------------------------------------------------------------------------------------#
