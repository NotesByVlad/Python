#----------------------------------------   Class vs Instance   -------------------------------------------------------#
#                                        -----------------------

"""
In Python, a **Class** is a blueprint for creating objects, defining properties
and methods common to all objects created from the class. An **Instance** is
a specific object created from a class.

Key differences between Class and Instance:
1. **Class** defines the structure and behavior.
2. **Instance** is a specific object that uses the class to instantiate itself.
3. You use the class to create multiple instances, each with its own data.

"""

#----------------------------------------------------------------------------------------------------------------------#

# 1. Class Definition

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"A {self.species} makes a {self.sound} sound."

# Creating instances (objects) of the class
dog = Animal("Dog", "bark")
cat = Animal("Cat", "meow")

print(dog.make_sound())  # Output: A Dog makes a bark sound.
print(cat.make_sound())  # Output: A Cat makes a meow sound.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Accessing Attributes of Class and Instance

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"{self.name} works as a {self.position}"

# Using the class to create instances
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")

print(emp1.get_details())  # Output: Alice works as a Manager
print(emp2.get_details())  # Output: Bob works as a Developer

# Accessing class attributes
print(Employee.__dict__)  # Output: {'__module__': '__main__',
                          # 'get_details': <function ...>,
                          # '__init__': <function ...>,
                          # '__dict__': <attribute '__dict__' of 'Employee' objects>,
                          # '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
                          # '__doc__': None}

# Instance-specific data
print(emp1.__dict__)  # Output: {'name': 'Alice', 'position': 'Manager'}

#----------------------------------------------------------------------------------------------------------------------#

# 3. Methods and Attributes Specific to Instances

class Shape:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

# Creating instances with different sides
triangle = Shape([3, 4, 5])
square = Shape([4, 4, 4, 4])

print(triangle.perimeter())  # Output: 12
print(square.perimeter())    # Output: 16

#----------------------------------------------------------------------------------------------------------------------#

# 4. Modifying Instance Attributes

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

# Creating an instance
car1 = Car("Tesla", "Model S")
print(car1.display_info())  # Output: Tesla Model S

# Modifying instance attributes
car1.model = "Model 3"
print(car1.display_info())  # Output: Tesla Model 3

#----------------------------------------------------------------------------------------------------------------------#

# 5. Class Attribute vs Instance Attribute

class BankAccount:
    bank_name = "Global Bank"  # Class Attribute

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance Attribute
        self.balance = balance

# Accessing class and instance attributes
print(BankAccount.bank_name)  # Output: Global Bank
print(car1.bank_name)          # Output: AttributeError since 'car1' is not related to class 'BankAccount'

account1 = BankAccount("John Doe", 1000)
print(account1.account_holder)  # Output: John Doe
print(account1.balance)         # Output: 1000

#----------------------------------------------------------------------------------------------------------------------#

