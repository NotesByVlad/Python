# Exception Handling with Comprehensions

# Handling exceptions inside list comprehensions
numbers = ["1", "2", "3", "a", "4", "b"]

# Try to convert each item to an integer
converted_numbers = []
for item in numbers:
    try:
        converted_numbers.append(int(item))
    except ValueError:
        converted_numbers.append(None)

print("Converted numbers:", converted_numbers)  # Output: [1, 2, 3, None, 4, None]

# Using a list comprehension with exception handling (try-except inside comprehension)
safe_numbers = [int(item) if item.isdigit() else None for item in numbers]
print("Safe numbers:", safe_numbers)  # Output: [1, 2, 3, None, 4, None]
