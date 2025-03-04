# ---------------------------------- Hard Exercises (Classes & Objects) ---------------------------------------------- #

# 1. Create a class `Library` that stores a list of books. Add methods `add_book()` and `list_books()`.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.details())

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}"
# TODO 1. Create a Library object and add a few books, then list all books.---------------------------------------------



# 2. Create a class `CarRental` with attributes `cars_available` and a method `rent_car()`
#    that reduces the number of available cars.
class CarRental:
    def __init__(self, cars_available):
        self.cars_available = cars_available

    def rent_car(self):
        if self.cars_available > 0:
            self.cars_available -= 1
            return True
        else:
            return False
# TODO 2. Create a CarRental object with `cars_available=10` and attempt to rent 3 cars.--------------------------------



# 3. Create a class `Course` with attributes `title`, `students` (list of Student objects).
#    Add a method `average_grade()` that computes the average grade of all students.
class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_grade(self):
        total_grade = 0
        for student in self.students:
            total_grade += student.average_grade()
        return total_grade / len(self.students)

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
# TODO 3. Create a Course object, add a few students with their grades, and compute the average grade.------------------

