# -----------------------------------------------------
x = -1

if x < 0:
    raise Exception('Negative numbers not allowed')

# -----------------------------------------------------
# name = 0
#
# if type(name) != str:
#     raise TypeError('Only string type permitted')
# else:
#     print('"name" is indeed a string')

# -----------------------------------------------------
# class MyCustomError(Exception):
#     pass
#
# value = -1
#
# if value < 0:
#     raise MyCustomError('Value is negative')


# # -----------------------------------------------------
# class MyCustomError(Exception):
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print('calling str')
#         if self.message:
#             return f'MyCustomError, {self.message}'
#         else:
#             return 'MyCustomError has been raised'
#
#
# raise MyCustomError
# raise MyCustomError('We have a problem')

# ----------------------------------------------------------------------------------------------------------------------
def check_if_odd(x):
    assert not x % 2, 'Number is not even'


def check_divide(x):
    assert int(x) != 0, 'Cannot divide by Zero'


number = 3

try:
    check_if_odd(number)
    check_divide(number)

except AssertionError as error:
    print(error)

else:
    print('Number is even and not zero')
