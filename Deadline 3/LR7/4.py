from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой на сумму: {amount}")
    
    def refund(self, amount):
        print(f"Возврат по карте на сумму: {amount}")


class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal на сумму: {amount}")
    
    def refund(self, amount):
        print(f"Возврат через PayPal на сумму: {amount}")


if __name__ == "__main__":
    card = CreditCardPayment()
    card.pay(1000)
    card.refund(200)
    
    paypal = PayPalPayment()
    paypal.pay(500)
    paypal.refund(100)
    
    try:
        ps = PaymentSystem()
    except TypeError as e:
        print(f"Нельзя создать экземпляр абстрактного класса: {e}")