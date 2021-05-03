'''

General Rules for Functions - parameters and results

Defining a function (or a procedure, or a method):

    def function_name(parameter_1, parameter_2, ..., parameter_n):

        """This function performs some actions"""

        value = statement(parameter_1, parameter_2, parameter_n)

        return value

Calling the Function:

    my_value = function_name(my_parameter_1, my_parameter_2, ..., my_parameter_n)

'''

import math


def function_1():  # Void Function
    print('Function 1')
    print('Takes no parameters.')
    print('Does not return anything')


def function_2(a, b, c):  # Void Function
    print('Function 2')
    print('Receives 3 parameters')
    print('Parameters:', a, b, c)
    print('Does not return anything')


def function_3():
    print('Function 3')
    print('Receives no parameters')
    print('May return anything')
    return math.pi


def function_4():
    print('Function 4')
    print('Takes no parameters')
    print('May return many things')
    return math.pi, math.e, math.tau  # This is actually a Tuple: (math.pi, math.e, math.tau)


def function_5(a, b, c):
    # a, b, and c are local variables names.
    # they exist only within the function.

    print('Function 5')
    print('Receives parameters')
    print('Parameters:', a, b, c)
    print('May return many things')
    return math.sin(a), math.sin(b), math.sin(c)


def main():
    function_1()
    x, y, z = 1, 2, 3
    function_2(x, y, z)
    result = function_3()
    print('Result:', result)
    result_1, result_2, result_3 = function_4()
    print(result_1, result_2, result_3)
    x = 4
    y = 10
    z = 100
    result_4, result_5, result_6 = function_5(x, y, z)
    print(result_4, result_5, result_6)


if __name__ == '__main__':
    main()
