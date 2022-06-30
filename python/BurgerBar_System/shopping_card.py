class ShoppingCart:

    def __init__(self):
        """
        Creating shopping card object.
        """
        self.objects = []
        self.to_pay = 0

    def add_product(self, product):
        """
        Add chosen product by user to shopping cart!
        Update self.objects param and self.to_pay param.
        :param product: str
        :return: None
        """
        if product.quantity == 1:
            self.objects.append(product)
            self.to_pay += product.price
        else:
            for i in range(product.quantity):
                self.objects.append(product)
                self.to_pay += product.price

    def clear_card(self):
        """
        Clear of the shooping cart after order fulfillment.
        :return: None
        """
        self.objects.clear()
        self.to_pay = 0

    @property
    def products(self):
        """
        :return: list
        """
        return self.objects

    @property
    def amount(self):
        """
        :return: int
        """
        return self.to_pay
