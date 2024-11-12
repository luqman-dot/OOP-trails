from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(Payment):
    def make_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")

class MomoPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing mobile money payment of {amount}.")

credit_card = CreditCard()
credit_card.make_payment(100)

momo_payment = MomoPayment()
momo_payment.make_payment(50)
