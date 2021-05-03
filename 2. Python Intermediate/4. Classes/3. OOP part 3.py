# Third - Improving a Class ------------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last):
        self._first_name = first
        self._last_name = last
        self.__email = f'{first.lower()}_{last.lower()}@company.com'


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman')
employee_2 = Employee('Rod', 'Stewart')
print(employee_1)
print(employee_2)

# Attributes may be created for each instance
employee_1.salary = 100
employee_2.salary = 200
print(employee_1.salary)
print(employee_2.salary)

# Attributes may be protected
print(employee_1._first_name)
print(employee_1._last_name)
print(employee_1.__email)
