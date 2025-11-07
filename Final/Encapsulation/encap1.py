##Encapsulation = Data Hiding + Data Binding
##Encapsulation is conceptual — it enables data hiding, but also ensures controlled interaction between objects
##Abstraction hides complexity.
##Encapsulation implements that hiding by restricting access.

class BadBankAccount:
    def __init__(self,balance):
        self.balance = balance


acc1=BadBankAccount(0.0)
acc1.balance = -1
#print(acc1.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property ##help provide controlled access
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount should be positive.")
        self._balance+=amount

    def withdraw(self,amount):
        if amount > self._balance:
            raise ValueError("Insufficient Funds.")
        elif amount<=0:
            raise ValueError("Withdraw amount should be positive.")
        else:
            self._balance -= amount

account1 = BankAccount()
print(account1.balance)
account1.deposit(20)
print(account1.balance)
account1.withdraw(10)
print(account1.balance)