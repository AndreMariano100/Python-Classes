import pickle
import os

'''

Pickle shall be used to save and import more structured data types, 
which would be more complicated to convert to and from the string format.

Reading and writing shall be performed in binary mode: 'wb' and 'rb'.

'''

#####################################
# My Data
my_dictionary = {'0ne': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4
                 }

my_list = ['value 1', 10.55, [1, 2, 3], (True, False)]

####################################
# Saving the data
path = os.getcwd()
my_saved_data_path = os.path.join(path, 'Files', 'my_data_file.txt')

file_handler = open(my_saved_data_path, 'wb')
pickle.dump((my_dictionary, my_list), file_handler)
file_handler.close()

####################################
# Reading the data with new names
my_file_data = os.path.join(path, 'Files', 'my_data_file.txt')
pickle_handler = open(my_file_data, 'rb')
my_dictionary_2, my_list_2 = pickle.load(pickle_handler)

####################################
# Comparing the data
print(f'My original dict: {my_dictionary}')
print(f'My dict from file: {my_dictionary_2}')

print(f'My original list: {my_list}')
print(f'My list from file: {my_list_2}')
