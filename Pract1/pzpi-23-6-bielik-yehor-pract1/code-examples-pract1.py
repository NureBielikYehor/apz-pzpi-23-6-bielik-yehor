from abc import ABC, abstractmethod

# Абстрактний цільовий інтерфейс, який очікує система
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> str:
        pass


# Сторонній платіжний сервіс з іншим інтерфейсом
class ThirdPartyPaymentGateway:
    def pay_with_card(self, amount: float, currency: str) -> str:
        return f"Payment of {amount} {currency} was completed"


# Адаптер, який узгоджує інтерфейси
class PaymentAdapter(PaymentProcessor):
    def __init__(self, gateway: ThirdPartyPaymentGateway):
        self.gateway = gateway

    def process_payment(self, amount: float, currency: str) -> str:
        return self.gateway.pay_with_card(amount, currency)


# Клієнтський код
gateway = ThirdPartyPaymentGateway()
payment_processor = PaymentAdapter(gateway)

result = payment_processor.process_payment(49.99, "USD")
print(result)
# → "Payment of 49.99 USD was completed"