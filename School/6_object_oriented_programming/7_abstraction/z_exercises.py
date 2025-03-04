# ---------------------------------- Abstraction Exercises -------------------------------------------------------- #

# 1. Create an abstract class `Shape` with an abstract method `area()`.
#    Then create subclasses `Circle` and `Square` implementing the `area()` method.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
# TODO 1. Create a Square object with `side=4` and calculate its area using the `area()` method.------------------------

