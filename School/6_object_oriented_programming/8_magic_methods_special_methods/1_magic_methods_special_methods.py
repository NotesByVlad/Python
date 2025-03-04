#----------------------------------------   Magic Methods and Special Methods   ---------------------------------------#
#                                        ---------------------------------------

"""
Magic methods, also known as dunder methods (double underscore methods),
are special methods in Python that allow customization of default behavior
of classes and objects. They provide built-in operations like arithmetic
operations, string representation, and more.

Special methods are defined by prefixing and suffixing the method name with
double underscores, e.g., `__init__`, `__str__`, `__add__`, etc.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Magic Methods:
'''
1. Magic methods allow developers to define how objects interact with built-in functions and operations.
2. They enable operators like +, -, *, etc., to work seamlessly with custom objects.
3. Common magic methods include __init__, __str__, __repr__, __add__, __len__, __eq__, and many more.
'''

#----------------------------------------------------------------------------------------------------------------------#

# 1. __init__ - Constructor Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

# Creating an object
person1 = Person("Alice", 30)
print(person1.display())  # Output: Name: Alice, Age: 30

#----------------------------------------------------------------------------------------------------------------------#

# 2. __str__ - String Representation

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1)  # Output: Toyota Corolla

#----------------------------------------------------------------------------------------------------------------------#

# 3. __add__ - Overloading Addition Operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2
print(c3)  # Output: 6 + 8i

#----------------------------------------------------------------------------------------------------------------------#

# 4. __len__ - Overloading the len() function

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

book1 = Book("Python Programming", 450)
print(len(book1))  # Output: 450

#----------------------------------------------------------------------------------------------------------------------#

# 5. __eq__ - Overloading Equality Operator

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

rect1 = Rectangle(5, 10)
rect2 = Rectangle(5, 10)
rect3 = Rectangle(3, 6)

print(rect1 == rect2)  # Output: True
print(rect1 == rect3)  # Output: False

#----------------------------------------------------------------------------------------------------------------------#

# 6. __repr__ - Official String Representation

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Student({self.id}, {self.name})"

student1 = Student(1, "John Doe")
print(repr(student1))  # Output: Student(1, John Doe)

#----------------------------------------------------------------------------------------------------------------------#

