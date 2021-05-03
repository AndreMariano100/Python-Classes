def show_numbers(*args):
    for arg in args:
        print(arg)


show_numbers(0)
show_numbers(10, 20, 30, 40, 50)

new_numbers = [100, 200, 300]
show_numbers(new_numbers)
show_numbers(*new_numbers)


def show_content(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f'Key: {key}, Value: {value}')


my_list = ['a', 'b', 'c']
my_dict = {'Name': 'John',
           'Surname': 'Doe',
           'Age': '30'}
show_content(*my_list, **my_dict)
show_content('Banana', 'Apple', 'Orange', city='Rio', country='Brazil')
