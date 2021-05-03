# Sixth - Class / Static Methods -------------------------------------------------------------------------------------
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

    # Class method affects all instances at once
    @classmethod
    def set_new_raise(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_even(number):
        return not number % 2


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman', 10000)
employee_2 = Employee('Rod', 'Stewart', 20000)

# Class attribute (variable)
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

# Access class method
Employee.set_new_raise(1.10)
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

# employee_1.raise_amount = 1.20
# print(employee_1.raise_amount)
# Employee.set_new_raise(1.10)
# print(Employee.raise_amount)
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)

print(Employee.is_even(2))
print(employee_1.is_even(3))
print(employee_2.is_even(4))