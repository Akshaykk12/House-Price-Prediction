from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Credit Card."

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using PayPal."
    
class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Bitcoin."