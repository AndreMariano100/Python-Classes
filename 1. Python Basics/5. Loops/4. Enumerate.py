# Enumerate
"""Python’s enumerate() lets you write Pythonic for loops when you need a count and the value from an iterable.
But you don´t want to create and increment a variable yourself.

The big advantage of enumerate() is that it returns a tuple with the counter and value,
so you don’t have to increment the counter yourself. It also gives you the option to change
the starting value for the counter."""

# Revision from for loop

#values = ["a", "b", "c"]

#     # Basic for loop
#
# for value in values:
#     print(value)
# # Prints
# #a
# #b
# #c
#
#     #Basic for loop with an Index
# index = 0
#
# for value in values:
#     print(index, value)
#     index += 1
# # # Prints
# # #0 a
# # #1 b
# # #2 c
# #
#     #Basic for loop - error on index - there is no update index at the end of the loop
# index = 0
#
# for value in values:
#     print(index, value)
# # Prints
# #0 a
# #0 b
# #0 c
#
    #Basic for loop - error index - trying to eliminate update index error - range() & len()

# for index in range(len(values)):
#     #value = values[index]
#     print(index, value)
#
# # Prints    without line value
# #0 a        0 c
# #1 b        0 c
# #2 c        0 c
#
# # #######################################################################################################
# # As none os this is a Pythonic code lets see the Enumerate.
#
# # Enumerate()
#
    # Enumerate() Basics
# for count, value in enumerate(values):
#     print(count, value)
#
# #prints
# #0 a
# #1 b
# #2 c
#
#
# # When you use enumerate(), the function gives you back two loop variables:
# #    The count of the current iteration
# #    The value of the item at the current iteration.
# # Don’t need to remember to access the item from the iterable,
# # and you don’t need to remember to advance the index at the end of the loop.
#
#     #Enumerate() - Additional argument - Value of count
#
#print(values[0])
#
# #prints
# # a
#
#     #Enumerate() - Additional argument - Count starts at wherever I want
#
# for count, value in enumerate(values, start=1):
#     print(count, value)
#
# # prints
# #1 a
# #2 b
# #3 c
#
#     #Example with Enumerate ()
#
# users = ["Test User", "Real User 1", "Real User 2"]
# for index, user in enumerate(users):
#     if index == 0:
#         print("Extra verbose output for:", user)
#     else:
#         print(user)
#
# #Extra verbose output for: Test User
# #Test User
# #Real User 1
# #Real User 2
#

