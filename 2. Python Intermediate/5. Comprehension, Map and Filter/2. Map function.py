# MAP

numbers = [10, 15, 21, 33, 42, 55]
numbers2 = []
for i in numbers:
    x = i*2
    numbers2.append(x)
print(f'numbers2', numbers2)


# MAP permite processar e transformar todos os itens em um interaçao sem usar um loop explicito.
# É util quando quiser aplicar a cada item de uma interação uma funçao.

numbers = [10, 15, 21, 33, 42, 55]
mapped_numbers = map(lambda x: x*2, numbers)
print(f'mapped_numbers', mapped_numbers)

numbers = [10, 15, 21, 33, 42, 55]
mapped_numbers = list(map(lambda x: x*2, numbers))
print(f'mapped_numbers', mapped_numbers)

mapped_numbers2 = list(map(lambda x: x*2, [10, 15, 21, 33, 42, 55]))
print(f'mapped_numbers2', mapped_numbers2)
#
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

number_powers = list(map(pow, base_numbers, powers))
print(f'number_powers', number_powers)
#
# para de calcular assim que atinge o menor

base_numbers = [2, 4, 6, 8, 10, 12]
powers = [1, 2, 3, 4, 5]
number_powers = list(map(pow, base_numbers, powers))
print(f'number_powers', number_powers)
#
words = ['Atirei', 'o', 'pau', 'no', 'gato']
len_words = list(map(len, words))
print(f'len_words', len_words)
maiuscula = list(map(str.upper, words))
print(f'maiuscula', maiuscula)
#
# #
def my_func(a, b):
    return a + b


a = ['apple', 'banana', 'cherry']
b = ['orange', 'lemon', 'pineapple']
y = list(map(my_func, a, b))
x = list(map(my_func, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
print(x)
print(f'y', y)
#
map_dict = {'ovos': 12, 'bananas': 15, 'laranjas': 20}
key_list = list(map(lambda value: value*2, map_dict.values()))
len_keys = list(map(len, map_dict.keys()))
print(key_list)
print(len_keys)