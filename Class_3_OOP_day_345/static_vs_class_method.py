# Memory management concept

class Math:
    def __init__(self):
        initial = 0

    def square(self, x):
        return x**2


    @staticmethod  # Decorator  # More memory efficient # No instance # No relation with instance
    def add(x, y):
        return  x+y

    @classmethod        # No need to create object to use method
    def division(cls, x, y):
        return  x/y


a1 = Math()
print(a1.square(9.0))

print(a1.division(3,4))
print(Math.division(3, 4))
print(a1.division(9, 5))
print(Math.division(9, 5))

# Standalone function , vs static function
# Class oriented method
# object oriented method
# class variable vs instance variable
