# 1) None is the value a function returns when there is no return statement in the function

def has_no_return():
    pass

has_no_return()
print(has_no_return())

def difference(value1, value2):
    diff = value1 - value2
    return diff

x = difference(10 ,5)

#print('a diferença é', x)

""" Não há nem sinal da função pois a função difference dá um retorno, porém não faz
# um trabalho de conversa com o usuário"""

"-----------------------------"
# 2) print() itself has no return value. If you try to print a call to print(), then you’ll get None:

# print(print("Hello, world!"))

"-----------------------------"
# 3) None is falsy, which means not None is True. If all you want to know is whether a result is falsy,
# then a test like the following is sufficient:

# some_result = None
# if some_result is True:
#         print("Got a result!")
# else:
#         print("No result.")

"-----------------------------"
# 4) Using None as default Parameter

# def nig_function(new_elem, starter_list=[]):
#     starter_list.append(new_elem)
#     return starter_list
#
# my_list = ['a', 'b', 'c']
# print(nig_function('d', my_list))
# print(nig_function('a'))
# print(nig_function('b'))
# print(nig_function('c'))

# def andre_function(new_elem, starter_list=None):
#     if starter_list is None:
#         starter_list = []
#     starter_list.append(new_elem)
#     return starter_list
#
# my_list = ['a', 'b', 'c']
# print(andre_function('e', my_list))
# print(andre_function('a'))
# print(andre_function('b'))
# print(andre_function('c'))

"-----------------------------"
# 5) Using None as a Null Value in Python - quando None é um objeto de entrada válido

# class DontAppend:
#     pass
#
# def good_function(new_elem=DontAppend, starter_list=None):
#     if starter_list is None:
#         starter_list = []
#     if new_elem is not DontAppend:
#         starter_list.append(new_elem)
#     return starter_list
#
# my_list = ['a', 'b', 'c', 'd', 'e']
# print(good_function(my_list))
#
# print(good_function(None, my_list))

# class KeyNotFound:
#     pass
#
# my_dict = {'a':3, 'b':None, 'c':8}
# for key in ['a', 'b', 'c']:
#     value = my_dict.get(key, KeyNotFound)
#     if value is not KeyNotFound:
#         print(f"{key}->{value}")

""" CONCLUSÃO """
"""None é uma ferramenta poderosa na caixa de ferramentas do Python. Como True e False, None é uma keyword imutável. 
Como o null no Python, você pode utilizá-lo para marcar valores ausentes e resultados, e até mesmo parâmetros padrão 
que é uma escolha muito melhor do que tipos mutáveis."""
