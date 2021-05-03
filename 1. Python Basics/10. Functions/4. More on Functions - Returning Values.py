# Functions -----------------------
def squared(number):
    square = number ** 2
    return square


def squared_and_doubled(number):
    square = number ** 2
    doubled = 2 * number
    return square, doubled


# Main program --------------------
x = squared(2)
y = squared(3)
z = squared(5)
print(x, y, z)

x_1, x_2 = squared_and_doubled(2)
y_1, y_2 = squared_and_doubled(3)
z = squared_and_doubled(5)
print(x_1, x_2)
print(y_1, y_2)
print(z)
