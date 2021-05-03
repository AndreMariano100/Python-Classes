# Customise sub classes -------------------------------------------------------------------------------------
class Employee:

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        # self.email = f'{first.lower()}_{last.lower()}@company.com'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        self.first_name = ''
        self.last_name = ''

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'


# Main Program ---------------------------------------------------------------------------------------------------------
# Instance of Employee
emp_1 = Employee('Josh', 'Groslin', 25000)
print(emp_1)
print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.full_name)
print(emp_1.email)

emp_1.first_name = 'Jim'
print(emp_1)
print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.full_name)
print(emp_1.email)

# Create an email method, similar to full name method
# Previous reference to email would result in reference to the method, instead of returning the email
# josh_groslin@company.com
# <__main__.Employee object at 0x000001BB9D288FD0>

# Instead of calling the method with parenthesis, add the property decorator
# josh_groslin@company.com

# Same works with the full name method

# Property decorator does not allow changes from within the code
# A setter decorator may be added, with the same method name
emp_1.full_name = 'Robert Cray'
print(emp_1)
print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.full_name)
print(emp_1.email)

del emp_1.full_name
print(emp_1.email)
