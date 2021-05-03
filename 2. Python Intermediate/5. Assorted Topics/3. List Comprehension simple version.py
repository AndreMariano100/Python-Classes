# List Comprehensions

"""
Transforms one list in another list.

or...

Transforms one iterable in another iterable.
"""

numbers = [2, 1, 3, 4, 7, 11]

# Make a new list with the square of numbers
new_list_1 = []
for n in numbers:
    new_list_1.append(n**2)
print(f'New List 1: {new_list_1}')

# Or make a new list with the square of odd numbers
new_list_2 = []
for n in numbers:
    if n % 2 == 1:
        new_list_2.append(n**2)
print(f'New List 2: {new_list_2}')

# Using list comprehensions
# new_iterable = [operation(item) for item in original_iterable if condition]

new_list_3 = [n**2 for n in numbers]
print(f'New List 3: {new_list_3}')

new_list_4 = [n**2 for n in numbers if n % 2 == 1]
print(f'New List 4: {new_list_4}')

# Breaking comprehensions
new_list_5 = [
    n**2
    for n in numbers
    if n % 2 == 1]

# You can use two for loops in list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

value_1 = []
for row in matrix:
    for item in row:
        value_1.append(item)

value_2 = [item for row in matrix for item in row]
print(f'Value 1 {value_1}')
print(f'Value 2 {value_2}')

