'''
String Formatting
A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'.
These strings may contain replacement fields, which are expressions delimited by curly braces {}.
While other string literals always have a constant value, formatted
strings are really expressions evaluated at run time.

The parts of the string outside curly braces are treated literally.
A single opening curly bracket '{' marks a replacement field, which starts with a Python expression.
After the expression, there may be a conversion field, introduced by an exclamation point '!'.
A format specifier may also be appended, introduced by a colon ':'.
A replacement field ends with a closing curly bracket '}'.

General form:
    f'string'
    f'strin {var} string {var}'
    f'strin {expression} string {function()}'

>> name = "Eric"
>> age = 74
>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
'''

"""
Old string formatting
>>> name = "Eric"
>>> age = 74
>>> "Hello, %s. You are %s." % (name, age)
'Hello Eric. You are 74.'

>>> "Hello, {}. You are {}.".format(name, age)
'Hello, Eric. You are 74.'

"""
#Formating Float
pi = 3.1415
print(f'{pi}')
print(f'{pi:.3f}')

# Formatting String
for x in range(1, 11):
    print(f'{x:02} {x*x:03} {x*x*x:04}')

# Many variables
name = 'Sandra'
surname = 'Bullock'
age = '50'
print(f'Name: {name}\nSurname: {surname}\nAge: {age}')

# Justify String
s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'
s5 = 'abcde'

print(f'{s1:<5}', end='')
print(f'{s2:<5}', end='')
print(f'{s3:<5}', end='')
print(f'{s4:<5}', end='')
print(f'{s5:<5}')

print(f'{s1:>5}', end='')
print(f'{s2:>5}', end='')
print(f'{s3:>5}', end='')
print(f'{s4:>5}', end='')
print(f'{s5:>5}')

# Number Format
a = 300

# hexadecimal
print(f"{a:x}")
# octal
print(f"{a:o}")
# scientific
print(f"{a:.2e}")
