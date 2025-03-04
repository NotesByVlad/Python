#----------------------------------------   Object-Oriented Programming in Python   ----------------------------------------#
#                                        ------------------------------------

"""
Object-oriented programming (OOP) is a paradigm that allows developers to model real-world
entities as objects in code. Python provides robust support for OOP concepts, making it
easier to write modular, reusable, and scalable code.

### Key Concepts:
1. **Classes and Objects**
2. **Attributes and Methods**
3. **Constructors**
4. **Inheritance**
5. **Encapsulation**
6. **Polymorphism**
7. **Abstraction**
8. **Magic Methods and Special Methods**
9. **Class vs Instance**

"""

# 1. **Classes and Objects**:
# Classes define the blueprint for objects, and objects are instances of classes.

# Defining a class:
class Dog:
    # Class-level attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance-level attributes
        self.name = name
        self.age = age

# Creating objects:
my_dog = Dog("Buddy", 5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5

# Explanation:
# A class is defined using the `class` keyword, and objects are created by calling the class like a function.

# 2. **Attributes and Methods**:
# Attributes are variables associated with an object, and methods are functions defined within a class.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object and calling a method:
my_dog = Dog("Buddy", 5)
print(my_dog.bark())  # Output: Buddy says Woof!

# Explanation:
# Methods are defined within a class and typically operate on the instance attributes.

# 3. **Constructors**:
# Constructors are special methods (e.g., `__init__`) that are automatically called when an object is created.

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Creating an object:
my_cat = Cat("Whiskers", "black")
print(my_cat.name)   # Output: Whiskers
print(my_cat.color)  # Output: black

# Explanation:
# The constructor method `__init__` initializes an object’s attributes.

# 4. **Inheritance**:
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Creating an object:
my_dog = Dog("Buddy")
print(my_dog.speak())  # Output: Buddy says Woof!

# Explanation:
# The child class (`Dog`) inherits from the parent class (`Animal`) and overrides the `speak` method.

# 5. **Encapsulation**:
# Encapsulation restricts access to certain attributes or methods, using underscore `_` for protected and double underscore `__` for private.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Insufficient funds"

# Creating an object:
account = BankAccount("John", 1000)
print(account.deposit(500))  # Output: 1500
print(account.withdraw(700)) # Output: 800
# print(account.__balance)   # Error: AttributeError

# Explanation:
# Private attributes or methods are not directly accessible from outside the class.

# 6. **Polymorphism**:
# Polymorphism allows objects of different classes to be treated as objects of a common parent class.

class Bird:
    def speak(self):
        return "Chirp!"

class Dog:
    def speak(self):
        return "Woof!"

# Polymorphic function:
def make_sound(animal):
    print(animal.speak())

# Using the function with different objects:
make_sound(Bird())  # Output: Chirp!
make_sound(Dog())   # Output: Woof!

# Explanation:
# Polymorphism allows different classes to share the same interface for specific methods.

# 7. **Abstraction**:
# Abstraction hides implementation details and only exposes essential features. Achieved using abstract base classes.

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

# Creating an object:
circle = Circle(5)
print(circle.area())  # Output: 78.5

# Explanation:
# Abstract classes cannot be instantiated, and subclasses must implement abstract methods.

# 8. **Magic Methods and Special Methods**:
# Magic methods provide special functionality for objects, such as overloading operators.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating objects:
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: (4, 6)

# Explanation:
# Magic methods like `__add__` and `__str__` allow operator overloading and string representation.

# 9. **Class vs Instance**:
# Class attributes and methods are shared among all instances, while instance attributes and methods are specific to each object.

class Example:
    class_attribute = "I am shared"

    def __init__(self, value):
        self.instance_attribute = value

# Creating objects:
obj1 = Example("Instance 1")
obj2 = Example("Instance 2")

print(obj1.class_attribute)         # Output: I am shared
print(obj1.instance_attribute)      # Output: Instance 1
Example.class_attribute = "Changed"
print(obj2.class_attribute)         # Output: Changed

# Explanation:
# Class attributes are shared, while instance attributes are unique to each object.

# 10. **Summary**:
'''
1. **Classes and Objects**: Classes define the blueprint; objects are instances of classes.
2. **Attributes and Methods**: Attributes store data; methods define behavior.
3. **Constructors**: Special methods for initializing objects.
4. **Inheritance**: Enables code reuse by deriving new classes from existing ones.
5. **Encapsulation**: Restricts access to certain parts of an object.
6. **Polymorphism**: Allows different classes to be used interchangeably.
7. **Abstraction**: Hides implementation details, exposing only the essentials.
8. **Magic Methods**: Special methods for operator overloading and other features.
9. **Class vs Instance**: Class-level attributes/methods are shared; instance-level attributes/methods are unique.
'''

#----------------------------------------------------------------------------------------------------------------------#
