from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
    
    # def get_credits(self):
        # pass

class CreditCard(Payment):
    def make_payment(self, amount):
        return super().make_payment(amount)
    
class MomoPayment(Payment):
    def make_payment(self, amount):
        return super().make_payment
    

        