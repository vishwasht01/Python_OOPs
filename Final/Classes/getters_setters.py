from datetime import datetime

class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email #protected(Access Modifier)
        self.__password=password #private(Access Modifier) can be accessed within class only

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")##if I had to show the date and time at which my email was accessed
                                                    #then I had to change a lot of code so by using getters and setters
                                                    #I can only change that part
        return self._email

    def set_email(self,new_email):
        if "@" in new_email and "." in new_email:
            print(f"Email changed at {datetime.now()}")
            self._email = new_email
        else:
            print("Error Invalid E-mail")

user1 = User("Harshith", "harshith@outlook.com", "12345678")
print(user1.get_email())

user1.set_email("harshu@gmail.com")
print(user1.get_email())

