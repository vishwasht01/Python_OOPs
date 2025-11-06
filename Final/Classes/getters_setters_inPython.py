class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email #protected(Access Modifier)
        self.__password=password #private(Access Modifier) can be accessed within class only

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
        else:
            print("Error Invalid E-mail")

    # -------------------------
    # Password Getter (controlled)
    # -------------------------

    @property
    def password(self):
        # ⚠️ Do NOT return actual password in real systems!
        return "*" * len(self.__password)  # masked version

    # -------------------------
    # Password Setter (secure)
    # -------------------------
    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            print("Password too short! Must be at least 6 characters.")
        else:
            self.__password = new_password



user = User("Vishwas","vishu@gmail.com","1233499")
user.email = "vishu@outlook.com"
print(user.email)

print(user.password)
user.password = "1234567890"
print(user.password)