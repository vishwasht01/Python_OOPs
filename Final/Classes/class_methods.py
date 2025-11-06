class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        return cls(name, current_year - birth_year)

alice = Student.from_birth_year("Alice", 2000)
print(alice.name, alice.age)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def create(cls, brand):
        return cls(brand)

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.type = "Car"

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.type = "Bike"

car = Car.create("BMW")
bike = Bike.create("Yamaha")

print(car.brand, car.type)
print(bike.brand, bike.type)##Even though create() is defined in the parent class,
                            ##cls automatically refers to the subclass that called it.
