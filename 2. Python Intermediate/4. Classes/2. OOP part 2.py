# Second - Improving a Class ------------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last):
        # __init__ method runs every time an instance is created
        # self is a convention, it represents the instance
        # other parameters may be passed during creation
        self.first_name = first
        self.last_name = last
        self.email = f'{first.lower()}_{last.lower()}@company.com'


# Main Program ---------------------------------------------------------------------------------------------------------
# Instances of the class Employee
employee_1 = Employee('Paul', 'Newman')
# the name "employee_1" is secretly passed to the class Employee (the "self" in the init method)

employee_2 = Employee('Rod', 'Stewart')
employee_3 = Employee(first='Barbra', last='Streisand')

print(employee_1)
print(employee_2)
print(employee_3)

# Attributes may be created for each instance
employee_1.salary = 100
employee_2.salary = 200
print(employee_1.salary)
print(employee_2.salary)

# Attributes may be accessed for each instance
print(employee_1.first_name)
print(employee_1.last_name)
print(employee_1.email)
print(employee_2.email)
