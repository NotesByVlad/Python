# ---------------------------------- Polymorphism Exercises ---------------------------------------------------------- #

# 1. Create a class `Shape` with a method `area()`.
#    Then create subclasses `Circle` and `Rectangle` that override the `area()` method.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
# TODO 1. Create a Circle object with `radius=10` and calculate the area.-----------------------------------------------



# 2. Create a class `Employee` with a method `calculate_salary()`.
#    Create subclasses `FullTimeEmployee` and `PartTimeEmployee` that override this method.
class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 5000  # Example fixed salary

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20 * 80  # Example hourly wage for 80 hours
# TODO 2. Create a FullTimeEmployee object and calculate the salary.----------------------------------------------------

