# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# SORTED EXAMPLES
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# help(sorted)
# # Help on built-in function sorted in module builtins:
# # sorted(iterable, /, *, key=None, reverse=False)
# #     Return a new list containing all items from the iterable in ascending order.
# #
# #     A custom key function can be supplied to customize the sort order, and the

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # First example
# numbers = [6, 9, 3, 1]
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)
# sorted_reverse = sorted(numbers, reverse=True)
# print(sorted_reverse)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# list.sort() is a similar method. But with some differences:
# list.sort() may only be applied to list and modifies the list itself.
# numbers1 = [6, 9, 3, 1]
# print('numbers1', numbers1)
# sorted_numbers1 = numbers1.sort()
# print('numbers1', numbers1)
# print(sorted_numbers1)

# If you’re working with important data, and there is even a remote possibility
# that the original data will need to be recovered, then .sort() is not the best option.
# If the data is a copy, of if it is unimportant working data,
# or if no one will mind losing it because it can be retrieved,
# then .sort() can be a fine option.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # sorted() can be used on tuples and sets very similarly:
# numbers_tuple = (6, 9, 3, 1)
# numbers_set = {5, 5, 10, 1, 0}
# numbers_tuple_sorted = sorted(numbers_tuple)
# numbers_set_sorted = sorted(numbers_set)
# print(numbers_tuple)
# print(numbers_tuple_sorted)
# print(numbers_set)
# print(numbers_set_sorted)
#
# # sorted() returns a new list by definition. If you want, you can set it back, but it is worthless for sets...
# numbers_tuple_sorted = tuple(sorted(numbers_tuple))
# numbers_set_sorted = set(sorted(numbers_set))
# print(numbers_tuple_sorted)
# print(numbers_set_sorted)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Others simple examples:
# string_number_value = '34521'
# string_value = 'I like to sort'
# string_mix = 'What about a mix 9856771'
# sorted_string_number = sorted(string_number_value)
# sorted_string = sorted(string_value)
# sorted_mix = sorted(string_mix)
# print(string_number_value)
# print(sorted_string_number)
# print(string_value)
# print(sorted_string)
# print(string_mix)
# print(sorted_mix)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # You can sort by word
# string_value = 'I like to sort'
# sorted_string = sorted(string_value.split())
# print(string_value)
# print(sorted_string)
# # And make a new string based on sorted
# tbt_string = ' '.join(sorted_string)
# print(tbt_string)
# # The original sentence in this example is converted into a list of words
# # instead of leaving it as a str.
# # That list is then sorted and combined to form a str again instead of a list.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Limitations and Gotchas With Python Sorting
# # Lists With Non-Comparable Data Types Can’t Be sorted()
# mixed_types = [None, 0]
# sort_mixed = sorted(mixed_types)
# print(sort_mixed)
# # It’s trying to put the values in order by using the less than operator (<)
# # to determine which value is lower in sorting order.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # What about strings and numbers? If a iterable contains a combination of
# # integers and strings that are all numbers, they can be cast to
# # comparable data types by using a list comprehension:
# mixed_numbers = [5, "1", 100, "34"]
# # sort_mixed = sorted(mixed_numbers)
# # List comprehension to convert all values to integers
# sort_mixed = sorted([int(x) for x in mixed_numbers])
# print(mixed_numbers)
# print(sort_mixed)

