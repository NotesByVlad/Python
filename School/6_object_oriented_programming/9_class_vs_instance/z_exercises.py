# ---------------------------------- Class vs Instance Exercises ----------------------------------------------------- #

# 1. Create a class `Rectangle` with attributes `width` and `height`. Create two instances and compare their dimensions.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
# TODO 1. Create two Rectangle objects with different dimensions and compare their attributes (`width` and `height`).---



# 2. Create a class `Counter` with a class variable `counter` and
#    an instance method `increment()` to increase the counter.
class Counter:
    counter = 0  # Class variable

    def increment(self):
        Counter.counter += 1
# TODO 2. Create two Counter objects and call `increment()` on both to check if the class variable is shared.-----------

