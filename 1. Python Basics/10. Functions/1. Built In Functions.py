'''
Built-in functions come with Python, such as:
Name 	        Description
abs() 	        The abs() function is used to get the absolute (positive) value of a given number.
all() 	        The all() function is used to test whether all elements of an iterable are true or not.
any() 	        The any() function returns True if any element of the iterable is true.
                The function returns False if the iterable is empty.
ascii() 	    The ascii() function returns a string containing a printable representation
                (escape the non-ASCII characters ) of an object.
bin() 	        The bin() function is used to convert an integer number to a binary string.
                The result is a valid Python expression.
bool() 	        The bool() function is used to convert a value to a Boolean.
breakpoint()    This function drops you into the debugger at the call site.
bytearray() 	The bytearray() function is used to get a bytearray object.
bytes() 	    The bytes() function is used to get a new 'bytes' object.
callable() 	    The callable() function returns True if the object argument appears callable, False if not.
chr() 	        The chr() function returns the string representing a character whose Unicode codepoint is the integer.
classmethod() 	The classmethod() function is used to convert a method into a class method.
compile() 	    The compile() function is used to compile the source into a code.
complex() 	    The complex() function is used to create a complex number or convert a string or number
                to a complex number.
delattr() 	    The delattr() function is used to delete the specified attribute from the specified object.
dict() 	        The dict() function is used to create a new dictionary.
dir() 	        The dir() function returns all properties and methods of the specified object, without the values.
                The function will return all the properties and methods, even built-in properties which are default
                for all object.
divmod() 	    The divmod() function takes two non complex numbers as arguments and return a pair of numbers
                consisting of their quotient and remainder when using integer division. With mixed operand types,
                the rules for binary arithmetic operators apply.
enumerate() 	The enumerate() function returns an enumerate object. iterable must be a sequence, an iterator,
                or some other object which supports iteration.
eval() 	        The eval() function is used to evaluate the specified expression. If the expression is a correct
                Python statement, it will be executed.
exec() 	        The exec() function is used to execute the specified Python code. object must be either a string
                or a code object.
filter() 	    The filter() function construct an iterator from those elements of iterable for which
                function returns true.
float() 	    The float() function is used to convert the specified value into a floating point number.
format() 	    The format() function is used to format a specified value into a specified format.
frozenset() 	The frozenset() function returns a new frozenset object, optionally with elements taken from iterable.
getattr() 	    The getattr() function returns the value of the named attribute of object and name must be a string
globals() 	    The globals() function returns a dictionary representing the current global symbol table.
hasattr()       Returns True if the specified object has the specified attribute (property/method)
hash() 	        The hash() function returns the hash value of the object (if it has one).
help() 	        The help() function is used to execute the built-in help system.
hex() 	        The hex() function converts an integer number to a lowercase hexadecimal string prefixed with "0x".
id()         	The id() function is used to get the identity of an object.
input() 	    The input() function allows user input. If the prompt argument is present, it is written to
                standard output without a trailing newline.
int() 	        The int() function converts the specified value into an integer number.
isinstance() 	The isinstance() function returns true if the object argument is an instance of the classinfo argument,
                or of a subclass thereof.
issubclass() 	The issubclass() function returns true if the specified object is a subclass of the specified object,
                otherwise false. A class is considered a subclass of itself.
iter() 	        The iter() function returns an iterator object.
len() 	        The len() function is used to get the length of an object.
list() 	        The list() function is used to create a list object (list is actually a mutable sequence type).
locals() 	    The locals() function is used to get the local symbol table as a dictionary. Free variables
                are returned by locals() when it is called in function blocks, but not in class blocks.
map() 	        The map() function is used to execute a specified function for each item in a iterable.
max() 	        The max() function is used to find the item with the largest value in an iterable.
memoryview() 	The memoryview() function is used to get a memory view object from a specified object.
min() 	        The min() function is used to find the item with the smallest value in an iterable.
next() 	        The next() function is used to get the next item in an iterator.
object() 	    The object() function is used to create an empty object.
oct() 	        The oct() function is used to convert an integer number to an octal string.
open() 	        The open() function is used to open a file and returns it as a file object.
ord() 	        The ord() function is used to get an integer representing the Unicode code point of that character.
pow() 	        The pow() function is used to get the value of x to the power of y (xy). If z is present,
                return x to the power y, modulo z (computed more efficiently than pow(x, y) % z).
print() 	    The print() function is used to print objects to the text stream file, separated by sep and
                followed by end. sep, end and file, if present, must be given as keyword arguments.
property() 	    The property() function return a property attribute.
range() 	    The range() function is used to get a sequence of numbers, starting from 0 by default, and
                increments by 1 by default, and ends at a specified number.
repr() 	        The repr() function returns a string containing a printable representation of an object.
reversed() 	    The reversed() function is used to get a reverse iterator.
round() 	    The round() function returns the rounded floating point value number, rounded to ndigits
                digits after the decimal point. If ndigits is omitted, it defaults to zero.
set() 	        The set() function is used to create a set object.
setattr() 	    The setattr() function is used to set the value of the specified attribute of the specified object.
slice() 	    The slice() function is used to get a slice object representing the set of indices specified
                by range(start, stop, step).
sorted() 	    The sorted() function is used to get a new sorted list from the items in iterable.
staticmethod()  Transform a method into a static method.
str() 	        The str() function is used to convert the specified value into a string.
sum() 	        The sum() function is used to get the sum of all items in an iterable.
super()         Returns an object that represents the parent class
tuple() 	    The tuple() function is used to create a tuple in Python. Iterable may be a sequence, a container
                that supports iteration, or an iterator object.
type() 	        The type() function is used to get the type of an object.
vars() 	        The vars() function is used to get the __dict__ attribute of the given object.
zip() 	        The zip() function is used to make an iterator that aggregates elements from each of the iterables.
__import__()

Functions are easily identified by the parenthesis at the end.

Functions may be imported from modules, such as math
'''
