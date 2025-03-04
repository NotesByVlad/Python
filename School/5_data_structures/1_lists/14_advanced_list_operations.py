#----------------------------------------   Advanced List Operations   --------------------------------------------#
#                                               ----------------------------

"""
Advanced operations on lists allow for more complex manipulations like sorting, filtering, and mapping functions.

Key Points:
1. Use `map()` for applying a function to each element.
2. Use `filter()` to filter elements based on a condition.
3. Use `sorted()` to sort lists with custom criteria.
"""

#----------------------------------------------------------------------------------------------------------------------#

# Example List
my_list = [1, 2, 3, 4, 5]

# 1. Using map() to Apply a Function to Each Element
"""
The map() function applies a given function to each item in the list.
"""
squared_numbers = list(map(lambda x: x**2, my_list))
print("Squared numbers:", squared_numbers)

# 2. Using filter() to Filter Elements Based on a Condition
"""
The filter() function filters elements based on a condition.
"""
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print("Even numbers:", even_numbers)

# 3. Sorting with Custom Criteria
"""
You can sort a list using custom criteria with the `key` parameter.
"""
sorted_by_reverse = sorted(my_list, reverse=True)
print("List sorted in descending order:", sorted_by_reverse)

#----------------------------------------------------------------------------------------------------------------------#
