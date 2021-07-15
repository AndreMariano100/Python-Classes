# Working with string
# Create strings
my_string_0 = ''
my_string_1 = 'Strings may be created with single quotes'
my_string_2 = "Strings can also be created with double quotes"
my_string_3 = "Use double quotes whenever there's a single quote within the string"
my_string_4 = 'Use single quote whenever there is a "double quote" within the string'
my_string_5 = 'You can use special characters\nwithin the string'
my_string_6 = '''You can even have strings 
within triple quotes.
Very handy with very long strings'''

for i in range(7):
    print('my_string_'+str(i))

# Check the type: <class 'str'>
print(type(my_string_0))

# You may convert other types to string
a = [0, 1, 2, 3]
str_a = str(a)
print(str_a)
print(type(str_a))

# Basic string operations
# Concatenate and multiply
string_1 = 'rain'
string_2 = 'coat'
string_3 = string_1+string_2
print(string_3)
string_4 = 'bark! '
string_5 = 5 * string_4
print(string_5)

# in, not in
result = string_1 in string_3
print(result)
result = string_1 not in string_5
print(result)

# String comparison
# >, <, <=, >=, ==, !=
# Comparison via the ASCII value
print('A' > 'B')

# Built in Functions
print('String:', string_3)
print('len(), max(), min()')
print(len(string_3))
print(max(string_3))
print(min(string_3))

# Access by index
for i in range(len(string_3)):
    print(string_3[i], end='-')

# Slicing
print()
print(string_3[0:4])
print(string_3[4:len(string_3)])
print(string_3[:])
print(string_3[:4])
print(string_3[4:])

# Joining
name = 'Robert'
surname = 'Downey'
full_name = ' / '.join([name, surname])
print(full_name)

# Spliting
print(my_string_1)
words = my_string_1.split()
print(words)

# Immutable
try:
    my_string_1[0] = 'A'
except TypeError:
    print('Strings are immutable')

