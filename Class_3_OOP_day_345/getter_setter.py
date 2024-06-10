class Employee:
    def __init__(self):
        self._id = 100

    def get_id(self):
        print('Getter func called.')
        return self._id

    def set_id(self, id):
        print('Setter func called.')
        self._id = id

    def del_id(self):
        del self._id

    id = property(get_id, set_id, del_id)


employee1 = Employee()
employee1.id = 101
print(employee1.id)

employee1.set_id(10)
print(employee1.get_id())
