# ------------------------------------------------------------------------------------------------------
# COMMON TRACEBACKS
# ------------------------------------------------------------------------------------------------------

"""
    The Most Common Tracebacks in Python are:
    1. AttributeError
    2. ImportError
    3. IndexError
    4. KeyError
    5. NameError
    6. SyntaxError
    7. TypeError
    8. ValueError
"""

# ------------------------------------------------------------------------------------------------------
# Example 1 - AttributeError
# ------------------------------------------------------------------------------------------------------
# number = 1
# number.count

"""
Traceback (most recent call last):
  File "C:/Users/..., line 21, in <module>
    number.count
AttributeError: 'int' object has no attribute 'count'
"""

# ------------------------------------------------------------------------------------------------------
# Example 2 - ImportError
# ------------------------------------------------------------------------------------------------------
# import abcd

"""
Traceback (most recent call last):
  File "C:/Users/..., line 33, in <module>
    import abcd
ModuleNotFoundError: No module named 'abcd'
"""

# from math import abcd

"""
Traceback (most recent call last):
  File "C:/Users/..., line 42, in <module>
    from math import abcd 
ImportError: cannot import name 'abcd' from 'math' (unknown location)
"""

# ------------------------------------------------------------------------------------------------------
# Example 3 - IndexError
# ------------------------------------------------------------------------------------------------------
# my_list = ['a', 'b']
# print(my_list[2])

"""
Traceback (most recent call last):
  File "C:/Users/..., line 55, in <module>
    print(my_list[2])
IndexError: list index out of range
"""

# ------------------------------------------------------------------------------------------------------
# Example 4 - KeyError
# ------------------------------------------------------------------------------------------------------
# ages = {'Jack': 20, 'Daniels': 40}
# ages['Chivas']

"""
Traceback (most recent call last):
  File "C:/Users/..., line 68, in <module>
    ages['Chivas']
KeyError: 'Chivas'
"""

# ------------------------------------------------------------------------------------------------------
# Example 5 - NameError
# ------------------------------------------------------------------------------------------------------
# def example_5(person):
#     print(f'Hello, {persn}')
# example_5('World')

"""
Traceback (most recent call last):
  File "C:/Users/..., line 82, in <module>
    example_5('World')
  File "C:/Users/..., line 81, in example_5
    print(f'Hello, {persn}')
NameError: name 'persn' is not defined
"""

# ------------------------------------------------------------------------------------------------------
# Example 6 - SyntaxError
# ------------------------------------------------------------------------------------------------------
# def greet(person)

"""
File "C:/Users/..., line 96
    def greet(person)
                    ^
SyntaxError: invalid syntax
"""

# ------------------------------------------------------------------------------------------------------
# Example 7 - TypeError
# ------------------------------------------------------------------------------------------------------
# 1 + '1'

"""
Traceback (most recent call last):
  File "C:/Users/..., line 108, in <module>
    1 + '1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# ------------------------------------------------------------------------------------------------------
# Example 8 - ValueError
# ------------------------------------------------------------------------------------------------------
# a, b, c = [1, 2]

"""
Traceback (most recent call last):
  File "C:/Users/..., line 120, in <module>
    a, b, c = [1, 2]
ValueError: not enough values to unpack (expected 3, got 2)
"""