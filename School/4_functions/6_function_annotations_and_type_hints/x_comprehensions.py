# Using Function Annotations and Type Hints
from typing import List

def double_numbers(numbers: List[int]) -> List[int]:
    return [num * 2 for num in numbers]

numbers = [1, 2, 3, 4]
doubled = double_numbers(numbers)
print(doubled)  # Output: [2, 4, 6, 8]

# Using Type Hints with Dictionary Comprehensions
def create_square_dict(numbers: List[int]) -> dict:
    return {num: num ** 2 for num in numbers}

square_dict = create_square_dict([1, 2, 3, 4])
print(square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}
