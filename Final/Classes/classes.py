class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Owner:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number


owner1 = Owner("Mitch","999")
dog1 = Dog("Charlie","Pitbull",owner1)

owner2=Owner("Phil","888")
dog2 = Dog("Scotty","BullDog",owner2)

print(dog1)
print(dog1.owner.name)

print(dog2.owner.phone_number)

