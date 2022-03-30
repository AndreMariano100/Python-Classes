'''
Eval Function.
This function is used to calculate the value of the specified expression.
The Python code it executes can only be a single expression, not complex logic code,
which is similar to lambda expression.

Exec Function.
Execute Python code dynamically.
That is to say exec can execute complex Python code, unlike the eval function which can only evaluate an expression.
'''

a = eval('1 + 1')
print(a)
formula = '10**2'
b = eval(formula)
print(b)
var_0 = 0
var_1 = 10
var_2 = 20
var_3 = 30
for i in range(4):
    print(b*eval('var_'+str(i)))

line = 'print("sum of 5 and 6 is:",(5+6))'
exec(line)

exec('my_number = 3*4')
print(my_number)
