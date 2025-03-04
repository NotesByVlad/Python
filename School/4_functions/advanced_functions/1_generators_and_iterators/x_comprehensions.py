# Generator Function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

gen = count_up_to(5)
for num in gen:
    print(num)

# Generator Expression (similar to list comprehension)
gen_expr = (num ** 2 for num in range(1, 6))
print(list(gen_expr))  # Output: [1, 4, 9, 16, 25]

# Using generator with comprehension in a loop
numbers = [1, 2, 3, 4, 5]
gen_comprehension = (num * 2 for num in numbers if num % 2 == 0)
print(list(gen_comprehension))  # Output: [4, 8]
