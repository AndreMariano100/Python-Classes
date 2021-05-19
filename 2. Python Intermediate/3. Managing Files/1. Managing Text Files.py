'''
Access Modes:
    Read Only (‘r’) :
        Open text file for reading. The handle is positioned at the beginning of the file.
        If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
    Read and Write (‘r+’) :
        Open the file for reading and writing. The handle is positioned at the beginning of the file.
        Raises I/O error if the file does not exists.
    Write Only (‘w’) :
        Open the file for writing. For existing file, the data is truncated and over-written.
        The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
    Write and Read (‘w+’) :
        Open the file for reading and writing. For existing file, data is truncated and over-written.
        The handle is positioned at the beginning of the file.
    Append Only (‘a’) :
        Open the file for writing. The file is created if it does not exist.
        The handle is positioned at the end of the file.
        The data being written will be inserted at the end, after the existing data.
    Append and Read (‘a+’) :
        Open the file for reading and writing. The file is created if it does not exist.
        The handle is positioned at the end of the file.
        The data being written will be inserted at the end, after the existing data.

Create a File "Object":
    file_object = open(r'filename', 'access_mode')

    The file should exist in the same directory as the python program file else,
    full address of the file should be written on place of filename.

    The 'r' is placed before filename to prevent the characters in filename string to be treated as special character.
    For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of
    invalid address. The 'r' makes the string raw, that is, it tells that the string is without any special characters.
    The 'r' can be ignored if the file is in same directory and address is not being placed.
    The 'r' can be ignored when using 'os.path' to describe the filename.

    The file_object works as a handler to the operations performed later.
    It does not contains the data from from the file read.

Operations with the File "Object":
    The data may then be read from the file object with the read() method:
        data = file_object.read()

    The data may also be written to the file object with the write() method:
        file_object.write(data)

    After operating with the file object, it must be closed.
        file_object.close()

Working with sub folders (best practice):
    Determining current folder helps avoid error when moving project folder.
    Consider the following project folder organization on a project.

    project_folder
     |___ text_folder
          |___ text_file_1.txt
     |___ files_folder
     |___ classes_folder
     my_program.py

    'my_program.py' may import from the cited folders by simply stating the following:

        image = open(text_folder/text_file_1.txt)

    In order to avoid conflict when moving the project folder it is important
    to include the full current path to the folder:

        current_path = os.getcwd()

    from this path include the folder and the file_name:

        file_path = os.path.join(current_path, 'text_folder', 'text_file_1.txt')

'''
import os

# # Getting full current path
# current_path = os.getcwd()
# print('Current Path:', current_path)
#
# # Adding the directory and the file name to the path
# full_file_path = os.path.join(current_path, 'Files', 'my_text_file.txt')
# print('Full Path:', full_file_path)

# Open the file - Create the file handler
# 'r' = read only   / 'r+' = read and write
# 'w' = writing     / 'w+' = write and read
# 'a' = append      / 'a+' = append and read

# Reading values from file ---------------------------------------------------------------------------------------------
# file_object = open(full_file_path, 'r')
# print()
# print('File Handler:', file_object)
#
# # File handler methods
# print(f'\tIs the file closed? {file_object.closed}')
# print(f'\tWhat is the "mode" for the file handler? {file_object.mode}')
# print(f'\tWhat is the full name of the file handler? {file_object.name}')
# print(f'\tWhat is the encoding of the file handler? {file_object.encoding}')
# print()

'''
Reading the data from the file: There are three ways to read data from a text file.

    read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
        file_object.read([n])

    readline() : Reads a line of the file and returns in form of a string.
    For specified n, reads at most n bytes. However, does not reads more than one line, 
    even if n exceeds the length of the line.
        file_object.readline([n])

    readlines() : Reads all the lines and return them as each line a string element in a list.
        file_object.readlines()
'''
#
# data = file_object.read()
# print('Using read():')
# print(data)
#
# print('\nUsing readline():')
# file_object.seek(0)
# data_2_1 = file_object.readline()
# print(data_2_1)
# data_2_2 = file_object.readline()
# print(data_2_2)
# data_2_3 = file_object.readline()
# print(data_2_3)
# data_2_4 = file_object.readline()
# print(data_2_4)
# data_2_5 = file_object.readline()
# print(data_2_5)
#
# print('Using readlines():')
# file_object.seek(0)
# data_3 = file_object.readlines()
# print(data_3)
#
# # With a FOR loop you don't use the readline() method.
# print('\nUsing FOR loop:')
# file_object.seek(0)
# for data in file_object:
#     print(data)
#
# # Closing the file
# file_object.close()

# Reading numeric data -------------------------------------------------------------------------------------------------
# file_path = r'Files/my_data_file.txt'
# file_object = open(file_path, 'r')
# data = file_object.readlines()
# print(data)
# print(data[0])
# a, b = data[0].split(', ')
# print('A:', a, 'B:', b)
# print(a+b)
# file_object.close()

# Writing values to file -----------------------------------------------------------------------------------------------
# new_file_path = r'Files/my_text_file_2.txt'
#
# my_title = 'Flange Data\n'
# my_data = {'Flange Pressure': 150,
#            'Flange Diameter': 10,
#            'Flange Schedule': 'STD'}
# additional_data = ['flange face: raised face\n', 'flange type: welding neck\n', 'gasket type: spiral wound\n']
#
# file_object = open(new_file_path, 'w')
#
# # Write a string
# file_object.write(my_title)
#
# # Write many strings
# for k, v in my_data.items():
#     file_object.write(f'{k}: {v} \n')
#
# # Write a list of strings
# file_object.writelines(additional_data)
# file_object.close()

# Closing files --------------------------------------------------------------------------------------------------------

# Once you open, remember to close it
# file_path = r'Files/my_data_file.txt'
# file_object = open(file_path)
# # immediately insert the close method, after that you work with the file
# file_object.close()

# Alternative Method
#     Try: This block will test the excepted error to occur
#     Except:  Here you can handle the error
#     Else: If there is no exception then this block will be executed
#     Finally: Finally block always gets executed either exception is generated or not
file_path = r'Files/my_data_file.txt'
try:
    print('reading file')
    file_object = open(file_path, 'r')
except IOError:
    print('File not read / not found')
else:
    # perform more relevant operation
    print('more relevant operations')
    print('closing the file object')
    file_object.close()
finally:
    print('the code continues on all cases')

# Alternative Method 2
with open(file_path, 'r') as file_object:
    for lines in file_object:
        print(lines, end='')
print()
print(file_object.closed)
