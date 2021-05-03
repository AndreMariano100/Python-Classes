# ------------------------------------------------------------------------------------------------------
# TRACEBACK INTRODUCTION
# ------------------------------------------------------------------------------------------------------

"""
A traceback is a report containing the function calls made in your code at a specific point.
When your program results in an exception, Python will print the current traceback to help
you know what went wrong.
"""

# ------------------------------------------------------------------------------------------------------
# Example 1 - Traceback
# ------------------------------------------------------------------------------------------------------
# def example_1(someone):
#     print('Hello, ' + someon)
#
# example_1('Jack')

"""
Traceback (most recent call last):
  File "C:/Users/...", line 11, in <module>
    example_1('Jack')
  File "C:/Users/...", line 9, in example_1
    print('Hello, ' + someon)
NameError: name 'someon' is not defined
"""

# ------------------------------------------------------------------------------------------------------
# Example 2 - Specific Traceback Walkthrough
# ------------------------------------------------------------------------------------------------------
# def example_2(someone, say='Hello'):
#     print(say + ', ')
#
# example_2('Chad', sayy='Hello')

"""
Traceback (most recent call last):
  File "C:/Users/...", line 35, in <module>
    example_2('Chad', sayy='Hello')
TypeError: example_2() got an unexpected keyword argument 'sayy'
"""
