#----------------------------------------   Lists in Python   ---------------------------------------------------------#
#                                        -----------------------

"""
In programming, a list is a collection of items (elements) that can be of
different data types, stored in a single variable. Lists are one of the most
common and versatile data structures in Python.

Lists are mutable, meaning their content can be changed after they are created.
They are enclosed in square brackets `[]`, and elements are separated by commas.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Lists:
'''
Ordered: Lists maintain the order of elements, and each element can be accessed using its index.
Mutable: Lists can be modified after creation (adding, removing, or changing elements).
Heterogeneous: A list can contain elements of different data types (e.g., integers, strings, other lists).
Indexable and Iterable: Lists allow access to individual elements using their index and support iteration.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. List Initialization
list1 = [1, 2, 3, 4, 5]
list2 = ['Python', 'is', 'fun']
list3 = [1, 'Python', 3.14, [10, 20]]

# Printing the lists
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

# 2. List Length
print("\nLength of List 1:", len(list1))
print("Length of List 2:", len(list2))

# 3. Accessing Elements
print("\nFirst Element of List 1:", list1[0])  # Access by index
print("Last Element of List 2:", list2[-1])   # Access by negative index

# 4. Modifying Elements
list1[2] = 10  # Changing the third element
print("\nModified List 1:", list1)

# 5. Adding Elements
list1.append(6)  # Add element to the end
list2.insert(1, 'really')  # Insert at a specific position
print("\nList 1 after Append:", list1)
print("List 2 after Insert:", list2)

# 6. Removing Elements
list1.pop()  # Remove the last element
list2.remove('really')  # Remove a specific element by value
print("\nList 1 after Pop:", list1)
print("List 2 after Remove:", list2)

# 7. List Concatenation
combined_list = list1 + list3
print("\nConcatenated List:", combined_list)

# 8. List Repetition
repeated_list = list2 * 2
print("\nRepeated List 2 (2 times):", repeated_list)

# 9. List Slicing
sublist = list1[1:4]  # Extract a sublist (elements from index 1 to 3)
print("\nSliced List 1 (from index 1 to 3):", sublist)

# 10. Iterating Over a List
print("\nIterating over List 1:")
for element in list1:
    print(element, end=" ")

# 11. List Methods
list1.reverse()  # Reverse the order of elements
sorted_list = sorted(list3, key=str)  # Sorting the list (with mixed types, key=str)
list1.extend([7, 8, 9])  # Extend list with another list
list_copy = list1.copy()  # Create a copy of the list
list1.clear()  # Clear all elements from the list

print("\n\nReversed List 1:", list1)
print("Sorted List 3:", sorted_list)
print("Extended List 1:", list_copy)
print("Cleared List 1:", list1)

# 12. Checking Membership
print("\nIs 'Python' in List 2?", 'Python' in list2)
print("Is 10 in List 1?", 10 in list1)

# 13. Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("\nNested List:", nested_list)
print("Accessing Element (Row 2, Column 1):", nested_list[1][0])

# 14. List Comprehension
squared_list = [x**2 for x in range(5)]  # List of squares of numbers 0-4
print("\nList Comprehension (Squares):", squared_list)

# 15. Using `enumerate`
print("\nEnumerating List 2:")
for index, value in enumerate(list2):
    print(f"Index {index}: {value}")

# 16. Working with Different Data Types
mixed_list = [True, "Hello", 42, 3.14]
print("\nMixed Data Type List:", mixed_list)

#----------------------------------------------------------------------------------------------------------------------#