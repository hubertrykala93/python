class ProductNotAvailable(Exception):
    def __init__(self, product, message=' is currently unavailable!'):
        self.message = message
        self.product = product

        super(ProductNotAvailable, self).__init__(message, product)

    def __str__(self):
        return self.product.title() + self.message


class OrderFulfilled(Exception):
    def __init__(self, message='All orders have been fulfilled!'):
        self.message = message

    def __str__(self):
        return self.message
