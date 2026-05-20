class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


c1 = Car("Ford", "Mustang")
# c1.move()
b1 = Boat("Yamaha", "242X")
# b1.move()
p1 = Plane("Boeing", "747")
# p1.move()
# Polymorphism allows us to use the same method name for different types of objects. In the above example, we have defined a method called move() in each of the three classes. When we call the move() method on an object, Python will determine which class it belongs to and execute the appropriate method.
for x in (c1, b1, p1):
    x.move()
