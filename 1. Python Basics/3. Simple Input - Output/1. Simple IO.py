# Read two values from the user
# Add the values and show the result

# Part 1 - Input
# variable = input('prompt')

outside_diameter = input('Enter the pipe diameter [mm]: ')
thickness = input('Enter the pipe thickness [mm]: ')

# Part 2 - Perform the Data Processing

outside_diameter = float(outside_diameter)
thickness = float(thickness)
internal_diameter = outside_diameter - 2 * thickness

# Part 3 - Show the Result
# print(result)
print('Internal diameter:', internal_diameter)
