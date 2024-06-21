from complexsystemclass import ProductDAO, Invoice, Payment, SendNotification

class orderFascade:
    def OrderFascade(self):
        self.productdao = ProductDAO()
        self.invoice = Invoice()
        self.payment = Payment()
        self.notification = SendNotification()

    def createOrder(self):
        product =  self.productdao.getProduct(121)
        self.payment.makepayment()
        self.invoice.generateInvoice()
        self.notification.sendNotification()

        """Order created and all functionality done""" 