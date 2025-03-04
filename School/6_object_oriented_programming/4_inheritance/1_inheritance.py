#----------------------------------------   Inheritance in Python Classes   -------------------------------------------#
#                                        -----------------------------------

"""
Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass).
This promotes code reusability and establishes a hierarchical relationship between classes.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Inheritance:
'''
1. The subclass inherits attributes and methods from the superclass.
2. The superclass can have multiple subclasses.
3. You can override methods in the subclass.
4. Inheritance supports single or multiple inheritance.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Single Inheritance

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

# Creating an object of the subclass
dog = Dog()
print(dog.sound())  # Output: Bark

#----------------------------------------------------------------------------------------------------------------------#

# 2. Multiple Inheritance

class Parent1:
    def greet(self):
        return "Hello from Parent1"

class Parent2:
    def farewell(self):
        return "Goodbye from Parent2"

class Child(Parent1, Parent2):
    pass

# Creating an object of the child class
child = Child()
print(child.greet())      # Output: Hello from Parent1
print(child.farewell())   # Output: Goodbye from Parent2

#----------------------------------------------------------------------------------------------------------------------#

# 3. Method Overriding

class Vehicle:
    def info(self):
        return "This is a vehicle"

class Car(Vehicle):
    def info(self):
        return "This is a car"

# Creating objects of Vehicle and Car
vehicle = Vehicle()
car = Car()

print(vehicle.info())  # Output: This is a vehicle
print(car.info())      # Output: This is a car

#----------------------------------------------------------------------------------------------------------------------#

# 4. Using `super()` for Method Overriding

class Shape:
    def area(self):
        return "Calculating area"

class Rectangle(Shape):
    def area(self):
        return "Area of rectangle: Length * Breadth"

    def parent_area(self):
        return super().area()

# Creating a Rectangle object
rectangle = Rectangle()
print(rectangle.area())        # Output: Area of rectangle: Length * Breadth
print(rectangle.parent_area()) # Output: Calculating area

#----------------------------------------------------------------------------------------------------------------------#

# 5. Inheritance with Constructors

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, Student ID: {self.student_id}"

# Creating a Student object
student = Student("Eve", 12345)
print(student.display_info())  # Output: Name: Eve, Student ID: 12345

#----------------------------------------------------------------------------------------------------------------------#
