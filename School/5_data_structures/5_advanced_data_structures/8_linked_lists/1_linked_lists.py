# ----------------------------------------   Linked Lists in Python   -------------------------------------------------#
#                                         ----------------------------

"""
A **linked list** is a linear data structure where elements (called nodes) are connected by pointers.
    Each node contains:
1. **Data**: The value stored in the node.
2. **Next**: A pointer/reference to the next node in the sequence.

### Key Characteristics:
- **Dynamic size**: Unlike arrays, linked lists can grow or shrink dynamically.
- **Efficient insertions/deletions**: Inserting or deleting elements is faster
    compared to arrays (no shifting of elements).
- **Sequential access**: Unlike arrays, elements are not stored in contiguous memory locations.

### Types of Linked Lists:
1. **Singly Linked List**: Each node points to the next node.
2. **Doubly Linked List**: Each node has pointers to both the next and previous nodes.
3. **Circular Linked List**: The last node points back to the first node.
"""

# 1. **Singly Linked List**:
# A basic implementation of a singly linked list.

class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data  # Data held by the node
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    """Class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        """Add a node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Add a node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head

        # If the head node holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Traverse the list to find the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            return

        # Remove the node
        prev.next = current.next
        current = None

    def print_list(self):
        """Print all elements in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Using the SinglyLinkedList class:
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
print("Linked List after appending elements:")
sll.print_list()  # Output: 10 -> 20 -> 30 -> None

sll.prepend(5)
print("Linked List after prepending an element:")
sll.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None

sll.delete(20)
print("Linked List after deleting an element:")
sll.print_list()  # Output: 5 -> 10 -> 30 -> None


# 2. **Doubly Linked List**:
# A doubly linked list has pointers to both the next and previous nodes.

class DNode:
    """Class to represent a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node with the given data at the end of the list."""
        new_node = DNode(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head

        # Traverse to find the node to delete
        while current and current.data != key:
            current = current.next

        # If the node was not found
        if not current:
            return

        # If the node to be deleted is the head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            if current.next:  # If it's not the last node
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

        current = None

    def print_list(self):
        """Print all elements in the list."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Using the DoublyLinkedList class:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Doubly Linked List after appending elements:")
dll.print_list()  # Output: 10 <-> 20 <-> 30 <-> None

dll.delete(20)
print("Doubly Linked List after deleting an element:")
dll.print_list()  # Output: 10 <-> 30 <-> None


# 3. **Applications of Linked Lists**:
# Linked lists have several real-world applications in computer science, such as:
# - **Dynamic memory allocation**: Allocating memory as required.
# - **Implementing stacks and queues**: Using linked lists for dynamic structures.
# - **Undo functionality** in text editors: Storing changes as a linked list.
# - **Graph adjacency list representation**: Representing graphs efficiently.
# - **Polynomial manipulation**: Using linked lists to represent terms in a polynomial.


# 4. **Summary**:
'''
- A **linked list** is a linear data structure consisting of nodes connected by pointers.
- **Singly Linked List**: Each node points to the next node.
- **Doubly Linked List**: Each node has pointers to both the next and previous nodes.
- **Common operations**:
    - `append()`: Add a node at the end.
    - `prepend()`: Add a node at the beginning.
    - `delete()`: Remove a node by value.
    - `print_list()`: Traverse and print the list.
- **Applications**: Linked lists are used in dynamic data structures, undo functionality, 
    graph representation, and more.
'''

# ----------------------------------------------------------------------------------------------------------------------#
