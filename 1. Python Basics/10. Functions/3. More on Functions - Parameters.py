# Functions -----------------------
def print_hello(name):
    print('Hello', name)


def print_message(message):
    print('I am', message)


def print_bye():
    print('Bye')


def full_message(name, message):
    # print_hello(name)
    # print_message(message)
    # print_bye()
    print('Hello', name, '\nI am', message, '\nBye')


# Main program --------------------
print_hello('Paul')
print_message('excited!')
print_bye()

full_message('Paul', 'excited!')

parameters = ['John', 'tired!']
full_message(*parameters)

"""
arguments (*args) shall be passed on the right order
"""