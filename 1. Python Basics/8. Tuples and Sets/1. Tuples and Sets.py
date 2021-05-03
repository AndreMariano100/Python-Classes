'''

    Python Tuples - Almost like a list, but immutable

dir(tuple)

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

'''

# # Creating Tuples
if True:
    my_tuple_1 = ()
    my_tuple_2 = 'a', 'b', 'c'
    my_tuple_3 = tuple(['a', 'b', 'c'])
    single_tuple_1 = 'a',
    single_tuple_2 = ('a',)
    print(type(my_tuple_1))
    print(type(my_tuple_2))
    print(type(my_tuple_3))
    print(type(single_tuple_1))
    print(type(single_tuple_2))

# Tuples are iterable, like lists. Indexing same as list. Slicing same as list.
# my_tuple = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
# print(my_tuple)
# for item in my_tuple:
#     print(item, end=' ')
# print()
#
# for item in (my_tuple[5:]):
#     print(item, end=' ')
# print()
#
# my_tuple_2 = my_tuple[5:]
# print(my_tuple_2)
# print(type(my_tuple_2))

# Additional functions
# len(), max(), min(), count(), index()
my_letter_tuple = 'A', 'B', 'C', 'D', 'G', 'F', 'E'
print(f'Index of letter B: {my_letter_tuple.index("C")}')
print(f'Length of Tuple: {len(my_letter_tuple)}')
my_number_tuple = 1, 6, 3, 9, 5, 2, 8, 4, 7, 0
print(f'Max : {max(my_number_tuple)}')
print(f'Min : {min(my_number_tuple)}')
print(f'Count "7": {my_number_tuple.count(7)}')

# # It may seem like you can change it, but actually a new tuple is being created
my_tuple = ()
my_tuple += 10,
my_tuple += 20,
my_tuple += 30,
print(my_tuple)
#
# # Ziping
# data_1 = ['Name', 'Surname', 'City']
# data_2 = ['John', 'Nash', 'Illinois']
# zipped = tuple(zip(data_1, data_2))
# print(zipped)

# #################################################################
# # Python Sets
# '''
# Set is an unordered collection with no duplicates.
# Used primarily to test membership and eliminate duplicate entries.
# Created with curly braces or with the set() method.
# fluids = {water, oil}
#
# dir(set)
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__',
# '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
# '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
# '__str__', '__sub__', '__subclasshook__', '__xor__',
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update']
# '''
# names = ['Robert', 'Chris', 'Mark', 'Arnold', 'Steven', 'Robert', 'Chris']
# print(f'Original names list:\n{names}')
# set_1 = set(names)
# print(f'Names on set:\n{set_1}')
#
# # Check membership and add
# set_2 = set_1.copy()
# new_names = ['Michael', 'Michelle', 'Robert']
# print(f'New names list:\n{new_names}')
# for name in new_names:
#     if name in set_2:
#         print(f'Name {name} already belongs to set')
#     else:
#         set_2.add(name)
# print(f'Names on set:\n{set_2}')
#
# # Compare sets
# difference_1 = set_1.difference(set_2)
# print(f'Difference 1: {difference_1}')
# difference_2 = set_2.difference(set_1)
# print(f'Difference 2: {difference_2}')
#
# '''
# Set Methods Syntax Description
# add()           set_name.add(item)              The add() method adds an item to the set set_name.
# clear()         set_name.clear()                The clear() method removes all the items from the set set_name.
# difference()    set_name.difference(*others)    The difference() method returns a new set with items in
#                                                 the set set_name that are not in the others sets.
# discard()       set_name.discard(item)          The discard() method removes an item from the set set_name if present.
# intersection()  set_name.intersection(*others)  The intersection() method returns a new set with items common to the
#                                                 set set_name and all others sets.
# isdisjoint()    set_name.isdisjoint(other)      The isdisjoint() method returns True if the set set_name has no items
#                                                 in common with other set. Sets are disjoint if and only if their
#                                                 intersection is the empty set.
# issubset()      set_name.issubset(other)        The issubset() method returns True if every item in the set set_name
#                                                 is in other set.
# issuperset()    set_name.issuperset(other)      The issuperset() method returns True if every element in other
#                                                 set is in the set set_name.
# pop()           set_name.pop()                  The method pop() removes and returns an arbitrary item
#                                                 from the set set_name. It raises KeyError if the set is empty.
# remove()        set_name.remove(item)           The method remove() removes an item from the set set_name.
#                                                 It raises KeyError if the item is not contained in the set.
# symmetric_      set_name.                       The method symmetric_difference() returns a new set with
# difference()    symmetric_difference(other)     items in either the set or other but not both.
#
# union()         set_name.union(*others)         The method union() returns a new set with items from
#                                                 the set set_name and all others sets.
# update()        set_name.update(*others)        Update the set set_name by adding items from all others sets.
# '''
