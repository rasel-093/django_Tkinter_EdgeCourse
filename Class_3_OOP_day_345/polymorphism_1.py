def add(x, y, z = 0):
    return x+y+z


print(add(2, 3))
print(add(2, 3, 4))


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print('Most of the birds can fly but some can not')


class Sparrow(Bird):
    def flight(self):
        print('Sparrow can fly')  # Method overriding


class Ostrich(Bird):
    def flight(self):
        print('Ostriches can not fly.')


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()


obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

