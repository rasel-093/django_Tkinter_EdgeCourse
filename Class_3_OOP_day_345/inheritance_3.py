
# Type of inheritance
# multiple -> Multiple parents
# multilevel -> GrandParent -> Parent -> Child

class Animal:
    def __init__(self, origin, pet):
        self.origin = origin
        self.pet = pet

    def display_animal(self):
        if self.pet == True:
            print('This is a ', self.origin, ' pet animal')
        else:
            print('This is a ', self.origin, ' non pet animal')


class DetectiveAgents:
    def __init__(self, name):
        self.name = name

    def display_detective(self):
        if self.type == 1:
            print(self.name, 'is a good detective agent')
        else:
            print(self.name,' is not a good detective agent')


class Dog(Animal, DetectiveAgents):
    def __init__(self, name, type, origin, pet):
        self.name = name
        self.type = type
        self.origin = origin
        self.pet = pet

    def print_dog_info(self):
        super().display_animal()
        super().display_detective()


d1 = Dog('RAHU', 1, 'German', True)
d1.print_dog_info()
