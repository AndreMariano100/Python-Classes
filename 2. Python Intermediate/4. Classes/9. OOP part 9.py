# Customise sub classes -------------------------------------------------------------------------------------
class Employee:

    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, salary):
        # self is a convention, ir represents the instance
        # other parameters may be passed during creation
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

    def __init__(self, first, last, salary, language):
        super().__init__(first, last, salary)
        # Employee.__init__(self, first, last, salary)
        self.language = language


# Main Program ---------------------------------------------------------------------------------------------------------
# Instance of developer
dev_1 = Developer('Josh', 'Groslin', 25000, 'Java')
print(dev_1.email)
print(dev_1.language)

print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))

print(issubclass(Developer, Employee))
