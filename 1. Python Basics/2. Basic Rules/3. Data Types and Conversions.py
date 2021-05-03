'''
Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
    Text Type: 	        str
    Numeric Types: 	    int, float, complex
    Sequence Types: 	list, tuple, range
    Mapping Type: 	    dict
    Set Types: 	        set, frozenset
    Boolean Type: 	    bool
    Binary Types: 	    bytes, bytearray, memoryview

Setting the data type occurs naturally, during assignment to a variable
    x = "Hello World" 	                str
    x = 20 	                            int
    x = 20.5 	                        float
    x = 1j 	                            complex
    x = ["apple", "banana", "cherry"] 	list
    x = ("apple", "banana", "cherry") 	tuple
    x = range(6) 	                    range
    x = {"name" : "John", "age" : 36} 	dict
    x = {"apple", "banana", "cherry"} 	set
    x = frozenset({"apple",
                   "banana",
                   "cherry"})       	frozenset
    x = True 	                        bool
    x = b"Hello" 	                    bytes
    x = bytearray(5) 	                bytearray
    x = memoryview(bytes(5)) 	        memoryview
'''

# ############################################################################
# # Definition of data type happens on assignment (dynamically typed language)
# # Use the type() function to check on the current data type
# x = 'text'
# print(type(x))  # <class 'str'>
#
# x = 0
# print(type(x))  # <class 'int'>
#
# x = 0.0
# print(type(x))  # <class 'float'>
#
# x = True
# print(type(x))  # <class 'bool'>
#
# x = {}
# print(type(x))  # <class 'dict'>
#
# x = []
# print(type(x))  # <class 'list'>
#
# x = ()
# print(type(x))  # <class 'tuple'>
#
# ##################################################################
# # Digging into data types
#
# # Numbers
# # int, long, float, complex
# x = 10
# y = 51667292876
# Z = 20.0
# w = 0.867j
#
# # Strings
# my_str = 'Hello World!'
#
# # Lists
# my_list = [1.2, 10, 'a string', [0, 1, 2, 3, 4], 0.234j]
#
# # Reference to a item of a list is made with the item index
# # Lists always start at index 0
#
# print(my_list[0])     # 1.2
# print(my_list[1])     # 10
# print(my_list[3])     # [0, 1, 2, 3, 4]
# print(my_list[3][4])  # 4
#
# # Tuples
# tpl = (1.2, 10, 'string', [0, 1, 2, 3, 4], 0.234j)
#
# # Dictionaries
# dct = {'Name': 'John', 'Age': 30, 'Nationality': 'Belgium'}

# ##################################################################
# # Conversions - Use any of the following conversion functions

# # Converts x to an integer. base specifies the base if x is a string
# int(x [,base])

print(int(3.7))
print(int('5'))

# # Converts x to a floating-point number
# float(x)

print(float(4))
print(float('5'))

# # Converts object x to a string representation.
# str(x)
print(str(5.0))
print(str(2))

# # Converts an integer to a character.
# chr(x)
for i in range(256):
    print(chr(i), end=',')

# # Converts x to a long integer. base specifies the base if x is a string.
# long(x [,base] )
#
# # Creates a complex number.
# complex(real [,imag])
#
# # Converts object x to an expression string.
# repr(x)
#
# # Evaluates a string and returns an object.
# eval(str)
#
# # Converts s to a tuple.
# tuple(s)
#
# # Converts s to a list.
# list(s)
#
# # Converts s to a set.
# set(s)
#
# # Creates a dictionary. d must be a sequence of (key,value) tuples.
# dict(d)
#
# # Converts s to a frozen set.
# frozenset(s)
#
# # Converts an integer to a Unicode character.
# unichr(x)
#
# # Converts a single character to its integer value.
# ord(x)
#
# # Converts an integer to a hexadecimal string.
# hex(x)
#
# # Converts an integer to an octal string.
# oct(x)
