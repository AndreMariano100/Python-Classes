# #######################################################
# # The FOR loop
#
# # Simple FOR loop
_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
for number in _set:
    print(number**2, end=', ')
# prints: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100,

# Simple FOR loop with the range() function
for j in range(1, 11):
    print(j**2, end=', ')
# prints: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100,

# Simple FOR loop with the range(len()) function
_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(_set)):
    print(_set[i]**2, end=', ')
# prints: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100,

# Sub set with the enumerate() function
for i, item in enumerate(_set):
    print('Index:', i, 'Item:', item**2)

# prints:
# Index: 0 Item: 1
# Index: 1 Item: 2
# Index: 2 Item: 3
# Index: 3 Item: 4
# Index: 4 Item: 5
# Index: 5 Item: 6
# Index: 6 Item: 7
# Index: 7 Item: 8
# Index: 8 Item: 9
# Index: 9 Item: 10

# Skipping numbers with the range() function
for x in range(0, 11, 2):
    print(x, end=', ')
# prints: 0, 2, 4, 6, 8, 10,

# FOR loop with ELSE
for x in range(3, 7):
    print(x, end=', ')
else:
    print('The list has finished')
# prints: 3, 4, 5, 6, The list has finished

# FOR loop with BREAK
for i in range(11):
    print(i, end=', ')
    if i > 5:
        break
# prints: 0, 1, 2, 3, 4, 5, 6,

# #######################################################
# Two Dimensional FOR loop
import random
for i in range(5):
    print('Line', i+1, end=': ')
    for j in range(5):
        print(random.randint(1, 10), end=', ')
    print()

# Creating a two dimensional array 10 x 10
array = []
for i in range(10):
    line = []
    for j in range(10):
        line.append(random.randint(1, 10))
    array.append(line)

for line in array:
    print(line)

"""
IMPORTANT
How to loop if you only want the elements of a set:
"""
fruits = ['apple', 'orange', 'banana', 'mango']
colors = ['red', 'orange', 'yellow', 'green']

for fruit in fruits:
    print(fruit)

"""
How to loop if you only want the positions of the elements of a set:
"""
for i in range(len(fruits)):
    print(fruits[i], colors[i])

"""
How to loop if you want the positions and the elements of a set:
"""
for i, fruit in enumerate(fruits):
    print('Position:', i, 'Fruit:', fruit)
