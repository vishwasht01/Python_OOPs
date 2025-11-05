class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def say_hi(self,other):
        if isinstance(other,User):
            print(f"Hi {other.name}, I am {self.name}")


user1 = User("Vishwas" , "vishwas@gmail.com" , "12345")
user2 = User("Harshith", "harshith@outlook.com", "12345678")

user2.say_hi(user1)

user1.password = "123456789"
print(user1.password) ##So encapsulation_within_classes is created