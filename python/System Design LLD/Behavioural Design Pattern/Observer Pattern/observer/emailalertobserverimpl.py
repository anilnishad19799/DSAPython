# observerpattern/observer/emailalertobserverimpl.py

from observer.notificationalertobserver import NotificationAlertObserver
from observerable.stockobservable import StockObservable

class EmailAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, email: str, observable: StockObservable):
        self.email = email
        self.observable = observable

    def update(self):
        self.send_mail(self.email, "Product is in stock, hurry up!")

    def send_mail(self, email_id: str, msg: str):
        print(f"Mail sent to {email_id}: {msg}")
