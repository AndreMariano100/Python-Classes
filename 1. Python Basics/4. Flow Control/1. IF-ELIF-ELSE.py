# Control the flow of execution within a program
# if <condition-evaluating-to-boolean>:
#     statement
# elif <other_condition-evaluating-to-boolean>:
#     statement
# else:
#     statement

"""
Decision based on a comparison operator, identity operator or membership operator

==      Tests if two values are equal
!=      Tests that two values are not equal to each other
<       Tests to see if the left-hand value is less than the right-hand value
>       Tests if the left-hand value is greater than the right-hand value
<=      Tests if the left-hand value is less than or equal to the right-hand value
>=      Tests if the left-hand value is greater than or equal to the right-hand value

is, is not      Test whether the two items are the same
in, not in      Test whether an item is included in a set

Usually associated with logical operators: AND, OR, NOT

IMPORTANT!!!
 x = 100   -> attributes the value 100 to the variable x
 x == 100  -> compares x to 100, and return a boolean (True or False)

"""
# Single IF
x = 10
if x > 0:
    print('X is greater than 0')
    print('This will also be printed')
    print('As long as it is in the indented block of code')

# Single IF-ELSE
x = -5
if x > 0:
    print('X is greater than 0')
else:
    print('X is lower than 0')

letter = 'a'
if letter in ['a', 'e', 'i', 'o', 'u']:
    print('Letter is a vowel')
else:
    print('Letter is a consonant')

# IF-ELIF-ELSE
x = 50
if x > 100:
    print('X is greater than 100')
elif x > 10:
    # as many ELIF as you want
    print('X is lower than 100, but greater than 10')
else:
    print('X is lower than 10')

# Nested
grade_1 = 9
grade_2 = 8
if grade_1 > 5:
    if grade_2 > 5:
        print('You did well on both tests')
    else:
        print('You did well on the first test')
else:
    if grade_2 > 5:
        print('You did well on the second test')
    else:
        print('You performed poorly on both tests')

