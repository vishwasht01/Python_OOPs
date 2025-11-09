class Payment:
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class PayPal(Payment):
    def pay(self):
        print("Paid using PayPal")

def make_payment(payment_method):
    payment_method.pay()
##Adding new payment types (e.g., UPIPayment) doesn’t require changing make_payment() —
##That’s Open-Closed Principle (OCP) — the heart of polymorphism in design.