# Summary of the main features of the print() function

# 1st way of printing - direct print
print('This is the first message.')
# prints: This is the first message.

# 2nd way of printing - print variable
message = 'This is the second message.'
print(message)
# prints: This is the second message.

# 3rd way of printing - concatenating strings
name = 'John'
age = 30
print('Hello', name, ', you are', age, 'years old.')
# prints: Hello John , you are 30 years old.

# 4th way of printing- formatted strings
name = 'Mary'
age = 28
print(f'Hello {name}, you are {age} years old.')
# prints: Hello Mary, you are 28 years old.

# Printing with separators
name = 'Robert'
age = 45
profession = 'Medic'
print(name, age, profession, sep='/')
# prints: Robert/45/Medic

# Disabling new lines - set parameter 'end' to an empty string - ''
print('Printing on the same line...', end='')
print('OK')
# prints: Printing on the same line...OK

# Add a new line separating print statements
print('\n')
print('New Line')
print('\n')

# or even better
print('\nNew Line 2\n')

# General Example with 'end' parameter different from an empty string
print('Printing in a Nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating Multiple Arguments', end='\n * ')
print('Preventing Line Breaks')
# prints:
# Printing in a Nutshell
#  * Calling Print
#  * Separating Multiple Arguments
#  * Preventing Line Breaks

# Printing with time control - 'flush' parameter must be added to avoid buffering of the data
import time
num_seconds = 3
print('\nPrinting with time control')
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')
# prints:
# Printing with time control
# 3...2...1...Go!

# Animated prints 1
from itertools import cycle
from time import sleep
count = 0
print('\nAnimating print:')
for frame in cycle(r'-\|/-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.1)
    if frame == '-':
        count += 1
    if count == 10:
        break
# prints:
# Animating print:
# -

# Animated prints 2
print('\nAnimating print again:')


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)


for i in range(101):
    progress(i)
    sleep(0.05)

# prints:
# Animating print again:
# [##############################] 100%

