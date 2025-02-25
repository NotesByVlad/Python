# Conditional Statements with Comprehensions

# List Comprehension with 'if' condition (filtering)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)  # Output: [1, 3, 5, 7, 9]

# Example with string filtering
words = ["apple", "banana", "cherry", "date"]
short_words = [word for word in words if len(word) < 6]
print("Short words:", short_words)  # Output: ['apple', 'date']
