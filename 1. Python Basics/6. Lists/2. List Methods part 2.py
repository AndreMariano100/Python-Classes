import os
#########################################################################
# Iterating
#
# c_list = ['Africa', 'Europe', 'Asia', 'Americas', 'New World']
#
# for i in range(len(c_list)):
#     print('Item number: ', i, ' Item: ', c_list[i])
#
# for item in c_list:
#     print('Item number: ', c_list.index(item), ' Item: ', item)
#
# for i, item in enumerate(c_list):
#     print('Item number: ', i, ' Item: ', item)

####################################################################
# Lists with 2 dimensions - nested lists
# Regular matrix
line_1 = [1, 2, 3, 4, 5]
line_2 = [6, 7, 8, 9, 10]
line_3 = [11, 12, 13, 14, 15]
line_4 = [16, 17, 18, 19, 20]
line_5 = [21, 22, 23, 24, 25]

matrix = [line_1, line_2, line_3, line_4, line_5]
for line in matrix:
    print(line)
print(f'Matrix: {matrix}')


# Null Matrix
single_line = 10*[0]
null_matrix = 10*[single_line]

# null_matrix = 10*[10*[0]]

for lines in null_matrix:
    print(lines)

# ID Matrix
id_matrix = []
for i in range(10):
    line = []
    for j in range(10):
        if i == j:
            line.append('1')
        else:
            line.append('0')
    id_matrix.append(line)

for lines in id_matrix:
    print(lines)

user = input('Work with matrix (y/n)?')
if user == 'n':
    pass
else:
    # Accessing Values
    matrix = []
    for i in range(5):
        line = []
        for j in range(5):
            line.append('0')
        matrix.append(line)

    while True:
        clear = lambda: os.system('cls')
        for lines in matrix:
            print(lines)

        _line = input('Matrix Line (x to quit):')
        if _line == 'x':
            break
        else:
            _line = int(_line)-1

        _column = input('Matrix Column (x to quit):')
        if _column == 'x':
            break
        else:
            _column = int(_column)-1

        value = input('New Value (x do quit):')
        if value == 'x':
            break
        matrix[_line][_column] = value
