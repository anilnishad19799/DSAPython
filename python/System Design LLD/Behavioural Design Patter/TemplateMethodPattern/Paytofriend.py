from PaymentFlow import PaymentFlow

class PayToFriend(PaymentFlow):
    def validate_request(self):
        print("Validate logic for PayToFriend")

    def debit_amount(self):
        print("Debit Amount Logic of PayToFriend")

    def calculate_fees(self):
        print("5% fees charges")

    def credit_amount(self):
        print("Amount credited to friend")
