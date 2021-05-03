# --------------------------------------------------------------------------------------------------
# First Rule - Commenting one line
# Add # (hashtag) at the beginning of the line and the Python interpreter will ignore
# whatever comes after it.

# x = 2
# y = 3
# z = 4
# print('This part of the code will not run')
# None of the lines above will be executed

x = 5
z = 6
print(x+z)
# The lines above will be executed

# --------------------------------------------------------------------------------------------------
'''
Second Rule - Commenting several lines
Comments in several lines shall be put in-between triple quotes
Quotes may be single or double
'''

# --------------------------------------------------------------------------------------------------
'''
Third Rule - Indentation
Indentation in Python uses 4 spaces (PyCharm converts TAB to 4 spaces)
Indentation serves to organize the code into levels and blocks of code

x = 0
if x < 10:
    print('X < 10')
    print('same indentation, will perform with the above expression')
else:
    print('X > 10')
    print('same indentation, will also perform with the above expression')
print('Not is the same indentation')
print('Will not follow any of the above conditions')
'''

# --------------------------------------------------------------------------------------------------
'''
Fourth Rule - Variable assignment
Assign values to your variables with the single equal sign: = 
Assignment happens from right to left!!!

x = 0           # Integer value 0 assigned to the variable named x
x = 'Zero'      # String 'Zero' assigned to the variable named x, overwrites the initial assignment
x = [0, 1, 2]   # List of values assigned to the variable named x.

It is possible to perform multiple assignment at once
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
'''

# --------------------------------------------------------------------------------------------------
'''
Fifth Rule - Keywords
The following words cannot be used elsewhere.
They are keywords to Python itself

    List of Keywords in Python
    and         as          not
    assert      finally     or
    break       for         pass
    class       from        nonlocal
    continue    global      raise
    def         if          return
    del         import      try
    elif        in          while
    else        is          with
    except      lambda      yield
    False       True        None
'''

# --------------------------------------------------------------------------------------------------
'''
Sixth Rule - Variable names

Variable names shall start with letter or underscore
May not start with number
May contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Are case sensitive
Usually have the following format:
    employee_name
    my_age
    button_1
'''

# --------------------------------------------------------------------------------------------------
'''
Seventh Rule - Style as PEP 8

Follow the Style Guide for Python Code known as PEP8

https://www.python.org/dev/peps/pep-0008/
https://pep8.org
'''

# --------------------------------------------------------------------------------------------------

'''
Eighth Rule: print and input

print() method used mainly to debug the code (shows values at the Terminal).
x = [1, 2, 3, 4]
y = str(x[0])

print(y)        - 1
print(type(y))  - <class 'str'>

input() method is used to read values from the user at the Terminal.
user_name = input('Enter your name:')
>>>Enter your name:

'''