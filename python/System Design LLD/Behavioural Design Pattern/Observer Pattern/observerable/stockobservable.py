from observer.notificationalertobserver import NotificationAlertObserver
from abc import ABC, abstractmethod

class StockObservable:
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add(self, observer:NotificationAlertObserver):
        pass

    @abstractmethod
    def remove(self, observer:NotificationAlertObserver):
        pass

    @abstractmethod
    def notifySubscribers(self):
        pass

    @abstractmethod
    def setStockCount(self, newstockadded):
        pass

    @abstractmethod
    def getStockCount(self):
        pass
