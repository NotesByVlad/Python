#----------------------------------------   Iterating Over a Tuple   --------------------------------------------#
#                                            ------------------------

"""
You can iterate over a tuple using a for loop or using the enumerate function to get both index and value.

Key Points:
1. Use a for loop to iterate through each element.
2. Use enumerate() to get the index along with the value.
"""

# Example Tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Iterating Using a For Loop
"""
Iterate through each element in the tuple.
"""
print("Original tuple:", my_tuple)
for item in my_tuple:
    print(item)

# 2. Using enumerate() to Get Index and Value
"""
Iterate through each element and its index using enumerate.
"""
for index, value in enumerate(my_tuple):
    print(f"Index {index}: Value {value}")

#----------------------------------------------------------------------------------------------------------------------#
