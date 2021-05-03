# Fourth - Creating methods -----------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.email = f'{first.lower()}_{last.lower()}@company.com'

        """
        Important: all attributes should be created at the init method
        """

    def full_name(self):
        print(f'Employee full name: {self.first_name} {self.last_name}')

    def full_name_2(self):
        return f'Employee full name: {self.first_name} {self.last_name}'

    def show_email(self):
        return self.email


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman')
employee_2 = Employee('Rod', 'Stewart')

# No parenthesis needed to access attributes
print(employee_1.last_name)

# Parenthesis needed to access methods
employee_1.full_name()
print(employee_2.full_name_2())

# Method vs attribute
print(employee_1.email)
print(employee_1.show_email())

"""
The instance name is secretly passed when accessing methods
    employee_1.full_name is actually converted to 
    Employee.full_name(employee_1) -> (self) 
"""

