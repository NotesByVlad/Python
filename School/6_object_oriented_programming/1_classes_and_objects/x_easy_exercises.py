# ---------------------------------- Easy Exercises (Classes & Objects) ---------------------------------------------- #

# 1. Create a simple class called `Car` with an attribute `brand`. Instantiate an object of this class.
class Car:
    def __init__(self, brand):
        self.brand = brand
# TODO 1. Instantiate the Car class with the brand 'Toyota' and print the object.---------------------------------------



# 2. Add a method `display_brand()` to the `Car` class that prints the brand.
class Car:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(self.brand)
# TODO 2. Create a Car object with the brand 'Honda' and call the `display_brand()` method.-----------------------------



# 3. Create another class `Person` with attributes `name` and `age`.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# TODO 3. Instantiate the Person class with `name='Alice'` and `age=30`.------------------------------------------------



# 4. Add a method `greet()` in the `Person` class that prints a greeting message.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# TODO 4. Create a Person object with `name='Bob'` and `age=25` and call the `greet()` method.--------------------------



# 5. Create a class `Rectangle` with attributes `length` and `width`.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
# TODO 5. Instantiate the Rectangle class with `length=10` and `width=5`.-----------------------------------------------



# 6. Add a method `area()` in the `Rectangle` class that returns the area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
# TODO 6. Create a Rectangle object with `length=10` and `width=5` and calculate its area.------------------------------

