'''
Pickle may be used to save and import more structured data types,
which would be more complicated to convert to and from the string format.

Pickle is used for "serialization" and "de-serialization" of the data (convert the object to and from a byte stream).

"Serialization" can also be performed with JSON and MARSHAL modules.

Important note:
    Json serialization is human readable (use for interoperability with different languages or a human-readable format).
    Pickle serialization is not human readable (use for all other cases).

Reading and writing shall be performed in binary mode: 'wb' and 'rb'.

Syntax:
    pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
        -> creates a file
    pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
        -> returns a string
    pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
    pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)

Never unpickle data that comes from an untrusted source or is transmitted over an insecure network.

'''

# Program Imports ------------------------------------------------------------------------------------------------------
import pickle
import os

# Program Data ---------------------------------------------------------------------------------------------------------
my_dictionary = {'0ne': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4}
my_list = ['value 1', 10.55, [1, 2, 3], (True, False)]

# Saving the Data ------------------------------------------------------------------------------------------------------
path = os.getcwd()
full_file_path = os.path.join(path, 'Files', 'my_data_file.pickle')

file_object = open(full_file_path, 'wb')
pickle.dump((my_dictionary, my_list), file_object)
file_object.close()

# Retrieving the Data --------------------------------------------------------------------------------------------------
file_object = open(full_file_path, 'rb')
my_dictionary_2, my_list_2 = pickle.load(file_object)
file_object.close()

# Comparing the Data ---------------------------------------------------------------------------------------------------
# Comparing the data
print(f'Dict: {my_dictionary_2}')
print(f'List: {my_list_2}')
