#----------------------------------------   Rearranging Elements in a List   --------------------------------------------#
#                                               ----------------------------

"""
Rearranging elements in a list involves altering the order of elements. Python provides built-in methods to sort,
reverse, or rearrange elements as needed.

Key Points:
1. Use `sort()` to sort the list in ascending order (in-place).
2. Use `sorted()` to create a new sorted list (does not modify the original).
3. Use `reverse()` to reverse the order of elements in the list (in-place).
4. Use slicing with `[::-1]` to create a reversed copy of the list.
5. Use custom sort keys with `sort()` or `sorted()` for advanced sorting.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [50, 20, 40, 10, 30]

# 1. Sorting in Ascending Order with sort()
"""
The sort() method sorts the list in ascending order (in-place).
"""
my_list.sort()
print("List sorted in ascending order:", my_list)

# 2. Sorting in Descending Order with sort()
"""
The sort() method can take a `reverse=True` argument to sort in descending order.
"""
my_list.sort(reverse=True)
print("List sorted in descending order:", my_list)

# 3. Using sorted() to Create a New Sorted List
"""
The sorted() function returns a new sorted list and leaves the original list unchanged.
"""
original_list = [50, 20, 40, 10, 30]
sorted_list = sorted(original_list)
print("Original list:", original_list)
print("New sorted list:", sorted_list)

# 4. Reversing the Order with reverse()
"""
The reverse() method reverses the elements of the list in-place.
"""
my_list.reverse()
print("List after reversing:", my_list)

# 5. Creating a Reversed Copy with Slicing
"""
Use slicing to create a reversed copy of the list without modifying the original.
"""
reversed_list = my_list[::-1]
print("Reversed copy of the list:", reversed_list)

# 6. Custom Sorting with sort() and sorted()
"""
You can sort a list using a custom key function by passing the `key` argument.
"""
# Sort by absolute value
custom_list = [-10, 15, -20, 5, 0]
custom_list.sort(key=abs)
print("List sorted by absolute value:", custom_list)

# Use sorted() with a lambda for string length sorting
string_list = ["apple", "kiwi", "banana", "cherry"]
sorted_strings = sorted(string_list, key=lambda x: len(x))
print("Strings sorted by length:", sorted_strings)

#----------------------------------------------------------------------------------------------------------------------#
