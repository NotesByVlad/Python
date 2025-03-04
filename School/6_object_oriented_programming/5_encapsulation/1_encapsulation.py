#----------------------------------------   Encapsulation in Python Classes   -----------------------------------------#
#                                        -------------------------------------

"""
Encapsulation is the practice of bundling data (attributes) and methods (functions)
that operate on the data into a single unit, typically a class.
It restricts direct access to some of the object's components,
and provides controlled access through methods.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Encapsulation:
'''
1. Data members are hidden and can only be accessed via public methods (getters and setters).
2. It helps to protect data from accidental modification.
3. Provides a way to control how data is accessed and modified.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Basic Example of Encapsulation

class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter method for account number
    def get_account_number(self):
        return self.__account_number

    # Setter method for account balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    # Getter method for balance
    def get_balance(self):
        return self.__balance

# Creating an Account object
acc = Account(123456, 1000)

# Accessing attributes directly will raise an error
# print(acc.__account_number)  # AttributeError

# Accessing private attributes via getters
print("Account Number:", acc.get_account_number())  # Output: Account Number: 123456

# Setting and getting balance
acc.set_balance(1200)
print("Balance:", acc.get_balance())  # Output: Balance: 1200

# Attempt to set a negative balance
acc.set_balance(-500)  # Output: Balance cannot be negative.

#----------------------------------------------------------------------------------------------------------------------#

# 2. Using Properties for Encapsulation

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Salary must be positive.")

# Creating an Employee object
emp = Employee("John Doe", 5000)

# Accessing salary
print("Salary:", emp.salary)  # Output: Salary: 5000

# Setting salary
emp.salary = 6000
print("Updated Salary:", emp.salary)  # Output: Updated Salary: 6000

# Attempt to set a negative salary
emp.salary = -2000  # Output: Salary must be positive.

#----------------------------------------------------------------------------------------------------------------------#

# 3. Encapsulation with Private Variables and Methods

class Car:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year

    def __private_method(self):
        return f"{self.__brand} - {self.__year}"

    def get_private_info(self):
        return self.__private_method()

# Creating a Car object
car = Car("Toyota", 2020)

# Accessing private information via public method
print(car.get_private_info())  # Output: Toyota - 2020

# Attempt to access private method directly
# print(car.__private_method())  # AttributeError

#----------------------------------------------------------------------------------------------------------------------#
