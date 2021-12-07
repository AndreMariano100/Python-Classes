"""
Create a function that will be used just once, and don't bother giving it a name.

lambda arguments: expression
"""

double = lambda i: i * 2

print(double(10))
print(double(100))
my_var = double(4)
print(my_var)

func0 = lambda: print('no args')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))
