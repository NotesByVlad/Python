#----------------------------------------   Function Annotations and Type Hints in Python   ---------------------------#
#                                        ---------------------------------------------------

"""
In Python, function annotations provide a way to attach metadata to function parameters and return values.
These annotations are often used as type hints to indicate the expected data types, but they are not enforced by
Python at runtime.

Type hints improve code readability, make it easier to understand a function's expected input and output, and
enhance tooling support for static type checking using tools like `mypy`.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Function Annotations and Type Hints:
'''
- Function Annotations: Metadata for parameters and return values, defined using a colon (`:`) after the parameter name.
- Type Hints: Specific annotations that indicate the expected data type.
- Syntax:
  - Parameters: `parameter_name: type`
  - Return Type: `-> type`
- `typing` Module: Provides advanced type hinting features such as `List`, `Dict`, `Tuple`, `Union`, `Optional`, 
  and more.
- Benefits: Improves code readability, aids in static analysis, and reduces runtime errors through better documentation.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Basic Function Annotations

def greet(name: str) -> str:
    """A function that takes a name and returns a greeting message."""
    return f"Hello, {name}!"

# Using the Function
print(greet("Alice"))  # Output: Hello, Alice!

#----------------------------------------------------------------------------------------------------------------------#

# Type Hints with Built-in Data Structures
from typing import List, Dict

def process_scores(scores: List[int]) -> Dict[str, float]:
    """Calculate the average score and return a dictionary with the result."""
    average = sum(scores) / len(scores)
    return {"average": average}

# Using the Function
scores = [85, 90, 78]
print(process_scores(scores))  # Output: {'average': 84.33333333333333}

#----------------------------------------------------------------------------------------------------------------------#

# Using `Optional` and `Union`
from typing import Optional, Union

def describe_age(age: Optional[Union[int, str]]) -> str:
    """Describe the age if provided, or return a default message."""
    if age is None:
        return "Age not provided."
    return f"Age: {age}"

# Using the Function
print(describe_age(30))         # Output: Age: 30
print(describe_age("Unknown")) # Output: Age: Unknown
print(describe_age(None))       # Output: Age not provided.

#----------------------------------------------------------------------------------------------------------------------#

# Advanced Type Hints with Callable and Custom Types
from typing import Callable, Tuple

# Defining a Custom Type Hint
Operation = Callable[[int, int], int]

def execute_operation(a: int, b: int, operation: Operation) -> int:
    """Execute a binary operation on two integers."""
    return operation(a, b)

# Using the Function with a Lambda Function
result = execute_operation(5, 3, lambda x, y: x + y)
print(result)  # Output: 8

#----------------------------------------------------------------------------------------------------------------------#

# Type Checking with `mypy`
'''
To perform static type checking, use the `mypy` tool. Install it using pip:
    pip install mypy

Run `mypy` on your Python file to identify type inconsistencies.
Example:
    mypy script.py
'''
#----------------------------------------------------------------------------------------------------------------------#
