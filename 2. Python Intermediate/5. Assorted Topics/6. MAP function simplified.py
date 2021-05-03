'''
MAP Function
    map(function, iterable)

    function : It is a function to which map passes each element of given iterable.
    iterable : It is a iterable which is to be mapped.

    The return value shall be passed to functions like list(), tuple(), set()

List Comprehension
    list = [expression for item in list]
    list = [x**2 for x in range(10)]
    up_list = [string.upper() for string in my_list]

    list = [expression for item in list if condition]
    list = [x**2 for x in range(10) if x % 2 == 0]
    up_list = [string.upper() for string in my_list if len(string) > 1]

'''
my_list = [1, 2, 3, 4, 5]


def my_power(x):
    return x**x


# To create a new list with all values passing through my_power()
new_list = []
for item in my_list:
    new_list.append(my_power(item))
print(f'My old list: {my_list}')
print(f'My new list: {new_list}')

# With map function
new_list_2 = list(map(my_power, my_list))
print(f'My new list 2: {new_list_2}')

# With list comprehension
new_list_3 = [my_power(x) for x in my_list]
print(f'My new list 3: {new_list_3}')

# Additional filters can be applied
new_list_4 = [my_power(x) for x in my_list if x % 2 == 0]
print(f'My new list 4: {new_list_4}')
