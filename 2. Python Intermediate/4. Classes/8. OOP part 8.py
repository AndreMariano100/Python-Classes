# Customise sub classes -------------------------------------------------------------------------------------
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
        self.salary = self.salary * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10


# Main Program ---------------------------------------------------------------------------------------------------------
# Instance of developer
dev_1 = Developer('Josh', 'Groslin', 25000)
print(dev_1.salary)
dev_1.apply_raise()
print(dev_1.salary)

