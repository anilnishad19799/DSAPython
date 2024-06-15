# observerpattern/store.py

from observerable.Iphoneobservableimpl import IphoneObservableImpl
from observer.emailalertobserverimpl import EmailAlertObserverImpl
from observer.mobilealertobserverimpl import MobileAlertObserverImpl

# Create an observable
iphone_stock = IphoneObservableImpl()

# Create observers
email_observer = EmailAlertObserverImpl("example@example.com", iphone_stock)
mobile_observer = MobileAlertObserverImpl("XYZUsername", iphone_stock)

# Register observers
iphone_stock.add(email_observer)
iphone_stock.add(mobile_observer)

# Change stock and notify observers
iphone_stock.set_stock_count(10)
iphone_stock.set_stock_count(100)

