#----------------------------------------   Adding and Removing Elements in a Set   -----------------------------#
#                                            ------------------------

"""
Sets are mutable, meaning you can add and remove elements after creation. Sets are also unique, so duplicates are not allowed.

Key Points:
1. Add elements using add() method.
2. Remove elements using remove() or discard() methods.
3. Pop a random element using pop().
4. Clear all elements with clear().
"""

# Example Set
my_set = {10, 20, 30, 40, 50}

# 1. Adding Elements
"""
Add an element to the set using add().
"""
print("Original set:", my_set)
my_set.add(60)  # Adding an element
print("Set after adding 60:", my_set)

# 2. Removing Elements
"""
Remove an element from the set using remove() (raises KeyError if element is not present) or discard() (does not raise an error).
"""
my_set.remove(20)  # Removes 20 from the set
print("Set after removing 20:", my_set)

# 3. Discarding Elements (doesn't raise an error if element is not found)
my_set.discard(30)  # Removes 30 if present
print("Set after discarding 30:", my_set)

# 4. Popping an Element (removes and returns a random element)
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# 5. Clearing the Set
my_set.clear()  # Removes all elements
print("Set after clearing:", my_set)

#----------------------------------------------------------------------------------------------------------------------#
