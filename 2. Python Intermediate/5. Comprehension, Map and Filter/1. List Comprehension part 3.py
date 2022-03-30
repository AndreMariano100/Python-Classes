# List Comprehension Part 3

'''
WALRUS OPERATOR
LIST COMPREHENSION - when to use it
LIST COMPREHENSION PERFORMANCE
'''

# Walrus operator, known as Operador Leoncio in Brazil,
# allows you to assign a value to a variable while also returning the value.
# It simplifies the code, avoiding unnecessary repetition of arguments
# Example:
# whithout Walrus
start = input('Do you want to continue?(y/n) ')
print(start == 'y')

# whith Walrus
print((start := input('Do you want to continue?(y/n) ')) == 'y')

# List Comprehension - when to avoid
# List Comprehension may run slower or use more memory.
# So, if your code does not require better performance, you should
# emphasizes the code logic and understandability.
# If you need better performance, you should try which method will be
# more suitable for your needs.
# Example creating a matrix - easy to understand:
matrix = [[i for i in range(5)] for _ in range(5)]
print(matrix)

# But, this logic is not always so logic:
matrix_flat = [num for row in matrix for num in row]
print(matrix_flat)

# In this case, a loop would be clear
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat)

# The main point is to write codes that your team can easily understand and modify

# # For processing small lists, List Comprehension may perform pretty well
# my_sum = sum([i * i for i in range(10**3)])
# print(my_sum)

# # But List Comprehension has to create the whole list in order to process it,
# # and may not be practical for larger lists
# my_sum_LC = sum([i * i for i in range(10**8)])
# print(my_sum_LC)

# # For these applications, the adoption of generators may be more adequate
# # generator creates an iterable that updates last value every time is necessary,
# # without the need to allocate a large amount of memory
# my_sum_G = sum(i * i for i in range(10**8))
# print(my_sum_G)

# # map function could also be used with a performance similar to the generator
# my_sum_M = sum(map(lambda i: i*i, range(10**8)))
# print(my_sum_M)

# But, how to chose which would be better for my application?
import timeit

def my_sum_LC():
    sum([i * i for i in range(10**7)])

def my_sum_G():
    sum(i * i for i in range(10**7))

def my_sum_M():
    sum(map(lambda i: i*i, range(10**7)))

time_LC = timeit.timeit(my_sum_LC, number=1)
print(time_LC)
time_generator = timeit.timeit(my_sum_G, number=1)
print(time_generator)
time_map = timeit.timeit(my_sum_M, number=1)
print(time_map)