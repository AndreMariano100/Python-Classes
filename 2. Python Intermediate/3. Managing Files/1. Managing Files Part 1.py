import os

'''
    file = open('filename', 'mode')

Mode may be:    'w' for writing
                'a' for appending
                'r' for reading

'file' in this case is an object that works as a handler to the operations performed later.
'file' does not contains the data from from the file read.

The data may then be read from the file with the read() method:
    data = file.read() 

The data may also be written to the file with the write() method:
    file.write(data)

After operating with the file it must be closed.
    file.close()

Determining current folder helps avoid error when moving project folder.
Consider the following project folder organization on a project.

project_folder
 |___images_folder
      |___image_01.jpg
 |___files_folder
 |___classes_folder
 my_program.py

'my_program.py' may import from the cited folders by simply stating the following:

    image = open(images_folder/image_01.jpg)

In order to avoid conflict when moving the project folder it is important
to include the full current path to the folder:

    current_path = os.getcwd()

from this path include the folder and the file_name:

    file_path = os.path.join(current_path, 'images_folder', 'image_01.jpg')

'''
# Getting full current path
path = os.getcwd()

# Adding the directory and the file name to the path
my_file_path = os.path.join(path, 'Files', 'my_text_file.txt')

# Open file
# 'r' = read only / 'w' = writing / 'a' = append
file_handler = open(my_file_path, 'r')

# # File handler methods
# print(f'Is the file closed? {file_handler.closed}')
# print(f'What is the "mode" for the file handler? {file_handler.mode}')
# print(f'What is the full name of the file handler? {file_handler.name}')
# print()

# #############################################################
# # Method One to Open File
# # Work with file line by line
# contents = []
# print('Traditional Method - Line by Line')
# for line in file_handler:
#     print(line)
#     contents.append(line)
# print()
# print(type(contents))
# print(contents[0])
#
# # Work with file as a whole
# print('Traditional Method - As a Whole')
# file_handler.seek(0)
# contents_2 = file_handler.read()
# print(f'Content: {contents_2}')
# print(type(contents_2))
# print(contents_2[0])
#
# # Close file
# file_handler.close()
# print()

##############################################################
# Method Two
print('Try Except Method')
try:
    file_handler = open(my_file_path, 'r')
    for lines in file_handler:
        print(lines, end='')
    file_handler.close()
    print()

except IOError:
    print('File not read')
finally:
    print()

##############################################################
# Method Three
print('The WITH Method')
with open(my_file_path, 'r') as file_handler:
    for lines in file_handler:
        print(lines, end='')
