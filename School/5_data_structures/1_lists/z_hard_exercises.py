# ---------------------------------- List exercises (hard) ----------------------------------------------------------- #

# Advanced-level exercises

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# TODO 1. Write a function that takes a list as input and returns the list with every second element
#  (starting from index 1). Use list slicing in the function. ----------------------------------------------------------

# TODO 2. Write a function that takes a list of integers and returns the list sorted in descending order without
#  modifying the original list. Use the `sorted()` function. -----------------------------------------------------------

# TODO 3. Write a function that takes a list of numbers and returns a new list where all elements are multiplied
#  by their index. Use list comprehension. -----------------------------------------------------------------------------

# TODO 4. Given the list `my_list`, use list comprehension to create a new list that contains the squares
#  of the numbers that are divisible by 5. -----------------------------------------------------------------------------

# TODO 5. Write a function that accepts a list of strings and returns the longest string in the list.
#  If there are multiple longest strings, return the first one. --------------------------------------------------------

# TODO 6. Write a function that removes all occurrences of a specified element from a list. The function
#  should take two parameters: the list and the element to remove. -----------------------------------------------------

# TODO 7. Write a function that removes all duplicate elements from a list while maintaining the original
#  order of elements. Use `set()` and list comprehension. --------------------------------------------------------------

# TODO 8. Write a function that rotates a list by `n` places to the right. The function should handle both
#  positive and negative values for `n`. (Use slicing and modulus). ----------------------------------------------------

# TODO 9. Write a function that takes two lists and returns a list of the elements that are common between
#  both lists, without duplicates. Use set intersection. ---------------------------------------------------------------

# TODO 10. Write a function that accepts a list of integers and returns the sum of all even numbers and the
#  sum of all odd numbers as a tuple. ----------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------- #

# Working with Lists of Strings (Advanced)

names = ['John', 'Andrew', 'Carl', 'David', 'Megan', 'Sarah', 'Kate']

# TODO 1. Write a function that returns a list of strings that contain the letter 'a' (case insensitive). --------------

# TODO 2. Write a function that accepts a list of strings and returns a list with each string capitalized in the list.--

# TODO 3. Write a function that returns a list of strings where the length of each string is greater than or equal to 5.

# TODO 4. Write a function that counts how many strings in the list contain the substring 'an' (case-insensitive). -----

# -------------------------------------------------------------------------------------------------------------------- #

# Complex List Operations

numbers = [5, 3, 8, 6, 1, 12, 7, 4, 2, 9]

# TODO 1. Write a function that finds and returns the three smallest numbers in the list, without modifying
#  the original list. --------------------------------------------------------------------------------------------------

# TODO 2. Write a function that takes two lists and returns a list of elements that are unique to each
#  list (i.e., not present in both lists). Use `symmetric_difference()`. -----------------------------------------------

# TODO 3. Write a function that takes a list and returns a list where each element is multiplied by 3 and then squared.
#  Use `map()` and `lambda`. -------------------------------------------------------------------------------------------

# TODO 4. Write a function that rotates a list `n` times to the left. Use slicing and modulus for performance
#  optimization. -------------------------------------------------------------------------------------------------------

# TODO 5. Write a function that accepts a list of numbers and removes any number that appears more than once in
#  the list, leaving only unique numbers. ------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------- #

# Nested Lists (Advanced)

nested_list = [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]]

# TODO 1. Write a function that takes a nested list and returns a list of the first elements (the characters). ---------

# TODO 2. Write a function that takes a nested list of dictionaries and returns a list of values associated with the
#  key 'name'. Assume the dictionaries have the same structure. --------------------------------------------------------

# TODO 3. Given a nested list, use list comprehension to flatten the list into a one-dimensional list. -----------------

# TODO 4. Write a function that accepts a nested list and a value, and checks whether the value exists in any of
#  the sublist. If it does, return the index of that sublist. ---------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------- #

# List Performance and Optimization

my_numbers = [i for i in range(1, 100001)]  # A list with 100,000 elements.

# TODO 1. Use `timeit` to measure the performance of list comprehension vs. `for` loop for squaring each number
#  in the list. Compare the results. -----------------------------------------------------------------------------------

# TODO 2. Use `heapq` module to find the 5 smallest numbers in the list efficiently. -----------------------------------

# TODO 3. Write a function that takes a list of numbers and returns the average of the numbers, excluding the
#  highest and lowest values. ------------------------------------------------------------------------------------------

# TODO 4. Write a function that takes two lists of numbers and returns the sum of all elements that appear
#  in both lists, ignoring duplicates. ---------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------- #

# Miscellaneous

# TODO 1. Write a function that takes a list of strings and returns the string with the most vowels.
#  If there is a tie, return the first one. ----------------------------------------------------------------------------

# TODO 2. Write a function that generates all combinations of two lists, combining each element from the first
#  list with every element from the second list. -----------------------------------------------------------------------

# TODO 3. Write a function that merges two sorted lists into one sorted list. Do not use the `sort()` method. ----------

# -------------------------------------------------------------------------------------------------------------------- #
