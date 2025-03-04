# ---------------------------------- Encapsulation Exercises --------------------------------------------------------- #

# 1. Create a class `BankAccount` with a private attribute `balance`. Add methods `deposit()` and `withdraw()`.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")
# TODO 1. Create a BankAccount object with an initial balance of 1000 and deposit 500.----------------------------------



# 2. Create a class `Person` with a private attribute `__age`. Add a method `get_age()` to access the private attribute.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age
# TODO 2. Create a Person object with `name='Mike'` and `age=30` and access the age using `get_age()` method.-----------

