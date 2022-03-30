# List Comprehension Part 1

'''
List Comprehension is an  elegant coding tool for creating list that allows to resume some
features in only one line.
It may be more useful and clean in some applications, but it must be used with caution once
it may turn reading and interpretation more difficult and it may also not be the most efficient
method to use.
'''
# We already see some methods to create a list:
# # Explicit:
my_sq_explicit = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(my_sq_explicit)

# # Applying loop for
my_sq_for = []
for base in range(10):
    my_sq_for.append(base*base)
print(my_sq_for)

# Another option is to create a map. map() function is based on functional programming,
# which means that it's based on pure functions in which outputs are derived from inputs
# without side effects. On map() is input an iterable (list or dict) and a function which
# will be applied for each item and the return is an object that can be easily turned into
# a list by the command list().
# # Example with map
my_base_list = [0,1,2,3,4,5,6,7,8,9]
def sq_function(base):
    return base*base

my_sq_map = list(map(sq_function,my_base_list))
print(my_sq_map)

# List comprehension may be the most pythonic way to create such a list:
my_sq_LC = [base * base for base in range(10)]
print(my_sq_LC)

# Although LC may be similar to map, it returns the list directly and map requires
# the additional list command.

# Python also has the functionality to create set and dictionary in a similar
# manner as List Comprehension

# Set Comprehension is quite the same as List Comprehension,
# but it does not ensure the proper other of the elements
my_sq_SC = {base * base for base in range(10)}
print(my_sq_SC)

# Dictionary Comprehension is similar, but you need to define a key
my_sq_DC = {i: i*i for i in range(10)}
print(my_sq_DC)

my_keys = ('a', 'b', 'c')
my_values = (1, 2, 3)
my_dict_1 = dict(zip(my_keys, my_values))
my_dict_2 = {k: v for (k, v) in zip(my_keys, my_values)}
print(my_dict_1)
print(my_dict_2)