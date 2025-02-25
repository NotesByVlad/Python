# Loop Control Statements in Comprehensions

# Using 'continue' in a comprehension (filtering with a condition)
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [2, 4]

# Using 'break' in a comprehension with a custom condition
# Simulate a break with a limit on the number of iterations
limited_numbers = [num for num in numbers[:3]]  # We stop at index 3
print("Limited numbers:", limited_numbers)  # Output: [1, 2, 3]

# 'else' in a comprehension (for loops with conditions)
# This is more about conditional expression used in comprehensions.
even_or_odd = [("even" if num % 2 == 0 else "odd") for num in numbers]
print("Even or Odd:", even_or_odd)  # Output: ['odd', 'even', 'odd', 'even', 'odd']
