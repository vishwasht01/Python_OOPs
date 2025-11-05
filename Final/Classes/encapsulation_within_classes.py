class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email #protected(Access Modifier)
        self.__password=password #private(Access Modifier) can be accessed within class only

    def clean_email(self):
        return self._email.lower().strip()

    def get_email(self):
        return self._email


user1 = User("Harshith", " Harshith@outlook.com ", "12345678")
print(user1.clean_email())


print(user1._email) ##Though it is Protected Python dosen't enforce restriction to access this.

user1._email = "harshith@gmail.com"
print(user1._email)

##print(user1__password) Not Possible as Python change __password to anything this step is called NameMangling

