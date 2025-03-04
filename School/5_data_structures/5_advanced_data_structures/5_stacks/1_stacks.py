# ----------------------------------------   Stacks in Python   -------------------------------------------------------#
#                                         ----------------------

"""
A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.
This means that the last element added to the stack is the first one to be removed. It can be imagined
as a collection of items arranged in a vertical stack, where you can only add or remove items from the
top of the stack.

### Key Concepts:
- **LIFO (Last In, First Out)**: The last element added is the first one to be removed.
- **Push**: Adding an item to the stack.
- **Pop**: Removing the top item from the stack.
- **Peek**: Viewing the top item without removing it.
- **Is Empty**: Checking whether the stack is empty.
- **Size**: Getting the number of elements in the stack.

"""

# 1. **Basic Stack Operations**:
# A stack has a few essential operations: `push`, `pop`, `peek`, `is_empty`, and `size`.

# Creating a stack:
stack = []

# Push operation (adding an element to the stack):
stack.append(10)  # Push 10 onto the stack
stack.append(20)  # Push 20 onto the stack
stack.append(30)  # Push 30 onto the stack
print("Stack after push operations:", stack)  # Output: [10, 20, 30]

# Pop operation (removing the top element from the stack):
top = stack.pop()  # Pop the last element (30)
print("Popped element:", top)  # Output: 30
print("Stack after pop operation:", stack)  # Output: [10, 20]

# Peek operation (viewing the top element without removing it):
top = stack[-1]  # Access the top element
print("Top element (peek):", top)  # Output: 20

# Checking if the stack is empty:
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)  # Output: False

# Getting the size of the stack:
size = len(stack)
print("Size of the stack:", size)  # Output: 2


# Explanation:
# - `push`: Adding elements to the stack using `append()`.
# - `pop`: Removing elements from the stack using `pop()`.
# - `peek`: Accessing the last element using indexing.
# - `is_empty`: Checking if the stack has no elements using `len()`.
# - `size`: Using `len()` to get the number of elements in the stack.

# 2. **Stack Implementation Using a Class**:
# A more formal stack implementation can be done using a class, which makes it reusable
# and encapsulates the stack operations.

class Stack:
	def __init__(self):
		self.stack = []  # Initialize an empty stack

	def push(self, item):
		"""Add an item to the stack"""
		self.stack.append(item)

	def pop(self):
		"""Remove and return the top item of the stack. Raise an error if empty."""
		if not self.is_empty():
			return self.stack.pop()
		else:
			raise IndexError("pop from empty stack")

	def peek(self):
		"""Return the top item without removing it"""
		if not self.is_empty():
			return self.stack[-1]
		else:
			raise IndexError("peek from empty stack")

	def is_empty(self):
		"""Check if the stack is empty"""
		return len(self.stack) == 0

	def size(self):
		"""Return the number of items in the stack"""
		return len(self.stack)


# Creating a stack instance:
stack = Stack()

# Performing stack operations:
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.stack)  # Output: [10, 20, 30]

top = stack.pop()
print("Popped element:", top)  # Output: 30
print("Stack after pop:", stack.stack)  # Output: [10, 20]

top = stack.peek()
print("Top element:", top)  # Output: 20

print("Is stack empty?", stack.is_empty())  # Output: False
print("Size of stack:", stack.size())  # Output: 2


# Explanation:
# This `Stack` class encapsulates stack operations and allows for more controlled and structured usage of stacks.
# Methods include `push()`, `pop()`, `peek()`, `is_empty()`, and `size()`.

# 3. **Using a Stack for Balancing Parentheses**:
# Stacks are commonly used for problems like balancing parentheses or brackets in expressions.

def is_balanced(expression):
	stack = Stack()  # Create a new stack
	# Define matching pairs
	matching = {')': '(', '}': '{', ']': '['}

	for char in expression:
		if char in "({[":
			stack.push(char)  # Push opening brackets onto the stack
		elif char in ")}]":
			if stack.is_empty() or stack.pop() != matching[char]:
				return False  # Unmatched closing bracket or empty stack
	return stack.is_empty()  # If the stack is empty, all brackets matched


# Test the function:
expression = "({[()]})"
print("Is the expression balanced?", is_balanced(expression))  # Output: True

expression = "({[())]}"
print("Is the expression balanced?", is_balanced(expression))  # Output: False

# Explanation:
# This is an example of a practical use case of stacks. The stack holds opening brackets,
# and when a closing bracket is encountered, it checks if the corresponding opening bracket
# is at the top of the stack.

# 4. **Applications of Stacks**:
# Stacks have several real-world applications in computer science, such as:
# - **Undo/Redo functionality** in applications.
# - **Expression evaluation** (e.g., postfix, infix expressions).
# - **Function calls in recursion** (call stack).
# - **Depth-First Search (DFS)** in graph algorithms.
# - **Backtracking** (e.g., solving mazes).

# 5. **Summary**:
'''
- A **stack** is a LIFO data structure where elements are added and removed from the top.
- **Common operations**:
    - `push()`: Add an item to the stack.
    - `pop()`: Remove and return the top item.
    - `peek()`: View the top item without removing it.
    - `is_empty()`: Check if the stack is empty.
    - `size()`: Get the number of elements in the stack.
- **Implementation**: A stack can be implemented using a list or a custom class to encapsulate the stack operations.
- **Applications**: Stacks are used in a variety of scenarios such as balancing parentheses, recursion, expression evaluation, and more.
'''

# ----------------------------------------------------------------------------------------------------------------------#
