'''
JSON - JavaScript Object Notation

JSON is text, and is the standard format for information exchange.

'''

# Program Imports ------------------------------------------------------------------------------------------------------
import json
import os

# Program Data ---------------------------------------------------------------------------------------------------------
my_dictionary = {'0ne': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4}
my_list = ['value 1', 10.55, [1, 2, 3], (True, False)]

# Saving the Data ------------------------------------------------------------------------------------------------------
path = os.getcwd()
full_file_path = os.path.join(path, 'Files', 'my_data_file.json')

file_object = open(full_file_path, 'w')
json.dump((my_dictionary, my_list), file_object)
file_object.close()

'''
Relevant Keywords
indent=4                -> number of white spaces
separator=(',', ':')    -> separators for the dict like format
'''

# Retrieving the Data --------------------------------------------------------------------------------------------------
file_object = open(full_file_path, 'r')
my_dictionary_2, my_list_2 = json.load(file_object)
file_object.close()

# Comparing the Data ---------------------------------------------------------------------------------------------------
# Comparing the data
print(f'Dict: {my_dictionary_2}')
print(f'List: {my_list_2}')
