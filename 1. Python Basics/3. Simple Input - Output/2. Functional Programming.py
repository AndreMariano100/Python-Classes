# Functional Programming

def read_data():
    value = input('Enter Value: ')
    value = float(value)
    return value


def process_data(value_1, value_2):
    result = value_1 + value_2
    return result


def show_data(result):
    print('Result: ', result)


def main():
    my_first_value = read_data()
    my_second_value = read_data()
    my_result = process_data(my_first_value, my_second_value)
    show_data(my_result)


# Line of code that will be executed
main()
