# observerpattern/observer/mobilealertobserverimpl.py

from observer.notificationalertobserver import NotificationAlertObserver
from observerable.stockobservable import StockObservable

class MobileAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, username: str, observable: StockObservable):
        self.username = username
        self.observable = observable

    def update(self):
        self.sendMsgOnMobile(self.username, "Product is in stock, hurry up!")

    def sendMsgOnMobile(self, username: str, msg: str):
        print(f"Message sent to {username}: {msg}")
