# Seventh - Inheritance -------------------------------------------------------------------------------------
class Employee:

    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f'{first.lower()}_{last.lower()}@company.com'
        Employee.number_of_employees += 1

    def full_name(self):
        print(f'Employee full name: {self.first_name} {self.last_name}')

    def apply_raise(self):
        self.salary = self.salary * Employee.raise_amount
        # self.salary = self.salary * self.raise_amount


class Developer(Employee):
    pass


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman', 10000)
employee_2 = Employee('Rod', 'Stewart', 20000)
print(employee_1.email)
print(employee_2.email)

# Instance of developer
dev_1 = Developer('Josh', 'Groslin', 25000)
print(dev_1.email)
print(help(Developer))

"""
Help on class Developer in module __main__:

class Developer(Employee)
 |  Developer(first, last, salary)
 |  
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |  
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, salary)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  apply_raise(self)
 |  
 |  full_name(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |  
 |  number_of_employees = 3
 |  
 |  raise_amount = 1.04

None
"""