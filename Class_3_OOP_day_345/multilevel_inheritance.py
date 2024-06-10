class Employee:
    def __init__(self, name, id):
        self.name = name
        self.__id = id  # Id is private now (using double underscore

    def employee_details(self):
        print('Mr. ', self.name, 'having id: ', self.id)


class Developer(Employee):
    def __init__(self, name, id, salary):
        self.salary = salary
        Employee.__init__(self, name, id)

    def developer_details(self):
        print(self.id, self.salary)


class PythonDeveloper(Developer):
    def __init__(self, name, id, salary, framework):
        self.framework = framework
        Developer.__init__(self, name, id, salary)
        Employee.__init__(self, name, id)

    def python_developer_details(self):
        print('Mr. ', self.name, 'is a ', self.framework , 'developer')


if __name__ == '__main__':
    pythondev = PythonDeveloper('Rasel', 93, 57000, 'DJango')
    pythondev.python_developer_details()
    pythondev.developer_details()
    pythondev.employee_details()  # Multilevel used
    # print(pythondev.__id) # will show error
# Hierarcical