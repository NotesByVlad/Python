# Queues with Comprehensions

from collections import deque

# A simple queue implemented as a deque
queue = deque([1, 2, 3])

# Enqueue (add elements to the end)
queue.append(4)
queue.append(5)

# List comprehension to print the current queue elements
print("Current queue:", [item for item in queue])  # Output: [1, 2, 3, 4, 5]

# Dequeue (remove elements from the front)
dequeued_element = queue.popleft()
print("Dequeued element:", dequeued_element)  # Output: 1

# Check the remaining queue
print("Remaining queue:", [item for item in queue])  # Output: [2, 3, 4, 5]
