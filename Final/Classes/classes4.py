class User:
    user_count = 0 ##Static / Class attribute

    def __init__(self,name,email):
        self.name=name
        self.email=email
        User.user_count+=1
        self.id = f"empU{User.user_count}"


user1 = User("Vishwas" , "vishwas@gmail.com")
user2 = User("Harshith", "harshith@outlook.com")

print(User.user_count)
print(user1.user_count) ##class attribute accessed via object
print(user1.id)
print(user2.id)