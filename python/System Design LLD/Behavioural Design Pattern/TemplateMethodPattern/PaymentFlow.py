from abc import ABC, abstractmethod

class PaymentFlow(ABC):
    @abstractmethod
    def validate_request(self):
        pass

    @abstractmethod
    def calculate_fees(self):
        pass

    @abstractmethod
    def debit_amount(self):
        pass

    @abstractmethod
    def credit_amount(self):
        pass

    def send_money(self):
        self.validate_request()
        self.debit_amount()
        self.calculate_fees()
        self.credit_amount()
