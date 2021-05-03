# Variable Scope---------------------------------------------------------------

"""
The existence of multiple, distinct namespaces means several different instances of
a particular name can exist simultaneously while a Python program runs.
As long as each instance is in a different namespace, they’re all maintained separately
and won’t interfere with one another.

Python searches for a variable ('x') in the following namespaces in the order shown:

LOCAL: If you refer to x inside a function, then the interpreter first searches for it in
       the innermost scope that’s local to that function.
ENCLOSING: If x isn’t in the local scope but appears in a function that resides inside another
       function, then the interpreter searches in the enclosing function’s scope.
GLOBAL: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
BUILT-IN: If it can’t find x anywhere else, then the interpreter tries the built-in scope.

If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.
"""

print('Variables Scope Examples')


def example_1():
    """
    Single Definition
    x is defined in only one location. It’s outside both f() and g(), so it resides in the global scope:

    x = 'Global'
    def f():
        def g():
            print(f' Variable x is {x} !')
        g()
    f()
    return

    """

    x = 'Global'
    #print(f'Variable x outside f() is {x}')

    def f():
        def g():
            print(f' Variable x is {x} !')

        g()

    f()

    return


"""
    It returns: 'Variable x is global !'
"""


def example_2():
    """
    Double Definition:
    x appears in two places, one outside f() and one inside f() but outside g():

    x = 'Global'
    def f():
        x = 'Enclosing'
        def g():
            print(f' Variable x is {x} !')
        g()
    f()
    return

    """

    x = 'Global'
    #print(f'Variable x outside f() is {x}')
    def f():
        x = 'Enclosing'
        #print(f'Variable x inside f(), outside g() is {x}')
        def g():
            print(f' Variable x is {x} !')
        g()
    f()
    return


"""
    It returns: 'Variable x is Enclosing !'
"""


def example_3():
    """
    Triple Definition:
    x is defined here, there, and everywhere.
    One definition is outside f(), another one is inside f() but outside g(), and a third is inside g():

    x = 'Global'
    def f():
        x = 'Enclosing'
        def g():
            x = 'Local'
            print(f' Variable x is {x} !')
        g()
    f()
    return

    """

    x = 'Global'
    def f():
        x = 'Enclosing'
        print(f'Variable x inside f(), outside g() is {x}')

        def g():
            x = 'Local'
            print(f' Variable x is {x} !')
        g()
    f()

    return


def example_4():
    """
    global keyword:
    If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
    The 'global' keyword makes the variable global.

    global x
    x = 'Global'
    print(f'Variable x outside f() is {x}')
    def f():
        global x
        x = 'Enclosing'
        print(f'Variable x inside f(), outside g() is {x}')
    f()
    print(f'Variable x outside f() is {x}')
    return

    """

    global x
    x = 'Global'
    print(f'Variable x outside f() is {x}')
    def f():
        global x
        x = 'Enclosing'
        print(f'Variable x inside f(), outside g() is {x}')
    f()
    print(f'Variable x outside f() is {x}')
    return


def example_5():
    """
    global keyword:
    If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
    The 'global' keyword makes the variable global.

    global x
    x = 'Global'
    print(f'Variable x outside f() is {x}')
    def f():
        #global x
        x = 'Enclosing'
        print(f'Variable x inside f(), outside g() is {x}')

        def g():
            global x
            x = 'Local'
            print(f' Variable x inside f() and inside g() is {x} !')

        g()
        print(f'Variable x inside f(), outside g() is {x}')
    f()
    print(f' Variable x outside f() is {x} !')
    return

    """
    global x
    x = 'Global'
    print(f'Variable x outside f() is {x}')

    def f():
        #global x
        x = 'Enclosing'
        print(f'Variable x inside f(), outside g() is {x}')

        def g():
            global x
            x = 'Local'
            print(f' Variable x inside f() and inside g() is {x} !')

        g()
        print(f'Variable x inside f(), outside g() is {x}')
    f()
    print(f' Variable x outside f() is {x} !')
    return



def main():
    user_choice = int(input('Choose the example to be shown (1, 2, 3, 4 or 5):'))
    if user_choice == 1:
        help(example_1)
        example_1()
        main()
    elif user_choice == 2:
        help(example_2)
        example_2()
        main()
    elif user_choice == 3:
        help(example_3)
        example_3()
        main()
    elif user_choice == 4:
        help(example_4)
        example_4()
        main()
    elif user_choice == 5:
        help(example_5)
        example_5()
        main()
    else:
        print('Wrong choice! Select 1, 2, 3, 4 or 5')
        exit()
    return


if __name__ == '__main__':
    main()
