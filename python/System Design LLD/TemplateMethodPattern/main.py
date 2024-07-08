from PaymentFlow import PaymentFlow
from Paytofriend import PayToFriend
from Paytomerchant import PayToMerchant

def send_money(payment: PaymentFlow):
    payment.send_money()

# Example usage
pay_to_friend = PayToFriend()
pay_to_merchant = PayToMerchant()

send_money(pay_to_friend)
send_money(pay_to_merchant)
