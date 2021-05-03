"""
Python’s zip() function behaves as follows:
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences
or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument,
it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
"""
import time

# Example 1 - zipping lists ---------------------------------
print('Example 1:')
my_numbers = [1, 2, 3]
my_letters = ['a', 'b', 'c']
zipped = zip(my_numbers, my_letters)
print(zipped)
print(type(zipped))
print(list(zipped))
input()
print('\n' * 2)


# Example 2 - zipping sets -----------------------------------
print('Example 2:')
my_set_1 = {2, 3, 1}
my_set_2 = {'b', 'a', 'c'}
print(list(zip(my_set_1, my_set_2)))
time.sleep(2)
print('\n' * 2)


# Example 3 - passing one argument ---------------------------
print('Example 3:')
my_list = [1, 2, 3]
zipped = zip(my_list)
print(list(zipped))
print('\n' * 2)


# Example 4 - passing arguments of unequal length -------------
print('Example 4:')
print(list(zip(range(5), range(100))))
print('\n' * 2)


# Example 5 - trailing / unmatched values --------------------
print('Example 5:')
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
print('\n' * 2)


# Example 6 ---------------------------------------------------
print('Example 6:')
print(list(zip(range(3), 'ABCD')))
print('\n' * 2)


# Example 7 - Traversing Lists in Parallel
print('Example 7:')
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for let, num in zip(letters, numbers):
    print(f'Letter: {let}')
    print(f'Number: {num}')

print('\n' * 2)


# Example 8 - Traversing Dictionaries in Parallel -------------
print('Example 8:')
dict_one = {'name': 'Andre', 'last_name': 'Mariano', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

print(list(zip(dict_one.items(), dict_two.items())))
print('\n' * 2)


# Example 9 - Unzipping a Sequence (unpacking operator *) ------
print('Example 9:')
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print('Numbers:', numbers)
print('Letters:', letters)
print('\n' * 2)


# Example 10 - Sorting in Parallel ----------------------------
print('Example 10:')
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]

data1 = list(zip(letters, numbers))
print(f'Data 1 {data1}')
data1.sort()
print('Sorted by letters: ', data1)  # Sort by letters --------

data2 = list(zip(numbers, letters))
data2.sort()  # Sort by numbers
print('Sorted by numbers: ', data2)

data3 = sorted(zip(letters, numbers))  # Sort by letters ------
print('Sorted by letters - method 2:', data3)
print('\n' * 2)


# Example 11 - Calculating in Pairs ----------------------------
print('Example 11:')
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')

print('\n' * 2)


# Example 12 - Building Dictionaries ---------------------------
print('Example 12:')
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(a_dict)

# Updating dictionaries
new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(a_dict)

