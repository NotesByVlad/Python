# ---------------------------------- Inheritance Exercises ----------------------------------------------------------- #

# 1. Create a base class `Animal` with a method `speak()`.
class Animal:
    def speak(self):
        return "Animal speaks"



# TODO 1. Create a subclass `Dog` that inherits from `Animal` and override the `speak()` method.------------------------
class Dog(Animal):
    def speak(self):
        return "Dog barks"


# TODO 2. Create a subclass `Cat` that inherits from `Animal` and override the `speak()` method.------------------------
class Cat(Animal):
    def speak(self):
        return "Cat meows"



# 2. Create a base class `Vehicle` with attributes `make` and `model`. Add a method `display_info()`.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"



# TODO 3. Create a subclass `Car` that inherits from `Vehicle` and add a method `honk()`.-------------------------------
class Car(Vehicle):
    def honk(self):
        return "Car honks"



# TODO 4. Create another subclass `Truck` that inherits from `Vehicle` and override the `display_info()` method.--------
class Truck(Vehicle):
    def display_info(self):
        return f"Truck: {self.make} {self.model} - Heavy Vehicle"

