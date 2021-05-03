'''
Modulo operator returns the remainder of dividing the left hand operand by right hand operand.
It's used to get the remainder of a division problem.
'''

# #---------------- Example 1 - Modulo with "int" -----------------
# a = 12
# b = 5
# print(f'\nModulo (%) of integer numbers -->  {a} % {b}  =  {a % b} \n')

# # ---------------- Example 2 - Modulo with "float" -----------------
# a = 12
# b = 5.5
# print(f'\nModulo (%) of float numbers -->  {a} % {b}  =  {a % b}\n')

# # ---------------- Example 3 - Alternative to Modulo -----------------
# import math
# a = 12
# b = 5.5
# print(f'\nAlternative to "%". Use of "math.fmod" -->  math.fmod({a}, {b}) = {math.fmod(a, b)} \n')
#
'''
   The official Python documentation suggest using math.fmod() over the Python modulo operator when working
   with float values because of the way math.fmod() calculates the result of the modulo operation.
   Also, if you’re using a negative operand, then you may see different results between math.fmod(x, y) and x % y.
'''

'''---------------- Python Modulo Operator Exceptions -----------------'''

''' ZeroDivisionError '''
# print('Modulo operator returns an error if the second term is zero.\n')
# a = 12
# b = 0
# print(f'{a} % {b}  =  {a % b}')

''' Rounding precision with float '''
# a = 13.3
# b = 1.1
#
# print('\nModulo operator may encounter rounding and precision issues when dealing with floating-point arithmetic.')
# print(f'{a} % {b}            = {a % b}')
#
# import math
# print(f'math.fmod({a},  {b}) = {math.fmod(a, b)}')
#
'''
    If maintaining floating-point precision is important to your application,
    then you can use the modulo operator with "decimal.Decimal". ')
'''

''' Modulo Operator With a Negative Operand '''
# print('\nIn Python the remainder in Modulo operator will take the sign of the divisor (second term).\n'
#       'Also, when any term is negative, the division is always rounded down, which may change the remainder.\n'
#       'Other languages may be different.\n')
# print(f'8 %  3 = {8 % 3}')
# print(f'8 % -3 = {8 % -3}')
# print(f'8 % -3 = {-8 % 3}')
# print(f'8 % -3 = {-8 % -3}')
#
# print('\nThe same does not happen when using math.fmod.\n'
#       'In that case it uses the sign of the divisor and the division is not rounded down.')
# import math
# print(f'math.fmod( 8.0,  3.0) = {math.fmod(8.0, 3.0)}')
# print(f'math.fmod( 8.0, -3.0) = {math.fmod(8.0, -3.0)}')
# print(f'math.fmod(-8.0,  3.0) = {math.fmod(-8.0, 3.0)}')
# print(f'math.fmod(-8.0, -3.0) = {math.fmod(-8.0, -3.0)}\n')

'''---------------- Example 1 -----------------'''
# import math
# a = float(input('Enter a number : '))
# b = float(input('Enter another number : '))
# print(f' Brute force (a - math.trunc(a/b) * b) --> remainder of {a} / {b}  = {a - math.trunc(a/b) * b}')
# print(f' Root division (a - a//b * b)          --> remainder of {a} / {b}  = {a - a//b * b}')
# print(f' Using Modulo (a % b)                  -->              {a} % {b}  = {a % b}')
# print(f' Using math Library (math.fmod(a, b)   -->     math.fmod({a}, {b}) = {math.fmod(a, b)}')

'''---------------- Modulo Operator and divmod() -----------------'''
'''
Python has the built-in function divmod(), which internally uses the modulo operator.
'''
''' 
    ndivmod() takes two parameters and returns a tuple containing the results of floor division
    and modulo using the supplied parameters
'''
# a = 37
# b = 5
# print(f'\ndivmod({a}, {b}) = {divmod(a, b)}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} % {b} = {a % b} \n')
#
# print(f'--- divmod() using negative numbers ---')
# a = 37
# b =-5
# print(f'divmod({a}, {b}) = {divmod(a, b)}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} % {b} = {a % b} \n')

'''---------------- Modulo Operator Precedence -----------------'''
# print(f'\nThe modulo operator (%) shares the same level of precedence as the multiplication (*), \n'
#       f'division (/), and floor division (//) operators. \n')
#
# print(f'4 * 10 % 12 - 9   = {4 * 10 % 12 - 9}')
# print(f'4 * 10 % (12 - 9) = {4 * 10 % (12 - 9)}\n')

'''---------------- Application 1 - Finding even or odd numbers -----------------'''
# print(f'\nEven numbers from 1 to 10')
# for number in range(1, 10):
#     if(number % 2 == 0):
#         print(number)
# print(f'\nOdd numbers from 1 to 10')
# for number in range(1, 11):
#     if(number % 2 != 0):
#         print(number)

'''---------------- Application 2 - Checking if a number is even or odd -----------------'''
#
#
# def is_even(num):
#     return num % 2 == 0
#
#
# a = float(input('Enter an integer number : '))
# if a != int(a):
#     print (f'You entered a non integer number. I will consider the number {int(a)}')
# a = int(a)
# if is_even(a) == True:
#     print(f'The number {a} is even.')
# else:
#     print(f'The number {a} is odd.')

'''---------------- Application 3 - Running Code at Specific Intervals in a Loop -----------------'''
#
#
# def split_names_into_rows(name_list, modulus):
#     for index, name in enumerate(name_list, start=1):
#         print(f"{name:-^15} ", end="")
#         if index % modulus == 0:
#             print()
#     print()
#
# names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
# columns = int(input(f'\nEnter number of columns: '))
# split_names_into_rows(names, columns)

'''---------------- Application 4 - Converting Time -----------------'''
#
#
# def minutes_to_hours(total_mins):
#     hours = total_mins // 60
#     minutes = total_mins % 60
#
#     print(f"\n{total_mins} minutes is equivalent to {int(hours)} hours and {int(minutes)} minutes")
#
#
# minutes = int(input(f'\nEnter time in minutes: '))
# minutes_to_hours(minutes)

'''---------------- Application 5 - Converting Units -----------------'''
#
#
# def convert_mm_to_inches(mm):
#     total_inches = mm / 25.4
#     feet = int(total_inches // 12)
#     inches = round(total_inches % 12, 2)
#     print(f'\n{int(mm)} mm = {feet} feet and {inches} inches')
#
#
# mm = float(input(f'\nEnter lenght in mm: '))
# convert_mm_to_inches(mm)

'''---------------- Application 6 - Determine if a Number is a Prime Number -----------------'''
#
# def check_prime_number(num):
#     if num < 2:
#         print(f"{num} must be greater than or equal to 2 to be prime.")
#         return
#
#     factors = [(1, num)]
#     i = 2
#
#     while i * i <= num:
#         if num % i == 0:
#             factors.append((i, num//i))
#         i += 1
#
#     if len(factors) > 1:
#         print(f"{num} is not prime. It has the following factors: {factors}")
#     else:
#         print(f"{num} is a prime number")
#
#
# num = int(input(f'Type an integer number: '))
# check_prime_number(num)
