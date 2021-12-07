# IS / IS NOT
list_1 = [0, 1, 2, 3]
list_2 = [0, 1, 2, 3]

if list_2 is list_1:
    print('They are the same list')
    print(f'\tlist 1: {list_1}')
    print(f'\tlist 2: {list_2}')
else:
    print('They are not the same!!!!')
    print(f'\tlist 1: {list_1}')
    print(f'\tlist 2: {list_2}')

if list_2 == list_1:
    print('They are equal')
else:
    print('They are different')
