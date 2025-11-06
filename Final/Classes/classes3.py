class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine() #composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

car = Car()
car.drive()