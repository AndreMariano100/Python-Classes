# Python Lists Methods
'''

# >>> dir(list)

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
 '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    Method      Description
    append()    Adds an element at the end of the list
    clear()     Removes all the elements from the list
    copy()      Returns a copy of the list
    count()     Returns the number of elements with the specified value
    extend()    Add the elements of a list (or any iterable), to the end of the current list
    index()     Returns the index of the first element with the specified value
    insert()    Adds an element at the specified position
    pop()       Removes the element at the specified position
    remove()    Removes the first item with the specified value
    reverse()   Reverses the order of the list
    sort()      Sorts the list
'''
####################################################################
# Creating Lists
print()
print('Creating lists')
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(f'My list 1:{my_list}')

my_list_2 = [10, 20, 30]
print(f'My list 2:{my_list_2}')

# Creating with a loop
my_list_3 = []
for i in range(1, 4):
    my_list_3.append(i*10)
print(f'My list 3:{my_list_3}')

# Create an empty list with multiplication
my_list_4 = 3*[0]
my_list_4[0] = 10
my_list_4[1] = 20
my_list_4[2] = 30
print(f'My list 4:{my_list_4}')
print()
my_list_5 = 3*[0]
for i in range(3):
    my_list_5[i] = 10 * i

########################################################################
# Python Built in Methods
print('Python Built-In Methods')
my_list = [10, 5, 14, 22, 5, 16]
print(f'List = {my_list}')
print('Len:', len(my_list))
print('Sum:', sum(my_list))
print('Sorted:', sorted(my_list))
print('Any:', any(my_list))
print('All:', all(my_list))
print()
my_list.append(0)
print(f' New List = {my_list}')
print('All', all(my_list))
print()

########################################################################
# Additional List Methods
print('Python Additional List Methods')

# Copy method
my_list_2 = my_list.copy()
my_list_3 = my_list
print(f'My list 2 copy of the original:\n{my_list_2}')
print(f'My list 3 equal the original:\n{my_list_3}')

print(f'Appending 100 to the end of list 2 (the copy)')
my_list_2.append(100)

print(f'My list 2:\n{my_list_2}')
print(f'My list original:\n{my_list}')

print(f'Appending 100 to the end of list 3')
my_list_3.append(100)

print(f'My list 3:\n{my_list_3}')
print(f'My list original:\n{my_list}')
print()

# Clear method
my_list_2 = my_list.copy()
print(f'my_list = {my_list_2}')
print(f'my_ist.clear() = {my_list_2.clear()}')
print()

# IN method
print(f'my_list:{my_list}')
print(f'100 in List: {100 in my_list}')

# Count Method
print(f'my_list.count(5):', my_list.count(5))

# Extend Method
my_list.extend([200, 300, 400])
print(f'my_list.extend():\n{my_list}')

# Index Method
print('my_list.index(300):', my_list.index(300))

# Insert Method
print('my_list.insert(2, 200)')
my_list.insert(2, 200)
print('my_list.insert(20, 500)')
my_list.insert(20, 500)
print(f'my_list:\n{my_list}')
print()

# Pop Method
print('Poping...')
my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(3):
    print(my_list_3)
    my_list_3.pop(i)
print(my_list_3)
print()

# Sub lists
print(f'my_list[0:3]{my_list_2[0:3]}')
print(f'my_list[3:]{my_list_2[3:]}')
print(f'my_list[:]{my_list_2[:]}')
print(f'my_list[-1]{my_list_2[-1]}')
