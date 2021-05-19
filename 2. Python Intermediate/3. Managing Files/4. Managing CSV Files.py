'''
CSV (comma separated values) is the most common format for a plain text that resembles tabular data.
Columns are separated with commas, and rows are separated by line breaks.

Example:
    column 1, columns 2, columns 3
    data_01, data_02, data_03
    data_11, data_12, data_13
    data_21, data_22, data_23
    data_31, data_32, data_33

The first line is usually the header for the data.
The separator may be specified (must be known):
    ',', comma
    '\t', tab
    ':', colon
    ';', semi-colon

'''

# Program imports ------------------------------------------------------------------------------------------------------
import csv
import os

# File path ------------------------------------------------------------------------------------------------------------
path = os.getcwd()
my_data_path = os.path.join(path, 'Files', 'my_data_file.csv')


# Reading the data as a list of lists ----------------------------------------------------------------------------------
with open(my_data_path) as file_object:
    my_data = []
    csv_data = csv.reader(file_object, delimiter=',')
    for row in csv_data:
        my_data.append(row)

print(my_data)
print(type(my_data))

# Reading the data as a list of dictionaries ---------------------------------------------------------------------------
with open(my_data_path) as csv_handler:
    my_data = []
    csv_dict = csv.DictReader(csv_handler, delimiter=',')
    for data in csv_dict:
        my_data.append(data)

print(my_data)
print(type(my_data))

"""
The first line of the CSV file is assumed to contain the keys to use to build the dictionary. If you don’t have these 
in your CSV file, you should specify your own keys by setting the fieldnames optional parameter to a list containing 
them.
"""

# Writing data from a list ---------------------------------------------------------------------------------------------
new_data_path = os.path.join(path, 'Files', 'ny_data_file_2.csv')
new_data = [['Andrew', 'andrew@gmail.com', '555-0010'],
            ['George', 'george@gmail.com', '555-0011'],
            ['Leonard', 'leonard@gmail.com', '555-0002'],
            ['Carol', 'carol@gmail.com', '555-0003']]

with open(new_data_path, mode='w', newline='') as file_object:
    data_writer = csv.writer(file_object, delimiter=',')
    for item in new_data:
        data_writer.writerow(item)

# Writing data from a dictionary ---------------------------------------------------------------------------------------
new_data_path = os.path.join(path, 'Files', 'ny_data_file_3.csv')
new_data = [{'name': 'Andrew', 'email': 'andrew@gmail.com', 'phone': '555-0010'},
            {'name': 'George', 'email': 'george@gmail.com', 'phone':  '555-0011'},
            {'name': 'Leonard', 'email': 'leonard@gmail.com', 'phone':  '555-0002'},
            {'name': 'Carol', 'email': 'carol@gmail.com', 'phone':  '555-0003'}]
field_names = ['name', 'email', 'phone']

with open(new_data_path, mode='w', newline='') as file_object:
    data_writer = csv.DictWriter(file_object, delimiter=';', fieldnames=field_names)
    data_writer.writeheader()
    for item in new_data:
        data_writer.writerow(item)
