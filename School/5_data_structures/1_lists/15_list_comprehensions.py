# List Comprehensions in Data Structures

# Basic List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Filtering Even Numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [2, 4]

# Merging Two Lists Using Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [item for item in list1] + [item for item in list2]
print("Merged list:", merged)  # Output: [1, 2, 3, 4, 5, 6]

# Nested List Comprehension (Flattening a 2D List)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sorting Using List Comprehension
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = [num for num in sorted(numbers)]
print("Sorted numbers:", sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
