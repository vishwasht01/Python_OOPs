##Static method belongs to the class itself rather than any instance of a class
##Static methods do not take self as a parameter meaning that they cannot access or modify instance specific data
class BankAccount:
    min_Bal = 100
    def __init__(self,name,balance=0):
        self.name=name
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"{self.name}'s new balance is : {self._balance}")
        else:
            print("Add valid amount")

    @staticmethod ## Belongs to BankAccount class dosen't get any input parameters like cls/self
    def is_valid_intrest(rate):
        return 0<=rate<=5

acc1 = BankAccount("Vishwas",50000)
acc1.deposit(8000)

print(BankAccount.is_valid_intrest(3))
print(acc1.is_valid_intrest(3)) ##Though is_valid_intrest a static method Python allows it because method resolution
                                # goes through the class.

##Protectd and Private Methods

class BankAccount:
    min_Bal = 100
    def __init__(self,name,balance=0):
        self.name=name
        self._balance=balance

    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self._balance+=amount
            print(f"{self.name}'s new balance is : {self._balance}")
        else:
            print("Add valid amount")

    def _is_valid_amount(self,amount): ##Protectd Method can be accesses outside class but not ethical
        return amount>0

    def __log_transaction(self,transaction_type,amount): ##Private cannot be accessed outside a class
        return f"{amount} {transaction_type} "