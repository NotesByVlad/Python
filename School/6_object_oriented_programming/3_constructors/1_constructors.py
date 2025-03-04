#----------------------------------------   Constructors in Python Classes   ------------------------------------------#
#                                        ----------------------------------

"""
In Python, constructors are special methods used to initialize the state (attributes) of an object when it is created.
The most common constructor is the `__init__` method, which is automatically called when an object is instantiated.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Constructors:
'''
1. The `__init__` method is used for initializing instance attributes.
2. Constructors can accept parameters to initialize different attributes.
3. Constructors ensure objects have necessary attributes for later use.
4. Optional parameters can be used to handle default values.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Constructor with Required Parameters

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Creating an object of the class
person1 = Person("Alice", 30)

# Using the constructor to initialize attributes
print(person1.display_info())  # Output: Name: Alice, Age: 30

#----------------------------------------------------------------------------------------------------------------------#

# 2. Constructor with Default Parameters

class Employee:
    def __init__(self, name, position="Unknown", salary=0):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

# Creating objects with and without default parameters
employee1 = Employee("Bob", "Manager", 60000)
employee2 = Employee("Charlie")

print(employee1.display_info())  # Output: Name: Bob, Position: Manager, Salary: 60000
print(employee2.display_info())  # Output: Name: Charlie, Position: Unknown, Salary: 0

#----------------------------------------------------------------------------------------------------------------------#

# 3. Constructor with Multiple Attributes and Type Checking

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

# Creating a product with type hints
product1 = Product("Laptop", 899.99, 50)
print(product1.display_info())  # Output: Product Name: Laptop, Price: 899.99, Stock: 50

#----------------------------------------------------------------------------------------------------------------------#

# 4. Constructor with Self Parameter and Validation

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if year >= 1886:  # The year the first car was made
            self.year = year
        else:
            raise ValueError("Year must be 1886 or later.")

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"

# Creating a valid car object
car1 = Car("Tesla", "Model S", 2022)
print(car1.display_info())  # Output: Tesla Model S (2022)

# Attempting to create an invalid car object (will raise a ValueError)
# car2 = Car("Ford", "Model T", 1800)  # Uncommenting this will raise an error

#----------------------------------------------------------------------------------------------------------------------#
