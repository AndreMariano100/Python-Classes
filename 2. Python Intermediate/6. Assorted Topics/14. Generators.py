# Creating a sequence
import sys

# 1. Range is a generator ----------------------------------------------------------------------------------------------

# a = range(5)
# print(a)
# print(type(a))
# print(f'Size a: {sys.getsizeof(a)}')
# b = list(a)
# print(b)
# print(type(b))
# print(f'Size b: {sys.getsizeof(b)}')

# Range is not equivalent to a list
# You may create infinite sequences with no memory problem when using generators
# Replace range(5) with range(500) above and run the code again

# 2. Functions as generators -------------------------------------------------------------------------------------------

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# You can iterate over with a loop
# for i in infinite_sequence():
#     print(i)
#     input()

# Or you may use the next() method
# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
