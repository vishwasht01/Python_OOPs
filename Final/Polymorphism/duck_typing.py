##If it walks like a duck and quacks like a duck, it’s a duck
class Bird:
    def fly(self):
        print("Flying in the sky")
class Airplane:
    def fly(self):
        print("Flying in the air")

def lets_fly(thing):
    thing.fly()

lets_fly(Bird())
lets_fly(Airplane())
