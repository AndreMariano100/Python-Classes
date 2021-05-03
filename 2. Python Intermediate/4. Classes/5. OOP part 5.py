# Fifth - Class Variables ------------------------------------------------------------------------------------------
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


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman', 10000)
employee_2 = Employee('Rod', 'Stewart', 20000)

employee_2.apply_raise()
print(employee_2.salary)

# Class attribute (variable)
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

# __dict__ internal method shows everything we got on the instance and on the class ("name space")
print(employee_1.__dict__)
print(Employee.__dict__)

# Class variables may be changed
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(employee_1.raise_amount)

# Instance attributes may be changed independently
employee_1.raise_amount = 1.10
print(employee_1.__dict__)
print(Employee.raise_amount)
print(employee_1.raise_amount)

print(employee_1.salary)
employee_1.apply_raise()
print(employee_1.salary)

print(Employee.number_of_employees)
