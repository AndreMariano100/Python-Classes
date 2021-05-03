# Variable scope #_#_#_#_#_#_#_#_#_#_#_#_#
"""
LOCAL: A variable x created inside a function is available inside that function;

ENCLOSING (Function inside function): the variable x is not available outside the function,
                                      but it is available for any function inside the function;

GLOBAL: A variable x created in the main body of the Python code is a global variable and belongs to the global scope.
        Global variables are available from within any scope, global and local.

"""

# EX1 - LOCAL -----------------------------------------------------

def myfunc_0():
    """ Local Scope example"""
    x = 300
    print(x)

myfunc_0()

# EX2 - ENCLOSING -----------------------------------------------------

def myfunc_1():
    """Enclosing Scope - Function inside function"""
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc_1()

# EX3 - GLOBAL -----------------------------------------------------

x = 300
def myfunc_2():
    """Global Scope"""
    print(x)
myfunc_2()
print(x)


# 'global' Keyword #_#_#_#_#_#_#_#_#_#_#_#_#
"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The 'global' keyword makes the variable global.
"""

# EX4 - global keyword ----------------------------------------------------

x=200
print(x)
def myfunc_3():
    global x
    x = 300
myfunc_3()
print(x)

# EX5 - global keyword - creating new object ----------------------------------------------------

x = 200
print(x)
def myfunc_4():
    global x, y
    x = 300
    y = 100
myfunc_4()
print(x + y)

# EX5 - global keyword - creating new object wrong ----------------------------------------------------

def myfunc_5():
    """Enclosing Scope - Function inside function"""
    x = 300
    def myinnerfunc_2():
        print(x)
        z = 200 # z is local to myinnerfunc_2(), myfunc_5() cannot access until it´s turned global!
        print(z)
    myinnerfunc_2()
    print(z) # Error message expected!
myfunc_5()
