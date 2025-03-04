# ----------------------------------------   Recursive Functions in Python   ----------------------------------------- #
#                                         -----------------------------------

"""
In Python, recursion is a technique in which a function calls itself in order to solve smaller instances of the
same problem. Recursive functions are useful for problems that can be broken down into simpler subproblems.

### Key Concepts:
- **Base Case**: A condition that stops the recursion by returning a result without making any further recursive calls.
  It prevents the function from calling itself indefinitely.
- **Recursive Case**: A part of the function that calls itself with a smaller or simpler problem, progressively
  breaking down the problem until the base case is reached.
- **Call Stack**: Each recursive function call is added to the call stack, and as each recursive call completes,
  it is removed from the stack, returning control to the previous function call.

### How Recursion Works:
1. The function calls itself with a modified argument (e.g., a smaller or simpler version of the original problem).
2. The recursive call continues until it reaches a base case, which stops further recursion.
3. The base case returns a value, and as the recursive calls "unwind," the results are returned back up the call stack.

"""


# 1. **Basic Recursive Function**:
# A simple example of a recursive function to calculate the factorial of a number.

def factorial(n):
	if n == 0:  # Base case
		return 1
	else:
		return n * factorial(n - 1)  # Recursive case


# Calling the recursive function
print(factorial(5))  # Output: 120


# Explanation:
# factorial(5) -> 5 * factorial(4)
# factorial(4) -> 4 * factorial(3)
# factorial(3) -> 3 * factorial(2)
# factorial(2) -> 2 * factorial(1)
# factorial(1) -> 1 * factorial(0)
# factorial(0) -> 1 (Base case)

# 2. **Recursive Function to Calculate Fibonacci Numbers**:
# The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
# A recursive function to calculate the nth Fibonacci number:

def fibonacci(n):
	if n == 0:  # Base case
		return 0
	elif n == 1:  # Base case
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case


# Calling the recursive function
print(fibonacci(6))  # Output: 8 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8)


# Explanation:
# fibonacci(6) -> fibonacci(5) + fibonacci(4)
# fibonacci(5) -> fibonacci(4) + fibonacci(3)
# fibonacci(4) -> fibonacci(3) + fibonacci(2)
# fibonacci(3) -> fibonacci(2) + fibonacci(1)
# fibonacci(2) -> fibonacci(1) + fibonacci(0)
# fibonacci(1) -> 1
# fibonacci(0) -> 0

# 3. **Recursive Function to Calculate Power of a Number**:
# A recursive function to calculate x raised to the power of y (x^y):

def power(x, y):
	if y == 0:  # Base case: x^0 is always 1
		return 1
	else:
		return x * power(x, y - 1)  # Recursive case: x^y = x * x^(y-1)


# Calling the recursive function
print(power(2, 3))  # Output: 8 (2^3 = 8)


# Explanation:
# power(2, 3) -> 2 * power(2, 2)
# power(2, 2) -> 2 * power(2, 1)
# power(2, 1) -> 2 * power(2, 0)
# power(2, 0) -> 1 (Base case)

# 4. **Recursive Function for Sum of List Elements**:
# A recursive function to calculate the sum of elements in a list:

def sum_of_list(lst):
	if len(lst) == 0:  # Base case: empty list
		return 0
	else:
		return lst[0] + sum_of_list(lst[1:])  # Recursive case: sum of first element + sum of the rest


# Calling the recursive function
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15


# Explanation:
# sum_of_list([1, 2, 3, 4, 5]) -> 1 + sum_of_list([2, 3, 4, 5])
# sum_of_list([2, 3, 4, 5]) -> 2 + sum_of_list([3, 4, 5])
# sum_of_list([3, 4, 5]) -> 3 + sum_of_list([4, 5])
# sum_of_list([4, 5]) -> 4 + sum_of_list([5])
# sum_of_list([5]) -> 5 + sum_of_list([]) -> 0 (Base case)

# 5. **Recursive Function for Depth-First Search (DFS) in a Graph**:
# A recursive function to perform Depth-First Search (DFS) on a graph (represented as an adjacency list):

def dfs(graph, node, visited=None):
	if visited is None:
		visited = set()
	visited.add(node)
	print(node)

	for neighbor in graph[node]:
		if neighbor not in visited:
			dfs(graph, neighbor, visited)  # Recursive call for unvisited neighbors

	return visited


# Example graph (adjacency list)
graph = {
	'A': ['B', 'C'],
	'B': ['A', 'D', 'E'],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B', 'F'],
	'F': ['C', 'E']
}

# Calling the DFS function
dfs(graph, 'A')


# Output (the order may vary based on recursion):
# A
# B
# D
# E
# F
# C

# 6. **Recursion and Tail Recursion**:
# Tail recursion is a form of recursion where the recursive call is the last operation in the function.
# Python does not optimize tail recursion, but it’s a useful concept in other languages.

# Example of Tail Recursion to calculate the factorial:

def tail_factorial(n, acc=1):
	if n == 0:  # Base case
		return acc
	else:
		return tail_factorial(n - 1, n * acc)  # Recursive case (tail call)


# Calling the tail-recursive function
print(tail_factorial(5))  # Output: 120


# Explanation:
# tail_factorial(5, 1) -> tail_factorial(4, 5)
# tail_factorial(4, 5) -> tail_factorial(3, 20)
# tail_factorial(3, 20) -> tail_factorial(2, 60)
# tail_factorial(2, 60) -> tail_factorial(1, 120)
# tail_factorial(1, 120) -> tail_factorial(0, 120)
# tail_factorial(0, 120) -> 120 (Base case)

# 7. **Recursive Sorting Algorithm (Merge Sort)**:
# A common example of recursion is sorting algorithms. Here's an implementation of **Merge Sort**:

def merge_sort(arr):
	if len(arr) <= 1:  # Base case: single element or empty list is already sorted
		return arr
	else:
		mid = len(arr) // 2  # Find the middle index
		left = merge_sort(arr[:mid])  # Recursively sort the left half
		right = merge_sort(arr[mid:])  # Recursively sort the right half

		# Merge the two sorted halves
		return merge(left, right)


def merge(left, right):
	result = []
	i = j = 0

	# Merge the two lists by comparing elements
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	# Append any remaining elements from the left or right list
	result.extend(left[i:])
	result.extend(right[j:])

	return result


# Calling the recursive merge sort function
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # Output: [3, 9, 10, 27, 38, 43, 82]

# 8. **Summary**:
'''
- **Recursion**: A method where a function calls itself to solve smaller subproblems.
- **Base Case**: A condition that terminates the recursion.
- **Recursive Case**: The part of the function that calls itself with a simpler version of the problem.
- **Call Stack**: A stack that stores the current state of each recursive call.
- **Common Examples**: Factorial, Fibonacci numbers, Depth-First Search (DFS), Merge Sort.
- **Tail Recursion**: A specific form of recursion where the recursive call is the last operation in the function. 
  Python does not optimize tail recursion, but it's an important concept.
'''

# ---------------------------------------------------------------------------------------------------------------------#
