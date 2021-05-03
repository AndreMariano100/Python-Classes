"""
Global variables can be accessed anywhere, and modified anywhere.
Local variables exist within the local scope of the functions, and cannot be accessed from out of the function.

TIP: minimize the use of global variables.
"""


# Functions ---------------------------------
def my_function():
    my_value = 200
    print(f'My Value: {my_value}')

# Main Program ------------------------------
my_value = 20
my_function()
print(f'My main value: {my_value}')