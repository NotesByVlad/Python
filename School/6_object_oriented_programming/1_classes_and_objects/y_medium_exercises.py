# ---------------------------------- Medium Exercises (Classes & Objects) -------------------------------------------- #

# 1. Create a class `Book` with attributes `title`, `author`, and `year_published`. Add a method `details()`
#    that prints these details.
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}")
# TODO 1. Create a Book object with `title='1984'`, `author='George Orwell'`, and `year_published=1949`
#         and call `details()`.-----------------------------------------------------------------------------------------



# 2. Create a class `Account` with attributes `account_number` and `balance`. Add a method `deposit()`
#    to add to the balance.
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
# TODO 2. Create an Account object with `account_number=12345` and `balance=1000`, then deposit `500`.------------------



# 3. Create a class `Student` with attributes `name` and `grades`. Add a method `average_grade()`
#    to calculate the average.
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
# TODO 3. Create a Student object with `name='Charlie'` and `grades=[85, 90, 78]`, then calculate the average grade.----



# 4. Create a class `Circle` with an attribute `radius`. Add methods `circumference()` and `area()`.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)
# TODO 4. Create a Circle object with `radius=7` and calculate both circumference and area.-----------------------------

