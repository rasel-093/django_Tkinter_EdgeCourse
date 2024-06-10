class Employee:
    company_name = 'Apple'
    
    def __init__(self,id, name):
        self.name = name
        self.id = 100

    def show_details(self):
        print('Name: ', self.name, 'ID: ', self.id)


e1 = Employee(102, 'Khan Shaheb')
e2 = Employee(104, 'Zaman')
e1.show_details()
print(e1.company_name)
print(Employee.company_name)
e2.show_details()

print(e2.company_name)
print(Employee.company_name)

e2.company_name = 'Google'  # Only changes for e2
print(e2.company_name)
print(Employee.company_name)
Employee.company_name = "Google"
print(Employee.company_name)
