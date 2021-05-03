# Customise sub classes -------------------------------------------------------------------------------------
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, salary):
        # self is a convention, ir represents the instance
        # other parameters may be passed during creation
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f'{first.lower()}_{last.lower()}@company.com'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    def __repr__(self):
        """ Something that looks like the object when being created """
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"


# Main Program ---------------------------------------------------------------------------------------------------------
# Instance of Employee
dev_1 = Employee('Josh', 'Groslin', 25000)

print(dev_1)
# Without __repr__
# <__main__.Employee object at 0x00000273AD7D7D00>

# With __repr__
# Employee('Josh', 'Groslin', 25000)

# With __str__
# Josh Groslin - josh_groslin@company.com

"""
Adjust other dunder methods as necessary
__add__ -> +
__sub__ -> -
__mul__ -> *
__truediv__ -> /
__floordiv__ -> //

__gt__  -> >
__ge__  -> >=
__lt__  -> <
__le__  -> <=
__eq__  -> ==
__ne__  -> !=

__len__ -> length

"""