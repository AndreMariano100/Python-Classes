'''
FILTER function
    filter(function, sequence)

    function: function that tests if each element of a sequence true or not.
    sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
    Returns: returns an iterator that is already filtered.

'''

def double(x):
    return 2*x

def is_even(x):
    return x % 2 == 0

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The function to filter must return True or False
new_list = list(filter(is_even, my_list))
print(f'New list: {new_list}')

new_list_2 = list(map(double, my_list))
print(f'New list 2: {new_list_2}')

new_list_3 = list(map(double, (filter(is_even, my_list))))
print(f'New list 3: {new_list_3}')
