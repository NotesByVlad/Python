# ----------------------------------------   Attributes and Methods in Python Classes   -------------------------------#
#                                        -----------------------------------------------

"""
In Python, attributes and methods are essential components of classes.
Attributes are variables that hold data for an object, and methods are functions defined within the class
to operate on the object's data.
Attributes can be class-level (shared across all instances) or instance-level (unique to each object).
Methods define the behavior of the object.
"""
# ---------------------------------------------------------------------------------------------------------------------#

# Key Points about Attributes and Methods:
'''
Attributes:
- Instance Attributes: Defined within the `__init__` method and belong to the instance (object).
- Class Attributes: Defined within the class but outside any method and shared across all instances.

Methods:
- Instance Methods: Operate on instance attributes and `self` refers to the object.
- Class Methods: Operate on class-level attributes, and `cls` refers to the class.
- Static Methods: Do not take `self` or `cls` as arguments and do not interact with class or instance data.
'''


# ---------------------------------------------------------------------------------------------------------------------#

# 1. Class with Instance Attributes and Methods

class Car:
	# Class attribute
	wheels = 4

	def __init__(self, brand, model):
		# Instance attributes
		self.brand = brand
		self.model = model

	def display_info(self):
		# Instance method
		return f"{self.brand} {self.model}, Wheels: {self.wheels}"

	def start_engine(self):
		# Another instance method
		return f"The {self.brand} {self.model} engine is starting."


# Creating an object of the class
car1 = Car("Toyota", "Camry")

# Accessing instance attributes
print(car1.display_info())  # Output: Toyota Camry, Wheels: 4

# Using methods
print(car1.start_engine())  # Output: The Toyota Camry engine is starting.


# ---------------------------------------------------------------------------------------------------------------------#

# 2. Class with Class Attributes and Class Methods

class Animal:
	# Class attribute
	kingdom = 'Animalia'

	def __init__(self, species, name):
		# Instance attributes
		self.species = species
		self.name = name

	def display_info(self):
		# Instance method
		return f"{self.name} is a {self.species} belonging to the {self.kingdom} kingdom."

	@classmethod
	def display_kingdom(cls):
		# Class method
		return f"This is the {cls.kingdom} kingdom."


# Creating an object of the class
animal1 = Animal("Dog", "Buddy")

# Accessing instance attributes
print(animal1.display_info())  # Output: Buddy is a Dog belonging to the Animalia kingdom.

# Accessing class method
print(Animal.display_kingdom())  # Output: This is the Animalia kingdom.


# ---------------------------------------------------------------------------------------------------------------------#

# 3. Static Method Example

class MathOperations:

	def __init__(self, value):
		self.value = value

	def double(self):
		# Instance method
		return self.value * 2

	@staticmethod
	def add(a, b):
		# Static method
		return a + b


# Creating an object of the class
math1 = MathOperations(10)

# Using instance method
print(math1.double())  # Output: 20

# Using static method
print(MathOperations.add(5, 7))  # Output: 12

# ---------------------------------------------------------------------------------------------------------------------#
