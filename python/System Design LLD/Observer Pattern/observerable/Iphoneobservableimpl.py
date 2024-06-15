# observerpattern/observable/iphoneobservableimpl.py
from typing import List
from observerable.stockobservable import StockObservable
from observer.notificationalertobserver import NotificationAlertObserver

class IphoneObservableImpl(StockObservable):
    def __init__(self):
        self.observers: List[NotificationAlertObserver] = []
        self.stock_count = 0

    def add(self, observer: NotificationAlertObserver):
        self.observers.append(observer)

    def remove(self, observer: NotificationAlertObserver):
        self.observers.remove(observer)

    def notify_subscribers(self):
        for observer in self.observers:
            observer.update()

    def set_stock_count(self, new_stock_added: int):
        if self.stock_count == 0:
            self.notify_subscribers()
             
        self.stock_count = self.stock_count + new_stock_added

    def get_stock_count(self) -> int:
        return self.stock_count