# mixed_numbers = [5, .1, 100, .34]
# sort_mixed = sorted(mixed_numbers)
# print(mixed_numbers)
# print(sort_mixed)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Python can also implicitly convert a value to another type.
# # In the example below, the evaluation of 1 <= 0 is a false statement,
# # so the output of the evaluation will be False.
# similar_values = [False, 0, 1, 'A' == 'B', 1 <= 0]
# sort_similar = sorted(similar_values)
# print(similar_values)
# print(sort_similar)
# # In Python, when you sort equal values, they will retain their original order in the output.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # When You’re Sorting Strings, Case Matters
# names = ['Harry', 'Suzy', 'Al', 'Mark']
# sort_names = sorted(names)
# print(names)
# print(sort_names)
# names_2 = ['harry', 'Suzy', 'al', 'Mark']
# sort_names_2 = sorted(names_2)
# print(names_2)
# print(sort_names_2)
# print([(ord(name[0]), name[0]) for name in sorted(names_2)])
# # This example uses ord() to return the Unicode Code Point of the first letter in each string
# # name[0] is returning the first character in each element of sorted(names_with_case),
# # and ord() is providing the Unicode Code Point.
# # Even though a comes before M in the alphabet, the code point for M comes before a,
# # so the sorted output has M first.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # If the first letter is the same, then sorted() will use the second character to determine order,
# # and the third character if that is the same, and so on, all the way to the end of the string:
# very_similar = ['hhhhhd', 'hhhhha', 'hhhhhc','hhhhhb']
# sort_similar = sorted(very_similar)
# print(very_similar)
# print(sort_similar)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Strings that contain identical values will end up sorted shortest to longest
# # due to the shorter strings not having elements to compare to with the longer strings:
# lengths = ['hhhh', 'hh', 'hhhhh','h']
# print(lengths)
# lengths.sort()
# print(lengths)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Sorted or sort can use a key parameter to specify a function (or a method) which receives an argument
# # and returns a key to be used for ordering.
# string_value = 'This is a test string for SRGE.'
# sorted_string = sorted(string_value.split(), key=str.lower)
# print(string_value)
# print(sorted_string)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Simple example for key in sorted:
# fruits = ['banana', 'Uva', 'pera', 'Melancia']
# print(fruits)
# fruits.sort(key=len, reverse=True) # sort by length
# print(fruits)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # There are two main limitations when you’re using functions with the key argument.
# # First, the number of required arguments in the function passed to key must be one.
# def add(x, y):
#     return x + y
# values = [1, 2, 3, 4, 5]
# values.sort(key=add)

# # The second limitation is that the function used with key must be able to handle all the values in the iterable.
# values = ['4', '3', '2', '1']
# sort_values = sorted(values, key=int)
# print(values)
# print(sort_values)
# values_2 = ['4', '3', '2', 'one']
# sort_values_2 = sorted(values_2, key=int)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Other example to highlight usability: order by the last letter in each string
# def reverse_str(word):
#     return word[::-1]
# students = ['Paul', 'Gene', 'Simmons', 'Frehley', 'Peter']
# last_1st_name = sorted(students, key=reverse_str)
# print(students)
# print(last_1st_name)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Another example for key in sorted:
# students = [('Paul', 'Stanley', 69),
#             ('Gene', 'Simmons', 71),
#             ('Ace', 'Frehley', 70),
#             ('Peter', 'Criss', 75)]
# print(students)
# students.sort(key=lambda student: student[2]) # sort by age
# print(students)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # With class:
# class Bolt:
#     def __init__(self, type, grade, temp):
#         self.type = type
#         self.grade = grade
#         self.temp = temp
#
#     def __repr__(self): # In Python, __repr__ is a special method used to represent a class’s objects as a string.
#         return repr((self.type, self.grade, self.temp))
#
#
# bolts = [Bolt(193, 'B7', -46),
#          Bolt(320, 'L7', -100),
#          Bolt(320, 'L43', -100),
#          Bolt(193, 'B16', -29),
#          Bolt(193, 'B8M', -196)]
# print(bolts)
# bolts.sort(key=lambda Bolt: Bolt.temp)
# print(bolts)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # EXTRA
# # Reversing is another subject. You also have a built-in function that reverses a list,
# # but it won't sort the items.
# values = ['1', '3', '2', '4']
# print(values)
# reversed_values = values.reverse()
# print(reversed_values)
# print(values)
# # Note that .reverse() reversed the list in place and didn’t return a new list but None.
#
# # If ypu want to create a reversed copy ypu should use:
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(digits)
# reversed_digits = list(reversed(digits))
# print(reversed_digits)
#
# # This works for strings also!
# text = 'subi no onibus'
# print(text)
# reversed_text = list(reversed(text))
# print(reversed_text)



