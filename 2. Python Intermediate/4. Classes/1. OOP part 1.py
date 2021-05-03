"""
Classes
Serve as instance factories. Their attributes provide behavior—data and functions
—that is inherited by all the instances generated from them.

Instances
Represent the concrete items in a program’s domain. Their attributes record data
that varies per specific object.

"""


# First - Creating a Class ---------------------------------------------------------------------------------------------
class Employee:
    pass


# Main Program ---------------------------------------------------------------------------------------------------------
# Creating instances of the class Employee
employee_1 = Employee()
employee_2 = Employee()
print(employee_1)
print(employee_2)

# Attributes may be created for each instance
employee_1.first_name = 'Paul'
employee_1.last_name = 'Newman'
employee_1.email = 'paul_newman@company.com'

employee_2.first_name = 'Rod'
employee_2.last_name = 'Stewart'
employee_2.email = 'rod_stewart@company.com'

# Attributes may be accessed at any time, for each instance
print(employee_1.email)
print(employee_2.email)
