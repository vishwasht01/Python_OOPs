from getpass import getpass

class BankAccount:
    def __init__(self,name,balance,password):
        self.name = name
        self.balance=balance
        self.__password=password
        print(f"Welcome {self.name}\n")

    def getBalance(self):
        entered_password = getpass("Enter your Password\n")
        if entered_password == self.__password:
            print(f"Your Balance is ₹{self.balance}\n")
        else:
            print("Entered Password is incorrect\n")