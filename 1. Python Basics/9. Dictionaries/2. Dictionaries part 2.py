# Dictionaries Exercises

# 1. Sorting

if True:
    my_dict = {1: 69,
               2: 64,
               3: 76,
               4: 23,
               5: 65,
               6: 34}

    # 1.1. Sort by the key, showing the keys
    for i in sorted(my_dict.keys()):
        print(i, end=" ")
    print()

    # 1.2. Sort by the key, showing the keys and values
    for i in sorted(my_dict.keys()):
        print((i, my_dict[i]), end=' ')
    print()

    # 1.3. Sort by the value, showing the values
    for i in sorted(my_dict.values()):
        print(i, end=" ")
    print()

    # 1.4. Sorting the dictionary by the values
    for item in sorted(my_dict.values()):
        for key, value in my_dict.items():
            if value == item:
                print((value, key), end=' ')

    print()

# 2. Handling missing keys
if True:
    my_dict = {'A': 1, 'B': 2}

    # 2.1 Using get() method and default value
    # value = my_dict['C']
    print(my_dict.get('C'))
    print(my_dict.get('C', 'Not Found'))

    # 2.2 Using setdefault() method and default value
    print(my_dict.setdefault('C', 3))
    print(my_dict)
    print(my_dict.setdefault('B', 0))
    print(my_dict)

    # 2.3 With Try-Except Block
    try:
        value = my_dict['D']
    except KeyError:
        my_dict['D'] = 4
        print(my_dict)
# 3. Dictionary with lists or tuples
if True:
    my_dict = {'line_1': ('material_1', 'temperature_1', 'pressure_1'),
               'line_2': ('material_2', 'temperature_2', 'pressure_2'),
               'line_3': ('material_3', 'temperature_3', 'pressure_3')}

    # 3.1 Accessing all values
    for data in my_dict.keys():
        print(data, '/', my_dict[data])

    # 3.2 Accessing specific data
    for data in my_dict.keys():
        print(f'Material: {data} / {my_dict[data][0]}')

# 4. Dictionary with dictionaries
if True:
    my_dict = {'line_1': {'SPEC': 'B11', 'Max Temperature': '150', 'Max Pressure_1': '20'},
               'line_2': {'SPEC': 'B3', 'Max Temperature': '60', 'Max Pressure_1': '20'},
               'line_3': {'SPEC': 'B14', 'Max Temperature': '90', 'Max Pressure_1': '20'}}

    # 4.1 Accessing all values
    for data in my_dict.keys():
        print(data, '/', my_dict[data])

    # 4.2 Accessing specific data
    for data in my_dict.keys():
        print(f'Line: {data} / Max Temperature: {my_dict[data]["Max Temperature"]}')
