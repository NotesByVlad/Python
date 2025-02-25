# Loops with Comprehensions

# Using 'for' loop in list comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Using 'for' loop in set comprehensions
unique_numbers = {num for num in numbers if num % 2 != 0}
print("Unique odd numbers:", unique_numbers)  # Output: {1, 3, 5}

# Nested loops in list comprehensions
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)  # Output: [1, 2, 3, 4, 5, 6]
