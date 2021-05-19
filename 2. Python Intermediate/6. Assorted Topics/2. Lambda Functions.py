"""
Lambda Functions

Anonymous functions

"""

def double(x):
    return 2 * x


triple = lambda x: 3*x

print(double(3))
print(triple(3))

my_power = lambda x, y: x**y

print(my_power(2, 3))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(map(lambda x: x-1, a))
print(f'New List: {new_list}')
