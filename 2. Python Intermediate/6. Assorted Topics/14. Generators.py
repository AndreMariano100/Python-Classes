# Creating a sequence
import sys

# 1. Range is a generator ----------------------------------------------------------------------------------------------

a = range(30)
print(a)
print(type(a))
print(f'Size a: {sys.getsizeof(a)}')

# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(b)
print(type(b))
print(f'Size b: {sys.getsizeof(b)}')

# j = iter(b)
# print(next(j))
# print(next(j))
# print(next(j))

# Range is not equivalent to a list
# You may create infinite sequences with no memory problem when using generators
# Replace range(5) with range(500) above and run the code again

# 2. Functions as generators -------------------------------------------------------------------------------------------

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

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
