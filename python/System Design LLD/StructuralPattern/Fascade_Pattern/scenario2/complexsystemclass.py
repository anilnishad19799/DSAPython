""" This is complex system class where many small helper class is there """

class ProductDAO:
    def getProduct(self, productid):
        return "Based on productid"
    
class Payment:
    def makepayment(self) -> bool:
        return True

class Invoice:
    def generateInvoice(self):
        return "Invoice"
    
class SendNotification:
    def sendNotification(self):
        "send notification on customer mobile "
