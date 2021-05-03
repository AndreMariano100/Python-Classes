'''

Dictionaries in Python

dictionary = {  key_1: value_1,
                key_2: value_2,
                key_3: value_3 }

Keys must be unique.
Keys may be string or numbers.

print(dir(dict))

 ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
  '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
  '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
  '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

clear()
     Remove all items from the dictionary.
copy()
      Return a shallow copy of the dictionary.
fromkeys()
    Create a new dictionary with keys from iterable and values set to value.
    Fromkeys is a class method that returns a new dictionary. value defaults to None.
    All of the values refer to just a single instance, so it generally doesn’t make sense for value
    to be a mutable object such as an empty list. To get distinct values, use a dict comprehension instead.

get(key[, default])
    Return the value for key if key is in the dictionary, else default.
                    If default is not given, it defaults to None, so that this method never raises a KeyError.
items()
    Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

keys()
    Return a new view of the dictionary’s keys. See the documentation of view objects.

pop(key[, default])
    If key is in the dictionary, remove it and return its value, else return default.
    If default is not given and key is not in the dictionary, a KeyError is raised.

popitem()
    Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
    popitem() is useful to destructively iterate over a dictionary, as often used in set algorithms.
    If the dictionary is empty, calling popitem() raises a KeyError.

reversed(d)
    Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).

setdefault(key[, default])
    If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
    default defaults to None.

update([other])
    Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
    update() accepts either another dictionary object or an iterable of key/value pairs
    (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary
    is then updated with those key/value pairs: d.update(red=1, blue=2).

values()
    Return a new view of the dictionary’s values. See the documentation of view objects.
    An equality comparison between one dict.values() view and another will always return False.
    This also applies when comparing dict.values() to itself:
'''


# Main features for Python Dictionaries
released = {
    "iphone": 2007,
    "iphone 3G": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4S": 2011,
    "iphone 5": 2012}

# print(f'My iphone dictionary:{released}')
# prints: {'iphone': 2007, 'iphone 3G': 2008, 'iphone 3GS': 2009, 'iphone 4': 2010, 'iphone 4S': 2011, 'iphone 5': 2012}

############################################################################################
# # Access a value in the dictionary

# # the syntax is: mydict[key]
# print(f'The year iphone was released: {released["iphone"]}')

# # if the values does not exist returns KeyError: 'iphones'
# print(f'The year iphone was released: {released["iphones"]}')

# # but you can handle the error
# try:
#     print(f'The year iphone was released: {released["iphones"]}')
# except KeyError:
#     print('Key not in the dictionary')

# # or you may give it a standard value with the get() method
# print(f'The year iphone was released: {released.get("iphone")}')
# print(f'The year iphone was released: {released.get("iphones")}')
# print(f'The year iphone was released: {released.get("iphones", "Not in Dictionary")}')
#
# year = released.get("iphone")
# if year:
#     print('Found')
# else:
#     print('Not Found')
#
# # or you may check for a key in the dictionary
# if "iphone" in released:
#     print('"iphone" is a key')
# else:
#     print('"iphone" is a not key')

############################################################################################
# # Add and delete a value to the dictionary
# # {'iphone': 2007, 'iphone 3G': 2008, 'iphone 3GS': 2009, 'iphone 4': 2010, 'iphone 4S': 2011, 'iphone 5': 2012}

# the syntax is: mydict[key] = "value"
# print(released)
# released["iphone 5S"] = 2013
# print(released)
#
# # Remove a key and it's value
# del released["iphone"]
# print(released)
#
# # Check the length
# print(f"The length of my dictionary:{len(released)}")

# # Prints all keys
# print('Only the keys')
# for release in released:
#     print(release)
#
# print('Only the keys again')
# for key in released.keys():
#     print(key)
# print()
#
# # Print only the values
# print('Only the values')
# for value in released.values():
#     print(value)
# print()
#
#
# # Prints all keys and values
# print('Keys and Values')
# for key, val in released.items():
#     print(key, val)
# print()
#
# # You may get only the keys, or only the values in the form of a list
# phones = list(released.keys())
# years = list(released.values())
# print(phones)
# print(years)

############################################################################################
# rodar cmd
# digitar ipython
# dict.[tab]
# dict.clear?
# dict.keys?
# dict.get?
# dict.pop?
# digitar exit

############################################################################################
# Dict and ZIP

keys = ['name_1', 'name_2', 'name_3', 'name_4']
values = ['value_1', 'value_2', 'value_3', 'value_4']

# zip and create list, tuple, set or dict
my_set = dict(zip(keys, values))
print(my_set)



