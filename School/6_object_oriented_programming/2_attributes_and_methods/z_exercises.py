# ---------------------------------- Attributes and Methods Exercises ----------------------------------------------- #

# 1. Create a class `Person` with attributes `name` and `age`. Add a method `greet()` that prints a greeting message.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
# TODO 1. Create a Person object with `name='Alice'` and `age=30`. Call the `greet()` method.---------------------------



# 2. Create a class `Car` with attributes `make` and `model`. Add a method `display_info()` to show the car information.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"
# TODO 2. Create a Car object with `make='Toyota'` and `model='Corolla'`.
#         Display the information using `display_info()` method.--------------------------------------------------------

