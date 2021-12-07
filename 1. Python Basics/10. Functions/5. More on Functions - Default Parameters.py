# Functions -----------------------
def greetings(name='John', surname='Doe', age='30'):
    print(f'First Name: {name}, Last Name: {surname}, Age: {age}')


"""
Non default parameters are mandatory when calling the method.
Default parameters allow to call the method with no values informed.
*args must come before **kwargs in the method header.
"""
greetings('Fabio', 'Marangone', age='28')

# Main program --------------------
# greetings()
#
# greetings(name='Daniel', surname='Clyde')
# greetings(age='40', name='Paul', surname='Whitacker')
# greetings(surname='Third', age='110', name='Amenadiel')
# greetings()

"""
keyword (**kwargs) arguments may be passed in any order
"""

# greetings('Barbara', 'Smith', '25')
# greetings('Kate', '35', 'Brown')
#
# my_data_dict = {'name': 'John',
#                 'surname': 'Paul Johnes',
#                 'age': 100}
#
# my_data_list = ['Morgan', 'Freeman', '60']
#
# greetings(*my_data_list)
# greetings(**my_data_dict)
"""
Arguments (*args) must be passed in the right order
"""