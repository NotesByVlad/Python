# ----------------------------------------   Queues in Python   ------------------------------------------------------#
#                                         ----------------------

"""
A **queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle. This means that the first element added to the queue is the first one to be removed. It can be imagined as a collection of items arranged in a line, where elements are added at one end (rear) and removed from the other (front).

### Key Concepts:
- **FIFO (First In, First Out)**: The first element added is the first one to be removed.
- **Enqueue**: Adding an item to the rear of the queue.
- **Dequeue**: Removing an item from the front of the queue.
- **Peek/Front**: Viewing the front item without removing it.
- **Is Empty**: Checking whether the queue is empty.
- **Size**: Getting the number of elements in the queue.
"""

# 1. **Basic Queue Operations**:
# A queue has a few essential operations: `enqueue`, `dequeue`, `peek`, `is_empty`, and `size`.

# Creating a queue:
from collections import deque
queue = deque()

# Enqueue operation (adding an element to the rear of the queue):
queue.append(10)  # Enqueue 10
queue.append(20)  # Enqueue 20
queue.append(30)  # Enqueue 30
print("Queue after enqueue operations:", list(queue))  # Output: [10, 20, 30]

# Dequeue operation (removing the front element from the queue):
front = queue.popleft()  # Dequeue the front element (10)
print("Dequeued element:", front)  # Output: 10
print("Queue after dequeue operation:", list(queue))  # Output: [20, 30]

# Peek operation (viewing the front element without removing it):
front = queue[0]  # Access the front element
print("Front element (peek):", front)  # Output: 20

# Checking if the queue is empty:
is_empty = len(queue) == 0
print("Is the queue empty?", is_empty)  # Output: False

# Getting the size of the queue:
size = len(queue)
print("Size of the queue:", size)  # Output: 2


# Explanation:
# - `enqueue`: Adding elements to the queue using `append()`.
# - `dequeue`: Removing elements from the queue using `popleft()`.
# - `peek`: Accessing the front element using indexing.
# - `is_empty`: Checking if the queue has no elements using `len()`.
# - `size`: Using `len()` to get the number of elements in the queue.

# 2. **Queue Implementation Using a Class**:
# A more formal queue implementation can be done using a class, which encapsulates the queue operations.

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty queue

    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue. Raise an error if empty."""
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue"""
        return len(self.queue)


# Creating a queue instance:
queue = Queue()

# Performing queue operations:
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue after enqueues:", list(queue.queue))  # Output: [10, 20, 30]

front = queue.dequeue()
print("Dequeued element:", front)  # Output: 10
print("Queue after dequeue:", list(queue.queue))  # Output: [20, 30]

front = queue.peek()
print("Front element:", front)  # Output: 20

print("Is queue empty?", queue.is_empty())  # Output: False
print("Size of queue:", queue.size())  # Output: 2


# Explanation:
# This `Queue` class encapsulates queue operations and allows for more controlled and structured usage of queues.
# Methods include `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, and `size()`.

# 3. **Queue Applications: Simulating a Printer Queue**:
# Queues are commonly used for tasks like simulating a printer queue or scheduling.

def simulate_printer_queue(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)  # Add each task to the queue

    while not queue.is_empty():
        current_task = queue.dequeue()  # Process the front task
        print("Printing:", current_task)

# Test the function:
tasks = ["Document1", "Document2", "Document3"]
simulate_printer_queue(tasks)
# Output:
# Printing: Document1
# Printing: Document2
# Printing: Document3


# Explanation:
# This is an example of how queues are used in real-world scenarios. The queue holds tasks, and each task is processed in the order it was added.

# 4. **Applications of Queues**:
# Queues have several real-world applications in computer science, such as:
# - **Task scheduling** (e.g., CPU scheduling, printer queues).
# - **Breadth-First Search (BFS)** in graph algorithms.
# - **Message queues** in networking and distributed systems.
# - **Handling requests** in web servers.
# - **Simulations** (e.g., queuing models in operations research).

# 5. **Summary**:
'''
- A **queue** is a FIFO data structure where elements are added at the rear and removed from the front.
- **Common operations**:
    - `enqueue()`: Add an item to the rear of the queue.
    - `dequeue()`: Remove and return the front item.
    - `peek()`: View the front item without removing it.
    - `is_empty()`: Check if the queue is empty.
    - `size()`: Get the number of elements in the queue.
- **Implementation**: A queue can be implemented using `collections.deque` or a custom class to encapsulate queue operations.
- **Applications**: Queues are used in various scenarios such as task scheduling, BFS, simulations, and more.
'''

# ----------------------------------------------------------------------------------------------------------------------#
