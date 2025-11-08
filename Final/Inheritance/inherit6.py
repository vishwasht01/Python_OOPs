##Inheritance implies “IS-A” relationship
class Engine:
    def start(self): print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition(HAS-A)

    def drive(self):
        self.engine.start()
        print("Car moving")


