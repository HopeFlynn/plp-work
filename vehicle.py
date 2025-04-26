# Base Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"The {self.brand} {self.model} is moving...")


# Subclass 1
class Car(Vehicle):
    def move(self):
        print(f"The {self.brand} {self.model} is driving on the road! 🚗")


# Subclass 2
class Plane(Vehicle):
    def move(self):
        print(f"The {self.brand} {self.model} is flying in the sky! ✈️")


# Subclass 3
class Bicycle(Vehicle):
    def move(self):
        print(f"The {self.brand} {self.model} is pedaling along! 🚲")


# Creating a list of different vehicle objects
vehicles = [
    Car("Toyota", "Corolla"),
    Plane("Boeing", "747"),
    Bicycle("Giant", "Escape 3")
]

# Demonstrate Polymorphism
for v in vehicles:
    v.move()
