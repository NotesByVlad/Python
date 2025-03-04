# Stacks with Comprehensions

# A simple stack implemented as a list
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# List comprehension to print the current stack elements
print("Current stack:", [item for item in stack])  # Output: [1, 2, 3]

# Pop elements from the stack (LIFO - Last In First Out)
popped_element = stack.pop()
print("Popped element:", popped_element)  # Output: 3

# Check the remaining stack
print("Remaining stack:", [item for item in stack])  # Output: [1, 2]
