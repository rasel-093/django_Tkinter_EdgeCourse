class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def employee_details(self):
        print('Mr. ', self.name, 'having id: ', self.id)


class Programmer(Employee):
    def display_programmer(self):
        print('Mr. ', self.name, 'having id: ', self.id)

# self is a keyword in python used for instant object.
# Data abstraction -> Method can't be accessed without creating object.


e1 = Employee('Khan', 101)
e2 = Employee('Zaman', 103)
e2.employee_details()
p1 = Programmer('Musa', 1112)
p1.display_programmer()
p1.employee_details()
