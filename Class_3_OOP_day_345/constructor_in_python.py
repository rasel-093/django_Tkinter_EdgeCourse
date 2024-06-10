
class Person:
    def __init__(self, name, age, occupation, salary, address):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary
        self.address = address

    def details_info(self):     #self is an object
        print('Mr. ', self.name, ' is at: ', self.age, self.occupation,' and his salary is ',  self.salary, self.address)

    def calculate_net_salary(self, rate):
        net_salary = self.salary - self.salary*rate
        return net_salary


# p1 = Person('Rasel',25, 'Admin', 56000.0, 'RUET')
# p2 = Person('khan', 30, 'SW Developer', 643543.0, 'Dhaka')
#
# p1.details_info()
# p2.details_info()
#
# print(p1.calculate_net_salary(.10))

# persons = np.array(
#     [
#         Person('Rasel',25, 'Admin', 56000.0, 'RUET'),
#         Person('khan', 30, 'SW Developer', 643543.0, 'Dhaka')
#
#     ]
# )
#
# for person in persons:
#     person

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def details_info(self):     # self is an object
        print(self.id, self.name,  self.salary)


employees = [
    Employee("Rasel", 1, 500000),
    Employee("Shezan", 2, 400000),
    Employee("Tanzid", 3, 500000),
    Employee("Toufiq", 4, 700000),
    Employee("Mued", 5, 340000),
    Employee("Tanvir", 6, 200000)
]
for employee in employees:
    employee.details_info()
