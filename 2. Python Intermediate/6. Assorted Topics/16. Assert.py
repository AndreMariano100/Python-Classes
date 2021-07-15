# assert <condition>, <error message>
# It is a debugging tool!

# --------------------------------------------------
# name = 'Paul'
#
# assert name == 'Paul'
# # Does nothing. Moves on.
#
# # assert name == 'John'
# # Raises AssertionError
#
# assert name == 'John', 'name should be "John"'
# # Raises AssertionError with the required message

# --------------------------------------------------
# def avg(grades):
#     assert len(grades) != 0, 'List is empty'
#     return sum(grades)/len(grades)
#
# # class_grades = [87, 90, 74, 88, 92]
# # print("Average of Grades:", avg(class_grades))
#
# class_grades = []
# print("Average of Grades:", avg(class_grades))
#
# # -----------------------------------------------------
import sys


def win_machine():
    assert 'win32' in sys.platform
    print('Platform is Windows based')


def linux_machine():
    assert 'linux' in sys.platform
    print('Platform is Linux based')


# try:
#     win_machine()
# except:
#     print('Machine is not Windows based')

try:
    linux_machine()
except:
    print('Machine is not Linux based')