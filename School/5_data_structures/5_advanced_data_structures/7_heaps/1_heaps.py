# ----------------------------------------   Heaps in Python   ----------------------------------------#
#                                        ------------------------------------

'''
A **heap** is a special tree-based data structure that satisfies the **heap property**:
- For a **max heap**: The value of each parent node is greater than or equal to its children.
- For a **min heap**: The value of each parent node is less than or equal to its children.

### Key Concepts:
- A heap is usually implemented as a binary heap.
- A heap is commonly represented using an array (or list in Python).
- **Heapify**: The process of rearranging elements to maintain the heap property.
- Heaps are commonly used to implement **priority queues** and for **sorting** (heap sort).

### Python provides the `heapq` module, which implements a min-heap by default.
'''

# 1. **Basic Heap Operations Using `heapq`**:
import heapq

# Creating a min-heap:
heap = []

# Pushing elements onto the heap (insertion):
heapq.heappush(heap, 10)  # Add 10 to the heap
heapq.heappush(heap, 5)   # Add 5 to the heap
heapq.heappush(heap, 20)  # Add 20 to the heap
heapq.heappush(heap, 1)   # Add 1 to the heap
print("Heap after pushes:", heap)  # Output: [1, 5, 20, 10]

# Popping the smallest element (root) from the heap:
smallest = heapq.heappop(heap)
print("Popped smallest element:", smallest)  # Output: 1
print("Heap after pop:", heap)  # Output: [5, 10, 20]

# Peeking at the smallest element without removing it:
smallest = heap[0]
print("Smallest element (peek):", smallest)  # Output: 5

# Converting a list into a heap:
nums = [8, 3, 10, 1, 5]
heapq.heapify(nums)  # Transform the list into a heap
print("Heapified list:", nums)  # Output: [1, 3, 10, 8, 5]

# Explanation:
# - `heappush`: Inserts an element while maintaining the heap property.
# - `heappop`: Removes and returns the smallest element.
# - `heapify`: Rearranges a list into a valid heap.

# 2. **Max Heap Implementation**:
# Since `heapq` only supports min-heaps, a max-heap can be implemented by inverting the values.

# Creating a max-heap:
max_heap = []
heapq.heappush(max_heap, -10)  # Push -10 (invert sign for max-heap)
heapq.heappush(max_heap, -5)   # Push -5
heapq.heappush(max_heap, -20)  # Push -20
heapq.heappush(max_heap, -1)   # Push -1
print("Max-Heap after pushes:", [-x for x in max_heap])  # Output: [20, 10, 5, 1]

# Popping the largest element:
largest = -heapq.heappop(max_heap)  # Invert sign again to get the original value
print("Popped largest element:", largest)  # Output: 20
print("Max-Heap after pop:", [-x for x in max_heap])  # Output: [10, 1, 5]

# Explanation:
# - By pushing `-value` instead of `value`, we reverse the order in a min-heap, effectively creating a max-heap.

# 3. **Heap Implementation Using a Class**:
# A heap can also be implemented using a custom class for more flexibility.

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Insert an item into the heap"""
        heapq.heappush(self.heap, item)

    def pop(self):
        """Remove and return the smallest item"""
        if not self.is_empty():
            return heapq.heappop(self.heap)
        else:
            raise IndexError("pop from empty heap")

    def peek(self):
        """Return the smallest item without removing it"""
        if not self.is_empty():
            return self.heap[0]
        else:
            raise IndexError("peek from empty heap")

    def is_empty(self):
        """Check if the heap is empty"""
        return len(self.heap) == 0

    def size(self):
        """Return the number of items in the heap"""
        return len(self.heap)


# Using the MinHeap class:
heap = MinHeap()
heap.push(10)
heap.push(5)
heap.push(20)
heap.push(1)
print("Heap after pushes:", heap.heap)  # Output: [1, 5, 20, 10]

smallest = heap.pop()
print("Popped smallest element:", smallest)  # Output: 1
print("Heap after pop:", heap.heap)  # Output: [5, 10, 20]

print("Smallest element (peek):", heap.peek())  # Output: 5
print("Is heap empty?", heap.is_empty())  # Output: False
print("Size of heap:", heap.size())  # Output: 3


# Explanation:
# This `MinHeap` class encapsulates heap operations and allows for more controlled usage.
# Methods include `push()`, `pop()`, `peek()`, `is_empty()`, and `size()`.

# 4. **Heap Applications: Priority Queue**:
# Heaps are commonly used to implement priority queues.

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        """Add an item with a given priority"""
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return the item with the highest priority (lowest priority value)"""
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        else:
            raise IndexError("pop from empty priority queue")

    def peek(self):
        """Return the item with the highest priority without removing it"""
        if not self.is_empty():
            return self.heap[0][1]
        else:
            raise IndexError("peek from empty priority queue")

    def is_empty(self):
        """Check if the priority queue is empty"""
        return len(self.heap) == 0


# Using the PriorityQueue class:
pq = PriorityQueue()
pq.push(3, "Task 3")
pq.push(1, "Task 1")
pq.push(2, "Task 2")

print("Popped item with highest priority:", pq.pop())  # Output: "Task 1"
print("Peek item with highest priority:", pq.peek())  # Output: "Task 2"


# Explanation:
# - Priority queues use heaps to maintain efficient access to the item with the highest priority.

# 5. **Applications of Heaps**:
# Heaps have several real-world applications in computer science, such as:
# - **Priority queues** (e.g., task scheduling, Dijkstra's algorithm).
# - **Heap sort** (a sorting algorithm based on heaps).
# - **Finding the k largest/smallest elements** in a collection.
# - **Merging sorted lists**.
# - **Median finding** in a data stream.

# 6. **Summary**:
'''
- A **heap** is a binary tree structure that satisfies the heap property:
    - **Min-Heap**: Parent node is smaller than its children.
    - **Max-Heap**: Parent node is larger than its children.
- **Common operations**:
    - `push()`: Insert an element into the heap.
    - `pop()`: Remove and return the root element.
    - `peek()`: View the root element without removing it.
    - `heapify()`: Transform a list into a valid heap.
- **Applications**: Heaps are used in priority queues, sorting, and more.
'''

# ----------------------------------------------------------------------------------------------------------------------#
