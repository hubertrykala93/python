class ShoppingCard:

    def __init__(self):
        self.objects = []
        self.to_pay = 0

    def add_product(self, product):
        if product.quantity == 1:
            self.objects.append(product)
            self.to_pay += product.price
        else:
            for i in range(product.quantity):
                self.objects.append(product)
                self.to_pay += product.price

    @property
    def products(self):
        return self.objects

    @property
    def amount(self):
        return self.to_pay
