class Person:
    name = 'Mr. Khan'
    age = 23
    occupation = 'Data Scientist'
    salary = 234350.00
    address = 'Talaimari'
    reduction = 0.10

    def details_info(self):     #self is an object
        print('Mr. ', self.name, ' is at: ', self.age, self.occupation,' and his salary is ',  self.salary, self.address)

    def calculate_net_salary(self):
        net_salary = self.salary - self.salary*self.reduction
        return net_salary



p1 = Person()
print(type(p1))  # Creating an instance: Object
# print(p1.name, p1.age, p1.occupation, p1.salary, p1.address)
#
p2 = Person()
p2.name = 'Zaman'
p2.age = 30
p2.occupation = 'Android developer'
p2.address = 'RUET'
p2.reduction = 0.15
# print(p2.name, p2.address)
p1.details_info()
p2.details_info()
# netSal = p1.calculate_net_salary(.10)
# print(netSal)

print(p2.calculate_net_salary())
