from abc import ABC , abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount): pass

class Razorpay(PaymentProcessor):
    def process(self, amount):
        print(f"Processing ₹{amount} with Razorpay")

class Paypal(PaymentProcessor):
    def process(self, amount):
        print(f"Processing ₹{amount} with PayPal")

def checkout(processor: PaymentProcessor):
    processor.process(500)

checkout(Razorpay())
##The checkout() function doesn’t care which payment system is used —
##it’s abstracted away. Adding new gateways doesn’t break existing code.