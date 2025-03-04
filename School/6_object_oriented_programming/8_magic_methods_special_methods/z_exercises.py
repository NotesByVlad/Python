# ---------------------------------- Magic Methods & Special Methods Exercises -------------------------------------- #

# 1. Create a class `Point` with x and y coordinates.
#    Override the `__str__` method to return a formatted string of the point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
# TODO 1. Create a Point object with `x=3` and `y=4`. Print the object using the `__str__` method.----------------------



# 2. Create a class `ComplexNumber` with attributes `real` and `imaginary`.
#    Override the `__add__` method to allow addition of two complex numbers.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
# TODO 2. Create two ComplexNumber objects and add them using the overridden `__add__` method.--------------------------

