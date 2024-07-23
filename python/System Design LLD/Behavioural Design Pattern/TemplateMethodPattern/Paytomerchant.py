from PaymentFlow import PaymentFlow

class PayToMerchant(PaymentFlow):
    def validate_request(self):
        print("Validate logic for PayToMerchant")

    def debit_amount(self):
        print("Debit Amount Logic of PayToMerchant")

    def calculate_fees(self):
        print("10% fees charges")

    def credit_amount(self):
        print("Amount credited to merchant")
