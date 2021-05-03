import csv
import os

'''
CSV is the most common format for spreadsheets and databases.
Columns are separated with commas, and rows are separated by line breaks.
'''

####################################
# getting the full path
path = os.getcwd()
my_data_path = os.path.join(path, 'Files', 'my_csv_file.csv')

####################################
# Reading the data
with open(my_data_path) as csv_handler:
    data = []
    csv_data = csv.reader(csv_handler, delimiter=';')
    for row in csv_data:
        data.append(row)

print(data)
'''
Each row is returned as a list of strings
'''
####################################
# Reading into a dictionary
with open(my_data_path) as csv_handler:
    csv_dict = csv.DictReader(csv_handler, delimiter=';')
    for row in csv_dict:
        print(row)

####################################
# Writing data
new_data_path = os.path.join(path, 'Files', 'new_csv_file.csv')
new_data = [['Andrew', 'andrew@gmail.com', '555-0010'],
            ['George', 'george@gmail.com', '555-0011'],
            ['Leonard', 'leonard@gmail.com', '555-0002'],
            ['Carol', 'carol@gmail.com', '555-0003']]

with open(new_data_path, mode='w', newline='') as new_csv_handler:
    data_writer = csv.writer(new_csv_handler, delimiter=';')
    for item in new_data:
        data_writer.writerow(item)
